#%%global prever rc3

Name: log4cplus
Version: 2.1.1
Release: 5%{?prever:.%{prever}}%{?dist}
Summary: Logging Framework for C++

%define VER %(echo %{version} | tr . _)

# Threadpool is Zlib
# catch/* is BSL-1.0
License: (BSD-2-Clause OR Apache-2.0) AND Zlib AND BSL-1.0
URL: https://github.com/log4cplus/log4cplus
Source0: https://github.com/log4cplus/log4cplus/releases/download/REL_%{VER}/%{name}-%{version}%{?prever:-%{prever}}.tar.xz
Source1: https://github.com/log4cplus/log4cplus/releases/download/REL_%{VER}/%{name}-%{version}%{?prever:-%{prever}}.tar.xz.sig
Source2: codesign.key

%description
log4cplus is a simple to use C++ logging API providing thread-safe, flexible,
and arbitrarily granular control over log management and configuration. It is
modeled after the Java log4j API.

%package devel
Summary: Development files for log4cplus C++ logging framework
Requires: %{name} = %{version}-%{release}
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: gnupg2

%description devel
This package contains headers and libraries needed to develop applications
using log4cplus logging framework.

%package static
Summary: Static development files for log4cplus C++ logging framework
Requires: %{name}-devel = %{version}-%{release}

%description static
This package contains static libraries needed to develop applications
using log4cplus logging framework.

%prep
%if 0%{?fedora}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%setup -q %{?prever:-n %{name}-%{version}-%{prever}}

%build
%configure --enable-static
make %{?_smp_mflags}


%install
%make_install

rm -f $RPM_BUILD_ROOT/%{_libdir}/liblog4cplus*.la

%ldconfig_scriptlets

%files
%doc LICENSE README.md ChangeLog
%{_libdir}/liblog4cplus*.so.9*

%files devel
%dir %{_includedir}/log4cplus
%dir %{_includedir}/log4cplus/boost
%dir %{_includedir}/log4cplus/config
%dir %{_includedir}/log4cplus/helpers
%dir %{_includedir}/log4cplus/internal
%dir %{_includedir}/log4cplus/spi
%dir %{_includedir}/log4cplus/thread
%dir %{_includedir}/log4cplus/thread/impl
%{_libdir}/lib*.so
%{_includedir}/log4cplus/*.h*
%{_includedir}/log4cplus/boost/*.h*
%{_includedir}/log4cplus/config/*.h*
%{_includedir}/log4cplus/helpers/*.h*
%{_includedir}/log4cplus/internal/*.h*
%{_includedir}/log4cplus/spi/*.h*
%{_includedir}/log4cplus/thread/*.h*
%{_includedir}/log4cplus/thread/impl/*.h*
%{_libdir}/pkgconfig/log4cplus.pc

%files static
%{_libdir}/lib*.a


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 22 2023 Martin Osvald <mosvald@redhat.com> - 2.1.1-1
- New version 2.1.1 (rhbz#2250290)
- Fix incorrect upstream URL and SourceX (rhbz#2249526)
- SPDX migration

* Thu Aug 10 2023 Martin Osvald <mosvald@redhat.com> - 2.1.0-2
- New version 2.1.0 (rhbz#2169015)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 04 2022 Martin Osvald <mosvald@redhat.com> - 2.0.8-3
- Remove extra {} as it is no longer brace expansion

* Fri Sep 23 2022 Federico Pellegrin <fede@evolware.org> - 2.0.8-2
- Add generation of static package

* Thu Jul 21 2022 Martin Osvald <mosvald@redhat.com> - 2.0.8-1
- New version 2.0.8

* Thu Jun 02 2022 Martin Osvald <mosvald@redhat.com> - 2.0.7-1
- New version 2.0.7
- Add source code signature verification

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Jonathan Wakely <jwakely@redhat.com> - 2.0.5-13
- Rebuilt for removed libstdc++ symbol (#1937698)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 20 2020 Pavel Zhukov <pzhukov@redhat.com> - 2.0.5-11
- New version v2.0.5

* Wed Aug 26 2020 Jeff Law <law@redhat.com> - 1.2.0-13
- Drop forcing of C++11 mode.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 26 2018 Tomas Hozza <thozza@redhat.com> - 1.2.0-7
- Added gcc-c++ as an explicit BuildRequires

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Mar 23 2016 Zdenek Dohnal zdohnal@redhat.com - 1.2.0-2
- Replacing hard names with macros, returning and commenting macro prever in
  specfile

* Fri Mar 18 2016 zdohnal <zdohnal@redhat.com> - 1.2.0-1
- Update to 1.2.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-0.5.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Tomas Hozza <thozza@redhat.com> - 1.1.3-0.4.rc3
- Fixed typo so that log4cplus is compiled with C++11 support (#1297906)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.3-0.3.rc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.3-0.2.rc3
- Rebuilt for GCC 5 C++11 ABI change

* Tue Dec 16 2014 Tomas Hozza <thozza@redhat.com> - 1.1.3-0.1.rc3
- update to 1.1.3rc3
- build the library with c++11 support

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Oct 24 2013 Tomas Hozza <thozza@redhat.com> - 1.1.2-1
- update to 1.1.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu May 23 2013 Tomas Hozza <thozza@redhat.com> 1.1.1-1
- update to 1.1.1

* Mon Feb 18 2013 Adam Tkac <atkac redhat com> - 1.1.0-1
- update to 1.1.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-0.3.rc10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Sep 21 2012 Adam Tkac <atkac redhat com> - 1.1.0-0.2.rc10
- some fixes related to pkg review

* Thu Sep 20 2012 Adam Tkac <atkac redhat com> - 1.1.0-0.1.rc10
- initial package
