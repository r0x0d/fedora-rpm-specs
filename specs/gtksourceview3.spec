%global glib_version 2.48
%global gtk_version 3.20

%global po_package gtksourceview-3.0

Name: gtksourceview3
Version: 3.24.11
Release: 15%{?dist}
Summary: Source code editing widget

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL: https://wiki.gnome.org/Projects/GtkSourceView
Source0: https://download.gnome.org/sources/gtksourceview/3.24/gtksourceview-%{version}.tar.xz
# fix build with GCC 14 -Wincompatible-pointer-types
Patch0:  0001-gcc14.patch

BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(glib-2.0) >= %{glib_version}
BuildRequires: pkgconfig(gtk+-3.0) >= %{gtk_version}
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(pango)
BuildRequires: gettext
BuildRequires: itstool
BuildRequires: vala
BuildRequires: make

Requires: glib2%{?_isa} >= %{glib_version}
Requires: gtk3%{?_isa} >= %{gtk_version}

%description
GtkSourceView is a GNOME library that extends GtkTextView, the standard GTK+
widget for multiline text editing. GtkSourceView adds support for syntax
highlighting, undo/redo, file loading and saving, search and replace, a
completion system, printing, displaying line numbers, and other features
typical of a source code editor.

This package contains version 3 of GtkSourceView.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package tests
Summary: Tests for the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
The %{name}-tests package contains tests that can be used to verify
the functionality of the installed %{name} package.

%prep
%autosetup -n gtksourceview-%{version} -p1

%build
%configure --disable-gtk-doc --disable-static --enable-installed-tests

make %{?_smp_mflags}

%install
%make_install

# remove unwanted files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{po_package}

%ldconfig_scriptlets

%files -f %{po_package}.lang
%doc README AUTHORS NEWS MAINTAINERS
%license COPYING
%{_datadir}/gtksourceview-3.0
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/GtkSource-3.0.typelib

%files devel
%{_includedir}/gtksourceview-3.0
%{_datadir}/gtk-doc/html/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_datadir}/gir-1.0/GtkSource-3.0.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gtksourceview-3.0.deps
%{_datadir}/vala/vapi/gtksourceview-3.0.vapi

%files tests
%{_libexecdir}/installed-tests/gtksourceview-3.0/
%{_datadir}/installed-tests/gtksourceview-3.0/

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.11-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 3.24.11-14
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 2019 Kalev Lember <klember@redhat.com> - 3.24.11-1
- Update to 3.24.11

