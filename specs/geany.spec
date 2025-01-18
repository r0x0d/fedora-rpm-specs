%global geany_docdir %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}

# The  Python templates in /usr/share/geany/templates can not be byte-compiled.
%undefine  py_auto_byte_compile

Name:      geany
Version:   2.0
Release:   6%{?dist}
Summary:   A fast and lightweight IDE using GTK3

# Automatically converted from old format: GPLv2+ and MIT - review is highly recommended.
License:   GPL-2.0-or-later AND LicenseRef-Callaway-MIT
URL:       http://www.geany.org/
Source0:   http://download.geany.org/%{name}-%{version}.tar.bz2

BuildRequires: gcc gcc-c++
BuildRequires: python3-docutils
BuildRequires: desktop-file-utils, gettext, pango-devel, intltool
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: perl(XML::Parser)
BuildRequires: make

Requires: vte291%{?_isa}
Requires: geany-libgeany = %{version}-%{release}

Provides: bundled(scintilla) = 5.3.7
Provides: bundled(lexilla) = 5.2.7

Recommends: xterm


%description
Geany is a small and fast integrated development environment with basic
features and few dependencies to other packages or Desktop Environments.

Some features:
- Syntax highlighting
- Code completion
- Code folding
- Construct completion/snippets
- Auto-closing of XML and HTML tags
- Call tips
- Support for Many languages like C, Java, PHP, HTML, Python, Perl, Pascal
- symbol lists and symbol name auto-completion
- Code navigation
- Simple project management
- Plugin interface


%package libgeany
Summary:   Core functions of Geany
Requires:  geany = %{version}-%{release}

%description libgeany
This package contains the core functions of Geany which will be used by
Geany plugins.


%package devel
Summary:   Header files for building Geany plug-ins
Requires:  geany = %{version}-%{release}
Requires:  pkgconfig gtk3-devel

%description devel
This package contains the header files and pkg-config file needed for building
Geany plug-ins. You do not need to install this package to use Geany.

%prep
%setup -q

# remove waf since this isn't needed for the build, we're building the package
# with autotools
rm -f waf
rm -f wscript


%build
RST2HTML=/usr/bin/rst2html-3

%configure --docdir=%{geany_docdir} --enable-gtk3
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT DOCDIR=$RPM_BUILD_ROOT/%{geany_docdir}
rm -f $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.ico
desktop-file-install --delete-original \
        --dir=${RPM_BUILD_ROOT}%{_datadir}/applications         \
        --mode 0644                                             \
        $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop
%find_lang %{name}

# remove static libraries
find $RPM_BUILD_ROOT -name "*.la" -delete

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Richard Hughes <richard@hughsie.com> -->
<!--
BugReportURL: https://sourceforge.net/p/geany/feature-requests/739/
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">geany.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <description>
    <p>
      Geany is a small and lightweight Integrated Development Environment.
      It was developed to provide a small and fast IDE.
      Another goal was to be as independent as possible from a KDE or GNOME -
      Geany only requires the GTK3 runtime libraries.
    </p>
  <!-- FIXME: Probably needs another paragraph or two -->
  </description>
  <url type="homepage">http://www.geany.org/</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/geany/a.png</screenshot>
    <screenshot>https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/geany/b.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

%files -f %{name}.lang
%exclude %{geany_docdir}/TODO

%doc %{geany_docdir}
%doc %{_mandir}/man1/geany.1*

