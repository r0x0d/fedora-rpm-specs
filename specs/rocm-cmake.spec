# there is no debug package - this is just cmake modules
%global debug_package %{nil}

%global rocm_release 6.2
%global rocm_patch 0
%global rocm_version %{rocm_release}.%{rocm_patch}

Name:     rocm-cmake
Version:  %{rocm_version}
%if 0%{?suse_version} || 0%{?rhel} && 0%{?rhel} < 10
Release:    1%{?dist}
%else
Release:  %autorelease
%endif
Summary:  CMake modules for common build and dev tasks within the ROCm project
License:  MIT
URL:      https://github.com/ROCm/rocm-cmake
Source:   %{url}/archive/rocm-%{version}.tar.gz#/rocm-cmake-rocm-%{version}.tar.gz

BuildArch: noarch
BuildRequires: cmake
Requires: cmake

%description
rocm-cmake is a collection of CMake modules for common build and development
tasks within the ROCm project. It is therefore a build dependency for many of
the libraries that comprise the ROCm platform.

rocm-cmake is not required for building libraries or programs that use ROCm; it
is required for building some of the libraries that are a part of ROCm.


%prep
%autosetup -n rocm-cmake-rocm-%{version}


%build
%cmake
%cmake_build


%install
%cmake_install

if [ -f %{buildroot}%{_prefix}/share/doc/rocm-cmake/LICENSE ]; then
    rm %{buildroot}%{_prefix}/share/doc/rocm-cmake/LICENSE
fi

%files
%dir %{_datadir}/rocm
%dir %{_datadir}/rocmcmakebuildtools

%doc CHANGELOG.md
%license LICENSE
%{_datadir}/rocm/*
%{_datadir}/rocmcmakebuildtools/*

%changelog
%if 0%{?suse_version}
* Sat Nov 9 2024 Tom Rix <Tom.Rix@amd.com> - 6.2.1-1
- Stub for tumbleweed

%else
%autochangelog
%endif

