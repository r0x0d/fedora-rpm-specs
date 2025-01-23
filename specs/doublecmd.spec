%global debug_package %{nil}

Name:           doublecmd
Version:        1.1.22
Release:        1%{?dist}
Summary:        Cross platform open source file manager with two panels

# Full licenses description in licensecheck.txt file
License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND MIT AND MPL-1.1 AND MPL-2.0 AND Apache-2.0 AND BSD-2-Clause AND Zlib
URL:            http://doublecmd.sourceforge.net
Source0:        https://sourceforge.net/projects/%{name}/files/Double%20Commander%20Source/%{name}-%{version}-src.tar.gz
Source1:        %{name}-qt.desktop
Source2:        licensecheck.txt
Source3:        io.sourceforge.DoubleCmd.DoubleCmdGtk.metainfo.xml
Source4:        io.sourceforge.DoubleCmd.DoubleCmdQt.metainfo.xml
Source5:        %{name}-qt6.desktop

BuildRequires:  fpc >= 2.6.0
BuildRequires:  fpc-src
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  lazarus >= 1.0.0
BuildRequires:  lazarus-lcl-gtk2
BuildRequires:  lazarus-lcl-qt5
BuildRequires:  lazarus-lcl-qt6
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  util-linux
BuildRequires:  pkgconfig(pango)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

ExclusiveArch:  %{ix86} x86_64

%description
Double Commander GTK2 is a cross platform open source file manager with two
panels side by side.
It is inspired by Total Commander and features some new ideas.

%package        gtk
Summary:        Twin-panel (commander-style) file manager (GTK)
Group:          File tools
Requires:       %{name}-common%{?_isa} = %{version}-%{release}

%description    gtk
Double Commander GTK is a cross platform open source file manager with two
panels side by side.
It is inspired by Total Commander and features some new ideas.

%package        qt
Summary:        Twin-panel (commander-style) file manager (Qt5)
Group:          File tools
Requires:       %{name}-common%{?_isa} = %{version}-%{release}

%description    qt
Double Commander QT6 is a cross platform open source file manager with two
panels side by side.
It is inspired by Total Commander and features some new ideas.

%package        qt6
Summary:        Twin-panel (commander-style) file manager (Qt6)
Group:          File tools
Requires:       %{name}-common%{?_isa} = %{version}-%{release}

%description    qt6
Double Commander QT6 is a cross platform open source file manager with two
panels side by side.
It is inspired by Total Commander and features some new ideas.

%package        common
Summary:        Common files for Double Commander

Requires:       hicolor-icon-theme
Requires:       polkit%{?_isa}

%description    common
Common files for Double Commander GTK2 and Qt.

%prep
%autosetup -p0
# Sure to not use libbz2 and libssh2 bundling
rm -rf libraries


%build
lcl=qt5 ./build.sh beta
mv ./%name ./%name-qt
mv ./%name.zdli ./%name-qt.zdli
./clean.sh

lcl=qt6 ./build.sh beta
mv ./%name ./%name-qt6
mv ./%name.zdli ./%name-qt6.zdli
./clean.sh

lcl=gtk2 ./build.sh beta

%install
install/linux/install.sh --install-prefix=%{buildroot}
install -pm 0755 ./%{name}-qt %{buildroot}%{_libdir}/%{name}/%{name}-qt
ln -s ../%{_lib}/%{name}/%{name}-qt %{buildroot}%{_bindir}/%{name}-qt
install -pm 0644 ./%{name}-qt.zdli %{buildroot}%{_libdir}/%{name}/%{name}-qt.zdli
install -pm 0755 ./%{name}-qt6 %{buildroot}%{_libdir}/%{name}/%{name}-qt6
ln -s ../%{_lib}/%{name}/%{name}-qt6 %{buildroot}%{_bindir}/%{name}-qt6
install -pm 0644 ./%{name}-qt6.zdli %{buildroot}%{_libdir}/%{name}/%{name}-qt6.zdli
desktop-file-install %{SOURCE1}
desktop-file-install %{SOURCE5}
cp %{SOURCE2} .
install -D -p -m644 %{SOURCE3} %{buildroot}%{_metainfodir}/io.sourceforge.DoubleCmd.DoubleCmdGtk.metainfo.xml
install -D -p -m644 %{SOURCE4} %{buildroot}%{_metainfodir}/io.sourceforge.DoubleCmd.DoubleCmdQt.metainfo.xml
install -D -p -m644 %{SOURCE4} %{buildroot}%{_metainfodir}/io.sourceforge.DoubleCmd.DoubleCmdQt6.metainfo.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-qt.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-qt6.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/io.sourceforge.DoubleCmd.DoubleCmdGtk.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/io.sourceforge.DoubleCmd.DoubleCmdQt.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/io.sourceforge.DoubleCmd.DoubleCmdQt6.metainfo.xml


%files gtk
%{_libdir}/%{name}/%{name}
%{_bindir}/%{name}
%{_libdir}/%{name}/%{name}.zdli
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/io.sourceforge.DoubleCmd.DoubleCmdGtk.metainfo.xml


%files qt
%{_libdir}/%{name}/%{name}-qt
%{_bindir}/%{name}-qt
%{_libdir}/%{name}/%{name}-qt.zdli
%{_datadir}/applications/%{name}-qt.desktop
%{_metainfodir}/io.sourceforge.DoubleCmd.DoubleCmdQt.metainfo.xml

%files qt6
%{_libdir}/%{name}/%{name}-qt6
%{_bindir}/%{name}-qt6
%{_libdir}/%{name}/%{name}-qt6.zdli
%{_datadir}/applications/%{name}-qt6.desktop
%{_metainfodir}/io.sourceforge.DoubleCmd.DoubleCmdQt6.metainfo.xml

