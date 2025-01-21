%global libhandy_version 1.5.0

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:          yelp
Epoch:         2
Version:       42.2
Release:       8%{?dist}
Summary:       Help browser for the GNOME desktop

# Automatically converted from old format: LGPLv2+ and ASL 2.0 and GPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+ AND Apache-2.0 AND GPL-2.0-or-later
URL:           https://wiki.gnome.org/Apps/Yelp
Source:        https://download.gnome.org/sources/%{name}/42/%{name}-%{tarball_version}.tar.xz

# https://bugzilla.gnome.org/show_bug.cgi?id=687960
Patch1:        0001-Center-new-windows.patch

BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libhandy-1) >= %{libhandy_version}
BuildRequires: pkgconfig(liblzma)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(libexslt)
BuildRequires: pkgconfig(libxslt)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(webkit2gtk-4.1)
BuildRequires: pkgconfig(yelp-xsl)
BuildRequires: desktop-file-utils
BuildRequires: bzip2-devel
BuildRequires: gcc
BuildRequires: gettext-devel
BuildRequires: intltool
BuildRequires: itstool
BuildRequires: make
Requires:      libhandy%{?_isa} >= %{libhandy_version}
Requires:      yelp-libs%{?_isa} = %{epoch}:%{version}-%{release}
Requires:      yelp-xsl

%description
Yelp is the help browser for the GNOME desktop. It is designed
to help you browse all the documentation on your system in
one central tool, including traditional man pages, info pages and
documentation written in DocBook.

%package libs
Summary: Libraries for yelp

%description libs
This package contains libraries used by the yelp help browser.

%package devel
Summary: Development files for yelp-libs
Requires: %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}

%description devel
This package contains header files for the libraries in the yelp-libs package.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%configure --disable-static
%make_build

%install
%make_install

find $RPM_BUILD_ROOT%{_libdir} -name '*.la' -delete

%find_lang %{name}

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/yelp.desktop

