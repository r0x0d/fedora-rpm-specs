Summary:	A modern implementation of a DBM
Name:		tokyocabinet
Version:	1.4.48
Release:	27%{?dist}
License:	LGPL-2.1-or-later
URL:		http://fallabs.com/tokyocabinet/
Source:		http://fallabs.com/%{name}/%{name}-%{version}.tar.gz
Patch0:		tokyocabinet-fedora.patch
Patch1:		tokyocabinet-manhelp.patch
BuildRequires: make
BuildRequires:	pkgconfig zlib-devel bzip2-devel autoconf gcc

%description
Tokyo Cabinet is a library of routines for managing a database. It is the 
successor of QDBM. Tokyo Cabinet runs very fast. For example, the time required
to store 1 million records is 1.5 seconds for a hash database and 2.2 seconds
for a B+ tree database. Moreover, the database size is very small and can be up
to 8EB. Furthermore, the scalability of Tokyo Cabinet is great.

%package devel
Summary:	Headers for developing programs that will use %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description devel
This package contains the libraries and header files needed for
developing with %{name}.

%package devel-doc
Summary:	Documentation files for developing programs that will use %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig
BuildArch:	noarch

%description devel-doc
This package contains documentation files for the libraries and header files
needed for developing with %{name}.

%prep
%setup -q
%patch -P0 -p0 -b .fedora
%patch -P1 -p1 -b .manhelp

%build
autoconf
%configure --enable-off64 CFLAGS="$CFLAGS"
make %{?_smp_mflags}
										
%install
make DESTDIR=%{buildroot} install

rm -rf %{buildroot}%{_datadir}/%{name}
rm -rf %{buildroot}%{_libdir}/lib%{name}.a

%check
%ifnarch x86_64
make check
%endif

%ldconfig_scriptlets

%files
%doc ChangeLog COPYING README
%{_bindir}/tc*
%{_libdir}/libtokyocabinet.so.*
%{_libexecdir}/tcawmgr.cgi
%{_mandir}/man1/tc*.gz

%files devel
%{_includedir}/tc*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/t*.gz

%files devel-doc
%doc doc/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.48-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.48-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.4.48-25
- Bump release and build for %%patchX usage removal

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.48-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.48-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 03 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.4.48-22
- migrated to SPDX license

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.48-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.48-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.48-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.48-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.48-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.48-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.48-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.48-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.48-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.48-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 27 2018 Marek Skalický <mskalick@redhat.com> - 1.4.48-11
- Add missing BuildRequires: gcc/gcc-c++

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.48-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.48-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.48-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.48-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.48-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.48-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.48-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.48-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 20 2013 Honza Horak <hhorak@redhat.com> - 1.4.48-1
- Update to 1.4.48
- Fix help vs. man page differences

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.47-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 18 2012 Honza Horak <hhorak@redhat.com> - 1.4.47-5
- Split devel documentation files into new sub-package tokyocabinet-devel-doc

* Tue Sep 18 2012 Honza Horak <hhorak@redhat.com> - 1.4.47-4
- Minor spec file fixes

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.47-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.47-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 14 2011 Honza Horak <hhorak@redhat.com> - 1.4.47-1
- Update to 1.4.47

* Wed Jul 13 2011 Honza Horak <hhorak@redhat.com> - 1.4.46-3
- change project URL and source URL to actual destination

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.46-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 06 2010 Deji Akingunola <dakingun@gmail.com> - 1.4.46-1
- Update to 1.4.46

* Thu Apr 22 2010 Deji Akingunola <dakingun@gmail.com> - 1.4.43-2
- Enable 64-bit file offset support (Fix Fedora bug #514383)

* Thu Mar 11 2010 Deji Akingunola <dakingun@gmail.com> - 1.4.43-1
- Update to 1.4.43 (Fix Fedora bug #572594)

* Thu Mar 04 2010 Deji Akingunola <dakingun@gmail.com> - 1.4.42-1
- Update to 1.4.42

* Thu Dec 17 2009 Deji Akingunola <dakingun@gmail.com> - 1.4.41-1
- Update to 1.4.41

* Wed Sep 30 2009 Deji Akingunola <dakingun@gmail.com> - 1.4.33-1
- Update to 1.4.33

* Fri Aug 28 2009 Deji Akingunola <dakingun@gmail.com> - 1.4.32-1
- Update to 1.4.32

* Mon Aug 10 2009 Deji Akingunola <dakingun@gmail.com> - 1.4.30-1
- New upstream version

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 03 2009 Deji Akingunola <dakingun@gmail.com> - 1.4.23-1
- Update to version 1.4.23

* Tue Mar 03 2009 Deji Akingunola <dakingun@gmail.com> - 1.4.9-1
- Update to version 1.4.9

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 13 2009 Deji Akingunola <dakingun@gmail.com> - 1.3.27-1
- Update to version 1.3.27

* Mon Aug 25 2008 Deji Akingunola <dakingun@gmail.com> - 1.3.4-1
- Update to 1.3.4

* Sun May 25 2008 Masahiro Hasegawa <masahase@gmail.com> - 1.2.6-1
- Update to 1.2.6

* Mon Apr 28 2008 Deji Akingunola <dakingun@gmail.com> - 1.2.5-1
- Update to 1.2.5

* Fri Feb 08 2008 Deji Akingunola <dakingun@gmail.com> - 1.1.14-1
- Update to 1.1.14

* Fri Jan 11 2008 Deji Akingunola <dakingun@gmail.com> - 1.1.7-1
- Update to 1.1.7

* Tue Dec 18 2007 Deji Akingunola <dakingun@gmail.com> - 1.1.4-1
- Update to 1.1.4

* Sat Nov 24 2007 Deji Akingunola <dakingun@gmail.com> - 1.0.8-1
- Update to 1.0.8

* Sat Nov 24 2007 Deji Akingunola <dakingun@gmail.com> - 1.0.6-1
- Initial package
