%global tests 1

Name:           dolphin
Summary:        KDE File Manager
Version:        24.12.1
Release:        1%{?dist}

License:        BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:            https://invent.kde.org/system/dolphin
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{maj_ver_kf6}.%{min_ver_kf6}.%{bug_ver_kf6}/src/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  systemd-rpm-macros

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6Baloo)
BuildRequires:  cmake(KF6BalooWidgets)
BuildRequires:  cmake(KF6Bookmarks)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6FileMetaData)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6UserFeedback)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6GuiAddons)

BuildRequires:  cmake(PlasmaActivities)

BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  qt6-qtbase-private-devel

BuildRequires:  cmake(packagekitqt6)
BuildRequires:  cmake(Phonon4Qt6)

%if 0%{?tests}
BuildRequires: xorg-x11-server-Xvfb
BuildRequires: rubygem(test-unit)
%endif

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

Recommends:     konsole-part%{?_isa}
Recommends:     kio-fuse%{?_isa}
Recommends:     kio-extras%{?_isa}
Recommends:     %{name}-plugins

%description
%{summary}.

%package        libs
Summary:        Dolphin runtime libraries
%description    libs
%{summary}.

%package        devel
Summary:        Developer files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel%{?_isa}
Requires:       kf6-kio-devel%{?_isa}
%description    devel
%{summary}.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf6 \
  %{?flatpak:-DFLATPAK:BOOL=ON} \
  -DKDE_INSTALL_SYSTEMDUSERUNITDIR=%{_userunitdir} \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}

%cmake_build


%install
%cmake_install

%find_lang dolphin --all-name --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%if 0%{?tests}
xvfb-run -a bash -c "%ctest" || :
%endif


