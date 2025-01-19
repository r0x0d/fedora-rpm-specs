Name: libatasmart
Version: 0.19
Release: 30%{?dist}
Summary: ATA S.M.A.R.T. Disk Health Monitoring Library
Source0: http://0pointer.de/public/libatasmart-%{version}.tar.xz
Patch0: libatasmart-0.19-wd-fix.patch
License: LGPL-2.1-or-later
Url: http://git.0pointer.de/?p=libatasmart.git;a=summary
BuildRequires:  gcc
BuildRequires: systemd-devel
BuildRequires: make

%description
A small and lightweight parser library for ATA S.M.A.R.T. hard disk
health monitoring.

%package devel
Summary: Development Files for libatasmart Client Development
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig
Requires: vala

%description devel
Development Files for libatasmart Client Development

%ldconfig_scriptlets

%prep
%autosetup

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT \( -name *.a -o -name *.la \) -exec rm {} \;
rm $RPM_BUILD_ROOT%{_docdir}/libatasmart/README

%files
%doc README LGPL
%{_libdir}/libatasmart.so.*
%{_sbindir}/skdump
%{_sbindir}/sktest

%files devel
%{_includedir}/atasmart.h
%{_libdir}/libatasmart.so
%{_libdir}/pkgconfig/libatasmart.pc
%{_datadir}/vala/vapi/atasmart.vapi
%doc blob-examples/SAMSUNG* blob-examples/ST* blob-examples/Maxtor* blob-examples/WDC* blob-examples/FUJITSU* blob-examples/INTEL* blob-examples/TOSHIBA* blob-examples/MCC*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Apr 13 2023 Lukáš Zaoral <lzaoral@redhat.com> - 0.19-25
- migrate to SPDX license format

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 13 2017 Kevin Fenzi <kevin@scrye.com> - 0.19-13
- Fix issue with WD drives. Fixes bug #921430
- https://bugs.freedesktop.org/show_bug.cgi?id=61998

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 04 2012 Kay Sievers <kay@redhat.com> - 0.19-2
- rebuild for libudev1

* Sun May 20 2012 Lennart Poettering <lpoetter@redhat.com> - 0.19-1
- New upstream release

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 11 2011 Lennart Poettering <lpoetter@redhat.com> - 0.18-1
- New upstream release

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec  9 2009 Matthias Clasen <mclasen@redhat.com> - 0.17-2
- Fix an unitialized variable that causes problems in udisks

* Tue Oct 27 2009 Lennart Poettering <lpoetter@redhat.com> 0.17-1
- New upstream release
- Fixes bug 491552

* Tue Sep 29 2009 Lennart Poettering <lpoetter@redhat.com> 0.16-1
- New upstream release
- Second try at fixing #515881

* Fri Sep 18 2009 Lennart Poettering <lpoetter@redhat.com> 0.15-1
- New upstream release
- Fixes #515881

* Thu Aug 6 2009 Lennart Poettering <lpoetter@redhat.com> 0.14-1
- New upstream release

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 22 2009 Lennart Poettering <lpoetter@redhat.com> 0.13-1
- New upstream release

* Wed Apr 15 2009 Lennart Poettering <lpoetter@redhat.com> 0.12-1
- New upstream release

* Tue Apr 14 2009 Lennart Poettering <lpoetter@redhat.com> 0.11-1
- New upstream release

* Mon Apr 13 2009 Lennart Poettering <lpoetter@redhat.com> 0.10-1
- New upstream release

* Sun Apr 12 2009 Lennart Poettering <lpoetter@redhat.com> 0.9-1
- New upstream release

* Fri Apr 10 2009 Lennart Poettering <lpoetter@redhat.com> 0.8-1
- New upstream release

* Tue Apr 7 2009 Lennart Poettering <lpoetter@redhat.com> 0.7-1
- New upstream release

* Sat Apr 5 2009 Lennart Poettering <lpoetter@redhat.com> 0.6-1
- New upstream release

* Fri Apr 3 2009 Lennart Poettering <lpoetter@redhat.com> 0.5-1
- New upstream release

* Thu Apr 2 2009 Lennart Poettering <lpoetter@redhat.com> 0.4-1
- New upstream release

* Tue Mar 24 2009 Lennart Poettering <lpoetter@redhat.com> 0.3-1
- New upstream release

* Thu Mar 19 2009 Lennart Poettering <lpoetter@redhat.com> 0.2-1
- New upstream release

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jul 25 2008 Lennart Poettering <lpoetter@redhat.com> 0.1-1
- Initial version
