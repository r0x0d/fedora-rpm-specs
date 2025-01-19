Name:           goocanvas
Version:        1.0.0
Release:        28%{?dist}
Summary:        A canvas widget for GTK+ that uses cairo for drawing

License:        LGPL-2.0-or-later
URL:            https://wiki.gnome.org/Projects/GooCanvas
Source0:        https://download.gnome.org/sources/%{name}/1.0/%{name}-%{version}.tar.bz2
Patch0:         %{name}-fix-gcc14-build.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig, gettext, gtk2-devel
BuildRequires:  cairo-devel >= 1.4.0
BuildRequires:  make

%description
GooCanvas is a canvas widget for GTK+ that uses the cairo 2D library for
drawing. It has a model/view split, and uses interfaces for canvas items and
views, so you can easily turn any application object into canvas items.

%prep
%autosetup -p1

%build
%set_build_flags
%configure
%make_build


%install
%make_install

# remove static libraries and libtool droppings
rm -f $RPM_BUILD_ROOT/%{_libdir}/lib%{name}.{a,la}

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/lib%{name}.so\.*

%package devel
Summary:        A new canvas widget for GTK+ that uses cairo for drawing
Requires:       %{name} = %{version}-%{release} pkgconfig

%description devel
GooCanvas is a new canvas widget for GTK+ that uses the cairo 2D library for
drawing. It has a model/view split, and uses interfaces for canvas items and
views, so you can easily turn any application object into canvas items.

These are the files used for development.

%files devel
%{_includedir}/%{name}-1.0
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/gtk-doc/html/%{name}


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 27 2024 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-27
- Add %{name}-fix-gcc14-build.patch to fix bug (#2327765)
- Migrate to SPDX license
- Use macros in build and install section

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 04 2016 Pete Walter <pwalter@fedoraproject.org> - 1.0.0-11
- Update project's URL (#1380991)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 1.0.0-2
- Rebuild for new libpng

* Fri Feb 11 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 1.0.0-1
- Upstream 1.0.0 (final release !)
- Re-enable demos

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Apr 26 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 0.15-1
- Update to upstream 0.15

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 23 2009 Denis <denis@poolshark.org> - 0.14-1
- Update to upstream 0.14

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Denis Leroy <denis@poolshark.org> - 0.13-1
- Update to upstream 0.13
- Updated URLs to gnome.org

* Tue Sep 30 2008 Bernard Johnson <bjohnson@symetrix.com> - 0.10-2
- demo application does not build; remove it

* Sun Jun 29 2008 Bernard Johnson <bjohnson@symetrix.com> - 0.10-1
- v 0.10

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.9-4
- Autorebuild for GCC 4.3

* Mon Aug 27 2007 Bernard Johnson <bjohnson@symetrix.com> - 0.9-3
- don't explicitely require gtk2; no special versioning needed since FC6+

* Sun Aug 26 2007 Bernard Johnson <bjohnson@symetrix.com> - 0.9-2
- require gtk2 not gtk2-devel (bz #254239)

* Sun Aug 19 2007 Bernard Johnson <bjohnson@symetrix.com> - 0.9-1
- 0.9
- update license tag to LGPLv2+

* Sat May 05 2007 Bernard Johnson <bjohnson@symetrix.com> - 0.6-2
- bump for incorrect tag in buildsys

* Mon Mar 19 2007 Bernard Johnson <bjohnson@symetrix.com> - 0.6-1
- initial release
