Name:              gcin
Version:           2.9.0
Release:           16%{?dist}
Summary:           An input method focused on Chinese users
#Main program is LGPLv2;
#eggtrayicon.cpp eggtrayicon.h are LGPLv2+;
#Files under qt-im are GPLv2 or QPL;
#Tables has files under Array;
# Automatically converted from old format: LGPLv2+ and (QPL or GPLv2) and MIT and Array - review is highly recommended.
License:           LicenseRef-Callaway-LGPLv2+ AND (QPL-1.0 OR GPL-2.0-only) AND LicenseRef-Callaway-MIT AND LicenseRef-Array
URL:               http://hyperrate.com/dir.php?eid=67
Source0:           http://hyperrate.com/gcin-source/%{name}-%{version}.tar.xz
Source1:           %{name}.conf
Patch0:            0002-Fix-FTBFS-on-big-endian.patch
Patch1:            0003-C99-Fixes.patch
BuildRequires:     gcc-c++
BuildRequires:     anthy-devel
BuildRequires:     desktop-file-utils
BuildRequires:     gettext
BuildRequires:     gtk2-devel
BuildRequires:     gtk3-devel
BuildRequires:     libXtst-devel
BuildRequires:     qt4-devel
BuildRequires:     libcurl-devel
Requires:          %{name}-data = %{version}-%{release}
Requires:          %{name}-libs = %{version}-%{release}
Requires:          %{name}-table = %{version}-%{release}
Requires:          imsettings
Requires(post):    %{_sbindir}/alternatives
Requires(postun):  %{_sbindir}/alternatives

%description
Gcin is an input method with support of Gtk and Qt. Although gcin is focused 
mainly on Traditional Chinese. However, it is also very useful for 
Simplified Chinese, Japanese, and many other languages.

%package           anthy
Summary:           Anthy support for %{name}
Requires:          %{name}%{?_isa} = %{version}-%{release}

%description       anthy
The package provides Japanese input implementation with Anthy library.

%package           data
Summary:           Data files for %{name}
Requires:          %{name} = %{version}-%{release}
Requires:          hicolor-icon-theme
BuildArch:         noarch

%description       data
The package provides shared data for %{name}.

%package           gtk2
Summary:           Gtk2 IM module for %{name}
Requires:          gtk2
Requires:          %{name}%{?_isa} = %{version}-%{release}
Requires:          %{name}-im-client%{?_isa} = %{version}-%{release}
Requires:          %{name}-libs%{?_isa} = %{version}-%{release}

%description       gtk2
The package provides Gtk2 IM module for %{name}.

%package           gtk3
Summary:           Gtk3 IM module for %{name}
Requires:          gtk3
Requires:          %{name}%{?_isa} = %{version}-%{release}
Requires:          %{name}-im-client%{?_isa} = %{version}-%{release}
Requires:          %{name}-libs%{?_isa} = %{version}-%{release}

%description       gtk3
The package provides Gtk3 IM module for %{name}.

%package           im-client
Summary:           Im client library for %{name}
Requires:          gtk2%{?_isa}
Requires:          %{name}%{?_isa} = %{version}-%{release}

%description       im-client
The package provides im client library for %{name}.

%package           libs
Summary:           Shared libraries for %{name}
Requires:          %{name}-im-client%{?_isa} = %{version}-%{release}

%description       libs
The package provides shared libraries for %{name}.

%package           qt4
Summary:           Qt4 IM module for %{name}
Obsoletes:         %{name}-qt3 < %{version}-%{release}
Requires:          qt4
Requires:          %{name}%{?_isa} = %{version}-%{release}
Requires:          %{name}-im-client%{?_isa} = %{version}-%{release}
Requires:          %{name}-libs%{?_isa} = %{version}-%{release}

%package           qt5
Summary:           Qt5 IM module for %{name}
Obsoletes:         %{name}-qt4 < %{version}-%{release}
BuildRequires:     qt5-qtbase-devel
BuildRequires:     qt5-qtbase-static
# uses private apis
BuildRequires: qt5-qtbase-private-devel
BuildRequires: make
Requires:          %{name}%{?_isa} = %{version}-%{release}
Requires:          %{name}-im-client%{?_isa} = %{version}-%{release}
Requires:          %{name}-libs%{?_isa} = %{version}-%{release}