%files -f dolphin.lang
%license LICENSES/*
%doc README*
%{_kf6_datadir}/qlogging-categories6/dolphin.*
%{_kf6_bindir}/dolphin
%{_kf6_bindir}/servicemenuinstaller
%{_kf6_datadir}/config.kcfg/dolphin_*
%{_kf6_datadir}/knsrcfiles/*
%if 0%{?flatpak}
%{_datadir}/dbus-1/services/org.freedesktop.FileManager1.service
%else
%{_datadir}/dbus-1/services/org.kde.dolphin.FileManager1.service
%endif
%{_userunitdir}/plasma-dolphin.service
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%dir %{_kf6_datadir}/kglobalaccel/
%{_kf6_datadir}/kglobalaccel/org.kde.dolphin.desktop
%{_kf6_datadir}/kconf_update/dolphin_detailsmodesettings.upd
%{_kf6_datadir}/kconf_update/dolphin_directorysizemode.py
%{_kf6_datadir}/kconf_update/dolphin_directorysizemode.upd
%dir %{_kf6_datadir}/dolphin
%{_kf6_datadir}/dolphin/dolphinpartactions.desktop
%{_kf6_datadir}/zsh/site-functions/_dolphin
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.dolphin.svg

%files libs
%{_kf6_libdir}/libdolphinprivate.so.*
%{_kf6_libdir}/libdolphinvcs.so.*
%{_kf6_plugindir}/parts/dolphinpart.so
%{_kf6_qtplugindir}/dolphin/
%{_kf6_qtplugindir}/kf6/kfileitemaction/movetonewfolderitemaction.so

%files devel
%{_includedir}/Dolphin/
%{_includedir}/dolphin*_export.h
%{_kf6_libdir}/cmake/DolphinVcs/
%{_kf6_libdir}/libdolphinvcs.so
%{_datadir}/dbus-1/interfaces/org.freedesktop.FileManager1.xml


%changelog
* Tue Jan 07 2025 Steve Cossette <farchord@gmail.com> - 24.12.1-1
- 24.12.1

* Fri Dec 20 2024 Steve Cossette <farchord@gmail.com> - 24.12.0.1-1
- Bugfix release 24.12.0.1

* Sat Dec 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.12.0-1
- 24.12.0

* Fri Nov 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.90-1
- 24.11.90

* Fri Nov 15 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.11.80-1
- 24.11.80

* Tue Nov 05 2024 Steve Cossette <farchord@gmail.com> - 24.08.3-1
- 24.08.3

* Mon Oct 14 2024 Jan Grulich <jgrulich@redhat.com> - 24.08.2-2
- Rebuild (qt6)

* Tue Oct 08 2024 Steve Cossette <farchord@gmail.com> - 24.08.2-1
- 24.08.2

* Wed Sep 25 2024 Alessandro Astone <ales.astone@gmail.com> - 24.08.1-1
- 24.08.1

* Thu Aug 22 2024 Steve Cossette <farchord@gmail.com> - 24.08.0-1
- 24.08.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.05.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jul 07 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.2-1
- 24.05.2

* Fri Jun 14 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.1-1
- 24.05.1

* Fri May 17 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.05.0-1
- 24.05.0

* Fri Apr 12 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.2-1
- 24.02.2

* Thu Apr 04 2024 Jan Grulich <jgrulich@redhat.com> - 24.02.1-2
- Rebuild (qt6)

* Fri Mar 29 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.1-1
- 24.02.1

* Wed Feb 21 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.02.0-1
- 24.02.0

* Fri Feb 16 2024 Jan Grulich <jgrulich@redhat.com> - 24.01.95-2
- Rebuild (qt6)

* Wed Jan 31 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.95-1
- 24.01.95

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 24.01.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 24.01.90-1
- 24.01.90

* Sat Dec 23 2023 ales.astone@gmail.com - 24.01.85-1
- 24.01.85

* Sun Dec 03 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.80-1
- Update to 24.01.80

* Wed Nov 29 2023 Jan Grulich <jgrulich@redhat.com> - 24.01.75-2
- Rebuild (qt6)

* Sat Nov 25 2023 Alessandro Astone <ales.astone@gmail.com> - 24.01.75-1
- 24.01.75
- Requires konsole-part

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sat Sep 16 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.1-1
- 23.08.1

* Sat Aug 26 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.0-1
- 23.08.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 23.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jul 08 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.3-1
- 23.04.3

* Tue Jun 06 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.2-1
- 23.04.2

* Sat May 13 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.1-1
- 23.04.1

* Fri Apr 14 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.04.0-1
- 23.04.0

* Fri Mar 31 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.90-1
- 23.03.90

* Mon Mar 20 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.03.80-1
- 23.03.80

* Thu Mar 02 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 22.12.3-1
- 22.12.3

* Sun Feb 12 2023 Justin Zobel <justin@1707.io> - 22.12.2-2
- Fix FTBFS on Fedora 38

* Tue Jan 31 2023 Marc Deop <marcdeop@fedoraproject.org> - 22.12.2-1
- 22.12.2

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 22.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 03 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Mon Dec 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.12.0-1
- 22.12.0

* Fri Nov 04 2022 Marc Deop i Argemí (Private) <marc@marcdeop.com> - 22.08.3-1
- 22.08.3

* Fri Oct 14 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.2-1
- 22.08.2

* Thu Sep 08 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.1-1
- 22.08.1

* Fri Aug 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.08.0-1
- 22.08.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 22.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 07 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- 22.04.3

* Fri Jun 24 2022 Than Ngo <than@redhat.com> - 22.04.2-1
- 22.04.2

* Thu May 12 2022 Justin Zobel <justin@1707.io> - 22.04.1-1
- Update to 22.04.1

* Mon May 09 2022 Justin Zobel <justin@1707.io> - 22.04.0-1
- Update to 22.04.0

* Wed Mar 02 2022 Marc Deop <marcdeop@fedoraproject.org> - 21.12.3-1
- 21.12.3

* Mon Feb 07 2022 Rex Dieter <rdieter@fedoraproject.org> - 21.12.2.1-1
- 21.12.2.1

* Wed Feb 02 2022 Rex Dieter <rdieter@fedoraproject.org> - 21.12.2-1
- 21.12.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Rex Dieter <rdieter@fedoraproject.org> - 21.12.1-1
- 21.12.1

* Thu Dec 09 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.12.0-1
- 21.12.0

* Tue Nov 02 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.3-1
- 21.08.3

* Fri Oct 15 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.2-1
- 21.08.2

* Wed Sep 01 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.1-2
- Port-to-KTerminalLauncherJob.patch backport

* Wed Sep 01 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.1-1
- 21.08.1

* Tue Aug 10 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.0-2
- respin

* Fri Aug 06 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.0-1
- 21.08.0

* Wed Jul 28 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.3-1
- 21.04.3

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 10 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.2-1
- 21.04.2

* Tue May 11 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.1-1
- 21.04.1

* Mon May 10 2021 Timothée Ravier <travier@redhat.com> - 21.04.0-2
- Recommends dolphin-plugins

* Sat Apr 17 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.0-1
- 21.04.0
- disable daemon_autostart, see how well systemd/user/plasma-dolphin.service works instead

* Tue Mar 02 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.3-1
- 20.12.3

* Tue Feb 02 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.2-1
- 20.12.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.12.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 21 2021 Neal Gompa <ngompa13@gmail.com> - 20.12.1-3
- Recommend kio-fuse to be installed

* Sat Jan 16 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.1-2
- backport knetattach fix (kde#431626)

* Fri Jan 15 14:17:03 CST 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.1-1
- 20.12.1

* Wed Nov  4 13:52:11 CST 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.3-1
- 20.08.3

* Fri Oct 30 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.1-2
- backport dolphin autostart/session-restore fix (kde#417219)

* Tue Sep 15 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.1-1
- 20.08.1

* Mon Aug 17 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.0-1
- 20.08.0

* Mon Aug 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.3-3
- .spec cosmetics

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.3-1
- 20.04.3

* Fri Jun 12 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.2-1
- 20.04.2

* Tue May 26 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.1-1
- 20.04.1

* Thu Apr 23 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.0-1
- 20.04.0

* Thu Mar 05 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.3-1
- 19.12.3

* Tue Feb 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.2-1
- 19.12.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 08 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.1-1
- 19.12.1

* Mon Nov 11 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.3-1
- 19.08.3

* Thu Oct 17 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.2-2
- autostart dolphin on login, remove dbus activation, f31+ (#1394927,#1754395)

* Thu Oct 17 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.2-1
- 19.08.2

* Sat Sep 28 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.1-1
- 19.08.1

* Tue Aug 13 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.0-1
- 19.08.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.3-1
- 19.04.3

* Tue Jun 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.2-1
- 19.04.2

* Tue May 07 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.1-1
- 19.04.1

* Thu Mar 07 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.3-1
- 18.12.3

* Tue Feb 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.2-1
- 18.12.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.1-1
- 18.12.1

* Sat Dec 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.12.0-1
- 18.12.0

* Tue Nov 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.3-1
- 18.08.3

* Wed Oct 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.2-1
- 18.08.2

* Fri Sep 07 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.1-1
- 18.08.1

* Wed Aug 15 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.0-1
- 18.08.0

* Thu Jul 12 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.3-1
- 18.04.3

* Tue Jun 05 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.2-1
- 18.04.2

* Tue May 08 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.1-1
- 18.04.1

* Sat Apr 14 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.0-1
- 18.04.0

* Tue Mar 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.3-1
- 17.12.3

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 17.12.2-2
- Escape macros in %%changelog

* Tue Feb 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.2-1
- 17.12.2

* Thu Jan 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.1-1
- 17.12.1

* Tue Dec 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.12.0-1
- 17.12.0

* Wed Nov 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.3-1
- 17.08.3

* Wed Oct 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.2-1
- 17.08.2

* Tue Sep 05 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.1-1
- 17.08.1

* Sat Aug 26 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.0-1
- 17.08.0

* Sun Aug 06 2017 Björn Esser <besser82@fedoraproject.org> - 17.04.3-2
- Rebuilt for AutoReq cmake-filesystem

* Fri Jul 28 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.3-1
- 17.04.3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.2-1
- 17.04.2

* Wed May 10 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.1-1
- 17.04.1

* Sat Apr 22 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.0-2
- use %%find_lang for HTML handbooks

* Fri Apr 14 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.0-1
- 17.04.0, +translations, cmake-style kf5 deps

* Wed Mar 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.3-1
- 16.12.3

* Wed Feb 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.2-1
- 16.12.2

* Tue Jan 10 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.1-1
- 16.12.1, update URL

* Mon Dec 26 2016 Rex Dieter <rdieter@math.unl.edu> - 16.12.0-1
- 16.12.0, support bootstrap, %%check: enable tests

* Wed Nov 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.3-1
- 16.08.3

* Thu Oct 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.2-1
- 16.08.2

* Tue Sep 06 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.1-1
- 16.08.1

* Thu Sep 01 2016 Rex Dieter <rdieter@fedoraproject.org> 16.08.0-2
- update URL (#1325154)

* Fri Aug 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.0-1
- 16.08.0

* Fri Aug 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.07.90-2
- Recommends: kio-extras (#1366585)

* Sat Aug 06 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.07.90-1
- 16.07.90

* Fri Jul 29 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.07.80-1
- 16.07.80

* Fri Jul 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.3-1
- 16.04.3

* Sun Jun 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.2-1
- 16.04.2

* Sun May 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.1-1
- 16.04.1

* Mon Apr 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.0-1
- 16.04.0

* Sun Mar 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.3-1
- 15.12.3

* Sun Feb 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.2-1
- 15.12.2

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 18 2016 Rex Dieter <rdieter@fedoraproject.org> 15.12.1-2
- cosmetics, tighten BR: baloo-widgets, -BR: cmake

* Mon Jan 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.1-1
- 15.12.1

* Fri Jan 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.0-2
- %%kf5_kinit_requires (#1294982), cosmetics
- libs: move remaining plugins here, drop (arch'd) dep on main pkg

* Sun Dec 20 2015 Rex Dieter <rdieter@fedoraproject.org> 15.12.0-1
- 15.12.0

* Tue Nov 17 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.08.3-1
- 15.08.3

* Tue Sep 15 2015 Rex Dieter <rdieter@fedoraproject.org> - 15.08.1-1
- 15.08.1
- cosmetics, move dolphinpart to -libs
- relax BR on baloo-widgets

* Mon Aug 31 2015 Daniel Vrátil <dvratil@redhat.com> - 15.08.0-1
- Reviving Dolphin stand-alone package (#1258430)