%files common
%doc doc/changelog.txt doc/README.txt licensecheck.txt
%license doc/COPYING.LGPL.txt doc/COPYING.modifiedLGPL.txt doc/COPYING.txt
%exclude %{_libdir}/%{name}/%{name}
%exclude %{_libdir}/%{name}/%{name}-qt
%exclude %{_libdir}/%{name}/%{name}-qt6
%exclude %{_libdir}/%{name}/%{name}.zdli
%exclude %{_libdir}/%{name}/%{name}-qt.zdli
%exclude %{_libdir}/%{name}/%{name}-qt6.zdli
%exclude %{_bindir}/%{name}
%exclude %{_bindir}/%{name}-qt
%exclude %{_bindir}/%{name}-qt6
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/icons/hicolor/scalable/apps/doublecmd.svg
%{_datadir}/polkit-1/actions/org.doublecmd.root.policy

%changelog
* Tue Jan 21 2025 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.22-1
- Update to 1.1.22

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan 09 2025 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.21-1
- Update to 1.1.21

* Mon Nov 11 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.20-1
- Update to 1.1.20

* Mon Oct 07 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.19-1
- Update to 1.1.19

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 02 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.16-1
- Update to 1.1.16
- Fix #2295133

* Tue Jun 18 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.15-1
- Update to 1.1.15
- Add Qt6 build

* Mon Apr 08 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.12-1
- Update to 1.1.12

* Fri Mar 15 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.11-1
- Update to 1.1.11

* Tue Feb 20 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.10-1
- Update to 1.1.10

* Wed Jan 24 2024 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.9-1
- Update to 1.1.9

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Dec 26 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.8-1
- Update to 1.1.8

* Mon Dec 04 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.7-1
- Update to 1.1.7

* Tue Nov 21 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.6-1
- Update to 1.1.6

* Mon Nov 13 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 1.1.5-1
- Update to 1.1.5
- Fixed BRs thanks to suve

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jul 06 2023 Daniel Rusek <mail@asciiwolf.com> - 1.0.11-2
- Add AppStream metadata

* Mon Apr 03 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.11-1
- Update to 1.0.11

* Mon Jan 23 2023 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.10-1
- Update to 1.0.10

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 05 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.9-1
- Update to 1.0.9

* Mon Sep 19 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.8-1
- Update to 1.0.8

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 06 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.6-1
- Update to 1.0.6

* Mon Apr 11 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.5-1
- Update to 1.0.5

* Wed Feb 09 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.4-1
- Update to 1.0.4

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 11 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.3-1
- Update to 1.0.3

* Wed Jan 05 2022 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.2-2
- Fix license

* Mon Dec 13 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.2-1
- Update to 1.0.2

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 10 2021 Vasiliy N. Glazov <vascom2@gmail.com> - 0.9.10-1
- Update to 0.9.10

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 28 2020 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.9-1
- Update to 0.9.9

* Tue May 19 2020 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.8-1
- Update to 0.9.8

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 09 2020 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.7-1
- Update to 0.9.7

* Fri Oct 18 2019 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6-3
- Added licensecheck.txt file

* Tue Oct 15 2019 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6-2
- Corrected license and spec cleanup

* Fri Oct 11 2019 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6-1
- Update to 0.9.6

* Tue Aug 13 2019 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.5-1
- Update to 0.9.5

* Wed Aug 29 2018 Vasiliy N. Glazov <vascom2@gmail.com> 0.8.4-1
- Update to 0.8.4

* Thu Dec 14 2017 Vasiliy N. Glazov <vascom2@gmail.com> 0.8.3-1
- Update to 0.8.3

* Thu Dec 14 2017 Vasiliy N. Glazov <vascom2@gmail.com> 0.8.2-1
- Update to 0.8.2

* Thu Dec 14 2017 Vasiliy N. Glazov <vascom2@gmail.com> 0.8.0-1
- Update to 0.8.0

* Mon Mar 06 2017 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.8-1
- Update to 0.7.8

* Mon Dec 26 2016 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.7-1
- Update to 0.7.7

* Fri Sep 16 2016 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.5-1
- Update to 0.7.5

* Fri Jul 15 2016 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.3-1
- Update to 0.7.3

* Fri Jun 03 2016 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.2-1
- Update to 0.7.2

* Thu Apr 21 2016 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.1-1
- Update to 0.7.1

* Mon Mar 14 2016 Vasiliy N. Glazov <vascom2@gmail.com> 0.7.0-1
- Update to 0.7.0

* Thu Nov 19 2015 Vasiliy N. Glazov <vascom2@gmail.com> 0.6.6-1
- Update to 0.6.6
- One spec for GTK and Qt version

* Fri Oct 09 2015 Vasiliy N. Glazov <vascom2@gmail.com> 0.6.5-1
- Update to 0.6.5

* Tue Feb 10 2015 Vasiliy N. Glazov <vascom2@gmail.com> 0.6.0-1
- Update to 0.6.0

* Wed Oct 12 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.5.0-svn3993.1.R
- Update to new revision

* Tue Aug 30 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.5.0-svn3926.1.R
- Update to new revision

* Tue Aug 30 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.5.0-svn3860.1.R
- Update to new revision

* Mon Aug 08 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.5.5-svn3789.2.R
- Added documentation package

* Mon Aug 08 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.5.5-svn3789.1.R
- Removed .svn files
- Update svn to 3789

* Thu Jul  28 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.5.5-svn3765.2.R
- Split packages
- Clean spec

* Thu Jul  28 2011 Vasiliy N. Glazov <vascom2@gmail.com> 0.5.5-svn3765.1.R
- Initial build for Fedora

* Fri Jun 11 2010 - Alexander Koblov <Alexx2000@mail.ru>
- Initial package, version 0.4.6