%description       qt4
The package provides Qt4 IM module for %{name}.

%description       qt5
The package provides Qt5 IM module for %{name}.

%package           table
Summary:           Table Engines for %{name}
Requires:          %{name} = %{version}-%{release}
Requires:          %{name}-libs = %{version}-%{release}
Requires:          %{name}-data = %{version}-%{release}
BuildArch:         noarch

%description       table
This package contains table engines for %{name}.

%prep
%autosetup -p1
sed -i.strip -e 's|install[ \t][ \t]*-s|install|' Makefile
find . -type f -executable -regex ".*\.\(cpp\|h\)" -exec chmod 0644 "{}" \;

%build
%configure --prefix=%{_prefix} --use_i18n=Y
make OPTFLAGS="%{optflags}"

%install
%make_install
mkdir -p %{buildroot}%{_sysconfdir}/X11/xinit/xinput.d
install -pDm644 %{S:1} %{buildroot}%{_sysconfdir}/X11/xinit/xinput.d/%{name}.conf
mkdir -p %{buildroot}%{_mandir}/man1
install -pm644 man/*.1 %{buildroot}%{_mandir}/man1
rm -rf %{buildroot}%{_datadir}/doc/

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/gcin-tools.desktop

%post
alternatives --install %{_sysconfdir}/X11/xinit/xinputrc xinputrc %{_sysconfdir}/X11/xinit/xinput.d/%{name}.conf 40

%post             data
touch --no-create %{_datadir}/icons/%{name} &>/dev/null || :

%posttrans        data
gtk-update-icon-cache %{_datadir}/icons/%{name} &>/dev/null || :

%postun
if [ $1 -eq 0 ]; then
    alternatives --remove xinputrc %{_sysconfdir}/X11/xinit/xinput.d/%{name}.conf >/dev/null 2>&1 || :
   [ -L %{_sysconfdir}/alternatives/xinputrc -a "`readlink %{_sysconfdir}/alternatives/xinputrc`" = "%{_xinputconf}" ] && alternatives --auto xinputrc || :
fi

%postun           data
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/%{name} &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/%{name} &>/dev/null
fi

%files -f %{name}.lang
%doc AUTHORS {Changelog,README}.html
%license COPYING
%config(noreplace) %{_sysconfdir}/X11/xinit/xinput.d/%{name}.conf
%{_bindir}/%{name}*
%{_bindir}/gtab*
%{_bindir}/juyin-learn
%{_bindir}/pho*
%{_bindir}/sim2trad
%{_bindir}/txt2gtab-phrase
%{_bindir}/trad2sim
%{_bindir}/ts*
%{_datadir}/applications/gcin-tools.desktop
%{_mandir}/man1/*.1*
%dir %{_datadir}/%{name}
%dir %{_libdir}/%{name}

%files            anthy
%{_libdir}/%{name}/anthy-module.so

%files            data
%{_datadir}/%{name}/script/
%{_datadir}/icons/%{name}/
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png

%files            im-client
%{_libdir}/%{name}/libgcin-im-client.so
%{_libdir}/%{name}/libgcin-im-client.so.*

%files            libs
%{_libdir}/%{name}/intcode-module.so
%{_libdir}/%{name}/%{name}*.so

%files            gtk2
%{_libdir}/gtk-2.0/immodules/im-gcin.so

%files            gtk3
%{_libdir}/gtk-3.0/immodules/im-gcin.so

%files            qt4
%{_libdir}/qt4/plugins/inputmethods/im-gcin.so

%files            qt5
%{_libdir}/qt5/plugins/platforminputcontexts/libgcinplatforminputcontextplugin.so

%files            table
%{_datadir}/%{name}/table/

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.9.0-15
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 10 2023 Peter Fordham <peter.fordham@gmail.com> - 2.9.0-9
- Fix various C99 compliance issues.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Jan Grulich <jgrulich@redhat.com> - 2.9.0-7
- Rebuild (qt5)

* Tue May 17 2022 Jan Grulich <jgrulich@redhat.com> - 2.9.0-6
- Rebuild (qt5)

* Tue Mar 08 2022 Jan Grulich <jgrulich@redhat.com> - 2.9.0-5
- Rebuild (qt5)

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Nov 28 2020 Zamir SUN <sztsian@gmail.com> - 2.9.0-1
- Update to 2.9.0

* Fri Nov 27 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.8.9-8
- drop hard-coded Qt5 runtime dependency

* Mon Nov 23 07:52:23 CET 2020 Jan Grulich <jgrulich@redhat.com> - 2.8.9-7
- rebuild (qt5)

* Fri Sep 11 2020 Jan Grulich <jgrulich@redhat.com> - 2.8.9-6
- rebuild (qt5)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.8.9-4
- rebuild (qt5)

* Thu Feb 20 2020 Robin Lee <cheeselee@fedoraproject.org> - 2.8.9-3
- Fix multiple definition errors (RHBZ#1799389)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Jan Grulich <jgrulich@redhat.com> - 2.8.9-2
- rebuild (qt5)

* Wed Oct 02 2019 Zamir SUN <sztsian@gmail.com> - 2.8.9-1
- Update to 2.8.9

* Wed Sep 25 2019 Jan Grulich <jgrulich@redhat.com> - 2.8.6-7
- rebuild (qt5)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 17 2019 Jan Grulich <jgrulich@redhat.com> - 2.8.6-5
- rebuild (qt5)

* Wed Jun 05 2019 Jan Grulich <jgrulich@redhat.com> - 2.8.6-4
- rebuild (qt5)

* Sun Apr 28 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.8.6-3
- fix runtime qt5 deps, track private api usage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Zamir SUN <sztsian@gmail.com> - 2.8.6-1
- Update to upstream 2.8.6

* Mon Jul 23 2018 Zamir SUN <sztsian@gmail.com> - 2.8.5-7
- Fix FTBFS by remove smp flags

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Robin Lee <cheeselee@fedoraproject.org> - 2.8.5-5
- BR gcc-c++ for http://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Sun Feb 25 2018 Zamir SUN <sztsian@gmail.com> - 2.8.5-4
- Fix xinput config XIM_ARGS.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Zamir SUN <sztsian@gmail.com> - 2.8.5-2
- Fix big-endian build failure

* Tue Jan 09 2018 Zamir SUN <sztsian@gmail.com> - 2.8.5-1
- Update to upstream 2.8.5
- Add Qt5 support

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 12 2014 Christopher Meng <rpm@cicku.me> - 2.8.2-1
- Update to 2.8.2
- Drop Qt3 support.

* Mon Aug 26 2013 Jon Ciesla <limburgher@gmail.com> - 2.8.1-4
- libmng rebuild.

* Mon Aug 05 2013 Christopher Meng <rpm@cicku.me> - 2.8.1-3
- Fix FTBFS(BZ#).

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Christopher Meng <rpm@cicku.me> - 2.8.1-1
- Update to 2.8.1

* Wed Jul 03 2013 Christopher Meng <rpm@cicku.me> - 2.8.0-4
- Correct the License.
- Correct the gtk scripts.

* Tue Jul 02 2013 Christopher Meng <rpm@cicku.me> - 2.8.0-3
- Small fix.

* Tue Jul 02 2013 Christopher Meng <rpm@cicku.me> - 2.8.0-2
- Qt3 path fix.

* Mon Jul 01 2013 Christopher Meng <rpm@cicku.me> - 2.8.0-1
- Major upgrade.
- SPEC rework.
- XInput conf rework.

* Mon Apr 08 2013 Jon Ciesla <limburgher@gmail.com> - 1.6.1-6
- Drop desktop vendor tag.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.6.1-2
- Rebuild for new libpng

* Tue May 03 2011 Parag Nemade <paragn AT fedoraproject.org> - 1.6.1-1
- update to latest stable release 1.6.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 09 2010 Parag Nemade <paragn AT fedoraproject.org> - 1.5.5-4
- Resolves:rh#660992-FTBFS gcin-1.5.5-3.fc15

* Tue Sep 07 2010 Parag Nemade <paragn AT fedoraproject.org> - 1.5.5-3
- update to latest stable release 1.5.5
- Fix gtk-im module Makefile issue 

* Tue Jun 29 2010 Chung-Yen Chang <candyz0416@gmail.com> - 1.5.5.pre3-2
- update to 1.5.5.pre3

* Wed Jun 23 2010 Chung-Yen Chang <candyz0416@gmail.com> - 1.5.1-1
- update to 1.5.1

* Wed Jun 23 2010 Chung-Yen Chang <candyz0416@gmail.com> - 1.5.0-2
- update to 1.5.0

* Wed Jun 23 2010 Chung-Yen Chang <candyz0416@gmail.com> - 1.5.0-1
- update to 1.5.0

* Wed May 05 2010 Chung-Yen Chang <candyz0416@gmail.com> - 1.4.6-2
- patch to add -lm to LDFLAGS
- patch to stop using GTK+ deprecated AP

* Tue Jan 05 2010 Chung-Yen Chang <candyz0416@gmail.com> - 1.4.6-1
- update to 1.4.6

* Fri Nov 27 2009 Chung-Yen Chang <candyz0416@gmail.com> - 1.4.5-6
- fix No icon for im-chooser (#468829)

* Tue Nov 24 2009 Chung-Yen Chang <candyz0416@gmail.com> - 1.4.5-5
- fix No icon for im-chooser (#468829)

* Mon Nov 16 2009 Chung-Yen Chang <candyz0416@gmail.com> - 1.4.5-4
- Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu May 07 2009 Chung-Yen Chang <candyz0416@gmail.com> - 1.4.5-2
- remove gtk_bug_fix.so and rebuild

* Thu May 07 2009 Chung-Yen Chang <candyz0416@gmail.com> - 1.4.5-1
- update to 1.4.5

* Tue Mar 31 2009 Michael Schwendt <mschwendt@fedoraproject.org> - 1.4.4-5
- fix unowned directory (#473616)

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 04 2009 Chung-Yen Chang <candyz0416@gmail.com> - 1.4.4-3
- rename Changelog to Changelog.html

* Wed Feb 04 2009 Chung-Yen Chang <candyz0416@gmail.com> - 1.4.4-2
- rename README to README.html

* Wed Feb 04 2009 Chung-Yen Chang <candyz0416@gmail.com> - 1.4.4-1
- update to 1.4.4

* Tue Oct 21 2008 Jens Petersen <petersen@redhat.com> - 1.4.2-4
- add gcin-1.4.2-gtk-immodules-lang.patch to not enable gcin gtk immodule for all
  langs (#453093)
- spec file cleanup
- update xinput conf file to set icon and setup program (#456512)

* Mon Sep 29 2008 Jens Petersen <petersen@redhat.com> - 1.4.2-3
- update im-client.patch to fix patch fuzz

* Fri Jun 27 2008 Chung-Yen Chang <candyz0416@gmail.com> - 1.4.2-2
- update gcin.conf (change gcin to /usr/bin/gcin)
- add imsettings to Requires
- fix bug #453085

* Thu Jun 26 2008 Chung-Yen Chang <candyz0416@gmail.com> - 1.4.2-1
- update to 1.4.2

* Fri Jun 20 2008 Chung-Yen Chang <candyz0416@gmail.com> - 1.4.1-1
- update to 1.4.1

* Wed May 21 2008 Chung-Yen Chang <candyz0416@gmail.com> - 1.4.0-1
- update to 1.4.0

* Sat May 17 2008 Chung-Yen Chang <candyz0416@gmail.com> - 1.3.9-3
- add /bin/sh /bin/bash to requires

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3.9-2
- Autorebuild for GCC 4.3

* Wed Jan 30 2008 Chung-Yen Chang <candyz0416@gmail.com> - 1.3.9-1
- update to 1.3.9

* Wed Jan 23 2008 Chung-Yen Chang <candyz0416@gmail.com> - 1.3.8-1
- update to 1.3.8

* Tue Nov 27 2007 Chung-Yen Chang <candyz0416@gmail.com> - 1.3.7.1-1
- update to 1.3.7.1

* Mon Oct 15 2007 Chung-Yen Chang <candyz0416@gmail.com> - 1.3.5-2
- update im-client.patch and newcj3.patch

* Sun Oct 14 2007 Chung-Yen Chang <candyz0416@gmail.com> - 1.3.5-1
- update to 1.3.5

* Thu Sep 20 2007 Chung-Yen Chang <candyz0416@gmail.com> - 1.3.4-3
- update license field to LGPLv2
- add im-chooser to require

* Tue Apr 17 2007 Chung-Yen Chang <candyz0416@gmail.com> - 1.3.4-2
- disable i18n and do not make po

* Tue Apr 17 2007 Chung-Yen Chang <candyz0416@gmail.com> - 1.3.4-1
- update to 1.3.4

* Tue Jan 30 2007 Chung-Yen Chang <candyz0416@gmail.com> - 1.3.3-1
- update to 1.3.3

* Mon Jan 01 2007 Chung-Yen Chang <candyz0416@gmail.com> - 1.3.2-1
- update to 1.3.2

* Sun Dec 03 2006 Chung-Yen Chang <candyz0416@gmail.com> - 1.3.1-1
- update to 1.3.1

* Thu Nov 23 2006 Chung-Yen Chang <candyz0416@gmail.com> - 1.3.0.1-2
- rebuild

* Thu Nov 23 2006 Chung-Yen Chang <candyz0416@gmail.com> - 1.3.0.1-1
- update to 1.3.0.1

* Fri Nov 17 2006 Chung-Yen Chang <candyz0416@gmail.com> - 1.2.9-3
- add gcin129update.patch

* Fri Nov 17 2006 Chung-Yen Chang <candyz0416@gmail.com> - 1.2.9-2
- update NewCJ3.cin

* Wed Nov 15 2006 Chung-Yen Chang <candyz0416@gmail.com> - 1.2.9-1
- update to 1.2.9
- add NewCJ3.cin

* Fri Oct 20 2006 Chung-Yen Chang <candyz0416@gmail.com> - 1.2.8-1
- update to 1.2.8

* Mon Oct 09 2006 Chung-Yen Chang <candyz0416@gmail.com> - 1.2.7-1
 - update to 1.2.7

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 1.2.6-2
 - rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Tue Sep 26 2006 Chung-Yen Chang <candyz0416@gmail.com> - 1.2.6-1
- update to 1.2.6

* Fri Sep 15 2006 Chung-Yen Chang <candyz0416@gmail.com> - 1.2.5-2
- rebuild

* Fri Sep 08 2006 Chung-Yen Chang <candyz0416@gmail.com> - 1.2.5-1
- update to 1.2.5
- add icons

* Tue Sep 05 2006 Chung-Yen Chang <candyz0416@gmail.com> - 1.2.4-1
- update to 1.2.4

* Fri Sep 01 2006 Chung-Yen Chang <candyz0416@gmail.com> - 1.2.3-3
- make tag and make build again

* Fri Sep 01 2006 Chung-Yen Chang <candyz0416@gmail.com> - 1.2.3-2
- make new-sources to upload new source tarball

* Fri Sep 01 2006 Chung-Yen Chang <candyz0416@gmail.com> - 1.2.3-1
- update to 1.2.3

* Tue Aug 29 2006 Chung-Yen Chang <candyz0416@gmail.com> - 1.2.2-13
- typo fix

* Thu Aug 24 2006 Chung-Yen Chang <candyz@cle.linux.org.tw> - 1.2.2-12
- modify spec file only for fc5 and later (branch the spec file)

* Thu Aug 24 2006 Chung-Yen Chang <candyz@cle.linux.org.tw> - 1.2.2-11
- fix to handle fedora tag correctly

* Thu Aug 24 2006 Chung-Yen Chang <candyz@cle.linux.org.tw> - 1.2.2-10
- Remove patch5 (not necessary)

* Wed Aug 23 2006 Chung-Yen Chang <candyz@cle.linux.org.tw> - 1.2.2-9
- Fix patch5 for fc3 only bug

* Sun Aug 20 2006 Chung-Yen Chang <candyz@cle.linux.org.tw> - 1.2.2-8
- Fix changelog

* Sun Aug 20 2006 Chung-Yen Chang <candyz@cle.linux.org.tw> - 1.2.2-7
- Remove -devel subpackage
- install desktop file

* Sat Aug 19 2006 Chung-Yen Chang <candyz@cle.linux.org.tw> - 1.2.2-6
- a few more fixes from Jens Petersen

* Sat Aug 19 2006 Chung-Yen Chang <candyz@cle.linux.org.tw> - 1.2.2-5
- improvements from Jens Petersen:
- don't use configure macro
- add .conf suffix to xinput.d file and update install scripts for fc6
- move lib to libdir and drop ld.so.conf.d file
- other minor cleanup

* Sat Aug 19 2006 Chung-Yen Chang <candyz@cle.linux.org.tw> - 1.2.2-4
- rebuild 1.2.2-4

* Fri Aug 18 2006 Chung-Yen Chang <candyz@cle.linux.org.tw> - 1.2.2-3
- Add COPYING Changelog to doc
- Use Dist Tag

* Fri Aug 18 2006 Chung-Yen Chang <candyz@cle.linux.org.tw> - 1.2.2-2
- fix x86_64 problems

* Thu Aug 17 2006 Chung-Yen Chang <candyz@cle.linux.org.tw> - 1.2.2-1
- rebuild 1.2.2-1

* Thu Aug 17 2006 Chung-Yen Chang <candyz@cle.linux.org.tw> - 1.2.1-7
- rebuild 1.2.1-7

* Wed Aug 16 2006 Chung-Yen Chang <candyz@cle.linux.org.tw> - 1.2.1-4
- rebuild 1.2.1-4

* Thu Jul 13 2006 Chung-Yen Chang <candyz@cle.linux.org.tw> - 1.2.1-1
- update to 1.2.1

* Mon May 08 2006 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 1.2.0

* Mon May 01 2006 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 1.1.9

* Mon Apr 03 2006 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 1.1.8

* Wed Mar 29 2006 Chung-Yen Chang <candyz@cle.linux.org.tw>
- rebuild for FC5

* Wed Feb 22 2006 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 1.1.7

* Thu Feb 02 2006 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 1.1.6

* Sat Jan 07 2006 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 1.1.5

* Mon Dec 19 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 1.1.4-2

* Mon Dec 12 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 1.1.4

* Mon Nov 21 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 1.1.3

* Tue Nov 08 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 1.1.2

* Sun Oct 30 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 1.1.1

* Mon Oct 24 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 1.1.0

* Mon Oct 03 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 1.0.9

* Mon Sep 26 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 1.0.8

* Mon Sep 19 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 1.0.7

* Mon Sep 05 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 1.0.4

* Mon Aug 22 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 1.0.3

* Wed Aug 10 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 1.0.2

* Fri Jul 08 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 1.0.1

* Mon Jun 27 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 1.0.0

* Thu Jun 23 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 0.9.9

* Thu Jun 16 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- rebuild for fc4

* Tue May 31 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 0.9.7

* Thu May 19 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 0.9.6

* Thu May 12 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 0.9.5

* Wed May 04 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 0.9.3

* Mon Apr 25 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- fix alternatives

* Fri Apr 22 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 0.9.2

* Sat Apr 16 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 0.9.1

* Tue Apr 05 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 0.9.0

* Tue Mar 22 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 0.8.9

* Mon Mar 14 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 0.8.8

* Tue Mar 08 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 0.8.7

* Sat Mar 05 2005 Chung-Yen Chang <candyz@cle.linux.org.tw>
- update to 0.8.6

* Mon Aug 23 2004 Chung-Yen Chang <candyz@cle.linux.org.tw>
- frist build for Fedora Core 2
