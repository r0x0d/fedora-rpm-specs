%global build_type_safety_c 2

Name:           lcms
Version:        1.19
Release:        41%{?dist}

Summary:        Color Management System
License:        MIT
URL:            http://www.littlecms.com/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz

Patch0:         %{name}-1.19-rhbz675186.patch
# bug 992979 / CVE-2013-4276
# Stack-based buffer overflows in ColorSpace conversion calculator
# and TIFF compare utility
Patch1:         %{name}-1.19-rhbz991757.patch
# bug 1003950
Patch2:         %{name}-1.19-rhbz1003950.patch
Patch3: lcms-c99.patch

BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  swig >= 1.3.12
BuildRequires:  zlib-devel

Provides:       littlecms%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

# This package is provided only for foo2zjs. No other packages should depend on it.
Provides:       deprecated()

%description
LittleCMS intends to be a small-footprint, speed optimized color management
engine in open source form.

%package        libs
Summary:        Library for %{name}
Provides:       littlecms-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       deprecated()

%description    libs
The %{name}-libs package contains library for %{name}.

%package        devel
Summary:        Development files for LittleCMS
Requires:       %{name}-libs%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       littlecms-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Provides:       deprecated()

%description    devel
Development files for LittleCMS.

%prep
%autosetup -p1
find . -type f -name '*.[ch]' -exec chmod -x '{}' \;
chmod 0644 AUTHORS COPYING ChangeLog NEWS README.1ST doc/TUTORIAL.TXT doc/LCMSAPI.TXT

# Convert not UTF-8 files
pushd doc
mkdir -p __temp
for f in LCMSAPI.TXT TUTORIAL.TXT ;do
cp -p $f __temp/$f
iconv -f ISO-8859-1 -t UTF-8 __temp/$f > $f
touch -r __temp/$f $f
done
rm -rf __temp
popd

%build
%configure --without-python --disable-static
# remove rpath from libtool
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make_install
find %{buildroot} -type f -name '*.la' -delete

