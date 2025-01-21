Name:		totem-pl-parser
Version:	3.26.6
Release:	12%{?dist}
Summary:	Totem Playlist Parser library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:	LicenseRef-Callaway-LGPLv2+
Url:		https://wiki.gnome.org/Apps/Videos
Source0:	https://download.gnome.org/sources/%{name}/3.26/%{name}-%{version}.tar.xz
Patch0: totem-pl-parser-c99.patch

BuildRequires:	glib2-devel
BuildRequires:	libxml2-devel
BuildRequires:	gobject-introspection-devel
BuildRequires:	gettext
BuildRequires:	gtk-doc
BuildRequires:	libarchive-devel
BuildRequires:	libgcrypt-devel
BuildRequires:	uchardet-devel
BuildRequires:	meson

%description
A library to parse and save playlists, as used in music and movie players.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%meson -Denable-gtk-doc=true \
	-Denable-libarchive=yes \
	-Denable-libgcrypt=yes \
	-Dintrospection=true
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING.LIB
%doc AUTHORS NEWS README.md
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/*.typelib
%{_libexecdir}/totem-pl-parser/

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gtk-doc/html/totem-pl-parser
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/*.gir

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 3.26.6-11
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Florian Weimer <fweimer@redhat.com> - 3.26.6-8
- Fix C compatibility issue

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 29 2021 Bastien Nocera <bnocera@redhat.com> - 3.26.6-2
+ totem-pl-parser-3.26.6-2
- Build with character set detection (#1977257)

* Fri Jun 25 2021 Bastien Nocera <bnocera@redhat.com> - 3.26.6-1
+ totem-pl-parser-3.26.6-1
- Update to 3.26.6

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Sep 29 2020 Bastien Nocera <bnocera@redhat.com> - 3.26.5-3
+ totem-pl-parser-3.26.5-3
- Disable quvi, upstream is dead, and it doesn't compile with lua 5.4

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 28 2020 Bastien Nocera <bnocera@redhat.com> - 3.26.5-1
+ totem-pl-parser-3.26.5-1
- Update to 3.26.5

* Fri Feb 14 2020 Bastien Nocera <bnocera@redhat.com> - 3.26.4-3
+ totem-pl-parser-3.26.4-3
- Disable quvi support on RHEL

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Bastien Nocera <bnocera@redhat.com> - 3.26.4-1
+ totem-pl-parser-3.26.4-1
- Update to 3.26.4

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 Kalev Lember <klember@redhat.com> - 3.26.3-1
- Update to 3.26.3

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 16 2019 Bastien Nocera <bnocera@redhat.com> - 3.26.2-1
+ totem-pl-parser-3.26.2-1
- Update to 3.26.2, remove unused libsoup and gmime dependencies

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Bastien Nocera <bnocera@redhat.com> - 3.26.1-1
+ totem-pl-parser-3.26.1-1
- Update to 3.26.1
- Fixes KQED podcast parsing (#1560759)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 11 2017 Merlin Mathesius <mmathesi@redhat.com> - 3.26.0-2
- Cleanup spec file conditionals

* Thu Sep 14 2017 Kalev Lember <klember@redhat.com> - 3.26.0-1
- Update to 3.26.0

* Fri Sep 08 2017 Kalev Lember <klember@redhat.com> - 3.25.90-3
- Switch to gmime 3.0

* Fri Aug 11 2017 Kalev Lember <klember@redhat.com> - 3.25.90-2
- Bump and rebuild for an rpm signing issue

* Thu Aug 10 2017 Kalev Lember <klember@redhat.com> - 3.25.90-1
- Update to 3.25.90

* Mon Jul 31 2017 Kalev Lember <klember@redhat.com> - 3.25.3-3
- Backport an upstream patch to fix rhythmbox build

* Mon Jul 31 2017 Florian Weimer <fweimer@redhat.com> - 3.25.3-2
- Rebuild with binutils fix for ppc64le (#1475636)

* Thu Jul 27 2017 Kalev Lember <klember@redhat.com> - 3.25.3-1
- Update to 3.25.3

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 21 2016 Kalev Lember <klember@redhat.com> - 3.10.7-1
- Update to 3.10.7
- Update project URLs
- Use make_install macro

* Fri Sep 02 2016 Kalev Lember <klember@redhat.com> - 3.10.6-3
- Drop old obsoletes
- Don't set group tags

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Kalev Lember <klember@redhat.com> - 3.10.6-1
- Update to 3.10.6

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 30 2015 Kalev Lember <kalevlember@gmail.com> - 3.10.5-1
- Update to 3.10.5
- Use license macro for COPYING.LIB

* Thu Feb 19 2015 Richard Hughes <rhughes@redhat.com> - 3.10.4-1
- Update to 3.10.4

* Tue Oct 28 2014 Richard Hughes <rhughes@redhat.com> - 3.10.3-2
- Do not use quvi when compiling for non-Fedora.

* Mon Sep 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.10.3-1
- Update to 3.10.3
- Tighten subpackage requires with the _isa macro

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 3.10.2-3
- Rebuilt for gobject-introspection 1.41.4

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 24 2014 Richard Hughes <rhughes@redhat.com> - 3.10.2-1
- Update to 3.10.2

* Wed Feb 19 2014 Richard Hughes <rhughes@redhat.com> - 3.10.1-1
- Update to 3.10.1

* Fri Nov 29 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 3.10.0-2
- Rebuild for libquvi SONAME change.

* Wed Sep 25 2013 Kalev Lember <kalevlember@gmail.com> - 3.10.0-1
- Update to 3.10.0

* Wed Sep 18 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.92-1
- Update to 3.9.92

* Tue Aug 27 2013 Kalev Lember <kalevlember@gmail.com> - 3.9.5-1
- Update to 3.9.5

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Richard Hughes <rhughes@redhat.com> - 3.4.5-1
- Update to 3.4.5

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 3.4.4-1
- Update to 3.4.4

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 17 2013 Tomas Bzatek <tbzatek@redhat.com> - 3.4.3-2
- Rebuilt for new libarchive

* Wed Sep 19 2012 Tomas Bzatek <tbzatek@redhat.com> - 3.4.3-1
- Update to 3.4.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 18 2012 Richard Hughes <hughsient@gmail.com> - 3.4.2-1
- Update to 3.4.2

* Sat Apr 28 2012 Bastien Nocera <bnocera@redhat.com> 3.4.1-2
- Remove dependency on gtk2-devel for the devel sub-package

* Mon Apr 16 2012 Richard Hughes <hughsient@gmail.com> - 3.4.1-1
- Update to 3.4.1

* Tue Mar 27 2012 Richard Hughes <hughsient@gmail.com> - 3.4.0-1
- Update to 3.4.0

* Tue Mar 20 2012 Kalev Lember <kalevlember@gmail.com> - 3.3.92-1
- Update to 3.3.92

* Sun Feb 26 2012 Matthias Clasen <mclasen@redhat.com> - 3.2.0-1
- Update to 3.2.0

* Thu Jan 26 2012 Tomas Bzatek <tbzatek@redhat.com> - 2.32.6-5
- Rebuilt for new libarchive

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 17 2011 Daniel Drake <dsd@laptop.org> 2.32.6-3
- Add upstream compile fix for libquvi.so.7 (and rebuild for this version)
- Add upstream compile fix for glib-2.31

* Wed Nov 16 2011 Peter Robinson <pbrobinson@fedoraproject.org> 2.32.6-2
- Rebuild for new libarchive and quvi

* Tue Sep 20 2011 Bastien Nocera <bnocera@redhat.com> 2.32.6-1
- Update to 2.32.6

* Mon Jun 27 2011 Adam Williamson <awilliam@redhat.com> 2.32.5-2
- rebuild for new quvi

* Wed May 11 2011 Bastien Nocera <bnocera@redhat.com> 2.32.5-1
- Update to 2.32.5

* Mon Mar 21 2011 Bastien Nocera <bnocera@redhat.com> 2.32.4-1
- Update to 2.32.4

* Mon Feb 21 2011 Bastien Nocera <bnocera@redhat.com> 2.32.3-1
- Update to 2.32.3

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.32.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 31 2011 Bastien Nocera <bnocera@redhat.com> 2.32.2-2
- Fix quvi version dependency

* Fri Jan 28 2011 Bastien Nocera <bnocera@redhat.com> 2.32.2-1
- Update to 2.32.2

* Thu Jan 13 2011 Matthias Clasen <mclasen@redhat.com> 2.32.1-2
- Move girs to -devel

* Mon Oct 18 2010 Bastien Nocera <bnocera@redhat.com> 2.32.1-1
- Update to 2.32.1

* Tue Sep 28 2010 Bastien Nocera <bnocera@redhat.com> 2.32.0-1
- Update to 2.32.0

* Wed Sep 22 2010 Matthias Clasen <mclasen@redhat.com> 2.31.92-1
- Update to 2.31.92
- Rebuild against newer gobject-introspection

* Mon Sep 13 2010 Bastien Nocera <bnocera@redhat.com> 2.30.3-1
- Update to 2.30.3

* Wed Aug 04 2010 Bastien Nocera <bnocera@redhat.com> 2.30.2-1
- Update to 2.30.2

* Thu Jul 15 2010 Colin Walters <walters@verbum.org> - 2.30.1-2
- Rebuild with new gobject-introspection

* Wed May 12 2010 Bastien Nocera <bnocera@redhat.com> 2.30.1-1
- Update to 2.30.1

* Mon Mar 29 2010 Bastien Nocera <bnocera@redhat.com> 2.30.0-1
- Update to 2.30.0

* Mon Mar 15 2010 Bastien Nocera <bnocera@redhat.com> 2.29.92-1
- Update to 2.29.92

* Sat Feb 13 2010 Caolán McNamara <caolanm@redhat.com> 2.29.1-2
- Rebuild for gmime26

* Tue Jan 26 2010 Bastien Nocera <bnocera@redhat.com> 2.29.1-1
- Update to 2.29.1

* Fri Dec 11 2009 Bastien Nocera <bnocera@redhat.com> 2.28.2-1
- Update to 2.28.2

* Thu Oct 15 2009 Bastien Nocera <bnocera@redhat.com> 2.28.1-2
- Fix crasher when parsing multiple XML-ish playlists in Rhythmbox

* Tue Sep 29 2009 Bastien Nocera <bnocera@redhat.com> 2.28.1-1
- Update to 2.28.1

* Mon Sep 21 2009 Bastien Nocera <bnocera@redhat.com> 2.28.0-2
- Update source URL

* Mon Sep 21 2009 Bastien Nocera <bnocera@redhat.com> 2.28.0-1
- Update to 2.28.0

* Tue Sep 15 2009 Bastien Nocera <bnocera@redhat.com> 2.27.92-1
- Update to 2.27.92

* Tue Sep 08 2009 Bastien Nocera <bnocera@redhat.com> 2.27.2-4
- Version Obsoletes for totem-devel (#520874)

* Tue Aug 11 2009 Bastien Nocera <bnocera@redhat.com> 2.27.2-3
- Fix URL

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 23 2009 Bastien Nocera <bnocera@redhat.com> 2.27.2-1
- Update to 2.27.2

* Wed May 06 2009 Bastien Nocera <bnocera@redhat.com> 2.27.1-1
- Update to 2.27.1

* Tue Mar 31 2009 - Bastien Nocera <bnocera@redhat.com> - 2.26.1-1
- Update to 2.26.1

* Mon Mar 16 2009 - Bastien Nocera <bnocera@redhat.com> - 2.26.0-1
- Update to 2.26.0

* Tue Mar 03 2009 - Bastien Nocera <bnocera@redhat.com> - 2.25.92-1
- Update to 2.25.92

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.25.91-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 - Bastien Nocera <bnocera@redhat.com> - 2.25.91-1
- Update to 2.25.91

* Tue Feb 03 2009 - Bastien Nocera <bnocera@redhat.com> - 2.25.90-1
- Update to 2.25.90

* Tue Feb 03 2009 - Bastien Nocera <bnocera@redhat.com> - 2.25.1-3
- Rebuild for new libcamel

* Tue Dec 09 2008 - Bastien Nocera <bnocera@redhat.com> - 2.25.1-2
- Add evolution-data-server-devel Requires for the devel package

* Mon Dec 08 2008 - Bastien Nocera <bnocera@redhat.com> - 2.25.1-1
- Update to 2.25.1

* Fri Dec 05 2008 Matthew Barnes <mbarnes@redhat.com> - 2.24.2-3
- Rebuild against newer libcamel.

* Fri Nov 14 2008 Matthias Clasen  <mclasen@redhat.com> - 2.24.2-2
- Rebuild

* Thu Oct 30 2008 - Bastien Nocera <bnocera@redhat.com> - 2.24.2-1
- Update to 2.24.2

* Tue Oct 21 2008 Matthias Clasen  <mclasen@redhat.com> - 2.24.1-2
- Rebuild

* Tue Oct 07 2008 - Bastien Nocera <bnocera@redhat.com> - 2.24.1-1
- Update to 2.24.1

* Sun Sep 21 2008 - Bastien Nocera <bnocera@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Fri Aug 29 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.91-1
- Update to 2.23.91

* Tue Aug  5 2008 Matthias Clasen  <mclasen@redhat.com> - 2.23.3-2
- Rebuild

* Mon Jul 14 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.3-1
- Update to 2.23.3
- Fixes crasher when totem_cd_detect_type() generates an error (#455014)

* Wed Jun 11 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.2-1
- Update to 2.23.2

* Tue May 13 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.1-2
- Rebuild

* Fri May 09 2008 - Bastien Nocera <bnocera@redhat.com> - 2.23.1-1
- Update to 2.23.1
- Remove gnome-vfs2 dependencies

* Wed May 07 2008 - Bastien Nocera <bnocera@redhat.com> - 2.22.2-3
- Rebuild for new libcamel

* Sun May  4 2008 Matthias Clasen <mclasen@redhat.com> - 2.22.2-2
- Fix source url

* Tue Apr 08 2008 - Bastien Nocera <bnocera@redhat.com> - 2.22.2-1
- Update to 2.22.2

* Mon Mar 10 2008 - Bastien Nocera <bnocera@redhat.com> - 2.22.1-1
- Update to 2.22.1

* Mon Mar 10 2008 - Bastien Nocera <bnocera@redhat.com> - 2.22.0-1
- Update to 2.22.0

* Sun Feb 24 2008 - Bastien Nocera <bnocera@redhat.com> - 2.21.92-1
- Update to 2.21.92

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.21.91-3
- Autorebuild for GCC 4.3

* Tue Jan 29 2008 - Matthew Barnes <mbarnes@redhat.com> - 2.21.21-2
- Rebuild against newer libcamel-1.2.

* Mon Jan 21 2008 - Bastien Nocera <bnocera@redhat.com> - 2.21.91-1
- Update to 2.21.91

* Mon Jan 07 2008 - Bastien Nocera <bnocera@redhat.com> - 2.21.90-1
- Update to 2.21.90

* Thu Dec 06 2007 - Bastien Nocera <bnocera@redhat.com> - 2.21.6-1
- First package

