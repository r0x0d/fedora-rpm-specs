%global upstreamname RCCL
%global rocm_release 6.2
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')

# $gpu will be evaluated in the loops below
%global _vpath_builddir %{_vendor}-%{_target_os}-build-${gpu}

%bcond_with debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RelWithDebInfo
%endif

# downloads tests, use mock --enable-network
%bcond_with test
%if %{with test}
%global build_test ON
%global __brp_check_rpaths %{nil}
%else
%global build_test OFF
%endif

# rccl is not supported on gfx1103
# On 6.1.1
# lld: error: ld-temp.o <inline asm>:1:25: specified hardware register is not supported on this GPU
#        s_getreg_b32 s1, hwreg(HW_REG_HW_ID)
#
# On 6.2
# Problems reported with gfx10, removing gfx10 and default (gfx10 and gfx11) from build list
#
# Handle with a custom gpu list
%global rccl_gpu_list gfx9 gfx11 gfx90a gfx942 gfx1100

Name:           rccl
Version:        %{rocm_version}
Release:        %autorelease
Summary:        ROCm Communication Collectives Library

Url:            https://github.com/ROCm/rccl
License:        BSD-3-Clause AND MIT AND Apache-2.0
# From License.txt the main license is BSD 3
# Modifications from Microsoft is MIT
# The NVIDIA based header files below are Apache-2.0
#  src/include/nvtx3/nv*.h and similar
# The URL for NVIDIA in the License.txt https://github.com/NVIDIA/NVTX is Apache-2.0

Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz

BuildRequires:  cmake
BuildRequires:  hipify
BuildRequires:  ninja-build
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-rpm-macros-modules
BuildRequires:  rocm-smi-devel

%if %{with test}
BuildRequires:  gtest-devel
%endif

Requires:       rocm-rpm-macros-modules
Requires:       %{name}-data = %{version}-%{release}

# Only x86_64 works right now:
ExclusiveArch:  x86_64

%description
RCCL (pronounced "Rickle") is a stand-alone library of standard
collective communication routines for GPUs, implementing all-reduce,
all-gather, reduce, broadcast, reduce-scatter, gather, scatter, and
all-to-all. There is also initial support for direct GPU-to-GPU
send and receive operations. It has been optimized to achieve high
bandwidth on platforms using PCIe, xGMI as well as networking using
InfiniBand Verbs or TCP/IP sockets. RCCL supports an arbitrary
number of GPUs installed in a single node or multiple nodes, and
can be used in either single- or multi-process (e.g., MPI)
applications.

The collective operations are implemented using ring and tree
algorithms and have been optimized for throughput and latency. For
best performance, small operations can be either batched into
larger operations or aggregated through the API.

%package devel
Summary:        Headers and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers and libraries for %{name}

%package data
Summary:        Data for %{name}
BuildArch:      noarch

%description data
Data for %{name}

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description test
%{summary}
%endif

%prep
%autosetup -p1 -n %{name}-rocm-%{version}

# Allow user to set AMDGPU_TARGETS
sed -i -e '/AMD GPU targets to compile for/d' CMakeLists.txt

# No parallel-jobs flag
sed -i -e '/parallel-jobs/d' CMakeLists.txt

# No /opt/rocm/.info/version
sed -i -e 's@cat ${ROCM_PATH}/.info/version@echo %{rocm_version}@' CMakeLists.txt

%build
for gpu in %{rccl_gpu_list}
do
    module load rocm/$gpu

    %cmake -G Ninja \
           -DCMAKE_BUILD_TYPE=%{build_type} \
	   -DCMAKE_SKIP_RPATH=ON \
           -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
           -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
           -DROCM_SYMLINK_LIBS=OFF \
           -DAMDGPU_TARGETS=${ROCM_GPUS} \
           -DCMAKE_INSTALL_LIBDIR=$ROCM_LIB \
           -DCMAKE_INSTALL_BINDIR=$ROCM_BIN \
           -DBUILD_TESTS=%{build_test} \
           -DHIP_PLATFORM=amd

    %cmake_build
    module purge
done

%install

for gpu in %{rccl_gpu_list}
do
    %cmake_install
done

echo s@%{buildroot}@@ > br.sed
find %{buildroot}%{_libdir} -name '*.so.*.[0-9]' | sed -f br.sed >  %{name}.files
find %{buildroot}%{_libdir} -name '*.so.[0-9]'   | sed -f br.sed >> %{name}.files
find %{buildroot}%{_libdir} -name '*.so'         | sed -f br.sed >  %{name}.devel
find %{buildroot}%{_libdir} -name '*.cmake'      | sed -f br.sed >> %{name}.devel
%if %{with test}
find %{buildroot}           -name '%{name}*'     | sed -f br.sed >  %{name}.test
%endif

%files -f %{name}.files
%license LICENSE.txt
%exclude %{_docdir}/%{name}/LICENSE.txt

%files data
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/msccl-algorithms
%{_datadir}/%{name}/msccl-algorithms/*.xml
%{_datadir}/%{name}/msccl-unit-test-algorithms/*.xml

%files devel -f %{name}.devel
%doc README.md
%{_includedir}/%{name}

%if %{with test}
%files test -f %{name}.test
%endif

%changelog
%autochangelog