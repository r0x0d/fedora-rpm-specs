Name:    kitinerary
Version: 24.08.1
Release: 1%{?dist}
Summary: A library containing itinerary data model and itinerary extraction code

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND LGPL-2.0-or-later AND ODbL-1.0
URL:     https://invent.kde.org/frameworks/%{name}

Source0:        http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  kpublictransport
BuildRequires:  qt5-qtbase-private-devel

BuildRequires:  cmake(ZXing)
BuildRequires:  cmake(KF6I18n)

# kde-pim pkgs
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Archive)

# kde-pim cmake
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KPim6PkPass)

BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Qml)

BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(poppler)
%if 0%{?fedora}
BuildRequires:  libphonenumber-devel
BuildRequires:  protobuf-devel
%endif
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  osmctools

%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6Itinerary.so.*
%{_libexecdir}/kf6/kitinerary-extractor
%{_kf6_datadir}/mime/packages/application-vnd-kde-itinerary.xml

%files devel
%{_includedir}/KPim6/kitinerary/
%{_includedir}/KPim6/KItinerary/
%{_includedir}/KPim6/kitinerary_version.h
%{_kf6_libdir}/libKPim6Itinerary.so
%{_kf6_libdir}/cmake/KPim6Itinerary/
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch


%changelog
* Wed Sep 25 2024 Alessandro Astone <ales.astone@gmail.com> - 24.08.1-1
- 24.08.1

* Thu Aug 22 2024 Steve Cossette <farchord@gmail.com> - 24.08.0-1
- 24.08.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.05.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.2-1
- 24.05.2

* Fri Jun 14 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.1-1
- 24.05.1

* Fri May 17 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.0-1
- 24.05.0

* Fri Apr 12 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.2-1
- 24.02.2

* Fri Mar 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.1-1
- 24.02.1

* Sun Mar 10 2024 Marie Loise Nolden <loise@kde.org> - 24.02.0-2
- add missing BuildArch: noarch to -doc package

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Thu Feb 08 2024 Marek Kasik <mkasik@redhat.com> - 24.01.95-2
- Rebuild for poppler 24.02.0

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90
- Add doc package for KF6 API

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Fri Dec 8 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80