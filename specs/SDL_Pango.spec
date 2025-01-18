Summary: Rendering of internationalized text for SDL (Simple DirectMedia Layer)
Name: SDL_Pango
Version: 0.1.2
Release: 45%{?dist}
License: LGPL-2.0-or-later
URL: http://sdlpango.sourceforge.net/

Source0: http://downloads.sf.net/sdlpango/SDL_Pango-%{version}.tar.gz
Source1: doxygen.png
Patch0: SDL_Pango-0.1.2-suppress-warning.patch
Patch1: SDL_Pango-0.1.2-API-adds.patch
Patch2: SDL_Pango-0.1.2-matrix_declarations.patch
Patch99: SDL_Pango-0.1.2-fedora-c99.patch

BuildRequires: make
BuildRequires: pango-devel, SDL-devel, dos2unix
BuildRequires: autoconf, automake, libtool

%description
Pango is the text rendering engine of GNOME 2. SDL_Pango connects that engine
to SDL, the Simple DirectMedia Layer.


%package devel
Summary: Development files for SDL_pango
Requires: %{name} = %{version}-%{release}
Requires: pango-devel, SDL-devel, pkgconfig

%description devel
Development files for SDL_pango.


%prep
%setup -q
%patch -P0 -p1 -b .suppress-warning
%patch -P1 -p1 -b .API-adds
%patch -P2 -p1 -b .matrix_declarations
%patch -P99 -p1 -b .c99
# Clean up, we include the entire "docs/html" content for the devel package
rm -rf docs/html/CVS/
# Replace the corrupt doxygen.png file with a proper one
install -m 0644 -p %{SOURCE1} docs/html/doxygen.png
# Fix the (many) DOS encoded files, not *.png since they get corrupt
find . -not -name \*.png -type f -exec dos2unix -k {} \;
# For FC-5 x86_64 this is required, or the shared library doesn't get built
autoreconf -if


%build
%configure --disable-static
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%ldconfig_scriptlets


%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%doc docs/html/*
%{_includedir}/SDL_Pango.h
%{_libdir}/pkgconfig/SDL_Pango.pc
%exclude %{_libdir}/*.la
%{_libdir}/*.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 18 2023 DJ Delorie <dj@redhat.com> - 0.1.2-40
- Fix C99 compatibility issue

* Thu Mar 02 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.1.2-39
- migrated to SPDX license

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Mar 25 2021 Gwyn Ciesla <gwync@protonmail.com> - 0.1.2-34
- Fix Autoconf 2.71 FTBFS.

* Mon Jan 25 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-32
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 16 2014 Jaromir Capik <jcapik@redhat.com> - 0.1.2-18
- Fixing FTBFS

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 24 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.1.2-15
- Add disttag, cleanup spec

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Matthias Saou <http://freshrpms.net/> 0.1.2-9
- Include matrix declaraction patch (#475118), adapted in order to not
  create a regression from the "supress warning" patch.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org>
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Matthias Saou <http://freshrpms.net/> 0.1.2-7
- Rebuild for new BuildID feature.

* Fri Aug  3 2007 Matthias Saou <http://freshrpms.net/> 0.1.2-6
- Update License field.
- Remove dist tag, since the package will seldom change.

* Fri Sep 29 2006 Matthias Saou <http://freshrpms.net/> 0.1.2-5
- Update source URL.
- Disable static lib building instead of excluding it from the files list.

* Fri Sep 29 2006 Matthias Saou <http://freshrpms.net/> 0.1.2-4
- Add autoreconf and libtoolize calls since on FC5 x86_64 the shared library
  isn't build otherwise.
- Add API-adds patch (submitted upstream), required for the only project known
  to use SDL_Pango, so it does makes kind of sense...

* Tue Sep 26 2006 Matthias Saou <http://freshrpms.net/> 0.1.2-3
- Use dos2unix to convert all DOS encoded files.
- Replace the corrupt doxygen.png file with a proper one.

* Tue Sep 26 2006 Matthias Saou <http://freshrpms.net/> 0.1.2-2
- Change %%makeinstall to using DESTDIR, according to the guidelines.
- Include patch from Mamoru Tasaka to remove all compilation warnings.

* Fri Sep 22 2006 Matthias Saou <http://freshrpms.net/> 0.1.2-1
- Initial RPM release.

