Name:           kjots
Summary:        KDE Notes application
Version:        6.0.0
Release:        3%{?dist}
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://userbase.kde.org/KJots

Source0:        https://download.kde.org/%{stable_kf6}/%{name}/%{version}/%{name}-%{version}.tar.xz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules

# Qt
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6PrintSupport)

# KDE Frameworks:
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Bookmarks)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6TextWidgets)

# KDE PIM
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KPim6AkonadiNotes)
BuildRequires:  cmake(KPim6TextEdit)
BuildRequires:  cmake(KPim6KontactInterface)
BuildRequires:  cmake(KF6TextCustomEditor)
BuildRequires:  cmake(KF6TextAddonsWidgets)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KF6TextEditTextToSpeech)

# Checks:
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

%description
KJots is an application for writing and organizing notes.


%prep
%autosetup -p1 -n %{name}-%{version}


%build
%cmake_kf6 -DQT_MAJOR_VERSION=6
%cmake_build


%install
%cmake_install
%find_lang kjots --with-kde


%check
for f in %{buildroot}%{_kf6_datadir}/applications/*.desktop ; do
  desktop-file-validate $f
done
appstream-util validate-relax --nonet %{buildroot}/%{_kf6_metainfodir}/org.kde.kjots.appdata.xml


%files -f kjots.lang
%doc README
%license LICENSES/*
%{_kf6_bindir}/kjots
%{_kf6_datadir}/applications/org.kde.kjots.desktop
%{_kf6_datadir}/config.kcfg/kjots.kcfg
%{_kf6_datadir}/icons/hicolor/*/apps/kjots.*
%{_kf6_datadir}/kjots/
%{_kf6_metainfodir}/org.kde.kjots.appdata.xml
%{_kf6_qtplugindir}/kcm_kjots.so
%{_kf6_qtplugindir}/kjotspart.so
%{_kf6_qtplugindir}/pim6/kontact/kontact_kjotsplugin.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Dec 14 2024 Alessandro Astone <ales.astone@gmail.com> - 6.0.0-2
- Rebuild (kmime)

* Fri Aug 30 2024 Steve Cossette <farchord@gmail.com> - 6.0.0-1
- 6.0.0

* Fri Aug 30 2024 Steve Cossette <farchord@gmail.com> - 5.1.1^20231210.013931.1d19021-7
- Rebuild

* Mon Jul 29 2024 Miroslav Suchý <msuchy@redhat.com> - 5.1.1^20231210.013931.1d19021-6
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1^20231210.013931.1d19021-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1^20231210.013931.1d19021-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1^20231210.013931.1d19021-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 16 2024 Alessandro Astone <ales.astone@gmail.com> - 5.1.1^20231210.013931.1d19021-2
- Rebuild (kf6-kconfig)

* Fri Dec 15 2023 Steve Cossette <farchord@gmail.com> - 5.1.1^20231210.013931.1d19021-1
- Updated against git (For Qt6)

* Mon Sep 25 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 5.1.1-3
- Rebuild against ktextaddons 1.5.1

* Mon Aug 14 2023 Justin Zobel <justin.zobel@gmail.com> - 5.1.1-2
- Fix 5.1.1 build, remove patch and fix file paths

* Wed Jul 26 2023 Justin Zobel <justin.zobel@gmail.com> - 5.1.1-1
- Update to 5.1.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 5.1.0-3
- Exclude arches ppc64le,s390x

* Fri May 21 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 5.1.0-2
- New dependency KF5Libkdepim added

* Fri May 21 2021 Onuralp SEZER <thunderbirdtr@fedoraproject.org> - 5.1.0-1
- 5.1.0
- Source URL changed
- Old source version removed
- Files section fixed

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.0.2-8
- Remove obsolete scriptlets

* Tue Dec 19 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.0.2-7
- rebuild (pim-17.12.0)

* Mon Nov 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.0.2-6
- release++

* Wed Nov 22 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.0.2-5.1
- rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Rex Dieter <rdieter@fedoraproject.org> - 5.0.2-3
- rebuild (kde-apps-16.12.x)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.0.2-1
- 5.0.2, update URL

* Fri Jul 22 2016 Rex Dieter <rdieter@fedoraproject.org> - 5.0.1-3
- update URL

* Mon Mar 14 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.0.1-2
- fix url
- fix scriptlets
- fix %%license and %%doc
- validate appdata

* Sat Feb 13 2016 Daniel Vrátil <dvratil@fedoraproject.org> - 5.0.1-1
- initial package
