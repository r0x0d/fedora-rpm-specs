Name:           dqlite
Version:        1.17.1
Release:        1%{?dist}
Summary:        Embeddable, replicated and fault tolerant SQL engine

License:        LGPL-3.0-only WITH LGPL-3.0-linking-exception
URL:            https://github.com/canonical/dqlite
Source0:        %{URL}/archive/v%{version}.tar.gz
# https://github.com/ganto/copr-lxc4/issues/24
# https://github.com/canonical/dqlite/issues/643
Patch0:         dqlite-1.17.1-Skip-flaky-tests.patch

BuildRequires:  autoconf libtool
BuildRequires:  gcc
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(sqlite3)

%description
dqlite is a C library that implements an embeddable and replicated SQL database
engine with high-availability and automatic failover.

%package devel
Summary:        Development libraries for dqlite
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers and library for dqlite.

%prep
%autosetup -n %{name}-%{version} -p1

%build
autoreconf -i
%configure --disable-static --enable-build-raft=yes
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/libdqlite.la

%check
%make_build check

%ldconfig_scriptlets

%files
%doc AUTHORS README.md
%license LICENSE
%{_libdir}/libdqlite.so.*

%files devel
%{_libdir}/libdqlite.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}.h

%changelog
* Mon Jan 20 2025 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 1.17.1-1
- Update to 1.17.1

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Apr 14 2024 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 1.16.4-1
- Update to 1.16.4.
- Drop dependency on raft

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 30 2023 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 1.16.0-2
- Rebuild due to raft ABI change

* Wed Oct 04 2023 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 1.16.0-1
- Update to 1.16.0.

* Sun Jul 23 2023 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 1.15.1-1
- Update to 1.15.1.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Apr 08 2023 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 1.14.0-1
- Update to 1.14.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 18 2022 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 1.13.0-1
- Update to 1.13.0.

* Sun Dec 04 2022 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 1.12.0-1
- Update to 1.12.0

* Sun Oct 02 2022 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 1.11.1-1
- Update to 1.11.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Feb 27 2022 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> - 1.9.1-1
- Update to 1.9.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Dec 05 2021 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.9.0-1
- Initial import (#2017476).
