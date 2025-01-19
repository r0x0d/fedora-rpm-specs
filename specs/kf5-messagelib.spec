%global framework messagelib

Name:    kf5-%{framework}
Version: 23.08.5
Release: 3%{?dist}
Summary: KDE Message libraries

License: BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/pim/%{framework}/

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

## upstream patches

BuildRequires:  cmake(Grantlee5)

BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Positioning)
BuildRequires:  cmake(Qt5Qml) cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5WebChannel)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5Widgets)

BuildRequires:  cmake(Qca-qt5)
BuildRequires:  cmake(QGpgme)

%global kf5_ver 5.28
BuildRequires:  extra-cmake-modules >= %{kf5_ver}
BuildRequires:  kf5-karchive-devel >= %{kf5_ver}
BuildRequires:  kf5-kcodecs-devel >= %{kf5_ver}
BuildRequires:  kf5-kcompletion-devel >= %{kf5_ver}
BuildRequires:  kf5-kconfig-devel >= %{kf5_ver}
BuildRequires:  kf5-ki18n-devel >= %{kf5_ver}
BuildRequires:  kf5-kiconthemes-devel >= %{kf5_ver}
BuildRequires:  kf5-kitemviews-devel >= %{kf5_ver}
BuildRequires:  kf5-ktextwidgets-devel >= %{kf5_ver}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{kf5_ver}
BuildRequires:  kf5-kxmlgui-devel >= %{kf5_ver}
BuildRequires:  kf5-rpm-macros >= %{kf5_ver}

BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KF5TextAutoCorrectionWidgets)

#global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global majmin_ver %{version}
BuildRequires:  kf5-akonadi-mime-devel >= %{majmin_ver}
BuildRequires:  kf5-akonadi-notes-devel >= %{majmin_ver}
BuildRequires:  kf5-akonadi-search-devel >= %{majmin_ver}
BuildRequires:  kf5-grantleetheme-devel >= %{majmin_ver}
BuildRequires:  kf5-kcontacts-devel >= %{majmin_ver}
BuildRequires:  kf5-kidentitymanagement-devel >= %{majmin_ver}
BuildRequires:  kf5-kldap-devel >= %{majmin_ver}
BuildRequires:  kf5-kmailtransport-devel >= %{majmin_ver}
BuildRequires:  kf5-kmbox-devel >= %{majmin_ver}
BuildRequires:  kf5-kmime-devel >= %{majmin_ver}
BuildRequires:  kf5-kpimtextedit-devel >= %{majmin_ver}
BuildRequires:  kf5-libgravatar-devel >= %{majmin_ver}
BuildRequires:  kf5-libkdepim-devel >= %{majmin_ver}
BuildRequires:  kf5-libkleo-devel >= %{majmin_ver}, cmake(QGpgme)
BuildRequires:  kf5-pimcommon-devel >= %{majmin_ver}

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

Obsoletes:      kdepim-libs < 7:16.04.0

# messageviewer_defaultgrantleeheaderstyleplugin.so moved here
Conflicts:      kdepim-addons < 16.12

%description
%{summary}.

%package        libs
Summary:        Only the linkable libraries for %{name}
%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cmake(KF5Akonadi)
Requires:       cmake(KF5AkonadiMime)
Requires:       cmake(KF5Contacts)
Requires:       cmake(KF5IdentityManagement)
Requires:       cmake(KF5Libkleo)
Requires:       cmake(KPim5MessageCore)
Requires:       cmake(KPim5Mime)
Requires:       cmake(KPim5PimCommon)
Requires:       cmake(Qt5WebEngine)
%description    devel
%{summary}.


%prep
%autosetup -n %{framework}-%{version} -p1

