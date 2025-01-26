# -*- rpm-spec -*-

%define with_mingw 0
%if 0%{?fedora}
    %define with_mingw 0%{!?_without_mingw:1}
%endif

Summary: osinfo database files
Name: osinfo-db
Version: 20250124
Release: %autorelease
License: GPL-2.0-or-later
Source0: https://fedorahosted.org/releases/l/i/libosinfo/%{name}-%{version}.tar.xz
Source1: https://fedorahosted.org/releases/l/i/libosinfo/%{name}-%{version}.tar.xz.asc
URL: http://libosinfo.org/
BuildRequires: intltool
BuildRequires: osinfo-db-tools
BuildArch: noarch
Requires: hwdata

%if %{with_mingw}
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw64-filesystem >= 95
%endif

%description
The osinfo database provides information about operating systems and
hypervisor platforms to facilitate the automated configuration and
provisioning of new virtual machines

%if %{with_mingw}
%package -n mingw32-osinfo-db
Summary: %{summary}

%description -n mingw32-osinfo-db
This package provides the osinfo database of information about
operating systems for use with virtualization provisioning tools

%package -n mingw64-osinfo-db
Summary: %{summary}

%description -n mingw64-osinfo-db
This package provides the osinfo database of information about
operating systems for use with virtualization provisioning tools

%endif

%install
osinfo-db-import --root %{buildroot} --dir %{_datadir}/osinfo %{SOURCE0}
%if 0%{?rhel}
# Remove the upstream virtio-win / spice-guest-tools drivers
find %{buildroot}/%{_datadir}/osinfo/os/microsoft.com/ -name "win-*.d" -type d -exec rm -rf {} +
%endif

%if %{with_mingw}
osinfo-db-import --root %{buildroot} --dir %{mingw32_datadir}/osinfo %{SOURCE0}
osinfo-db-import --root %{buildroot} --dir %{mingw64_datadir}/osinfo %{SOURCE0}
%endif

%files
%dir %{_datadir}/osinfo/
%{_datadir}/osinfo/VERSION
%{_datadir}/osinfo/LICENSE
%{_datadir}/osinfo/datamap
%{_datadir}/osinfo/device
%{_datadir}/osinfo/os
%{_datadir}/osinfo/platform
%{_datadir}/osinfo/install-script
%{_datadir}/osinfo/schema

%if %{with_mingw}
%files -n mingw32-osinfo-db
%dir %{mingw32_datadir}/osinfo
%doc %{mingw32_datadir}/osinfo/LICENSE
%{mingw32_datadir}/osinfo/VERSION
%{mingw32_datadir}/osinfo/datamap
%{mingw32_datadir}/osinfo/device
%{mingw32_datadir}/osinfo/os
%{mingw32_datadir}/osinfo/platform
%{mingw32_datadir}/osinfo/install-script
%{mingw32_datadir}/osinfo/schema

%files -n mingw64-osinfo-db
%dir %{mingw64_datadir}/osinfo
%doc %{mingw64_datadir}/osinfo/LICENSE
%{mingw64_datadir}/osinfo/VERSION
%{mingw64_datadir}/osinfo/datamap
%{mingw64_datadir}/osinfo/device
%{mingw64_datadir}/osinfo/os
%{mingw64_datadir}/osinfo/platform
%{mingw64_datadir}/osinfo/install-script
%{mingw64_datadir}/osinfo/schema
%endif

%changelog
%autochangelog