%{_bindir}/%{name}
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*/*/*/*.svg
%{_datadir}/icons/*/*/*/*.png

%files libgeany
%{_libdir}/libgeany.so*

%files devel
%doc HACKING TODO
%{_includedir}/geany
%{_libdir}/pkgconfig/geany.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 23 2023 Dominic Hopf <dmaphy@fedoraproject.org> - 2.0-1
- New upstream release: Geany 2.0

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.38-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.38-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.38-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 09 2021 Dominic Hopf <dmaphy@fedoraproject.org> - 1.38-1
- New upstream release: Geany 1.38

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.37.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.37.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Nov 08 2020 Dominic Hopf <dmaphy@fedoraproject.org> - 1.37.1-1
- New upstream release: Geany 1.37.1

* Sat Oct 31 2020 Jeff Law <law@redhat.com> - 1.37-2
- Fix bogus volatile caught by gcc-11

* Sun Oct 25 2020 Dominic Hopf <dmaphy@fedoraproject.org> - 1.37-1
- New upstream release: Geany 1.37

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Dominic Hopf <dmaphy@fedoraproject.org> - 1.36-3
- Add Recommends for xterm (RHBZ#1793743)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 29 2019 Dominic Hopf <dmaphy@fedoraproject.org> - 1.36-1
- New upstream release: Geany 1.36

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 04 2019 Dominic Hopf <dmaphy@fedoraproject.org> - 1.35-1
- New upstream release: Geany 1.35

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.34.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 05 2019 Dominic Hopf <dmaphy@fedoraproject.org> - 1.34.1-2
- New upstream release: Geany 1.34.1

* Mon Dec 31 2018 Dominic Hopf <dmaphy@fedoraproject.org> - 1.34-1
- New upstream release: Geany 1.34
- Use the Python3 version of rst2html

* Mon Aug 13 2018 Kalev Lember <klember@redhat.com> - 1.33-4
- Require newer vte291 instead of vte3

* Sun Jul 22 2018 Dominic Hopf <dmaphy@fedoraproject.org> - 1.33-3
- RHBZ#1604065: Fix FTBFS, add gcc-c++ as BuildRequires

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Dominic Hopf <dmaphy@fedoraproject.org> - 1.33-1
- New upstream release: Geany 1.33

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 Dominic Hopf <dmaphy@fedoraproject.org> - 1.32-3
- Use pkgconfig to define requires (RHBZ#1539329)
- Fix license tag (RHBZ#1539333)

* Mon Nov 27 2017 Dominic Hopf <dmaphy@fedoraproject.org> - 1.32-1
- New upstream release: Geany 1.32

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Florian Weimer <fweimer@redhat.com> - 1.31-4
- Rebuild with binutils fix for ppc64le (#1475636)

* Wed Jul 26 2017 Dominic Hopf <dmaphy@fedoraproject.org> - 1.31-3
- Rebuild against GTK3 (RHBZ#1368632)
- Thanks very much to Rok Mandeljc for his efforts on this!

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 22 2017 Dominic Hopf <dmaphy@fedoraproject.org> - 1.31-1
- New upstream release: Geany 1.31

* Sun Mar 19 2017 Dominic Hopf <dmaphy@fedoraproject.org> - 1.30.1-1
- New upstream release: Geany 1.30.1

* Sun Mar 05 2017 Dominic Hopf <dmaphy@fedoraproject.org> - 1.30-2
- New upstream release: Geany 1.30

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 13 2016 Dominic Hopf <dmaphy@fedoraproject.org> - 1.29-2
- New upstream release: Geany 1.29
- Remove installation of obsolete tags files (RHBZ#1378631)
- undefine py_auto_byte_compile (RHBZ#1378646)
- fix typo in description (RHBZ#1378638)

* Mon Jul 11 2016 Dominic Hopf <dmaphy@fedoraproject.org> - 1.28-2
- Version of bundled Scintilla has changed as well: 3.5.6 -> 3.6.6

* Sun Jul 10 2016 Dominic Hopf <dmaphy@fedoraproject.org> - 1.28-1
- New upstream release: Geany 1.28

* Wed Mar 16 2016 Dominic Hopf <dmaphy@fedoraproject.org> - 1.27-1
- New upstream release: Geany 1.27

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 18 2015 Dominic Hopf <dmaphy@fedoraproject.org> - 1.26-1
- New upstream release: Geany 1.26

* Fri Aug 21 2015 Dominic Hopf <dmaphy@fedoraproject.org> - 1.25-6
- fix depency for geany-devel on GTK

* Wed Aug 19 2015 Dominic Hopf <dmaphy@fedoraproject.org> - 1.25-5
- roll back to GTK2

* Mon Jul 27 2015 Dominic Hopf <dmaphy@fedoraproject.org> - 1.25-4
- require vte3 instead of vte (RHBZ#1245831)
- do not require gtk3-devel for libgeany subpackage

* Tue Jul 14 2015 François Cami <fcami@fedoraproject.org> - 1.25-3
- Geany 1.25 bundles scintilla 3.5.6.
- Fix the included AppData file (GTK2 => GTK3).

* Mon Jul 13 2015 François Cami <fcami@fedoraproject.org> - 1.25-2
- Switch to gtk3 + disable rpath.

* Mon Jul 13 2015 Dominic Hopf <dmaphy@fedoraproject.org> - 1.25-1
- New upstream release: Geany 1.25

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Jason L Tibbitts III <tibbs@math.uh.edu> - 1.24.1-7
- Indicate that the package bundles scintilla 3.3.6.

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.24.1-6
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1.24.1-5
- Add an AppData file for the software center

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1.24.1-4
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 17 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 1.24.1-1 
- New upstream release: Geany 1.24.1

* Tue Apr 15 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 1.24-1
- New upstream release: Geany 1.24
- update sqlite3.c.tags and add std.css.tags for CSS3
- fix bogus date warnings

* Fri Jul 26 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.23.1-2
- Install docs to %%{_pkgdocdir} where available.

* Sun May 19 2013 Dominic Hopf <dmaphy@fedoraproject.org> - 1.23.1-1
- New upstream release: Geany 1.23.1

* Tue Apr 09 2013 Jon Ciesla <limburgher@gmail.com> - 1.23-2
- Drop desktop vendor tag.

* Sun Mar 10 2013 Dominic Hopf <dmaphy@fedoraproject.org> - 1.23-1
- New upstream release: Geany 1.23

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Dominic Hopf <dmaphy@fedoraproject.org> - 1.22-1
- New upstream release: Geany 1.22
- remove the previous patch to fix DSO linking, this is now included upstream
- update upstream URLs for tags files

* Mon May 21 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.21-5
- Add patch to fix FTBFS due to DSO linking, spec cleanup

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Dec 24 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 0.21-3
- update GTK+ tags to 2.24

* Sun Dec 18 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 0.21-2
- update Xfce tags to 4.8

* Sun Oct 02 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 0.21-1
- New upstream release: Geany 0.21

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 08 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 0.20-2
- install tags files correctly

* Thu Jan 06 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 0.20-1
- new upstream release
- a lot of new tags files

* Wed Dec 01 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.19.2-1
- New upstream release: Geany 0.19.2

* Fri Nov 19 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.19.1-2
- run update-desktop-database in %%post (#655152)

* Thu Aug 19 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.19.1-1
- New upstream release: Geany 0.19.1

* Sun Jun 13 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.19-2
- update tags files for GTK 2.20 and Geany Plugin API 0.19

* Sat Jun 12 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.19-1
- New upstream release: Geany 0.19

* Sun Apr 18 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.18.1-3
- improve handling of documentation directory
- add upstream comment about the desktopfile patch

* Thu Apr 15 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.18.1-2
- move TODO and HACKING into devel package
- add patch to fix mimetypes in desktop-file
- add Tcl tags
- replace the .gz of manpage with wildcard

* Sun Feb 14 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.18.1-1
- New Geany release: 0.18.1
- update GTK2 tags to 2.18
- add tags fpr drupal, LaTeX and libxml
- remove files concerned to the waf build system
- give the Summary and description a small rework

* Sun Aug 16 2009 Dominic Hopf <dmaphy@fedoraproject.org> - 0.18-6
- release bump to correct the update path

* Sun Aug 16 2009 Dominic Hopf <dmaphy@fedoraproject.org> - 0.18-2
- update icon cache

* Sun Aug 16 2009 Dominic Hopf <dmaphy@fedoraproject.org> - 0.18-1
- new upstream release
- remove button pixmaps patch since this fix is included in 0.18
- add new tags-files geany-api-0.18.c.tags and std.vala.tags
- remove Geany icon from pixmaps path and add it to 48x48 and scalable

* Mon Jul 27 2009 Dominic Hopf <dmaphy@fedoraproject.org> - 0.17-9
- install additional *.tags-files to $prefix/share/geany/tags

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jun 20 2009 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.17-7
- Fix commentary about button pixmap patch in spec file

* Sat Jun 20 2009 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.17-6
- Add new patch to fix button pixmaps
- Remove debug patch and previous patch to fix button pixmaps
- Remove tango icon patch

* Sat Jun 20 2009 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.17-5
- Fix spec file typo

* Sat Jun 20 2009 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.17-4
- Add patch to output debugging message

* Sat Jun 20 2009 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.17-3
- Add patch to fix missing button pixmaps

* Fri Jun 19 2009 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.17-2
- Add patch to give a tango Save All button

* Wed May 20 2009 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.17-1
- Update to version 0.17
- Replace gtk214.c.tags with gtk216.c.tags
- Add standard.css.tags
- Add all tags files to CVS

* Wed Apr 15 2009 pingou <pingou@pingoured.fr> - 0.16-3
- Add requires for gtk2-devel to geany-devel

* Thu Apr  2 2009 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.16-2
- Add Requires for pkgconfig to geany-devel subpackage (BZ 493566)

* Wed Feb 25 2009 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.16-1
- Update to 0.16
- Add tags files

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Oct 26 2008 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.15-1
- Update to 0.15
- Update URL
- Add intltool to BuildRequires

* Sun May 11 2008 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.14-1
- Update to 0.14
- New -devel sub-package for header files
- Corectly remove the .la libtool files
- Remove hack relating to finding the system installed html files
- No longer correct the desktop file

* Mon Mar 24 2008 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.13-2
- Fix docdir/doc_dir so geany correctly finds the system installed html docs (BZ
  438534)

* Sun Feb 24 2008 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.13-1
- Update to version 0.13

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.12-5
- Autorebuild for GCC 4.3

* Thu Oct 18 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.12-4
- Fix license tag
- Package new library files
- Remove static library .la files
- Package new icons

* Thu Oct 18 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.12-3
- Fix Version entry in .desktop file again

* Thu Oct 18 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.12-2
- Add a BuildRequires for perl(XML::Parser)

* Thu Oct 18 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.12-1
- Update to version 0.12

* Sun Sep  9 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.11-2
- Fix Version entry in .desktop file

* Sun Sep  9 2007 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.11-1
- Update to version 0.11

* Fri Feb 23 2007 Josef Whiter <josef@toxicpanda.com> 0.10.1-1
- updating to 0.10.1 of geany

* Thu Jan 25 2007 Josef Whiter <josef@toxicpanda.com> 0.10-5
- removed autoconf/automake/vte-devel from BR as they are not needed
- removed patch to dynamically link in libvte
- adding patch to find appropriate libvte library from the vte package
- added vte as a Requires

* Wed Jan 24 2007 Josef Whiter <josef@toxicpanda.com> 0.10-4
- added autoconf and automake as a BR

* Wed Jan 24 2007 Josef Whiter <josef@toxicpanda.com> 0.10-3
- adding patch to dynamically link in libvte instead of using g_module_open

* Thu Jan 04 2007 Josef Whiter <josef@toxicpanda.com> 0.10-2
- Fixed mixed spaces/tabs problem
- added sed command to install to fix the ScintillaLicense.txt eol encoding
- fixed the docs so they are installed into the right place
- added an rm pixmaps/geany.ico, its only for windows installations

* Thu Dec 28 2006 Josef Whiter <josef@toxicpanda.com> 0.10-1
- Initial Release
