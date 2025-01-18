%global rocm_release 6.3
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}
%global upstreamname rocm_smi_lib

%bcond_with test
%if %{with test}
%global build_test ON
%else
%global build_test OFF
%endif

%bcond_with doc

Name:       rocm-smi
Version:    %{rocm_version}
Release:    2%{?dist}
Summary:    ROCm System Management Interface Library

License:    MIT AND NCSA
URL:        https://github.com/ROCm/%{upstreamname}
Source0:    %{url}/archive/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz
Patch0:     0001-Fix-empty-return.patch

%if 0%{?rhel} || 0%{?suse_version}
ExclusiveArch:  x86_64
%else
# SMI requires the AMDGPU kernel module, which only builds on:
ExclusiveArch:  x86_64 aarch64 ppc64le riscv64
%endif

BuildRequires:  cmake
%if %{with doc}
# Fedora 38 has doxygen 1.9.6
%if 0%{?fedora} > 38
BuildRequires:  doxygen >= 1.9.7
BuildRequires:  doxygen-latex >= 1.9.7
%endif
%endif
BuildRequires:  gcc-c++

%description
The ROCm System Management Interface Library, or ROCm SMI library, is part of
the Radeon Open Compute ROCm software stack . It is a C library for Linux that
provides a user space interface for applications to monitor and control GPU
applications.

%package devel
Summary: ROCm SMI Library development files
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
ROCm System Management Interface Library development files

%if %{with test}
%package test
Summary:        Tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description test
%{summary}
%endif

%prep
%autosetup -n %{upstreamname}-rocm-%{version} -p1

# Don't change default C FLAGS and CXX FLAGS:
sed -i '/CMAKE_C.*_FLAGS/d' CMakeLists.txt

# Fix script shebang
sed -i -e 's@env python3@python3@' python_smi_tools/*.py
sed -i -e 's@env python3@python3@' python_smi_tools/rsmiBindingsInit.py.in

%build
%cmake -DFILE_REORG_BACKWARD_COMPATIBILITY=OFF -DCMAKE_INSTALL_LIBDIR=%{_lib} \
       -DCMAKE_SKIP_INSTALL_RPATH=TRUE \
       -DBUILD_TESTS=%build_test

%cmake_build

%install
%cmake_install

# For Fedora < 38, the README is not installed if doxygen is disabled:
install -D -m 644 README.md %{buildroot}%{_docdir}/rocm_smi/README.md

F=%{buildroot}%{_datadir}/doc/rocm_smi/LICENSE.txt
if [ -f $F ]; then
    rm $F
fi

%files
%doc %{_docdir}/rocm_smi
%license License.txt
%{_bindir}/rocm-smi
%{_libexecdir}/rocm_smi
%{_libdir}/librocm_smi64.so.1{,.*}
%{_libdir}/liboam.so.1{,.*}

%files devel
%{_includedir}/rocm_smi/
%{_includedir}/oam/
%{_libdir}/librocm_smi64.so
%{_libdir}/liboam.so
%{_libdir}/cmake/rocm_smi/

%if %{with test}
%files test
%{_datarootdir}/rsmitst_tests
%endif

%changelog
* Thu Jan 16 2025 Tom Rix <Tom.Rix@amd.com> - 6.3.1-2
- Update license and url
- Fix script shebangs

* Sun Dec 22 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.1-1
- Update to 6.3.1

* Sat Dec 7 2024 Tom Rix <Tom.Rix@amd.com> - 6.3.0-1
- Update to 6.3

* Sun Nov 3 2024 Tom Rix <Tom.Rix@amd.com> - 6.2.1-1
- Stub for tumbleweed
