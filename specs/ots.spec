Name:		ots
Summary:	A text summarizer
Version:	0.5.0
Release:	34%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:	GPL-2.0-or-later
URL:		http://libots.sourceforge.net/

Source0:	http://prdownloads.sourceforge.net/libots/ots-%{version}.tar.gz
Patch0: ots-c99.patch


BuildRequires: make
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libxml2-devel >= 2.4.23
BuildRequires:	popt-devel >= 1.5
BuildRequires:	libtool

Requires:	%{name}-libs = %{version}-%{release}

%description
The open text summarizer is an open source tool for summarizing texts.
The program reads a text and decides which sentences are important and
which are not.

 
%package	devel
Summary: 	Libraries and include files for developing with libots
Requires:	%{name}-libs = %{version}-%{release}
Requires: 	glib2-devel >= 2.0
Requires:	libxml2-devel >= 2.4.23
Requires:	popt-devel >= 1.5
Requires:	pkgconfig

%description	devel
This package provides the necessary development libraries and include
files to allow you to develop with libots.


%package	libs
Summary:	Shared libraries for %{name}

%description	libs
The %{name}-libs package contains shared libraries used by %{name}.


%prep
%autosetup -p1


%build
%configure --with-html-dir=%{_datadir}/gtk-doc/html/ots
# XXX: Disgusting kludge to fix upstream's broken package.
touch ./gtk-doc.make
%{__make} \
%if 0%{?flatpak}
    LIBTOOL=/usr/bin/libtool
%else
    LIBTOOL=%{_bindir}/libtool
%endif

%install
rm -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}



%ldconfig_scriptlets	libs


%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/ots

%files	libs
%doc COPYING
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la
%{_libdir}/libots-1.so.*
%{_datadir}/ots/

%files	devel
%doc COPYING
%{_libdir}/libots-1.so
%{_includedir}/libots-1/
%{_libdir}/pkgconfig/libots-1.pc


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 0.5.0-33
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 11 2023 Florian Weimer <fweimer@redhat.com> - 0.5.0-28
- Port to C99 (#2185829)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Aug 13 2019 Jan Beran <jaberan@redhat.com> - 0.5.0-20
- Add conditional LIBTOOL setting

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 08 2008 Peter Gordon <peter@thecodergeek.com> - 0.5.0-1
- Update to new upstream release (0.5.0).
- Drop GCC4 patch (fixed upstream):
  - 0.4.2-gcc4.patch

* Mon Apr 23 2007 Peter Gordon <peter@thecodergeek.com> - 0.4.2-11
- Remove static libraries (%%_libdir/*.a).
- Fix %%defattr lines in the %%files listings.
- Lots of formatting/aesthetic fixes.
- Remove pkgconfig from build-time dependencies (required by glib2-devel and
  libxml2-devel).
- Add LDFLAGS to fix shared library linking: libots-1.so.0 needs to link to
  glib2 and libxml2 libraries to fix unresolved symbol errors. (Resolves bug
  #237501; thanks to Matthias Clasen for the report).
- Split off libs subpackage to avoid potential multilib conflicts.    

* Mon Aug 27 2006 Michael J. Knox <michael[AT]knox.net.nz> - 0.4.2-10
- Rebuild for FC6

* Sun May 21 2006 Michael J. Knox <michael[AT]knox.net.nz> - 0.4.2-9
- rebuild and spec tidy

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 0.4.2-7
- rebuild on all arches

* Wed Mar 16 2005 Toshio Kuratomi <toshio@tiki-lounge.com> - 0.4.2-5
- Reenable man page.
- Disable rebuilding documentation via configure switch instead of an automake
  requiring patch.
- Remove the API documentation for now as it is just a placeholder.

* Wed Mar  2 2005 Caolan McNamara <caolanm@redhat.com> - 0.4.2-4
- rebuild with gcc4
- small lvalue assign patch

* Wed Feb 09 2005 Caolan McNamara <caolanm@redhat.com> - 0.4.2-3
- rebuilt

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 19 2004 Jeremy Katz <katzj@redhat.com> - 0.4.2-1
- 0.4.2

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Nov 28 2003 Jeremy Katz <katzj@redhat.com> 
- add some buildrequires (#111158)

* Mon Sep 15 2003 Jeremy Katz <katzj@redhat.com> 0.4.1-1
- 0.4.1

* Mon Aug  4 2003 Jeremy Katz <katzj@redhat.com> 0.4.0-1
- 0.4.0

* Tue Jul 22 2003 Jeremy Katz <katzj@redhat.com> 0.3.0-1
- update to 0.3.0

* Sat Jul 12 2003 Jeremy Katz <katzj@redhat.com> 0.2.0-2
- forcibly disable gtk-doc (openjade is busted on s390)

* Mon Jul  7 2003 Jeremy Katz <katzj@redhat.com> 0.2.0-1
- update to 0.2.0
- ldconfig in %%post/%%postun
- libtoolize
- clean up spec file a little, build gtk-doc
- fix libtool versioning 

* Thu Jun 05 2003 Rui Miguel Silva Seabra <rms@1407.org>
- fix spec
- disable gtk-doc (it's not building in RH 9,
  maybe it's broken for some reason)

* Fri May 02 2003 Rui Miguel Silva Seabra <rms@1407.org>
- define a longer description from the README file
- explicitly set file permissions

* Wed Apr 30 2003 Dom Lachowicz <cinamod@hotmail.com>
- created this thing
