%if 0%{?fedora} > 31 || 0%{?rhel} > 7
%global _without_python2 1
%else
%global _with_python2 1
%endif

Name:           libewf
Version:        20140608
Release:        31%{?dist}
Summary:        Library for the Expert Witness Compression Format (EWF)

License:        LGPL-3.0-or-later
URL:            http://sourceforge.net/projects/libewf/
Source0:        https://53efc0a7187d0baa489ee347026b8278fe4020f6.googledrive.com/host/0B3fBvzttpiiSMTdoaVExWWNsRjg/%{name}-%{version}.tar.gz
Patch0:         libewf-ewfoutput-openssl3.diff


BuildRequires: make
BuildRequires:  gcc-c++
BuildRequires:  fuse-devel
BuildRequires:  libuuid-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
#Needed for mount.ewf(.py) support
%if 0%{?_with_python2}
BuildRequires:  python2-devel
%endif


%description
Libewf is a library for support of the Expert Witness Compression Format (EWF),
it support both the SMART format (EWF-S01) and the EnCase format (EWF-E01). 
Libewf allows you to read and write media information within the EWF files.


%package -n     ewftools
Summary:        Utilities for the Expert Witness Compression Format (EWF)
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{name}-tools = %{version}-%{release}
Obsoletes:      %{name}-tools <= %{version}-%{release}
%if 0%{?_with_python2}
Requires:       python2-fuse >= 0.2
#Requires:       disktype
%endif

%description -n ewftools
Several tools for reading and writing EWF files.
It contains tools to acquire, verify and export EWF files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       zlib-devel
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1


%build
# FIXME: Package suffers from c11/inline issues
# Workaround by appending -std=gnu89 to CFLAGS
# Proper fix would be to fix the source-code
%configure --disable-static \
  --enable-wide-character-type \
%if 0%{?_with_python2}
  --enable-python \
%endif
%if "%{version}" <= "20140608"
  CFLAGS="${RPM_OPT_FLAGS} -std=gnu89"
%endif

# Remove rpath from libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# clean unused-direct-shlib-dependencies
sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

%make_build


%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'



%ldconfig_scriptlets


%files
%doc AUTHORS NEWS
%license COPYING
%{_libdir}/*.so.*

%files -n ewftools
%{_bindir}/ewf*
%{_mandir}/man1/*.gz
%if 0%{?_with_python2}
%{python2_sitearch}/pyewf.so
%endif

%files devel
%{_includedir}/libewf.h
%{_includedir}/libewf/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libewf.pc
%{_mandir}/man3/*.gz

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 20140608-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20140608-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jul 17 2024 Miroslav Suchý <msuchy@redhat.com> - 20140608-29
- convert license to SPDX

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20140608-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20140608-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20140608-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20140608-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20140608-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20140608-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 05 2021 Neal Gompa <ngompa@fedoraproject.org> - 20140608-22
- Fix ewfoutput to compile with OpenSSL 3.x

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 20140608-21
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20140608-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20140608-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20140608-18
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20140608-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20140608-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 17 2019 Nicolas Chauvet <kwizart@gmail.com> - 20140608-15
- Drop python2 support - rhbz#1738945

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20140608-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20140608-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 17 2018 Nicolas Chauvet <kwizart@gmail.com> - 20140608-12
- Few cleanup

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20140608-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20140608-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 23 2017 Nicolas Chauvet <kwizart@gmail.com> - 20140608-9
- Fix python2-fuse dependency
- Spec file update

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20140608-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20140608-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20140608-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140608-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20140608-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 13 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 20140608-3
- Append -stdc=gnu89 to CFLAGS (Fix F23FTBFS, RHBZ#1239643).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140608-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 25 2014 Michal Ambroz <rebus AT seznam.cz> - 20140608-1
- Update to 20140608

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130416-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130416-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20130416-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May 18 2013 Nicolas Chauvet <kwizart@gmail.com> - 20130416-1
- Update to 20130416

* Thu Feb 28 2013 Nicolas Chauvet <kwizart@gmail.com> - 20130128-1
- Update to 20130128
- Switch to LGPLv3+
- Add BR fuse-devel
- Spec clean-up

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100226-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100226-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100226-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100226-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 20100226-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Mon Mar  8 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 20100226-1
- Update to 20100226
- Avoid version on python module.

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 20080501-9
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080501-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 29 2009 kwizart < kwizart at gmail.com > - 20080501-7
- Switch to libuuid-devel usage over e2fsprogs-devel

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20080501-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 kwizart < kwizart at gmail.com > - 20080501-5
- Update mount_ewf to 20090113

* Sat Dec 27 2008 kwizart < kwizart at gmail.com > - 20080501-4
- Fix for python2.6

* Mon Sep 15 2008 kwizart < kwizart at gmail.com > - 20080501-3
- Update mount_ewf to 20080910
- Switch URL to sourceforge site

* Sat Jun  7 2008 kwizart < kwizart at gmail.com > - 20080501-2
- Update mount_ewf to 20080513

* Thu May  1 2008 kwizart < kwizart at gmail.com > - 20080501-1
- Update to 20080501 (bugfix)
- Patch for pkg-config was merged with this release
- Improve ewftools description.

* Tue Apr 29 2008 kwizart < kwizart at gmail.com > - 20080322-3
- Add disktype Requires for ewftools (required for mount.ewf support).
- Patch libewf.pc to export only the needed libs

* Tue Apr 22 2008 kwizart < kwizart at gmail.com > - 20080322-2
- Add support for mount.ewf with fuse-python

* Wed Mar 26 2008 kwizart < kwizart at gmail.com > - 20080322-1
- Update to 20080322 (Stable)
- License update: the BSD advertisement clause was removed.

* Mon Mar 17 2008 kwizart < kwizart at gmail.com > - 20080315-1
- Update to 20080315 (beta)
- Change versionning scheme (use date for version).

* Mon Nov  5 2007 kwizart < kwizart at gmail.com > - 0-2.20070512
- Update License to BSD with advertising

* Fri Nov  2 2007 kwizart < kwizart at gmail.com > - 0-1.20070512
- Initial package for Fedora