%files
%doc README.1ST ChangeLog doc/TUTORIAL.TXT
%license AUTHORS COPYING
%{_bindir}/*
%{_mandir}/man1/*.1*

%files libs
%doc NEWS
%license AUTHORS COPYING
%{_libdir}/lib%{name}.so.1*

%files devel
%doc doc/LCMSAPI.TXT
%{_includedir}/*
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Feb 04 2023 Florian Weimer <fweimer@redhat.com> - 1.19-36
- Fix C99 compatibility issue (#2167083)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 27 2020 Vitaly Zaitsev <vitaly@easycoding.org> - 1.19-29
- Revived package.
- Performed SPEC cleanup.

* Thu Aug 22 2019 Miro Hrončok <mhroncok@redhat.com> - 1.19-28
- Subpackage python2-lcms has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 1.19-25
- Rebuild with fixed binutils

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.19-22
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.19-21
- Python 2 binary package renamed to python2-lcms
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-17
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.19-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.19-14
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Dec  9 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 1.19-11
- apply patch for CVE-2013-4276 (#991757, #992979)
- apply patch for "Use of uninitialized values on 64 bit machines." (#1003950)
- add %%_isa in -libs base package deps
- drop %%defattr usage

* Wed Sep 04 2013 Nils Philippsen <nils@redhat.com>
- fix bogus dates in changelog

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 18 2013 Adam Tkac <atkac redhat com> - 1.19-8
- rebuild due to "jpeg8-ABI" feature drop

* Thu Nov  8 2012 Tomas Bzatek <tbzatek@redhat.com> - 1.19-7
- Fix source URL

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Mar 14 2011 Nicolas Chauvet <kwizart@gmail.com> - 1.19-4
- Fix rhbz#675186

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Nov 30 2009 Nicolas Chauvet <kwizart@fedoraproject.org> - 1.19-1
- Update to 1.19

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 22 2009 kwizart < kwizart at gmail.com > - 1.18-2
- Add lcms-CVE-2009-0793.patch from 1.18a

* Mon Mar 23 2009 kwizart < kwizart at gmail.com > - 1.18-1
- Update to 1.18 (final)
- Remove upstreamed patches
- Disable autoreconf - patch libtool to prevent rpath issue

* Fri Mar 20 2009 kwizart < kwizart at gmail.com > - 1.18-0.1.beta2
- Update to 1.18beta2
 fix bug #487508: CVE-2009-0723 LittleCms integer overflow
 fix bug #487512: CVE-2009-0733 LittleCms lack of upper-bounds check on sizes
 fix bug #487509: CVE-2009-0581 LittleCms memory leak

* Mon Mar  2 2009 kwizart < kwizart at gmail.com > - 1.17-10
- Fix circle dependency #452352

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Dec  4 2008 kwizart < kwizart at gmail.com > - 1.17-8
- Fix autoreconf and missing auxiliary files.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.17-7
- Rebuild for Python 2.6

* Tue Oct 28 2008 kwizart < kwizart at gmail.com > - 1.17-6
- Add lcms-fix_s390_lcms_h.patch - Fix #468245

* Tue Jun 3 2008 kwizart < kwizart at gmail.com > - 1.17-5
- Fix Array indexing error in ReadCurve - #448066

* Wed Feb 13 2008 kwizart < kwizart at gmail.com > - 1.17-4
- Fix packaging bug #432568 (multilib transition).

* Mon Feb 11 2008 kwizart < kwizart at gmail.com > - 1.17-3
- Rebuild for gcc 4.3
- Move libs to mutlilibs
- Prevent timestramps change
- Convert files-not-utf8

* Wed Aug 22 2007 kwizart < kwizart at gmail.com > - 1.17-2
- Disable static for now.

* Tue Aug 21 2007 kwizart < kwizart at gmail.com > - 1.17-1
- Update to 1.17
- Ship -static for static linking

* Thu Feb  8 2007 Alexander Larsson <alexl@redhat.com> - 1.16-3.fc7
- Remove requirement on python_sitearch dir (#225981)
- Don't ship with executable .c/.h files

* Mon Feb  5 2007 Alexander Larsson <alexl@redhat.com> - 1.16-2
- Run swig during build to fix warnings in generated code
- Fix build on 64bit

* Mon Feb  5 2007 Alexander Larsson <alexl@redhat.com> - 1.16-1
- Update to 1.16
- Specfile cleanups (#225981)
- Remove static libs

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 1.15-2
- rebuild against python 2.5

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> 
- rebuild

* Mon Feb 13 2006 Jesse Keating <jkeating@redhat.com> - 1.15-1.2.1
- rebump for build order issues during double-long bump

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.15-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.15-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Mon Jan  9 2006 Alexander Larsson <alexl@redhat.com> - 1.15-1
- Move from extras to core, update to 1.15

* Sun May 22 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.14-3
- Fix FC4 build (#114146).

* Fri Apr  8 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Thu May 20 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.14-1
- Update to 1.14.

* Thu May 20 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.13-0.fdr.1
- Updated to 1.13.

* Mon Feb 16 2004 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.12-0.fdr.2
- Spec patch from Ville Skyttä.
- New sub-package: python-lcms.

* Sun Dec 21 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.12-0.fdr.1
- Updated to 1.12.
- BuildReq swig >=1.3.12.

* Sun Nov 09 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.11-0.fdr.3
- Fixed doc attributes.

* Sat Oct 11 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.11-0.fdr.2
- Renamed to lcms to match upstream.
- Provides: littlecms.
- Fixed doc attributes.
- Excluding empty dir %%{_libdir}/python2.2/

* Thu Oct 09 2003 Phillip Compton <pcompton[AT]proteinmedia.com> - 0:1.11-0.fdr.1
- Initial RPM release.
