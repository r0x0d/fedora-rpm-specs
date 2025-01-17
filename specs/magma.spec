# rocm toolchain uses the hipcc wrapper of clang
%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')
# $gpu will be evaluated in the loops below
%global _vpath_builddir %{_vendor}-%{_target_os}-build-${gpu}
# Need a GPU to test while building
%bcond_with test
%if %{with test}
# Do not build everything, assumes your testing gpu if gfx10* or gfx11*
%global rocm_gpu_list default
%endif

Name:           magma
Version:        2.8.0
# The commit that matches the release tag
%global commit 06368d9b817710566f654b96114549216f8cee70
%global shortcommit %(c=%{commit}; echo ${c:0:12})
Release:        %autorelease
Summary:        Matrix Algebra on GPU and Multi-core Architectures
Url:            https://icl.utk.edu/magma/
License:        BSD-3-Clause AND MIT
# From the license check
# The main license is BSD-3-Clause
#   COPYRIGHT
# Then ICS, with file copied from OPEN BSD
#   control/strlcpy.cpp
# Then MIT, with a file copied from hipify
# hipify is used but not delivered
#   tools/hipify-perl
# Reported GPL but not used, other similar files for cuda
#   results/v1.5.0/cuda7.0-k40c/setup.txt

Source0:        https://bitbucket.org/icl/magma/get/%{commit}.tar.gz
# The source in the download here
# https://icl.utk.edu/projectsfiles/magma/downloads/magma-2.8.0.tar.gz
# Is missing files needed to build
# So fetch from git commit

# For versioning the *.so's
# https://bitbucket.org/icl/magma/issues/77/versioning-so
Patch0:         0001-Prepare-magma-cmake-for-fedora.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  flexiblas-devel
BuildRequires:  hipblas-devel
BuildRequires:  hipsparse-devel
BuildRequires:  ninja-build
BuildRequires:  python3
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-core-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-rpm-macros-modules

Requires:       rocm-rpm-macros-modules

# MIT
# Just the hipify-perl file is taken and it is very old
# This is older than any release of https://github.com/ROCm/HIPIFY.git
# So setting to earliest release -1
Provides:       bundled(hipify) = 3.4.0

# ROCm is only on x86_64:
ExclusiveArch:  x86_64

%description
Matrix Algebra on GPU and Multi-core Architectures (MAGMA) is a collection
of next-generation linear algebra libraries for heterogeneous computing.
The MAGMA package supports interfaces for current linear algebra packages
and standards (e.g., LAPACK and BLAS) to enable computational scientists
to easily port any linear algebra–reliant software component to
heterogeneous computing systems. MAGMA enables applications to fully
exploit the power of current hybrid systems of many-core CPUs and
multi-GPUs/coprocessors to deliver the fastest possible time to accurate
solutions within given energy constraints.

MAGMA features LAPACK-compliant routines for multi-core CPUs enhanced with
NVIDIA or AMD GPUs. MAGMA 2.7.2 now includes more than 400 routines that
cover one-sided dense matrix factorizations and solvers, two-sided
factorizations, and eigen/singular-value problem solvers, as well as a
subset of highly optimized BLAS for GPUs. A MagmaDNN package has been
added and further enhanced to provide high-performance data analytics,
including functionalities for machine learning applications that use MAGMA
as their computational back end. The MAGMA Sparse and MAGMA Batched
packages have been included since MAGMA 1.6.

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%prep
%autosetup -p1 -n icl-%{name}-%{shortcommit}

# Add some more gfx's
# https://bitbucket.org/icl/magma/issues/76/a-few-new-rocm-gpus
sed -i -e 's@1032 1033@1032 1033 1100 1101 1102 1103@' Makefile

# Remove some tests,
sed -i -e '/testing_zgenerate.cpp/d' testing/Makefile.src

# Change the bin,lib install locations
sed -i -e 's@DESTINATION lib@DESTINATION ${CMAKE_INSTALL_LIBDIR}@' CMakeLists.txt
sed -i -e 's@DESTINATION bin@DESTINATION ${CMAKE_INSTALL_BINDIR}@' CMakeLists.txt

# Version *.so
sed -i -e 's@magma_VERSION@"%{version}"@g' CMakeLists.txt

# python to python3, need env to find local bits like magmasubs.py
sed -i -e 's@env python@env python3@' tools/checklist_run_tests.py
sed -i -e 's@env python@env python3@' tools/check-style.py
sed -i -e 's@env python@env python3@' tools/codegen.py
sed -i -e 's@env python@env python3@' tools/parse-magma.py

