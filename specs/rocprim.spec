%global upstreamname rocPRIM
%global rocm_release 6.2
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}
# Compiler is hipcc, which is clang based:
%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')
# there is no debug package
%global debug_package %{nil}

# Option to test suite for testing on real HW:
%bcond_with check
# For documentation
%bcond_with doc

Name:           rocprim
Version:        %{rocm_version}
%if 0%{?is_opensuse} || 0%{?rhel} && 0%{?rhel} < 10
Release:        1%{?dist}
%else
Release:        %autorelease
%endif
Summary:        ROCm parallel primatives

License:        MIT and BSD

URL:            https://github.com/ROCm/%{name}
Source0:        %{url}/archive/rocm-%{rocm_version}.tar.gz#/%{upstreamname}-%{version}.tar.gz

# Only headers, cmake infra
BuildArch: noarch
# ROCm only working on x86_64
ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-compilersupport-macros
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-runtime-devel
BuildRequires:  rocm-rpm-macros

%if %{with doc}
BuildRequires:  doxygen
BuildRequires:  python3dist(marshalparser)
%endif

%if %{with check}
BuildRequires:  gtest-devel
%endif

%description
The rocPRIM is a header-only library providing HIP parallel primitives
for developing performant GPU-accelerated code on AMD ROCm platform.

%package devel
Summary:        ROCm parallel primatives
Provides:       rocprim-static = %{version}-%{release}

%description devel
The rocPRIM is a header-only library providing HIP parallel primitives
for developing performant GPU-accelerated code on AMD ROCm platform.

%prep
%setup -q -n %{upstreamname}-rocm-%{version}

%build
%cmake \
	-DCMAKE_CXX_COMPILER=hipcc \
	-DCMAKE_C_COMPILER=hipcc \
	-DCMAKE_LINKER=%rocmllvm_bindir/ld.lld \
	-DCMAKE_AR=%rocmllvm_bindir/llvm-ar \
	-DCMAKE_RANLIB=%rocmllvm_bindir/llvm-ranlib \
    -DBUILD_FILE_REORG_BACKWARD_COMPATIBILITY=OFF \
%if %{with check}
    -DBUILD_TEST=ON \
%endif
    -DCMAKE_PREFIX_PATH=%{rocmllvm_cmakedir}/.. \
    -DCMAKE_INSTALL_LIBDIR=share \
    -DROCM_SYMLINK_LIBS=OFF

%cmake_build


%install
%cmake_install

if [ -f %{buildroot}%{_prefix}/share/doc/rocprim/LICENSE.txt ]; then
    rm %{buildroot}%{_prefix}/share/doc/rocprim/LICENSE.txt
fi

%if %{with check}
%ctest
%endif

%files devel
%doc README.md
%license LICENSE.txt
%license NOTICES.txt
%{_includedir}/%{name}
%{_datadir}/cmake/rocprim

%changelog
%if 0%{?is_opensuse}
* Sun Nov 10 2024 Tom Rix <Tom.Rix@amd.com> - 6.2.1-1
- Stub for tumbleweed

%else
%autochangelog
%endif