%files -f %{name}.lang
%doc AUTHORS NEWS README.md
%license COPYING
%{_bindir}/*
%{_datadir}/applications/yelp.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.yelp.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Yelp.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Yelp-symbolic.svg
%{_datadir}/metainfo/yelp.appdata.xml
%{_datadir}/yelp/
%{_datadir}/yelp-xsl/xslt/common/domains/yelp.xml

%files libs
%{_libdir}/libyelp.so.0*
%dir %{_libdir}/yelp
%dir %{_libdir}/yelp/web-extensions
%{_libdir}/yelp/web-extensions/libyelpwebextension.so

%files devel
%{_libdir}/libyelp.so
%{_includedir}/libyelp


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2:42.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2:42.2-7
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:42.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:42.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Aug 11 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 2:42.2-4
- Drop unused libunwind dependencies

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:42.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:42.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 19 2022 Kalev Lember <klember@redhat.com> - 2:42.2-1
- Update to 42.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:42.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Milan Crha <mcrha@redhat.com> - 2:42.1-3
- Switch to WebKitGTK API 4.1 (using libsoup3)

* Fri Apr 08 2022 Kevin Fenzi <kevin@scrye.com> - 2:42.1-2
- Add dep on libunwind

* Sat Mar 26 2022 David King <amigadave@amigadave.com> - 2:42.1-1
- Update to 42.1

* Sat Mar 19 2022 David King <amigadave@amigadave.com> - 2:42.0-1
- Update to 42.0

* Mon Feb 14 2022 David King <amigadave@amigadave.com> - 2:42~beta-1
- Update to 42.beta

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:41.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec 07 2021 Kalev Lember <klember@redhat.com> - 2:41.2-1
- Update to 41.2

* Sat Sep 25 2021 Kalev Lember <klember@redhat.com> - 2:41.1-1
- Update to 41.1

* Mon Sep 20 2021 Kalev Lember <klember@redhat.com> - 2:41.0-1
- Update to 41.0

* Mon Aug 30 2021 David King <amigadave@amigadave.com> - 2:41~beta2-1
- Update to 41.beta2 (#1997839)

* Mon Aug 23 2021 Kalev Lember <klember@redhat.com> - 2:41~beta-1
- Update to 41.beta

* Tue Aug 03 2021 Kalev Lember <klember@redhat.com> - 2:40.3-1
- Update to 40.3

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:40.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jun 21 2021 Kalev Lember <klember@redhat.com> - 2:40.2-1
- Update to 40.2

* Mon Mar 22 2021 Kalev Lember <klember@redhat.com> - 2:40.0-1
- Update to 40.0

* Sun Feb 28 2021 Kalev Lember <klember@redhat.com> - 2:40~beta-2
- Drop libtool as-needed hack as as-needed is in default LDFLAGS now
- Remove unneeded ldconfig_scriptlets macro call
- Tighten soname globs

* Thu Feb 18 2021 Kalev Lember <klember@redhat.com> - 2:40~beta-1
- Update to 40.beta

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.38.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Kalev Lember <klember@redhat.com> - 2:3.38.2-1
- Update to 3.38.2

* Mon Oct  5 2020 Kalev Lember <klember@redhat.com> - 2:3.38.1-1
- Update to 3.38.1

* Sat Sep 12 2020 Kalev Lember <klember@redhat.com> - 2:3.38.0-1
- Update to 3.38.0

* Tue Aug 18 2020 David King <amigadave@amigadave.com> - 2:3.37.90-2
- Use make_build macro

* Mon Aug 17 2020 Kalev Lember <klember@redhat.com> - 2:3.37.90-1
- Update to 3.37.90

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Mar 07 2020 Kalev Lember <klember@redhat.com> - 2:3.36.0-1
- Update to 3.36.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 2:3.34.0-1
- Update to 3.34.0

* Tue Sep 03 2019 Kalev Lember <klember@redhat.com> - 2:3.33.92-1
- Update to 3.33.92

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.32.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 2019 David King <amigadave@amigadave.com> - 2:3.32.2-1
- Update to 3.32.2

* Mon Apr 08 2019 Kalev Lember <klember@redhat.com> - 2:3.32.1-1
- Update to 3.32.1

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 2:3.32.0-1
- Update to 3.32.0

* Mon Feb 04 2019 David King <amigadave@amigadave.com> - 2:3.31.90-1
- Update to 3.31.90

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.30.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 04 2018 David King <amigadave@amigadave.com> - 2:3.30.0-1
- Update to 3.30.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.28.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Kalev Lember <klember@redhat.com> - 2:3.28.1-1
- Update to 3.28.1
- Use upstream appdata file

* Tue Mar 13 2018 Kalev Lember <klember@redhat.com> - 2:3.28.0-1
- Update to 3.28.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.27.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2:3.27.1-2
- Switch to %%ldconfig_scriptlets

* Sat Jan 13 2018 David King <amigadave@amigadave.com> - 2:3.27.1-1
- Update to 3.27.1

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2:3.26.0-2
- Remove obsolete scriptlets

* Mon Sep 11 2017 David King <amigadave@amigadave.com> - 2:3.26.0-1
- Update to 3.26.0

* Tue Aug 22 2017 Ville Skyttä <ville.skytta@iki.fi> - 2:3.25.3-5
- Own %%{_libdir}/yelp dirs

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.25.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.25.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 David King <amigadave@amigadave.com> - 2:3.25.3-2
- Fix icon cache path in scriptlets (#1470335)

* Tue Jun 20 2017 David King <amigadave@amigadave.com> - 2:3.25.3-1
- Update to 3.25.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 20 2016 David King <amigadave@amigadave.com> - 2:3.22.0-1
- Update to 3.22.0

* Tue Jun 21 2016 David King <amigadave@amigadave.com> - 2:3.21.3-1
- Update to 3.21.3

* Tue Apr 12 2016 David King <amigadave@amigadave.com> - 2:3.20.1-1
- Update to 3.20.1

* Tue Mar 22 2016 Kalev Lember <klember@redhat.com> - 2:3.20.0-1
- Update to 3.20.0

* Tue Mar 01 2016 David King <amigadave@amigadave.com> - 2:3.19.91-1
- Update to 3.19.91

* Tue Feb 16 2016 David King <amigadave@amigadave.com> - 2:3.19.90-1
- Update to 3.19.90

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2:3.19.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 31 2015 Adam Williamson <awilliam@redhat.com> - 2:3.19.1-2
- bump epoch to keep up with F23

* Mon Oct 26 2015 David King <amigadave@amigadave.com> - 1:3.19.1-1
- Update to 3.19.1

* Mon Oct 12 2015 Kalev Lember <klember@redhat.com> - 1:3.18.1-1
- Update to 3.18.1

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 1:3.18.0-1
- Update to 3.18.0

* Tue Sep 01 2015 David King <amigadave@amigadave.com> - 1:3.17.91-1
- Update to 3.17.91

* Mon Aug 17 2015 Kalev Lember <klember@redhat.com> - 1:3.17.90-1
- Update to 3.17.90
- Use make_install macro

* Tue Jul 21 2015 David King <amigadave@amigadave.com> - 1:3.17.4-1
- Update to 3.17.4

* Tue Jun 23 2015 David King <amigadave@amigadave.com> - 1:3.17.3-1
- Update to 3.17.3

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 David King <amigadave@amigadave.com> - 1:3.17.2-1
- Update to 3.17.2

* Mon May 11 2015 David King <amigadave@amigadave.com> - 1:3.16.1-1
- Update to 3.16.1

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1:3.16.0-2
- Add an AppData file for the software center

* Mon Mar 23 2015 Kalev Lember <kalevlember@gmail.com> - 1:3.16.0-1
- Update to 3.16.0

* Mon Mar 02 2015 David King <amigadave@amigadave.com> - 1:3.15.91-1
- Update to 3.15.91

* Mon Feb 16 2015 David King <amigadave@amigadave.com> - 1:3.15.90-1
- Update to 3.15.90
- Use license macro for COPYING

* Wed Dec 10 2014 David King <amigadave@amigadave.com> - 1:3.14.1-3
- Use pkgconfig for BuildRequires

* Mon Nov 10 2014 Matthias Clasen <mclasen@redhat.com> - 1:3.14.1-2
- Drop the gnome-user-docs dependency (#1149511)

* Mon Oct 13 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.14.1-1
- Update to 3.14.1

* Tue Sep 23 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.14.0-2
- Drop unused build deps

* Tue Sep 23 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.14.0-1
- Update to 3.14.0

* Tue Sep 16 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.13.92-1
- Update to 3.13.92

* Tue Aug 19 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.13.90-1
- Update to 3.13.90

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 24 2014 Richard Hughes <rhughes@redhat.com> - 1:3.13.3-1
- Update to 3.13.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 25 2014 Kalev Lember <kalevlember@gmail.com> - 1:3.12.0-1
- Update to 3.12.0

* Wed Mar 05 2014 Richard Hughes <rhughes@redhat.com> - 1:3.11.91-1
- Update to 3.11.91

* Mon Nov 25 2013 Richard Hughes <rhughes@redhat.com> - 1:3.11.1-1
- Update to 3.11.1

* Tue Oct 29 2013 Richard Hughes <rhughes@redhat.com> - 1:3.10.1-1
- Update to 3.10.1

* Tue Sep 24 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.10.0-1
- Update to 3.10.0

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.9.91-1
- Update to 3.9.91

* Thu Aug 22 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.9.90-1
- Update to 3.9.90

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Matthias Clasen <mclasen@redhat.com> - 1:3.8.1-5
- Trim %%changelog

* Fri Jun 21 2013 Matthias Clasen <mclasen@redhat.com> - 1:3.8.1-4
- Don't install ChangeLog

* Sat May 25 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.8.1-3
- Make yelp-libs dep arch-specific, thanks to Michael Schwendt (#967180)
- Don't create empty /usr/share/gnome/help directory: this should be owned by
  individual packages that install files in there (#964421)
- Use configure --disable-static instead of removing the static .a afterwards

* Sat May 18 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1:3.8.1-2
- yelp should depend on yelp-libs not the other way around

* Tue May 14 2013 Richard Hughes <rhughes@redhat.com> - 1:3.8.1-1
- Update to 3.8.1

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.8.0-1
- Update to 3.8.0

* Fri Feb 22 2013 Kalev Lember <kalevlember@gmail.com> - 1:3.7.90-2
- Remove the desktop file vendor prefix

* Tue Feb 19 2013 Richard Hughes <rhughes@redhat.com> - 1:3.7.90-1
- Update to 3.7.90

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 16 2013 Richard Hughes <hughsient@gmail.com> - 1:3.7.4-1
- Update to 3.7.4

* Fri Jan 4 2013 Matthias Clasen <mclasen@redhat.com> - 1:3.7.3-2
- Optionally do the right thing with focus and window placement

* Fri Dec 21 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.7.3-1
- Update to 3.7.3

* Mon Nov 12 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.6.2-1
- Update to 3.6.2

* Tue Oct 16 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.6.1-1
- Update to 3.6.1

* Tue Sep 25 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Richard Hughes <hughsient@gmail.com> - 1:3.5.92-1
- Update to 3.5.92

* Tue Sep 04 2012 Richard Hughes <hughsient@gmail.com> - 1:3.5.91-1
- Update to 3.5.91

* Wed Aug 22 2012 Richard Hughes <hughsient@gmail.com> - 1:3.5.90-1
- Update to 3.5.90

* Fri Jul 27 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jul 15 2012 Ville Skyttä <ville.skytta@iki.fi> - 1:3.4.2-2
- Call ldconfig at -libs post(un)install time.
- Escape macros in %%changelog.

* Fri May 18 2012 Richard Hughes <hughsient@gmail.com> - 1:3.4.2-1
- Update to 3.4.2

* Tue Apr 24 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.4.1-2
- Silence rpm scriptlet output

* Tue Apr 17 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.4.1-1
- Update to 3.4.1

* Tue Mar 27 2012 Richard Hughes <hughsient@gmail.com> - 1:3.4.0-1
- Update to 3.4.0

* Tue Mar 20 2012 Kalev Lember <kalevlember@gmail.com> - 1:3.3.92-1
- Update to 3.3.92

* Sat Feb 25 2012 Matthias Clasen <mclasen@redhat.com> - 1:3.3.4-1
- Update to 3.3.4

* Tue Jan 17 2012 Matthias Clasen <mclasen@redhat.com> - 1:3.3.3-1
- Update to 3.3.3

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 21 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.3.2-1
- Update to 3.3.2

* Wed Nov  2 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.3.1-1
- Update to 3.3.1

* Wed Oct 26 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.2.1-2
- Rebuilt for glibc bug#747377

* Tue Oct 18 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.2.1-1
- Update to 3.2.1

* Tue Sep 27 2011 Ray <rstrode@redhat.com> - 1:3.2.0-1
- Update to 3.2.0

* Wed Sep 21 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.1.4-2
- Fix default uri

* Tue Sep 20 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.1.4-1
- Update to 3.1.4

* Wed Sep 07 2011 Kalev Lember <kalevlember@gmail.com> - 1:3.1.3-1
- Update to 3.1.3

* Thu Aug 16 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.1.2-1
- Update to 3.1.2

* Wed Jul  6 2011 Matthias Clasen <mclasen@redhat.com> - 1:3.1.1-1
- Update to 3.1.1

* Tue May 24 2011 Christopher Aillon <caillon@redhat.com> - 1:3.0.3-1
- Update to 3.0.3

* Sat May 07 2011 Christopher Aillon <caillon@redhat.com> - 1:3.0.2-3
- Update gsettings scriptlet

* Thu Apr 28 2011 Matthias Clasen <mclasen@redhat.com> 1:3.0.2-2
- Fix some strings appearing untranslated (e.g. 'Show Text Cursor')

* Mon Apr 25 2011 Matthias Clasen <mclasen@redhat.com> 1:3.0.2-1
- Update to 3.0.2

* Sun Apr 10 2011 Christopher Aillon <caillon@redhat.com> 1:3.0.1-1
- Update to 3.0.1

* Mon Apr  4 2011 Matthias Clasen <mclasen@redhat.com> 1:3.0.0-1
- Update to 3.0.0

* Tue Mar 22 2011 Matthias Clasen <mclasen@redhat.com> 1:2.91.92-1
- Update to 2.91.92

* Mon Mar  7 2011 Matthias Clasen <mclasen@redhat.com> 1:2.91.91-1
- Update to 2.91.91

* Mon Feb 21 2011 Matthias Clasen <mclasen@redhat.com> 1:2.91.90-1
- Update to 2.91.90
- Drop docbook-dtds dependency

* Thu Feb 10 2011 Matthias Clasen <mclasen@redhat.com> 1:2.91.10-4
- Rebuild against newer gtk

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.91.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> - 1:2.91.10-2
- Rebuild against new gtk

* Mon Jan 10 2011 Matthias Clasen <mclasen@redhat.com> - 1:2.91.10-1
- Update to 2.91.10

* Sun Jan  9 2011 Matthias Clasen <mclasen@redhat.com> - 1:2.91.9-1
- Update to 2.91.9

* Fri Dec  3 2010 Matthias Clasen <mclasen@redhat.com> - 1:2.31.7-4
- Rebuild against new gtk

* Thu Aug 12 2010 Matthias Clasen <mclasen@redhat.com> - 1:2.31.7-3
- Fix up dependencies for epoch

* Wed Aug 11 2010 Matthias Clasen <mclasen@redhat.com> - 1:2.31.7-2
- Carry over the epoch from F14

* Mon Jul 14 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.7-1
- Update to 2.31.7

* Sat Jul  3 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.6-2
- Rebuild against new webkit

* Wed Jun 30 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.6-1
- Update to 2.31.6

* Wed Jun 23 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.5-2.20100623git
- git snapshot that works with GLib 2.25.9

* Tue Jun  8 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.5-1
- Update to 2.31.5

* Thu May 27 2010 Matthias Clasen <mclasen@redhat.com> - 2.31.4-1
- Update to 2.31.4

* Mon May 24 2010 Matthew Barnes <mbarnes@redhat.com> - 2.30.1-2
- Require gnome-user-docs so that Help->Contents works.

* Tue Apr 27 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.1-1
- Update to 2.30.1

* Fri Apr  9 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.0-2
- Drop libbeagle dep
- Use GConf macros

* Mon Mar 29 2010 Matthias Clasen <mclasen@redhat.com> - 2.30.0-1
- Update to 2.30.0

* Mon Feb 22 2010 Matthias Clasen <mclasen@redhat.com> - 2.29.5-1
- Update to 2.29.5

* Mon Feb 08 2010 Matthew Barnes <mbarnes@redhat.com> - 2.29.4-1
- Update to 2.29.4
- Update version requirements.

* Mon Jan 25 2010 Matthew Barnes <mbarnes@redhat.com> - 2.29.3-1
- Update to 2.29.3

* Fri Jan 22 2010 Matthew Barnes <mbarnes@redhat.com> - 2.29.2-1
- Update to 2.29.2

* Tue Jan  5 2010 Matthew Barnes <mbarnes@redhat.com> - 2.29.1-1
- Update to 2.29.1

* Tue Jan  5 2010 Matthias Clasen <mclasen@redhat.com> - 2.28.1-2
- Use %%global instead of %%define where %%define doesn't work

* Fri Dec  4 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.1-1
- Update to 2.28.1

* Wed Dec  2 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-2
- make mono dep more automatic

* Mon Sep 21 2009 Matthias Clasen <mclasen@redhat.com> - 2.28.0-1
- Update to 2.28.0

* Mon Sep  7 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.5-1
- Update to 2.27.5

* Mon Aug 24 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.4-1
- Update to 2.27.4

* Sun Aug 23 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.3-2
- Remove space before ellipsis in menuitems

* Tue Jul 28 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.3-1
- Update to 2.27.3

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 18 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.2-3
- Drop unused direct dependencies

* Thu Jul  2 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.2-2
- Shrink GConf schemas

* Mon Jun 29 2009 Matthew Barnes <mbarnes@redhat.com> - 2.27.2-1
- Update to 2.27.2
- Bump gnome_doc_utils requirement to 0.17.2.

* Mon Jun 15 2009 Matthias Clasen <mclasen@redhat.com> - 2.27.1-1
- Update to 2.27.1

* Mon Apr 27 2009 Christopher Aillon <caillon@redhat.com> - 2.26.0-3
- Rebuild against newer gecko

* Mon Apr  6 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.0-2
- Clean up Requires a bit

* Mon Mar 16 2009 Matthias Clasen <mclasen@redhat.com> - 2.26.0-1
- Update to 2.26.0

* Mon Mar 02 2009 Matthew Barnes <mbarnes@redhat.com> - 2.25.1-1
- Update to 2.25.1

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 21 2008 Christopher Aillon <caillon@redhat.com> - 2.24.0-5
- Rebuild against newer gecko

* Sat Dec 20 2008 Caolán McNamara <caolanm@redhat.com> - 2.24.0-4
- rebuild for gecko

* Fri Nov 21 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-3
- %%summary and %%description tweakage

* Wed Sep 24 2008 Christopher Aillon <caillon@redhat.com> - 2.24.0-2
- Rebuild against newer gecko

* Mon Sep 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.24.0-1
- Update ot 2.24.0

* Mon Sep 01 2008 Matthew Barnes <mbarnes@redhat.com> - 2.23.91-1
- Update to 2.23.91

* Fri Aug 22 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.2-1
- Update to 2.23.2

* Tue Jul 22 2008 Martin Stransky <stransky@redhat.com> - 2.23.1-3
- rebuild for xulrunner update

* Fri Jun 20 2008 Matthias Clasen <mclasen@redhat.com> - 2.23.1-2
- Use a standard icon name in the desktop file

* Tue Jun 03 2008 Matthew Barnes <mbarnes@redhat.com> - 2.23.1-1
- Update to 2.23.1

* Mon May 19 2008 Matthew Barnes <mbarnes@redhat.com> - 2.22.1-2
- Require docbook-dtds (RH bug #447209).

* Mon Apr  7 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.1-1
- Update to 2.22.1

* Mon Mar 31 2008 Jon McCann <jmccann@redhat.com> - 2.22.0-4
- Disallow launchers when running under GDM.

* Mon Mar 31 2008 Matthew Barnes <mbarnes@redhat.com> - 2.22.0-3
- Update patch for RH bug #437328.

* Thu Mar 13 2008 Matthew Barnes <mbarnes@redhat.com> - 2.22.0-2
- Add patch for RH bug #437328 (searching with Beagle broken).

* Sun Mar 09 2008 Matthew Barnes <mbarnes@redhat.com> - 2.22.0-1
- Update to 2.22.0

* Thu Feb 28 2008 Martin Stransky <stransky@redhat.com> - 2.21.90-4
- updated xulrunner patch, rebuild against xulrunner

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.21.90-3
- Autorebuild for GCC 4.3

* Sun Feb 17 2008 Matthew Barnes <mbarnes@redhat.com> - 2.21.90-2
- Rebuild with GCC 4.3

* Mon Jan 28 2008 Matthew Barnes <mbarnes@redhat.com> - 2.21.90-1
- Update to 2.21.90

* Tue Jan 08 2008 Matthew Barnes <mbarnes@redhat.com> - 2.21.2-2
- Look for new-style xulrunner pkg-config files.
- Build requires gecko-devel-unstable.

* Tue Jan 08 2008 - Bastien Nocera <bnocera@redhat.com> - 2.21.2-1
- Update to 2.21.2

* Sun Dec 30 2007 Jeremy Katz <katzj@redhat.com> - 2.21.1-3
- Rebuild for new xulrunner

* Sat Dec  8 2007 Matthias Clasen <mclasen@redhat.com> - 2.21.1-2
- Rebuild against new libbeagle

* Mon Dec  3 2007 Matthias Clasen <mclasen@redhat.com> - 2.21.1-1
- Update to 2.21.1

* Mon Dec  3 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-9
- Rebuild against xulrunner again

* Thu Nov 22 2007 Martin Stransky <stransky@redhat.com> - 2.20.0-8
- rebuild against xulrunner

* Fri Nov 16 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-7
- Handle .HP tags in man pages

* Fri Nov 09 2007 Matthew Barnes <mbarnes@redhat.com> - 2.20.0-6
- Rebuild against gecko-libs 1.8.1.9.

* Mon Nov  5 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-5
- Fix a crash in search (#361041)

* Sun Nov  4 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-4
- Fix a crash when loading the rarian docs

* Thu Nov 01 2007 Matthew Barnes <mbarnes@redhat.com> - 2.20.0-3
- Rebuild against gecko-libs 1.8.1.8.

* Mon Oct 22 2007 Matthias Clasen <mclasen@redhat.com> - 2.20.0-2
- Rebuild against new dbus-glib

* Mon Sep 17 2007 Matthew Barnes <mbarnes@redhat.com> - 2.20.0-1
- Update to 2.20.0

* Thu Aug 28 2007 Matthew Barnes <mbarnes@redhat.com> - 2.19.90-3
- Remove --add-only-show-in from desktop-file-install (RH bug #258821).

* Wed Aug 22 2007 Matthew Barnes <mbarnes@redhat.com> - 2.19.90-2
- Mass rebuild

* Mon Aug 13 2007 Matthew Barnes <mbarnes@redhat.com> - 2.19.90-1
- Update to 2.19.90
- Remove "info-gnutls" patch (fixed upstream).
- Remove patch for GNOME bug #370167 (fixed upstream).
- Remove patch for GNOME bug #430365 (fixed upstream).
- Remove patch for GNOME bug #431078 (fixed upstream).

* Wed Aug  8 2007 Christopher Aillon <caillon@redhat.com> - 2.19.1-4
- Rebuild against newer gecko

* Fri Aug 03 2007 Matthew Barnes <mbarnes@redhat.com> - 2.19.1-3
- Require rarian-devel for building.

* Fri Aug  3 2007 Matthias Clasen <mclasen@redhat.com> - 2.19.1-2
- Update the license field

* Thu Aug 02 2007 Matthew Barnes <mbarnes@redhat.com> - 2.19.1-1
- Update to 2.19.1
- Adapt the "apropos" patch for 2.19.1.
- The "posix-man" patch appears to no longer apply.
- Update dependencies based on configure.ac.

* Wed Jul 25 2007 Jeremy Katz <katzj@redhat.com> - 2.18.1-7
- rebuild for toolchain bug

* Mon Jul 23 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.1-6
- Require gnome-doc-utils-stylesheets instead of gnome-doc-utils

* Fri Jul 20 2007 Kai Engert <kengert@redhat.com> - 2.18.1-5
- Rebuild against newer gecko

* Wed May 25 2007 Christopher Aillon <caillon@redhat.com> - 2.18.1-4
- Rebuild against newer gecko

* Wed Apr 18 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.1-3
- Improve the man parser a bit
- Fix another crash in the info parser 

* Tue Apr 17 2007 Matthias Clasen <mclasen@redhat.com> - 2.18.1-2
- Fix a crash in the info parser (#216308)

* Mon Apr 09 2007 Matthew Barnes <mbarnes@redhat.com> - 2.18.1-1
- Update to 2.18.1

* Fri Mar 23 2007 Christopher Aillon <caillon@redhat.com> - 2.18.0-2
- Rebuild against newer gecko

* Tue Mar 13 2007 Matthew Barnes <mbarnes@redhat.com> - 2.18.0-1
- Update to 2.18.0

* Wed Feb 28 2007 Matthew Barnes <mbarnes@redhat.com> - 2.16.2-5
- Rebuild against newer gecko.

* Fri Feb 23 2007 Matthias Clasen <mclasen@redhat.com> 2.16.2-4
- Don't own /usr/share/icons/hicolor

* Tue Feb 13 2007 Bill Nottingham <notting@redhat.com> 2.16.2-3
- own %%{_datadir}/gnome/help (#205799)
- rpmlint silencing:
 - add a URL: tag
 - add some docs

* Thu Dec 21 2006 Christopher Aillon <caillon@redhat.com> 2.16.2-2
- Rebuild against newer gecko

* Tue Dec  5 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.2-1
- Update to 2.16.2
- Drop obsolete patch

* Fri Nov  3 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.1-6
- Improve the whatis parser

* Fri Nov  3 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.1-5
- Silence %%pre

* Sun Oct 29 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.1-4
- Improve the previous fix

* Sun Oct 29 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.1-3
- Fix some crashes (#212888)

* Fri Oct 27 2006 Christopher Aillon <caillon@redhat.com> - 2.16.1-2
- Rebuild against newer gecko

* Sun Oct 22 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.1-1
- Update to 2.16.1

* Wed Oct 18 2006 Matthias Clasen <mclasen@redhat.com> - 2.16.0-5
- Fix scripts according to the packaging guidelines

* Thu Oct 12 2006 Christopher Aillon <caillon@redhat.com> - 2.16.0-4.fc6
- Update requires to the virtual gecko version instead of a specific app

* Thu Sep 14 2006 Christopher Aillon <caillon@redhat.com> - 2.16.0-3.fc6
- Rebuild

* Wed Sep  6 2006 Matthias Clasen  <mclasen@redhat.com> - 2.16.0-2.fc6
- Actually apply the Pango patch

* Mon Sep  4 2006 Matthias Clasen  <mclasen@redhat.com> - 2.16.0-1.fc6
- Update to 2.16.0

* Tue Aug 29 2006 Matthias Clasen  <mclasen@redhat.com> - 2.15.91-3.fc6
- Use Pango 

* Wed Aug 23 2006 Matthew Barnes <mbarnes@redhat.com> - 2.15.91-2
- Rebuild

* Thu Aug 10 2006 Matthew Barnes <mbarnes@redhat.com> - 2.15.91-1
- Update to 2.15.91

* Thu Jul 27 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.5-1
- Update to 2.15.5
- Rebuild against firefox-devel

* Tue Jul 18 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.2-2
- Go back to 2.15.2, since gecko 1.8 is still missing

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.15.3-1.1
- rebuild

* Tue Jun 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.3-1
- Update to 2.15.3

* Tue May 17 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.2-1
- Update to 2.15.2

* Mon May 15 2006 Matthew Barnes <mbarnes@redhat.com> - 2.15.1-3
- Bump mozilla_version from 1.7.12 to 1.7.13 (closes #190880).

* Mon May 15 2006 Matthew Barnes <mbarnes@redhat.com> - 2.15.1-2
- Add build requirements: startup-notification-devel
                          libgnomeprintui22-devel
                          libXt-devel

* Tue May  9 2006 Matthias Clasen <mclasen@redhat.com> - 2.15.1-1
- Update to 2.15.1

* Mon Apr 10 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.1-2
- Update to 2.14.1

* Mon Mar 13 2006 Matthias Clasen <mclasen@redhat.com> - 2.14.0-1
- Update to 2.14.0

* Mon Feb 27 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.6-1
- Update to 2.13.6

* Sun Feb 12 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.5-2
- Turn on info and man support for test3

* Sun Feb 12 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.5-1
- Update to 2.13.5

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2.13.4-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2.13.4-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Tue Jan 31 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.4-1
- Update to 2.13.4

* Thu Jan 19 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.3-1
- Update to 2.13.3
- enable search

* Wed Jan 18 2006 Matthias Clasen <mclasen@redhat.com> - 2.13.2-3
- Disable search, since it doesn't compile against 
  current beagle

* Thu Dec 15 2005 David Malcolm <dmalcolm@redhat.com> - 2.13.2-2
- Patched to include DocBook mimetype in desktop file, and added preun and post
  hooks to update-desktop-database (#175880)
- Patched to ensure that Yelp recognizes that it can handle the mimetype of the
  documentation as reported by gnomevfs (also #175880) 

* Thu Dec 15 2005 Matthias Clasen <mclasen@redhat.com> 2.13.2-1
- Update to 2.13.2

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov 30 2005 Matthias Clasen <mclasen@redhat.com> - 2.13.1-6
- Update to 2.13.1

* Wed Oct 19 2005 Jeremy Katz <katzj@redhat.com> - 2.12.1-5
- build on ppc64 now that we have mozilla there again

* Tue Oct 18 2005 Christopher Aillon <caillon@redhat.com> - 2.12.1-4
- Rebuild

* Mon Oct 17 2005 Matthias Clasen <mclasen@redhat.com> - 2.12.1-3
- Include the category General|Linux|Distributions|Other on the
  title page

* Mon Oct 17 2005 Matthias Clasen <mclasen@redhat.com> - 2.12.1-2
- Fix a double-free bug

* Thu Sep 29 2005 Matthias Clasen <mclasen@redhat.com> - 2.12.1-1
- Update to 2.12.1

* Thu Sep  8 2005 Matthias Clasen <mclasen@redhat.com> - 2.12.0-1
- Update to 2.12.0

* Wed Aug 17 2005 Jeremy Katz <katzj@redhat.com> - 2.11.1-5
- rebuild

* Wed Aug 17 2005 Ray Strode <rstrode@redhat.com> 2.11.1-4
- rebuild

* Sun Jul 31 2005 Christopher Aillon <caillon@redhat.com> 2.11.1-3
- Rebuild against newer mozilla

* Tue Jul 19 2005 Christopher Aillon <caillon@redhat.com> 2.11.1-2
- Rebuild against newer mozilla

* Wed Jul 13 2005 Matthias Clasen <mclasen@redhat.com> 2.11.1-1
- Newer upstream version

* Thu May 19 2005 Ray Strode <rstrode@redhat.com> 2.10.0-1
- Update to 2.10.0 (bug 157752, 146862).

* Thu May 19 2005 Christopher Aillon <caillon@redhat.com> 2.9.3-7
- Depend on mozilla 1.7.8

* Thu Apr 28 2005 Ray Strode <rstrode@redhat.com> 2.9.3-6
- Disable man support
- Disable info support
- Don't try to install schemas during install (bug 154035)

* Mon Apr 18 2005 Ray Strode <rstrode@redhat.com> 2.9.3-5
- Depend on mozilla 1.7.7

* Mon Apr  4 2005 Ray Strode <rstrode@redhat.com> 2.9.3-4
- rebuilt

* Wed Mar  9 2005 Christopher Aillon <caillon@redhat.com> 2.9.3-3
- Depend on mozilla 1.7.6

* Sat Mar  5 2005 Christopher Aillon <caillon@redhat.com> 2.9.3-2
- Rebuild against GCC 4.0

* Fri Jan 28 2005 Matthias Clasen <mclasen@redhat.com> 2.9.3-1
- Update to 2.9.3

* Mon Dec 20 2004 Christopher Aillon <caillon@redhat.com> 2.6.5-1
- Update to 2.6.5

* Sat Nov  6 2004 Marco Pesenti Gritti <mpg@redhat.com> 2.6.4-1
- Update to 2.6.4

* Wed Sep 22 2004 Christopher Aillon <caillon@redhat.com> 2.6.3-1
- Update to 2.6.3

* Fri Sep 03 2004 Matthias Clasen <mclasen@redhat.com> 2.6.2-2
- fix an translation problem

* Tue Aug 31 2004 Alex Larsson <alexl@redhat.com> 2.6.2-1
- update to 2.6.2

* Wed Jun 30 2004 Christopher Aillon <caillon@redhat.com> 2.6.1-1
- Update to 2.6.1

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Apr  1 2004 Alex Larsson <alexl@redhat.com> 2.6.0-1
- update to 2.6.0

* Mon Mar 15 2004 Alex Larsson <alexl@redhat.com> 2.5.90-2
- Fix requirements

* Wed Mar 10 2004 Alex Larsson <alexl@redhat.com> 2.5.90-1
- update to 2.5.90

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 25 2004 Alexander Larsson <alexl@redhat.com> 2.5.6-1
- update to 2.5.6

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 28 2004 Alexander Larsson <alexl@redhat.com> 2.5.3-1
- update to 2.5.3

* Wed Dec 24 2003 Tim Waugh <twaugh@redhat.com> 2.4.0-2
- Fix g_strdup_printf usage in info2html (bug #111200, patch from
  Miloslav Trmac).

* Tue Sep  9 2003 Alexander Larsson <alexl@redhat.com> 2.4.0-1
- update to 2.4.0 (only code change is bugfix from me)
- Fixed the utf8 manpage patch (#91689)

* Wed Aug 27 2003 Alexander Larsson <alexl@redhat.com> 2.3.6-2
- info and manpages are utf8

* Wed Aug 20 2003 Alexander Larsson <alexl@redhat.com> 2.3.6-1
- Update for gnome 2.3

* Wed Jul  9 2003 Alexander Larsson <alexl@redhat.com> 2.2.3-1.E
- Rebuild

* Mon Jul  7 2003 Alexander Larsson <alexl@redhat.com> 2.2.3-1
- update to 2.2.3

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 14 2003 Jeremy Katz <katzj@redhat.com> 2.2.0-3
- fix buildrequires

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Tue Jan 21 2003 Alexander Larsson <alexl@redhat.com> 2.2.0-1
- Update to 2.2.0
- Add libglade dependency

* Tue Jan  7 2003 Alexander Larsson <alexl@redhat.com> 2.1.4-1
- Updated to 2.1.4

* Mon Nov 18 2002 Tim Powers <timp@redhat.com>
- rebuild for all arches

* Mon Aug 12 2002 Alexander Larsson <alexl@redhat.com>
- Remove the strange copyright on the start page. Fixes #69106

* Thu Aug  8 2002 Havoc Pennington <hp@redhat.com>
- 1.0.2
- include libexecdir stuff

* Sat Jul 27 2002 Havoc Pennington <hp@redhat.com>
- rebuild with new gail
- 1.0.1

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue Jun 18 2002 Havoc Pennington <hp@redhat.com>
- put all the binaries in the file list... why is this package so hard?

* Mon Jun 17 2002 Havoc Pennington <hp@redhat.com>
- put images in file list, this thing will be non-ugly yet

* Sun Jun 16 2002 Havoc Pennington <hp@redhat.com>
- 1.0
- use desktop-file-install to install/munge .desktop files
- put the sgml stuff in file list

* Fri Jun 07 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Wed Jun  5 2002 Havoc Pennington <hp@redhat.com>
- 0.10

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Tue May 21 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Tue May 21 2002 Havoc Pennington <hp@redhat.com>
- 0.8

* Fri May  3 2002 Havoc Pennington <hp@redhat.com>
- 0.6.1

* Fri Apr 19 2002 Havoc Pennington <hp@redhat.com>
- 0.6

* Wed Jan 30 2002 Owen Taylor <otaylor@redhat.com>
- Rebuild for new gnome2 libraries

* Mon Jan 28 2002 Alex Larsson <alexl@redhat.com>
- Initial build.