* Sat Mar 16 2019 Kalev Lember <klember@redhat.com> - 3.24.10-1
- Update to 3.24.10

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Sep 07 2018 Kalev Lember <klember@redhat.com> - 3.24.9-4
- Rebuilt against fixed atk (#1626575)

* Fri Sep 07 2018 Pete Walter <pwalter@fedoraproject.org> - 3.24.9-3
- Drop glade catalog to avoid conflicting with gtksourceview4

* Fri Sep 07 2018 Pete Walter <pwalter@fedoraproject.org> - 3.24.9-2
- Update description to match gtksourceview4

* Fri Sep 07 2018 Kalev Lember <klember@redhat.com> - 3.24.9-1
- Update to 3.24.9

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Kalev Lember <klember@redhat.com> - 3.24.8-1
- Update to 3.24.8

* Wed Mar 14 2018 Kalev Lember <klember@redhat.com> - 3.24.7-1
- Update to 3.24.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.24.6-2
- Switch to %%ldconfig_scriptlets

* Mon Dec 11 2017 Kalev Lember <klember@redhat.com> - 3.24.6-1
- Update to 3.24.6

* Thu Oct 12 2017 Kalev Lember <klember@redhat.com> - 3.24.5-1
- Update to 3.24.5

* Thu Sep 07 2017 Kalev Lember <klember@redhat.com> - 3.24.4-1
- Update to 3.24.4

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.24.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Kalev Lember <klember@redhat.com> - 3.24.3-1
- Update to 3.24.3

* Mon Jun 12 2017 Kalev Lember <klember@redhat.com> - 3.24.2-1
- Update to 3.24.2

* Tue Apr 11 2017 Kalev Lember <klember@redhat.com> - 3.24.1-1
- Update to 3.24.1

* Tue Mar 21 2017 Kalev Lember <klember@redhat.com> - 3.24.0-1
- Update to 3.24.0

* Thu Mar 16 2017 Kalev Lember <klember@redhat.com> - 3.23.91-1
- Update to 3.23.91

* Tue Feb 14 2017 Richard Hughes <rhughes@redhat.com> - 3.23.90-1
- Update to 3.23.90

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 30 2016 Kalev Lember <klember@redhat.com> - 3.23.1-1
- Update to 3.23.1

* Thu Sep 22 2016 Kalev Lember <klember@redhat.com> - 3.22.0-2
- BR vala instead of obsolete vala-tools subpackage

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Sun Sep 11 2016 Kalev Lember <klember@redhat.com> - 3.21.6-1
- Update to 3.21.6
- Don't set group tags

* Thu Aug 18 2016 Kalev Lember <klember@redhat.com> - 3.21.5-1
- Update to 3.21.5

* Sun Aug 14 2016 Kalev Lember <klember@redhat.com> - 3.21.4-1
- Update to 3.21.4

* Sun Jul 17 2016 Kalev Lember <klember@redhat.com> - 3.21.3-1
- Update to 3.21.3

* Mon Jun 20 2016 David King <amigadave@amigadave.com> - 3.21.2-1
- Update to 3.21.2

* Tue May 03 2016 Kalev Lember <klember@redhat.com> - 3.21.1-1
- Update to 3.21.1

* Wed Mar 30 2016 Kalev Lember <klember@redhat.com> - 3.20.1-1
- Update to 3.20.1

* Sun Mar 20 2016 Kalev Lember <klember@redhat.com> - 3.20.0-1
- Update to 3.20.0

* Thu Feb 04 2016 David King <amigadave@amigadave.com> - 3.19.4-3
- Update URL
- Use global rather than define

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Kalev Lember <klember@redhat.com> - 3.19.4-1
- Update to 3.19.4

* Tue Dec 08 2015 Kalev Lember <klember@redhat.com> - 3.19.3-1
- Update to 3.19.3

* Mon Nov 23 2015 Kalev Lember <klember@redhat.com> - 3.19.2-1
- Update to 3.19.2

* Wed Oct 28 2015 Kalev Lember <klember@redhat.com> - 3.19.1-1
- Update to 3.19.1

* Sun Oct 11 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Sun Sep 20 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Mon Sep 14 2015 Kalev Lember <klember@redhat.com> - 3.17.7-1
- Update to 3.17.7

* Sun Aug 30 2015 Kalev Lember <klember@redhat.com> - 3.17.6-1
- Update to 3.17.6

* Sun Aug 16 2015 Kalev Lember <klember@redhat.com> - 3.17.5-1
- Update to 3.17.5
- Use make_install macro

* Mon Jul 20 2015 David King <amigadave@amigadave.com> - 3.17.4-1
- Update to 3.17.4

* Mon Jun 22 2015 David King <amigadave@amigadave.com> - 3.17.3-1
- Update to 3.17.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 25 2015 David King <amigadave@amigadave.com> - 3.17.2-1
- Update to 3.17.2

* Fri May 01 2015 Kalev Lember <kalevlember@gmail.com> - 3.17.1-1
- Update to 3.17.1

* Sun Apr 12 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.1-1
- Update to 3.16.1

* Sun Mar 22 2015 Kalev Lember <kalevlember@gmail.com> - 3.16.0-1
- Update to 3.16.0

* Thu Mar 05 2015 Kalev Lember <kalevlember@gmail.com> - 3.15.91-1
- Update to 3.15.91
- Set minimum required glib version

* Sun Feb 15 2015 David King <amigadave@amigadave.com> - 3.15.90-1
- Update to 3.15.90
- Use license macro for COPYING
- Use pkgconfig for BuildRequires

* Mon Jan 19 2015 Richard Hughes <rhughes@redhat.com> - 3.15.3-1
- Update to 3.15.3

* Tue Nov 25 2014 Kalev Lember <kalevlember@gmail.com> - 3.15.2-1
- Update to 3.15.2

* Mon Nov 10 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.2-1
- Update to 3.14.2

* Mon Oct 13 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.1-1
- Update to 3.14.1

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.14.0-1
- Update to 3.14.0

* Tue Sep 16 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.91-1
- Update to 3.13.91

* Thu Sep 4 2014 Vadim Rutkovsky <vrutkovs@redhat.com> - 3.13.90-2
- Build installed tests (#1117380)

* Mon Aug 18 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.90-1
- Update to 3.13.90
- Include vala vapi files

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Aug 12 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.3-1
- Update to 3.13.3

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.2-2
- Rebuilt for gobject-introspection 1.41.4

* Mon Jul 21 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.2-1
- Update to 3.13.2
- gtksourceview is now fully relicensed to LGPL, update the license tag

* Tue Jun 24 2014 Richard Hughes <rhughes@redhat.com> - 3.13.1-1
- Update to 3.13.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.2-1
- Update to 3.12.2

* Tue Apr 15 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.1-1
- Update to 3.12.1

* Sat Apr 05 2014 Kalev Lember <kalevlember@gmail.com> - 3.12.0-2
- Tighten -devel deps
- Set minimum required gtk3 version

* Mon Mar 24 2014 Richard Hughes <rhughes@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Tue Mar 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.91-1
- Update to 3.11.91

* Tue Feb 18 2014 Richard Hughes <rhughes@redhat.com> - 3.11.90-1
- Update to 3.11.90

* Thu Feb 06 2014 Ignacio Casal Quinteiro <icq@gnome.org> - 3.11.4-1
- Update to 3.11.4

* Tue Jan 14 2014 Richard Hughes <rhughes@redhat.com> - 3.11.3-1
- Update to 3.11.3

* Tue Dec 17 2013 Richard Hughes <rhughes@redhat.com> - 3.11.2-1
- Update to 3.11.2

* Tue Oct 29 2013 Richard Hughes <rhughes@redhat.com> - 3.11.1-1
- Update to 3.11.1

* Mon Oct 14 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 3.10.1-1
- Update to 3.10.1

* Tue Sep 24 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 3.10.0-1
- Update to 3.10.0

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.92-1
- Update to 3.9.92

* Tue Sep 03 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.91-1
- Update to 3.9.91

* Thu Aug 22 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.90-1
- Update to 3.9.90

* Wed Aug 07 2013 Adam Williamson <awilliam@redhat.com> - 3.9.4-1
- Update to 3.9.4

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 16 2013 Richard Hughes <rhughes@redhat.com> - 3.9.3-1
- Update to 3.9.3

* Thu Jun 20 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.2-1
- Update to 3.9.2

* Sun Jun 02 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.1-1
- Update to 3.9.1

* Mon May 13 2013 Matthias Clasen <mclasen@redhat.com> - 3.8.1-2
- Install a glade catalog

* Mon Apr 15 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 3.8.1-1
- Update to 3.8.1

* Mon Mar 25 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 3.8.0-1
- Update to 3.8.0

* Tue Mar 19 2013 Richard Hughes <rhughes@redhat.com> - 3.7.92-1
- Update to 3.7.92

* Thu Mar 07 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 3.7.91-1
- Update to 3.7.91

* Tue Feb 19 2013 Richard Hughes <rhughes@redhat.com> - 3.7.90-1
- Update to 3.7.90

* Mon Feb 04 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 3.7.3-1
- Update to 3.7.3

* Wed Jan 16 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 3.7.2-1
- Update to 3.7.2

* Mon Jan 07 2013 Ignacio Casal Quinteiro <icq@gnome.org> - 3.7.1-1
- Update to 3.7.1

* Mon Nov 05 2012 Ray Strode <rstrode@redhat.com> 3.6.1-1
- Update to 3.6.1

* Mon Sep 24 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 3.6.0-1
- Update to 3.6.0

* Wed Sep 19 2012 Richard Hughes <hughsient@gmail.com> - 3.5.4-1
- Update to 3.5.4

* Tue Aug 21 2012 Richard Hughes <hughsient@gmail.com> - 3.5.3-1
- Update to 3.5.3

* Tue Jul 31 2012 Richard Hughes <hughsient@gmail.com> - 3.5.2-1
- Update to 3.5.2

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 17 2012 Kalev Lember <kalevlember@gmail.com> - 3.4.2-1
- Update to 3.4.2

* Mon Apr 16 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 3.4.1-1
- Update to 3.4.1

* Mon Mar 26 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 3.4.0-1
- Update to 3.4.0

* Wed Mar 21 2012 Kalev Lember <kalevlember@gmail.com> - 3.3.5-1
- Update to 3.3.5

* Fri Feb 24 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 3.3.4-1
- Update to 3.3.4

* Mon Feb  6 2012 Matthias Clasen <mclasen@redhat.com> - 3.3.3-1
- Update to 3.3.3

* Sun Jan 08 2012 Ignacio Casal Quinteiro <icq@gnome.org> - 3.3.2-1
- Update to 3.3.2

* Sat Dec 17 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.3.1-1
- Update to 3.3.1

* Tue Nov 01 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.2.3-1
- Update to 3.2.3

* Sun Oct 16 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.2.2-1
- Update to 3.2.2

* Sun Oct 09 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.2.1-1
- Update to 3.2.1

* Mon Sep 26 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.2.0-1
- Update to 3.2.0

* Tue Sep 20 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.1.6-1
- Update to 3.1.6

* Tue Sep 06 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.1.5-1
- Update to 3.1.5

* Mon Aug 08 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.1.4-1
- Update to 3.1.4

* Mon Jul 04 2011 Ignacio Casal Quinteiro <icq@gnome.org> - 3.1.3-1
- Update to 3.1.3

* Thu Jun 16 2011 Tomas Bzatek <tbzatek@redhat.com> - 3.1.2-1
- Update to 3.1.2

* Tue Apr 26 2011 Matthias Clasen <mclasen@redhat.com> 3.0.1-1
- Update to 3.0.1

* Mon Apr  4 2011 Matthias Clasen <mclasen@redhat.com> 3.0.0-1
- Update to 3.0.0

* Tue Mar 22 2011 Matthias Clasen <mclasen@redhat.com> 2.91.9-1
- Update to 2.91.9

* Mon Mar  7 2011 Matthias Clasen <mclasen@redhat.com> 2.91.8-1
- Update to 2.91.8

* Tue Feb 22 2011 Matthias Clasen <mclasen@redhat.com> 2.91.6-1
- Update to 2.91.6

* Thu Feb 10 2011 Matthias Clasen <mclasen@redhat.com> 2.91.5-3
- Rebuild against newer gtk

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.91.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Matthias Clasen <mclasen@redhat.com> 2.91.5-1
- Update to 2.91.5

* Mon Jan 10 2011 Matthias Clasen <mclasen@redhat.com> 2.91.4-1
- Update to 2.91.4

* Sat Jan  8 2011 Matthias Clasen <mclasen@redhat.com> 2.91.3-1
- Update to 2.91.3

* Fri Dec  3 2010 Tomas Bzatek <tbzatek@redhat.com> 2.91.2-1
- Update to 2.91.2

* Tue Nov  2 2010 Matthias Clasen <mclasen@redhat.com> 2.91.1-1
- Update to 2.91.1

* Wed Oct  6 2010 Matthias Clasen <mclasen@redhat.com> 2.91.0-1
- Update to 2.91.0

* Wed Sep 29 2010 jkeating - 2.90.4-5.git7701e36
- Rebuilt for gcc bug 634757

* Tue Sep 21 2010 Matthias Clasen <mclasen@redhat.com> - 2.90.4-4.git7701e36
- git snapshot
- Rebuild with newer gobject-introspection

* Thu Jul 15 2010 Colin Walters <walters@verbum.org> - 2.90.4-2
- Rebuild with new gobject-introspection

* Tue Jul 13 2010 Matthias Clasen <mclasen@redhat.com> - 2.90.4-1
- Update to 2.90.4

* Tue Jun 29 2010 Matthias Clasen <mclasen@redhat.com> - 2.90.3-2
- Incorporate some review feedback

* Tue Jun 29 2010 Matthias Clasen <mclasen@redhat.com> - 2.90.3-1
- Initial packaging of GtkSourceview 3
