Name:           kio-gdrive
Version:        24.12.1
Release:        1%{?dist}
Summary:        An Google Drive KIO slave for KDE

License:        GPL-2.0-or-later
URL:            https://community.kde.org/KIO_GDrive
# use releaseme
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz


# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
# arch's where libkgapi is available (due to inderect dependencies on qtwebengine)
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires:  cmake
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  extra-cmake-modules
BuildRequires:  desktop-file-utils
BuildRequires:  cmake(KAccounts6)
BuildRequires:  libkgapi-devel
BuildRequires:  libaccounts-glib-devel
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  libappstream-glib
BuildRequires:  intltool
BuildRequires:  cmake(KF6Purpose)
Requires:       kaccounts-providers

# QML SSO.OnlineAccounts
Requires:       accounts-qml-module-qt6

%description
Provides KIO Access to Google Drive using the gdrive:/// protocol.

%prep
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang kio6_gdrive --all-name --with-html

%check
desktop-file-validate %{buildroot}%{_datadir}/remoteview/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml ||:

%files -f kio6_gdrive.lang
%license COPYING
%doc HACKING README.md
%{_qt6_plugindir}/kaccounts/daemonplugins/gdrive.so
%{_kf6_plugindir}/kfileitemaction/gdrivecontextmenuaction.so
%{_kf6_plugindir}/propertiesdialog/gdrivepropertiesplugin.so
%{_kf6_plugindir}/purpose/purpose_gdrive.so
%{_kf6_datadir}/accounts/services/kde/google-drive.service
%{_kf6_datadir}/knotifications6/gdrive.notifyrc
%{_kf6_datadir}/remoteview/gdrive-network.desktop
%{_kf6_datadir}/metainfo/org.kde.kio_gdrive.metainfo.xml
%{_kf6_qtplugindir}/kf6/kio/gdrive.so
%{_datadir}/purpose/purpose_gdrive_config.qml

%changelog
* Tue Jan 07 2025 Steve Cossette <farchord@gmail.com> - 24.12.1-1
- 24.12.1

* Sat Dec 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.12.0-1
- 24.12.0

* Fri Nov 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.90-1
- 24.11.90

* Fri Nov 15 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.80-1
- 24.11.80

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-1
- 24.08.3

* Tue Oct 08 2024 Steve Cossette <farchord@gmail.com> - 24.08.2-1
- 24.08.2

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

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Tue Dec 26 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.85-2
- Depend on accounts-qml-module

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Thu Dec 7 2023 Steve Cossette <farchord@gmail.com> - 24.01.80-1
- 24.01.80

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.2-1
- 23.04.2

* Sat May 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.1-1
- 23.04.1

* Wed Apr 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-3
- Rebuild

* Mon Apr 24 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 23.04.0-2
- Fix license

* Fri Apr 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.12.3-1
- 22.12.3

* Tue Jan 31 2023 Marc Deop <marcdeop@fedoraproject.org> - 22.12.2-1
- 22.12.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Mon Dec 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.12.0-1
- 22.12.0

* Fri Nov 04 2022 Marc Deop i Argemí (Private) <marc@marcdeop.com> - 22.08.3-1
- 22.08.3

* Fri Oct 14 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.2-1
- 22.08.2

* Thu Sep 08 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.1-1
- 22.08.1

* Sun Aug 21 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 22.08.0-1
- Update to 22.08.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- 22.04.3

* Tue May 24 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 22.04.1-1
- Update to 22.04.1

* Tue Apr 26 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 22.04.0-1
- Update to 22.04.0

* Thu Mar 03 2022 Marc Deop <marcdeop@fedoraproject.org> - 21.12.3-1
- 21.12.3

* Fri Feb 04 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 21.12.2-1
- Update to 21.12.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 21.12.1-1
- Update to 21.12.1

* Mon Dec 13 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.12.0-1
- Update to 21.12.0

* Fri Sep 24 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.08.1-1
- Update to 21.08.1

* Mon Aug 23 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.08.0-1
- Update to 21.08.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 15 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.04.3-1
- Update to 21.04.3

* Fri Jun 11 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.04.2-1
- Update to 21.04.2

* Wed May 19 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.04.1-1
- Update to 21.04.1

* Thu Apr 22 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 21.04.0-1
- Update to 21.04.0

* Mon Mar 15 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 20.12.3-1
- Update to 20.12.3

* Mon Feb 22 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 20.12.2-1
- Update to 20.12.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 20.12.1-2
- Add kaccounts-providers to requires

* Sun Jan 10 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 20.12.1-1
- Update to 20.12.1

* Fri Dec 11 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.12.0-1
- Update to 20.12.0

* Sat Nov 07 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.08.3-1
- Update to 20.08.3

* Wed Oct 21 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.08.2-1
- Update to 20.08.2

* Wed Sep 23 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.08.1-1
- Update to 20.08.1

* Thu Aug 20 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 20.08.0-1
- Update to 20.08.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jul 12 2020 Rex Dieter <rdieter@fedoraproject.org> - 1.3.0-2
- rebuild (kaccounts)

* Mon May 25 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 1.3.0-1
- Update to 1.3.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 1.2.7-2
- Enable LTO

* Fri Sep 06 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 1.2.7-1
- Update to 1.2.7

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Vasiliy N. Glazov <vascom2@gmail.com> 1.2.6-2
- Rebuild

* Mon May 20 2019 Vasiliy N. Glazov <vascom2@gmail.com> 1.2.6-1
- Update to 1.2.6

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 24 2018 Vasiliy N. Glazov <vascom2@gmail.com> 1.2.5-1
- Update to 1.2.5

* Mon Jul 16 2018 Vasiliy N. Glazov <vascom2@gmail.com> 1.2.4-1
- Update to 1.2.4
- Clean spec and BRs

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Oct 1 2017 Wolnei Tomazelli Junior <wolnei@fedoraproject.org> -  1.2.1-2
- Fix bogus date

* Sun Oct 1 2017 Wolnei Tomazelli Junior <wolnei@fedoraproject.org> -  1.2.1-1
- Build fixes
- Updated translations

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 22 2017 Wolnei Tomazelli Junior <wolnei@fedoraproject.org> -  1.2.0-1
- Integration with KAccounts
- Google Drive free space is now reported

* Wed May 17 2017 Rex Dieter <rdieter@fedoraproject.org> - 1.1.2-2
- rebuild (libkgapi), use %%find_lang for HTML docs too
- ExclusiveArch: %%{?qt5_qtwebengine_arches}

* Mon May 15 2017 Wolnei Tomazelli Junior <wolnei@fedoraproject.org> -  1.1.2-1
- Updated translations - v1.1.2
* Fri Feb 17 2017 Wolnei Tomazelli Junior <wolnei@fedoraproject.org> -  1.1.1-1
- Fixed wrong write permissions in the top-level accounts folder - v1.1.1
* Sun Jan 29 2017 Wolnei Tomazelli Junior <wolnei@fedoraproject.org> -  1.1.0-1
- update version 1.1
* Sat Jan 28 2017 Wolnei Tomazelli Junior <wolnei@fedoraproject.org> -  1.0.5-2
- Initial version of the package