# Rename translation files to avoid conflict with KF6
find ./po -type f -name libmessagecomposer.po -execdir mv {} libmessagecomposer5.po \;
find ./po -type f -name libmessagecore.po -execdir mv {} libmessagecore5.po \;
find ./po -type f -name libmessagelist.po -execdir mv {} libmessagelist5.po \;
find ./po -type f -name libmessageviewer.po -execdir mv {} libmessageviewer5.po \;
find ./po -type f -name libmimetreeparser.po -execdir mv {} libmimetreeparser5.po \;
find ./po -type f -name libtemplateparser.po -execdir mv {} libtemplateparser5.po \;
find ./po -type f -name libwebengineviewer.po -execdir mv {} libwebengineviewer5.po \;
sed -i "/TRANSLATION_DOMAIN/ s/libmessagecomposer/libmessagecomposer5/" messagecomposer/src/CMakeLists.txt
sed -i "/TRANSLATION_DOMAIN/ s/libmessagecore/libmessagecore5/" messagecore/src/CMakeLists.txt
sed -i "/TRANSLATION_DOMAIN/ s/libmessagelist/libmessagelist5/" messagelist/src/CMakeLists.txt
sed -i "/TRANSLATION_DOMAIN/ s/libmessageviewer/libmessageviewer5/" messageviewer/src/CMakeLists.txt
sed -i "/TRANSLATION_DOMAIN/ s/libmimetreeparser/libmimetreeparser5/" mimetreeparser/src/CMakeLists.txt
sed -i "/TRANSLATION_DOMAIN/ s/libtemplateparser/libtemplateparser5/" templateparser/src/CMakeLists.txt
sed -i "/TRANSLATION_DOMAIN/ s/libwebengineviewer/libwebengineviewer5/" webengineviewer/src/CMakeLists.txt
sed -i "s/libmessagecomposer/libmessagecomposer5/" messagecomposer/src/Messages.sh
sed -i "s/libmessagecore/libmessagecore5/" messagecore/src/Messages.sh
sed -i "s/libmessagelist/libmessagelist5/" messagelist/src/Messages.sh
sed -i "s/libmessageviewer/libmessageviewer5/" messageviewer/src/Messages.sh
sed -i "s/libmimetreeparser/libmimetreeparser5/" mimetreeparser/Messages.sh
sed -i "s/libtemplateparser/libtemplateparser5/" templateparser/src/Messages.sh
sed -i "s/libwebengineviewer/libwebengineviewer5/" webengineviewer/src/Messages.sh

%build
%cmake_kf5

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html


%ldconfig_scriptlets

