%global upstreamname hipSPARSE
%global rocm_release 6.2
%global rocm_patch 0
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

# Assumes gpu hw
%bcond_with check

# downloads tests, use mock --enable-network
%bcond_with test
%if %{with test}
%global build_test ON
%global __brp_check_rpaths %{nil}
%else
%global build_test OFF
%endif

# gfortran and clang rpm macros do not mix
%global build_fflags %{nil}

Name:           hipsparse
Version:        %{rocm_version}
%if 0%{?is_opensuse} || 0%{?rhel} && 0%{?rhel} < 10
Release:        1%{?dist}
%else
Release:        %autorelease
%endif
Summary:        ROCm SPARSE marshalling library
Url:            https://github.com/ROCmSoftwarePlatform/%{upstreamname}
License:        MIT

# Only x86_64 works right now:
ExclusiveArch:  x86_64

Source0:        %{url}/archive/refs/tags/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{rocm_version}.tar.gz
# Really turn the samples off
Patch0:         0001-prepare-hipsparse-cmake-for-fedora.patch

BuildRequires:  cmake
%if 0%{?is_opensuse}
BuildRequires:  gcc-fortran
%else
BuildRequires:  gcc-gfortran
%endif
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-rpm-macros-modules
BuildRequires:  rocprim-devel
BuildRequires:  rocsparse-devel

%if %{with test}
BuildRequires:  gtest-devel
BuildRequires:  rocblas-devel
%if 0%{?is_opensuse}
BuildRequires:  rocm-libomp-devel
%else
BuildRequires:  libomp-devel
%endif
%endif

Requires:       rocm-rpm-macros-modules

%description
hipSPARSE is a SPARSE marshalling library with multiple
supported backends. It sits between your application and
a 'worker' SPARSE library, where it marshals inputs to
the backend library and marshals results to your
application. hipSPARSE exports an interface that doesn't
require the client to change, regardless of the chosen
backend. Currently, hipSPARSE supports rocSPARSE and
cuSPARSE backends.

%package devel
Summary:        Libraries and headers for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
%{summary}

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description test
%{summary}
%endif

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

%build
for gpu in %{rocm_gpu_list}
do
    module load rocm/$gpu
    %cmake \
	-DCMAKE_CXX_COMPILER=hipcc \
	-DCMAKE_C_COMPILER=hipcc \
	-DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \
	-DCMAKE_AR=%rocmllvm_bindir/llvm-ar \
	-DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \
           -DCMAKE_BUILD_TYPE=%build_type \
	   -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
	   -DCMAKE_SKIP_RPATH=ON \
	   -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
	   -DROCM_SYMLINK_LIBS=OFF \
	   -DHIP_PLATFORM=amd \
	   -DAMDGPU_TARGETS=$ROCM_GPUS \
	   -DCMAKE_INSTALL_LIBDIR=$ROCM_LIB \
	   -DCMAKE_INSTALL_BINDIR=$ROCM_BIN \
	   -DBUILD_CLIENTS_BENCHMARKS=%{build_test} \
	   -DBUILD_CLIENTS_TESTS=%{build_test} \
	   -DBUILD_CLIENTS_TESTS_OPENMP=OFF \
	   -DBUILD_FORTRAN_CLIENTS=OFF

    %cmake_build
    module purge
done

%cmake_build

%if %{with test}
%if %{with check}
%check
gpu=default
find . -name 'hipsparse-test' -exec {} \;
%endif
%endif

%install
for gpu in %{rocm_gpu_list}
do
    %cmake_install
done

echo s@%{buildroot}@@ > br.sed
find %{buildroot}%{_libdir} -name '*.so.*.[0-9]' | sed -f br.sed >  %{name}.files
find %{buildroot}%{_libdir} -name '*.so.[0-9]'   | sed -f br.sed >> %{name}.files
find %{buildroot}%{_libdir} -name '*.so'         | sed -f br.sed >  %{name}.devel
find %{buildroot}%{_libdir} -name '*.cmake'      | sed -f br.sed >> %{name}.devel
find %{buildroot}           -name '%{name}*'     | sed -f br.sed >  %{name}.test

if [ -f %{buildroot}%{_prefix}/share/doc/hipsparse/LICENSE.md ]; then
    rm %{buildroot}%{_prefix}/share/doc/hipsparse/LICENSE.md
fi

%files -f %{name}.files
%license LICENSE.md

%files devel -f %{name}.devel
%doc README.md
%dir %{_libdir}/cmake/%{name}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*

%if %{with test}
%files test -f %{name}.test
%endif

%changelog
%if 0%{?is_opensuse}
* Sun Nov 10 2024 Tom Rix <Tom.Rix@amd.com> - 6.2.1-1
- Stub for tumbleweed

%else
%autochangelog
%endif
