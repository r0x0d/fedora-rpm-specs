Name:    liblogging
Version: 1.0.6
Release: 20%{?dist}
Summary: An easy to use logging library
License: BSD-2-Clause
URL:     http://www.liblogging.org/
Source0: http://download.rsyslog.com/liblogging/liblogging-%{version}.tar.gz

%package stdlog
Summary: An easy to use logging library - stdlog component
BuildRequires:  gcc
BuildRequires: dos2unix
BuildRequires: make

%package stdlog-devel
Summary: An easy to use logging library - stdlog development files
Requires: %{name}-stdlog%{_isa} = %{version}-%{release}
Requires: pkgconfig

%description
liblogging (the upstream project) is a collection of several components.
Namely: stdlog, journalemu, rfc3195.

%description stdlog
liblogging (the upstream project) is a collection of several components.
Namely: stdlog, journalemu, rfc3195.
The stdlog component of liblogging can be viewed as an enhanced version of the
syslog(3) API. It retains the easy semantics, but makes the API more
sophisticated "behind the scenes" with better support for multiple threads
and flexibility for different log destinations (e.g. syslog and systemd
journal).

%description stdlog-devel
This package contains development files for the %{name}-stdlog package.

%prep
%setup -q

%build
%configure \
  --disable-journal \
  --disable-rfc3195 \
  --disable-static \
  --enable-stdlog \

make V=1 %{?_smp_mflags}
dos2unix COPYING

%install
make DESTDIR=%{buildroot} install
# not packing stdlogctl yet
rm -f \
  %{buildroot}%{_bindir}/stdlogctl \
  %{buildroot}%{_libdir}/liblogging-stdlog.la \
  %{buildroot}%{_mandir}/man1/stdlogctl.1 \

%ldconfig_scriptlets stdlog

%files stdlog
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc ChangeLog
%{_libdir}/liblogging-stdlog.so.*

%files stdlog-devel
%{_includedir}/liblogging
%{_libdir}/liblogging-stdlog.so
%{_libdir}/pkgconfig/liblogging-stdlog.pc
%{_mandir}/man3/stdlog.3.gz

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 10 2023 Attila Lakatos <alakatos@redhat.com> - 1.0.6-15
- Migrate to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 30 2017 Radovan Sroka <rsroka@redhat.com> - 1.0.6-1
- rebase to 1.0.6

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 18 2014 Tom Callaway <spot@fedoraproject.org> - 1.0.4-3
- fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun May 18 2014 Tomas Heinrich <theinric@redhat.com> 1.0.4-1
- initial import
