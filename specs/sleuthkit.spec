# Disable LTO
#ld: sha2.o (symbol from plugin): undefined reference to symbol 'SHA384_Final@@OPENSSL_1_1_0'
%global _lto_cflags %nil


Name:           sleuthkit
Version:        4.12.1
Release:        5%{?dist}
Summary:        The Sleuth Kit (TSK)

# Automatically converted from old format: CPL and IBM and GPLv2+ - review is highly recommended.
License:        CPL-1.0 AND IPL-1.0 AND GPL-2.0-or-later
URL:            http://www.sleuthkit.org
Source0:        https://github.com/sleuthkit/sleuthkit/archive/sleuthkit-%{version}/sleuthkit-%{version}.tar.gz

BuildRequires: make
BuildRequires:  libtool

# afflib - BSD with advertising, GPL incompatible
BuildRequires:  gcc-c++
BuildRequires:  afflib-devel >= 3.3.4
# libewf - Newer versions are plain BSD (older are BSD with advertising)
BuildRequires:  libewf-devel
BuildRequires:  perl-generators
BuildRequires:  sqlite-devel

%if 0%{?el7}
BuildRequires:  devtoolset-8-toolchain, devtoolset-8-libatomic-devel
%endif

%{?_with_java:
BuildRequires:  java-devel >= 1:1.6.0
BuildRequires:  jpackage-utils

Requires:       java >= 1:1.6.0
Requires:       jpackage-utils
}

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: file
Requires: mac-robber

%description
The Sleuth Kit (TSK) is a collection of UNIX-based command line tools that
allow you to investigate a computer. The current focus of the tools is the
file and volume systems and TSK supports FAT, Ext2/3, NTFS, UFS,
and ISO 9660 file systems


%package        libs
Summary:        Library for %{name}

%description    libs
The %{name}-libs package contains library for %{name}.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       sqlite-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q -n %{name}-%{name}-%{version}
autoreconf -vif


%build
%if 0%{?el7}
. /opt/rh/devtoolset-8/enable
%endif
#export LIBS='-lpthread -ldl'
%configure --disable-static \
 %{!?_with_java:--disable-java}

# remove rpath from libtool
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build


%install
%if 0%{?el7}
. /opt/rh/devtoolset-8/enable
%endif
%make_install INSTALL="install -p"
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%ldconfig_scriptlets libs