%files
%license LICENSES/*
%{_kf5_datadir}/config.kcfg/customtemplates_kfg.kcfg
%{_kf5_datadir}/config.kcfg/templatesconfiguration_kfg.kcfg
%{_kf5_datadir}/knotifications5/messageviewer.notifyrc
%{_kf5_datadir}/knsrcfiles/messageviewer_header_themes.knsrc
%{_kf5_datadir}/libmessageviewer/
%{_kf5_datadir}/messagelist/
%{_kf5_datadir}/messageviewer/
%{_kf5_qtplugindir}/pim5/messageviewer/grantlee/5.0/messageviewer_grantlee_extension.so
%{_kf5_qtplugindir}/pim5/messageviewer/headerstyle/messageviewer_defaultgrantleeheaderstyleplugin.so
## check this -- rex
%dir %{_kf5_datadir}/org.kde.syntax-highlighting/
%{_kf5_datadir}/org.kde.syntax-highlighting/syntax/kmail-template.xml

%files libs -f %{name}.lang
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKPim5MessageComposer.so.*
%{_kf5_libdir}/libKPim5MessageCore.so.*
%{_kf5_libdir}/libKPim5MessageList.so.*
%{_kf5_libdir}/libKPim5MessageViewer.so.*
%{_kf5_libdir}/libKPim5MimeTreeParser.so.*
%{_kf5_libdir}/libKPim5TemplateParser.so.*
%{_kf5_libdir}/libKPim5WebEngineViewer.so.*

%files devel
%{_kf5_archdatadir}/mkspecs/modules/qt_MessageComposer.pri
%{_includedir}/KPim5/MessageComposer/
%{_kf5_libdir}/cmake/KPim5MessageComposer/
%{_kf5_libdir}/libKPim5MessageComposer.so

%{_kf5_archdatadir}/mkspecs/modules/qt_MessageCore.pri
%{_includedir}/KPim5/MessageCore/
%{_kf5_libdir}/cmake/KPim5MessageCore/
%{_kf5_libdir}/libKPim5MessageCore.so

%{_kf5_archdatadir}/mkspecs/modules/qt_MessageList.pri
%{_includedir}/KPim5/MessageList/
%{_kf5_libdir}/cmake/KPim5MessageList/
%{_kf5_libdir}/libKPim5MessageList.so

%{_kf5_archdatadir}/mkspecs/modules/qt_MessageViewer.pri
%{_includedir}/KPim5/MessageViewer/
%{_kf5_libdir}/cmake/KPim5MessageViewer/
%{_kf5_libdir}/libKPim5MessageViewer.so

%{_includedir}/KPim5/MimeTreeParser/
%{_kf5_libdir}/cmake/KPim5MimeTreeParser/
%{_kf5_libdir}/libKPim5MimeTreeParser.so
#{_kf5_archdatadir}/mkspecs/modules/qt_MimeTreeParser.pri

%{_kf5_archdatadir}/mkspecs/modules/qt_TemplateParser.pri
%{_includedir}/KPim5/TemplateParser/
%{_kf5_libdir}/cmake/KPim5TemplateParser/
%{_kf5_libdir}/libKPim5TemplateParser.so

%{_kf5_archdatadir}/mkspecs/modules/qt_WebEngineViewer.pri
%{_includedir}/KPim5/WebEngineViewer/
%{_kf5_libdir}/cmake/KPim5WebEngineViewer/
%{_kf5_libdir}/libKPim5WebEngineViewer.so


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 23.08.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.08.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 24 2024 Alessandro Astone <ales.astone@gmail.com> - 23.08.5-1
- 23.08.5

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.08.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 23.08.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec 21 2023 Alessandro Astone <ales.astone@gmail.com> - 23.08.2-3
- Fix translations and package them in the libs subpackage

* Wed Dec 20 2023 Alessandro Astone <ales.astone@gmail.com> - 23.08.2-2
- Split libs subpackage, to co-install with KF6 libksieve
- Rename translation files to avoid conflict with KF6 libksieve

* Thu Oct 12 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 23.08.2-1
- 23.08.2

* Sun Sep 24 2023 Kevin Kofler <Kevin@tigcc.ticalc.org> - 23.08.1-2
- Rebuild for ktextaddons 1.5.1 (#2239665)
- KF5TextAutoCorrection -> KF5TextAutoCorrectionWidgets (ktextaddons 1.5.1)

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

* Tue Jan 03 2023 Justin Zobel <justin@1707.io> - 22.12.1-1
- Update to 22.12.1

* Mon Dec 19 2022 Marc Deop <marcdeop@fedoraproject.org> - 22.12.0-1
- 22.12.0

* Wed Nov 30 2022 Jiri Kucera <jkucera@redhat.com> - 22.08.3-2
- Rebuild for gpgme 1.17.1

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

* Mon Jul 11 2022 Than Ngo <than@redhat.com> - 22.04.3-1
- 22.04.3

* Thu May 12 2022 Justin Zobel <justin@1707.io> - 22.04.1-1
- Update to 22.04.1

* Mon May 09 2022 Justin Zobel <justin@1707.io> - 22.04.0-1
- Update to 22.04.0

* Wed Mar 02 2022 Marc Deop <marcdeop@fedoraproject.org> - 21.12.3-1
- 21.12.3

* Fri Feb 04 2022 Rex Dieter <rdieter@fedoraproject.org> - 21.12.2-1
- 21.12.2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 21.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 06 2022 Marc Deop <marcdeop@fedoraproject.org> - 21.12.1-1
- 21.12.1

* Mon Dec 20 2021 Marc Deop <marcdeop@fedoraproject.org> - 21.12.0-1
- 21.12.0

* Tue Nov 02 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.3-1
- 21.08.3

* Thu Oct 21 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.08.2-1
- 21.08.2

* Wed Jul 28 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.3-1
- 21.04.3

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 21.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.2-1
- 21.04.2

* Tue May 11 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.1-1
- 21.04.1

* Tue Apr 27 2021 Rex Dieter <rdieter@fedoraproject.org> - 21.04.0-1
- 21.04.0

* Wed Mar 03 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.3-1
- 20.12.3

* Thu Feb 04 2021 Rex Dieter <rdieter@fedoraproject.org> - 20.12.2-1
- 20.12.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20.08.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov  6 15:46:32 CST 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.3-1
- 20.08.3

* Tue Sep 15 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.1-1
- 20.08.1

* Tue Aug 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.0-1
- 20.08.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.3-1
- 20.04.3

* Fri Jun 12 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.2-1
- 20.04.2

* Wed May 27 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.1-1
- 20.04.1

* Fri Apr 24 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.0-1
- 20.04.0

* Sat Mar 07 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.3-1
- 19.12.3
- BR: qca-qt5

* Tue Feb 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.2-1
- 19.12.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.1-1
- 19.12.1

* Mon Nov 11 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.3-1
- 19.08.3

* Fri Oct 18 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.2-1
- 19.08.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.3-1
- 19.04.3

* Wed Jun 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.2-1
- 19.04.2

* Fri Mar 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.3-1
- 18.12.3

* Tue Feb 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.2-1
- 18.12.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.1-1
- 18.12.1

* Fri Dec 14 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.12.0-1
- 18.12.0

* Wed Nov 28 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.3-2
- CVE-2018-19516: messagelib: HTML email can open browser window automatically

* Tue Nov 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.3-1
- 18.08.3

* Wed Oct 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.2-1
- 18.08.2

* Mon Oct 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.1-1
- 18.08.1

* Fri Jul 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.3-1
- 18.04.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.2-1
- 18.04.2

* Wed May 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.1-1
- 18.04.1

* Fri Apr 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.0-1
- 18.04.0

* Tue Mar 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.3-1
- 17.12.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Feb 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.2-1
- 17.12.2

* Thu Jan 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.1-1
- 17.12.1

* Tue Dec 12 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.12.0-1
- 17.12.0

* Wed Dec 06 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.11.90-1
- 17.11.90

* Wed Nov 22 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.11.80-1
- 17.11.80

* Wed Nov 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.3-1
- 17.08.3

* Mon Sep 25 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.1-1
- 17.08.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Fri Jul 28 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.3-1
- 17.04.3

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.2-1
- 17.04.2

* Mon May 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.1-1
- 17.04.1

* Thu Mar 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.3-1
- 16.12.3

* Thu Feb 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.2-1
- 16.12.2

* Mon Jan 16 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.1-1
- 16.12.1

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 16.08.3-2
- Rebuild for gpgme 1.18

* Mon Dec 05 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.3-1
- 16.08.3

* Fri Oct 28 2016 Than Ngo <than@redhat.com> - 16.08.2-2
- don't build on ppc64/s390x as qtwebengine is not supported yet

* Thu Oct 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.2-1
- 16.08.2

* Mon Oct 10 2016 Than Ngo <than@redhat.com> - 16.08.1-3
- CVE-2016-7967, JavaScript access to local and remote URLs (bz#1383610, bz#1382288)
- CVE-2016-7968, JavaScript execution in HTML Mails (bz#1382293, bz#1383959)

* Thu Sep 15 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.1-2
- pull in upstream fixes, including crasher fix for kde#364994

* Thu Sep 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.1-1
- 16.08.1

* Sun Sep 04 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.0-1
- 16.08.0, Conflicts: kdepim-addons < 16.07

* Sun Jul 10 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.3-1
- 16.04.3

* Sun Jun 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.2-1
- 16.04.2

* Wed May 25 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.1-1
- First try