# Remove some files we do not need to similify licenses
# GPL, results for cuda
rm -rf results/*
# ICS, Copy of strlcpy - just use strlcpy
sed -i -e '/strlcpy/d' control/Makefile.src
sed -i -e '/strlcpy/d' include/magma_auxiliary.h
sed -i -e 's@magma_strlcpy@strlcpy@' control/trace.cpp
rm control/strlcpy.cpp

%build

export HIP_PATH=`hipconfig -p`
export ROCM_PATH=`hipconfig -R`
export HIP_CLANG_PATH=`hipconfig -l`
RESOURCE_DIR=`${HIP_CLANG_PATH}/clang -print-resource-dir`
export DEVICE_LIB_PATH=${RESOURCE_DIR}/amdgcn/bitcode


for gpu in %{rocm_gpu_list}
do
    module load rocm/$gpu

    echo "BACKEND = hip"              > make.inc
    echo "FORT = false"              >> make.inc
    echo "GPU_TARGET = ${ROCM_GPUS}" >> make.inc

    make generate

    %cmake -G Ninja \
	   -DBLA_VENDOR=FlexiBLAS \
           -DCMAKE_CXX_COMPILER=hipcc \
           -DCMAKE_INSTALL_LIBDIR=$ROCM_LIB \
           -DCMAKE_INSTALL_BINDIR=$ROCM_BIN \
           -DGPU_TARGET=${ROCM_GPUS} \
           -DMAGMA_ENABLE_HIP=ON \
           -DUSE_FORTRAN=OFF

    %cmake_build
    module purge
done

%install
for gpu in %{rocm_gpu_list}
do
    %cmake_install
done

echo s@%{buildroot}@@ > br.sed
find %{buildroot}%{_libdir} -name '*.so.*.[0-9]' | sed -f br.sed >  %{name}.files
find %{buildroot}%{_libdir} -name '*.so.[0-9]'   | sed -f br.sed >> %{name}.files
find %{buildroot}%{_libdir} -name '*.so'         | sed -f br.sed >  %{name}.devel

%if %{with test}
%check
gpu=default
%{_vpath_builddir}/testing/testing_sgemm
# Results should be something like
# % MAGMA 2.8.0 svn 32-bit magma_int_t, 64-bit pointer.
# % HIP runtime 60140093, driver 60140093. OpenMP threads 12. 
# % device 0: AMD Radeon Pro W7900, 1760.0 MHz clock, 46064.0 MiB memory, gcn arch gfx1100
# % Sat Jul 13 15:46:03 2024
# % Usage: redhat-linux-build-default/testing/testing_sgemm [options] [-h|--help]
#
# % If running lapack (option --lapack), MAGMA and HIPBLAS error are both computed
# % relative to CPU BLAS result. Else, MAGMA error is computed relative to HIPBLAS result.
#
# % transA = No transpose, transB = No transpose
# %   M     N     K   MAGMA Gflop/s (ms)  HIPBLAS Gflop/s (ms)   CPU Gflop/s (ms)  MAGMA error  HIPBLAS error
# %========================================================================================================
#  1088  1088  1088    592.80 (   4.35)       8.92 ( 288.85)     ---   (  ---  )    1.32e-08        ---    ok
#  2112  2112  2112   14776.79 (   1.28)    15072.73 (   1.25)     ---   (  ---  )    1.19e-08        ---    ok
#  3136  3136  3136   17007.16 (   3.63)    10880.35 (   5.67)     ---   (  ---  )    1.14e-08        ---    ok
#  4160  4160  4160   12512.57 (  11.51)    25651.22 (   5.61)     ---   (  ---  )    5.88e-10        ---    ok
#  5184  5184  5184   11835.76 (  23.54)    13724.13 (  20.30)     ---   (  ---  )    4.23e-10        ---    ok
#  6208  6208  6208   5298.80 (  90.30)    15901.86 (  30.09)     ---   (  ---  )    8.32e-09        ---    ok
#  7232  7232  7232   11764.14 (  64.31)    20683.31 (  36.58)     ---   (  ---  )    5.11e-10        ---    ok
%endif

%files -f %{name}.files
%license COPYRIGHT

%files devel -f %{name}.devel
%{_includedir}/*.h
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