%files
%doc ChangeLog.txt NEWS.txt
%license licenses/*
# License is CPL 1.0 exept for some files.
%{_bindir}/blkcalc
%{_bindir}/blkcat
%{_bindir}/blkls
%{_bindir}/blkstat
#{_bindir}/disk_sreset
#{_bindir}/disk_stat
#fcat conflicts with freeze fcat
%exclude %{_bindir}/fcat
%{_bindir}/ffind
%{_bindir}/fiwalk
%{_bindir}/fls
%{_bindir}/fsstat
%{_bindir}/hfind
%{_bindir}/icat
%{_bindir}/ifind
%{_bindir}/ils
%{_bindir}/img_cat
%{_bindir}/img_stat
%{_bindir}/istat
%{_bindir}/jcat
%{_bindir}/jpeg_extract
%{_bindir}/jls
# This file is described as GPL in the doc
# But the license remains CPL in the source.
%{_bindir}/mactime
##
%{_bindir}/mmcat
%{_bindir}/mmls
%{_bindir}/mmstat
%{_bindir}/pstat
%{_bindir}/sigfind
%{_bindir}/sorter
## This file is GPLv2+
%{_bindir}/srch_strings
%{_bindir}/tsk_comparedir
%{_bindir}/tsk_gettimes
%{_bindir}/tsk_imageinfo
%{_bindir}/tsk_loaddb
%{_bindir}/tsk_recover
%{_bindir}/usnjls
#
%{_mandir}/man1/blkcalc.1*
%{_mandir}/man1/blkcat.1*
%{_mandir}/man1/blkls.1*
%{_mandir}/man1/blkstat.1*
#{_mandir}/man1/disk_sreset.1*
#{_mandir}/man1/disk_stat.1*
%exclude %{_mandir}/man1/fcat.1*
%{_mandir}/man1/ffind.1*
%{_mandir}/man1/fls.1*
%{_mandir}/man1/fsstat.1*
%{_mandir}/man1/hfind.1*
%{_mandir}/man1/icat.1*
%{_mandir}/man1/ifind.1*
%{_mandir}/man1/ils.1*
%{_mandir}/man1/img_cat.1*
%{_mandir}/man1/img_stat.1*
%{_mandir}/man1/istat.1*
%{_mandir}/man1/jcat.1*
%{_mandir}/man1/jls.1*
%{_mandir}/man1/mactime.1*
%{_mandir}/man1/mmcat.1*
%{_mandir}/man1/mmls.1*
%{_mandir}/man1/mmstat.1*
%{_mandir}/man1/sigfind.1*
%{_mandir}/man1/sorter.1*
%{_mandir}/man1/tsk_comparedir.1*
%{_mandir}/man1/tsk_gettimes.1*
%{_mandir}/man1/tsk_loaddb.1*
%{_mandir}/man1/tsk_recover.1*
%{_mandir}/man1/usnjls.1.*
%dir %{_datadir}/tsk
%{_datadir}/tsk/sorter/

%files libs
# CPL and IBM
%{_libdir}/*.so.*

%files devel
# CPL and IBM
%{_includedir}/tsk/
%{_libdir}/*.so
%{_libdir}/pkgconfig/tsk.pc


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Miroslav Suchý <msuchy@redhat.com> - 4.12.1-4
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 04 2023 Nicolas Chauvet <kwizart@gmail.com> - 4.12.1-1
- Update to 4.12.1

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec 28 2022 Nicolas Chauvet <kwizart@gmail.com> - 4.12.0-1
- Update to 4.12.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 04 2021 Nicolas Chauvet <kwizart@gmail.com> - 4.11.1-1
- Update to 4.11.1

* Sat Jul 31 2021 Nicolas Chauvet <kwizart@gmail.com> - 4.11.0-1
- Update to 4.11.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Mar 24 2021 Nicolas Chauvet <kwizart@gmail.com> - 4.10.2-1
- Update to 4.10.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 09 2020 Nicolas Chauvet <kwizart@gmail.com> - 4.10.1-1
- Update to 4.10.1

* Fri Sep 25 2020 Nicolas Chauvet <kwizart@gmail.com> - 4.10.0-1
- Update to 4.10.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 08 2020 Nicolas Chauvet <kwizart@gmail.com> - 4.9.0-1
- Update to 4.9.0

* Tue Jan 28 2020 Nicolas Chauvet <kwizart@gmail.com> - 4.8.0-1
- Update to 4.8.0

* Thu Dec 19 2019 Nicolas Chauvet <kwizart@gmail.com> - 4.7.0-1
- Update to 4.7.0

* Mon Aug 19 2019 Nicolas Chauvet <kwizart@gmail.com> - 4.6.7-1
- Update to 4.6.7

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Nicolas Chauvet <kwizart@gmail.com> - 4.6.6-1
- Update to 4.6.6

* Tue Mar 26 2019 Nicolas Chauvet <kwizart@gmail.com> - 4.6.5-1
- Update to 4.6.5

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Aug 13 2018 Nicolas Chauvet <kwizart@gmail.com> - 4.6.2-1
- Update to 4.6.2

* Tue Jul 17 2018 Nicolas Chauvet <kwizart@gmail.com> - 4.6.1-1
- Update to 4.6.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Nicolas Chauvet <kwizart@gmail.com> - 4.5.0-1
- Update to 4.5.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Sep 26 2016 Nicolas Chauvet <kwizart@gmail.com> - 4.3.0-1
- Update to 4.3.0
- Add sqlite-devel requires from devel sub-package rhbz#1346202
- Spec file clean-up

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 01 2015 Nicolas Chauvet <kwizart@gmail.com> - 4.2.0-1
- Update to 4.2.0
- Add license tag

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 4.1.3-6
- Rebuilt for GCC 5 C++11 ABI change

* Sun Jan 04 2015 Nicolas Chauvet <kwizart@gmail.com> - 4.1.3-5
- Cleanup spec file

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 18 2014 Ville Skyttä <ville.skytta@iki.fi> - 4.1.3-2
- Use system sqlite instead of bundled one

* Wed Feb 12 2014 Nicolas Chauvet <kwizart@gmail.com> - 4.1.3-1
- Update to 4.1.3

* Thu Oct 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 4.1.2-1
- Update to 4.1.2

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 4.1.0-2
- Perl 5.18 rebuild

* Wed Jul 24 2013 Nicolas Chauvet <kwizart@gmail.com> - 4.1.0-1
- Update to 4.1.0

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 4.0.2-3
- Perl 5.18 rebuild

* Fri Mar 01 2013 Nicolas Chauvet <kwizart@gmail.com> - 4.0.2-2
- Rebuilt for libewf

* Thu Feb 28 2013 Nicolas Chauvet <kwizart@gmail.com> - 4.0.2-1
- Update to 4.0.2

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Dec 10 2012 Nicolas Chauvet <kwizart@gmail.com> - 4.0.1-1
- Update to 4.0.1

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 22 2012 Nicolas Chauvet <kwizart@gmail.com> - 3.2.3-1
- Update to 3.2.3

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 26 2011 Nicolas Chauvet <kwizart@gmail.com> - 3.2.2-1
- Update to 3.2.2

* Sun Mar 27 2011 Nicolas Chauvet <kwizart@gmail.com> - 3.2.1-1
- Update to 3.2.1

* Sun Feb 13 2011 Nicolas Chauvet <kwizart@gmail.com> - 3.2.0-1
- Update to 3.2.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Apr 29 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 3.1.1-1
- Update to 3.1.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 10 2009 kwizart < kwizart at gmail.com > - 3.0.1-1
- Update to 3.0.1 (final)

* Tue Oct 28 2008 kwizart < kwizart at gmail.com > - 3.0.0-1
- Update to 3.0.0 (final)

* Fri Oct  3 2008 kwizart < kwizart at gmail.com > - 3.0.0-0.1.b4
- Update to 3.0.0b4

* Tue Jun 17 2008 kwizart < kwizart at gmail.com > - 2.52-1
- Update to 2.52
- Remove merged patches
- Remove clean unused-direct-shlib-dependencies 
- Fix rpath at source.
- Sort license within the spec
- Move configure.ac to pkg-config detection
- Remove Perl-Date-Manip installation

* Tue Mar 18 2008 kwizart < kwizart at gmail.com > - 2.51-1
- Update to 2.51
- Add libewf/afflib BR
- Requires mac-robber external package.
- Remove internal perl-Date-Manip.

* Fri Dec 28 2007 kwizart < kwizart at gmail.com > - 2.10-1
- Update to 2.10

* Mon Oct 29 2007 kwizart < kwizart at gmail.com > - 2.09-1
- Initial package for Fedora 
  (inspired from Oden Eriksson mdk spec).


