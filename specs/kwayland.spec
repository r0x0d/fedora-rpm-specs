Name:       kwayland
Version:    6.3.0
Release:    1%{?dist}
Summary:    Qt-style API to interact with the wayland-client API

License:    BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND MIT-CMU AND MIT
URL:        https://invent.kde.org/plasma/%{name}

Source0:    https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  appstream
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  make
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-static
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel

BuildRequires:  cmake(PlasmaWaylandProtocols)
BuildRequires:  cmake(Qt6WaylandClient)

Requires:   kf6-filesystem

# Renamed from kf6-kwayland
Obsoletes:      kf6-kwayland < 1:%{version}-%{release}
Provides:       kf6-kwayland = 1:%{version}-%{release}

%description
%{summary}.

%package    devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}
Requires:   qt6-qtbase-devel
Obsoletes:  kf6-kwayland-devel < 1:%{version}-%{release}
Provides:   kf6-kwayland-devel = 1:%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_datadir}/qlogging-categories6/*categories
%{_libdir}/libKWaylandClient.so.6
%{_libdir}/libKWaylandClient.so.%{version}

%files devel
%doc README.md
%license LICENSES/*.txt
%{_includedir}/KWayland/
%{_libdir}/cmake/KWayland/
%{_libdir}/libKWaylandClient.so
%{_libdir}/pkgconfig/KWaylandClient.pc
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch

%changelog
* Thu Feb 06 2025 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.3.0-1
- 6.3.0

* Thu Jan 23 2025 Steve Cossette <farchord@gmail.com> - 6.2.91-1
- 6.2.91

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 09 2025 Steve Cossette <farchord@gmail.com> - 6.2.90-1
- Beta 6.2.90

* Tue Dec 31 2024 Steve Cossette <farchord@gmail.com> - 6.2.5-1
- 6.2.5

* Tue Nov 26 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.2.4-1
- 6.2.4

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 6.2.3-1
- 6.2.3

* Tue Oct 22 2024 Steve Cossette <farchord@gmail.com> - 6.2.2-1
- 6.2.2

* Tue Oct 15 2024 Steve Cossette <farchord@gmail.com> - 6.2.1-1
- 6.2.1

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 6.2.0-2
- Rebuild (qt6)

* Thu Oct 03 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.2.0-1
- 6.2.0

* Thu Sep 12 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.90-1
- 6.1.90

* Tue Sep 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.5-1
- 6.1.5

* Fri Aug 09 2024 Steve Cossette <farchord@gmail.com> - 6.1.4-1
- 6.1.4

* Wed Jul 24 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.3-3
- rebuilt

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 16 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.3-1
- 6.1.3

* Wed Jul 03 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.2-1
- 6.1.2

* Tue Jun 25 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.1-1
- 6.1.1

* Thu Jun 13 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.1.0-1
- 6.1.0

* Fri May 24 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.90-1
- 6.0.90

* Wed May 22 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.5-1
- 6.0.5

* Tue Apr 16 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.4-1
- 6.0.4

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 6.0.3-2
- Rebuild (qt6)

* Tue Mar 26 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.3-1
- 6.0.3

* Tue Mar 12 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.2-1
- 6.0.2

* Sat Mar 09 2024 Marie Loise Nolden <loise@kde.org> - 6.0.1-2
- add missing BuildArch: noarch to -doc package

* Wed Mar 06 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.1-1
- 6.0.1

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 6.0.0-1
- 6.0.0

* Fri Feb 16 2024 Jan Grulich <jgrulich@redhat.com> - 5.93.0-2
- Rebuild (qt6)

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.93.0-1
- 5.93.0

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.92.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.92.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.92.0-1
- 5.92.0
- Add doc package for KF6 API

* Thu Dec 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.91.0-1
- 5.91.0

* Sun Dec 03 2023 Justin Zobel <justin.zobel@gmail.com> - 5.90.0-1
- Update to 5.90.0

* Wed Nov 29 2023 Jan Grulich <jgrulich@redhat.com> - 5.27.80-2
- Rebuild (qt6)

* Sun Nov 12 2023 Alessandro Astone <ales.astone@gmail.com> - 5.27.80-1
- Renamed from kf6-kwayland
- 5.27.80

* Tue Oct 17 2023 Jan Grulich <jgrulich@redhat.com> - 5.240.0^20230922.150947.770e361-3
- Rebuild (qt6)

* Thu Oct 05 2023 Justin Zobel <justin.zobel@gmail.com> - 5.240.0^20230922.150947.770e361-2
- Rebuild for Qt Private API

* Sat Sep 23 2023 Steve Cossette <farchord@gmail.com> - 5.240.0^20230922.150947.770e361-1
- Initial release
