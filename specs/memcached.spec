%define username   memcached
%define groupname  memcached
%bcond_without sasl
%bcond_with seccomp
%bcond_without tls
%bcond_with tests
%global selinuxtype	targeted
%global selinuxmoduletype	contrib
%global selinuxmodulename	memcached
%global selinuxmodulever	1.0.2
%global selinuxmoduledir	%{selinuxmodulename}-selinux-%{selinuxmodulever}

Name:           memcached
Version:        1.6.32
Release:        2%{?dist}
Epoch:          0
Summary:        High Performance, Distributed Memory Object Cache

License:        BSD-3-clause AND Zlib AND BSD-2-Clause AND LicenseRef-Fedora-Public-Domain
URL:            https://www.memcached.org/
Source0:        https://www.memcached.org/files/%{name}-%{version}.tar.gz
Source1:        memcached.sysconfig
# SELinux policy sources: https://pagure.io/memcached-selinux/tree/master
Source2:        https://releases.pagure.org/memcached-selinux/memcached-selinux-1.0.2.tar.gz
Source3:	memcached.conf

Patch1:         memcached-unit.patch

BuildRequires:  make
BuildRequires:  gcc libevent-devel systemd
BuildRequires:  perl-generators
BuildRequires:  perl(Test::More), perl(Test::Harness)
%{?with_sasl:BuildRequires: cyrus-sasl-devel}
%{?with_seccomp:BuildRequires: libseccomp-devel}
%{?with_tls:BuildRequires: openssl-devel}
BuildRequires:  systemd-rpm-macros

Requires(pre):  shadow-utils
# Rich dependency syntax - require selinux policy subpackage
# when selinux-policy-targeted is installed
# This ensures that the selinux subpackage is not installed when not needed
# (e.g. inside a container)
Requires: (%{name}-selinux if selinux-policy-targeted)
%{?systemd_requires}

%description
memcached is a high-performance, distributed memory object caching
system, generic in nature, but intended for use in speeding up dynamic
web applications by alleviating database load.

%package devel
Summary: Files needed for development using memcached protocol
Requires: %{name} = %{epoch}:%{version}-%{release}

%description devel
Install memcached-devel if you are developing C/C++ applications that require
access to the memcached binary include files.

%package selinux
Summary: Selinux policy module
License: GPL-2.0-only
BuildRequires: selinux-policy
%{?selinux_requires}

%description selinux
Install memcached-selinux to ensure your system contains the latest SELinux policy
optimised for use with this version of memcached.

%prep
# Unpack memcached sources into memcached-X.X.X directory
# and SELinux policy sources into memcached-selinux-X.X
%setup -q -b 2
%patch 1 -p1 -b .unit

%build
%configure \
  %{?with_sasl: --enable-sasl --enable-sasl-pwdb} \
  %{?with_seccomp: --enable-seccomp} \
  %{?with_tls: --enable-tls}

make %{?_smp_mflags}

pushd ../%{selinuxmoduledir}
make
popd

%check
# tests are disabled by default as they are unreliable on build systems
%{!?with_tests: exit 0}

# whitespace tests fail locally on fedpkg systems now that they use git
rm -f t/whitespace.t

# Parts of the test suite only succeed as non-root.
if [ `id -u` -ne 0 ]; then
  # remove failing test that doesn't work in
  # build systems
  rm -f t/daemonize.t t/watcher.t t/expirations.t
fi
make test

%install
make install DESTDIR=%{buildroot} INSTALL="%{__install} -p"
# remove memcached-debug
rm -f %{buildroot}/%{_bindir}/memcached-debug

# Perl script for monitoring memcached
install -Dp -m0755 scripts/memcached-tool %{buildroot}%{_bindir}/memcached-tool
install -Dp -m0644 scripts/memcached-tool.1 \
        %{buildroot}%{_mandir}/man1/memcached-tool.1

# Unit file
install -Dp -m0644 scripts/memcached.service \
        %{buildroot}%{_unitdir}/memcached.service

# Default configs
install -Dp -m0644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/sysconfig/%{name}

# install SELinux policy module
pushd ../%{selinuxmoduledir}
install -d %{buildroot}%{_datadir}/selinux/packages
install -d -p %{buildroot}%{_datadir}/selinux/devel/include/%{selinuxmoduletype}
# Not installing memcached.if - interface file from selinux-policy-devel will be used
# see. "Independant product policy" documentation for more details
install -m 0644 %{selinuxmodulename}.pp.bz2 %{buildroot}%{_datadir}/selinux/packages
popd

install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/memcached.conf

%pre
%sysusers_create_compat %{SOURCE3}

%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post
%systemd_post memcached.service

%post selinux
# install selinux policy module with priority 200 to override the default policy
%selinux_modules_install -s %{selinuxtype} -p 200 %{_datadir}/selinux/packages/%{selinuxmodulename}.pp.bz2 &> /dev/null

%preun
%systemd_preun memcached.service


%postun
%systemd_postun_with_restart memcached.service

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} -p 200 %{selinuxmodulename}
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype} &> /dev/null

%files
%doc AUTHORS ChangeLog COPYING NEWS README.md doc/CONTRIBUTORS doc/*.txt
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_bindir}/memcached-tool
%{_bindir}/memcached
%{_mandir}/man1/memcached-tool.1*
%{_mandir}/man1/memcached.1*
%{_unitdir}/memcached.service
%{_sysusersdir}/memcached.conf

%files devel
%{_includedir}/memcached/*

%files selinux
%attr(0644,root,root) %{_datadir}/selinux/packages/%{selinuxmodulename}.pp.bz2
%ghost %{_sharedstatedir}/selinux/%{selinuxtype}/active/modules/200/%{selinuxmodulename}
%license ../%{selinuxmoduledir}/COPYING

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.6.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 01 2024 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.32-1
- Update to 1.6.32
- Resolves: rhbz#2310685

* Thu Aug 01 2024 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.29-1
- Update to 1.6.29
- Resolves: rhbz#2295606

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.6.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 27 2024 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.28-1
- Update to 1.6.28
- Resolves: rhbz#2279529

* Tue May 28 2024 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.26-2
- Fix License tags to conform with SPDX

* Wed Apr 03 2024 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.26-1
- Update to 1.6.26
- Resolves: rhbz#2270552

* Wed Mar 13 2024 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.24-1
- Update to 1.6.24
- Resolves: rhbz#2266938

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.6.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.23-1
- Update to 1.6.23
- Resolves: rhbz#2257644

* Tue Oct 31 2023 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.22-2
- Update license tag to fully conform to SPDX

* Wed Oct 25 2023 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.22-1
- Update to 1.6.22
- Resolves: rhbz#2244603

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.6.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 19 2023 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.21-1
- Update to 1.6.21
- Resolves: rhbz#2215568

* Mon May 15 2023 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.20-1
- Update to 1.6.20
- Resolves: rhbz#2203537

* Sat Mar 11 2023 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.19-2
- Change the License tag to the SPDX format

* Thu Mar 09 2023 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.19-1
- Update to 1.6.19
- Resolves: rhbz#2176684

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.6.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jan 12 2023 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.18-1
- Update to 1.6.18
- Resolves: rhbz#2160271

* Tue Aug 30 2022 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.17-1
- Update to 1.6.17
- Resolves: rhbz#2121978

* Tue Aug 09 2022 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.16-1
- Update to 1.6.16
- Resolves: rhbz#2115502

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.6.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Tomas Korbar <tkorbar@redhat.com> - 1.6.15-2
- Resolves: rhbz#2096850

* Fri Apr 08 2022 Tomas Korbar <tkorbar@redhat.com> - 1.6.15-1
- Update to 1.6.15
- Resolves: rhbz#2070493

* Tue Feb 15 2022 Tomas Korbar <tkorbar@redhat.com> - 1.6.14-1
- Update to 1.6.14
- Resolves: rhbz#2053327

* Fri Jan 28 2022 Tomas Korbar <tkorbar@redhat.com> - 1.6.13-3
- Fix complete_incr_bin function
- Resolves: rhbz#2046734

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.6.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 14 2022 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.13-1
- Update to 1.6.13
- Resolves: rhbz#2040188

* Wed Sep 29 2021 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.12-1
- Update to 1.6.12

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0:1.6.10-2
- Rebuilt with OpenSSL 3.0.0

* Tue Jul 27 2021 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.10-1
- Update to 1.6.10
- Resolves: rhbz#1985842

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.6.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0:1.6.9-4
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.6.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.9-2
- Enable sasl pwdb (#1909724)

* Tue Nov 24 2020 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.9-1
- Update to 1.6.9

* Thu Oct 29 2020 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.8-1
- Update to 1.6.8

* Tue Sep 15 2020 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.7-2
- Rebuilt with libevent-2.1.12

* Mon Sep 07 2020 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.7-1
- Update to 1.6.7

* Tue Aug 04 2020 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.6-4
- Resolve FTBFS (#1863678)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.6.6-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 18 2020 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.6-1
- Update to 1.6.6

* Wed Apr 22 2020 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.5-1
- Update to 1.6.5

* Mon Apr 06 2020 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.3-2
- Fix undefined behaviour on build with -D_FORTIFY_SOURCE=2
- Found by tstellar@redhat.com

* Sun Mar 29 2020 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.3-1
- Update to 1.6.3

* Tue Mar 24 2020 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.2-1
- Update to 1.6.2

* Thu Mar 19 2020 Tomas Korbar <tkorbar@redhat.com> - 0:1.6.1-1
- Update to 1.6.1

* Wed Mar 04 2020 Tomas Korbar <tkorbar@redhat.com> - 0:1.5.22-2
- Enable TLS by default

* Fri Feb 07 2020 Tomas Korbar <tkorbar@redhat.com> - 0:1.5.22-1
- update to 1.5.22

* Thu Jan 30 2020 Tomas Korbar <tkorbar@redhat.com> - 0:1.5.21-1
- update to 1.5.21
- make memcached gcc 10 compliant

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.5.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Tomas Korbar <tkorbar@redhat.com> - 0:1.5.20-1
- update to 1.5.20

* Sun Sep 22 2019 Tomas Korbar <tkorbar@redhat.com> - 0:1.5.18-1
- update to 1.5.18

* Tue Sep 03 2019 Tomas Korbar <tkorbar@redhat.com> - 0:1.5.17-1
- update to 1.5.17

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.5.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 27 2019 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.5.16-1
- update to 1.5.16

* Wed May 22 2019 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.5.15-1
- update to 1.5.15

* Mon May 06 2019 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.5.14-1
- update to 1.5.14 (CVE-2019-11596)

* Tue Apr 16 2019 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.5.13-1
- update to 1.5.13

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.5.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Aug 30 2018 Vit Mojzis <vmojzis@redhat.com> - 0:1.5.10-2
- selinux: Update to 1.0.2
- selinux: Use license file from memcached-selinux tar
- add "Requires" for selinux subpackage

* Mon Aug 13 2018 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.5.10-1
- update to 1.5.10
- add conditional for running tests in check stage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.5.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jul 09 2018 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.5.9-1
- update to 1.5.9

* Tue Jun 05 2018 Vit Mojzis <vmojzis@redhat.com> - 0:1.5.8-2
- add "selinux" subpackage containing SELinux policy module

* Fri May 25 2018 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.5.8-1
- update to 1.5.8
- use system CFLAGS and LDFLAGS

* Thu Mar 29 2018 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.5.7-1
- update to 1.5.7
- use https URLs in spec

* Thu Mar 01 2018 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.5.6-1
- update to 1.5.6 (UDP port disabled by default)
- add gcc to build requirements

* Thu Feb 15 2018 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.5.5-2
- rebuild for new libevent

* Tue Feb 13 2018 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.5.5-1
- update to 1.5.5

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.5.4-2
- fix building with new gcc
- use macro for systemd scriptlet dependencies

* Thu Jan 04 2018 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.5.4-1
- update to 1.5.4

* Mon Nov 06 2017 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.5.3-1
- update to 1.5.3
- add build condition for seccomp support

* Mon Oct 02 2017 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.5.2-1
- update to 1.5.2

* Fri Aug 25 2017 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.5.1-1
- update to 1.5.1

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 24 2017 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.5.0-1
- update to 1.5.0

* Tue Jul 11 2017 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.4.39-1
- update to 1.4.39 (CVE-2017-9951)

* Tue Jun 27 2017 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.4.38-1
- update to 1.4.38

* Fri Jun 09 2017 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.4.37-1
- update to 1.4.37

* Wed Mar 22 2017 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.4.36-1
- update to 1.4.36

* Mon Feb 27 2017 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.4.35-1
- update to 1.4.35

* Wed Feb 15 2017 Joe Orton <jorton@redhat.com> - 0:1.4.34-3
- fix gcc 7 format-truncation error (#1423934)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.4.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.4.34-1
- update to 1.4.34

* Tue Nov 01 2016 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.4.33-1
- update to 1.4.33 (CVE-2016-8704, CVE-2016-8705, CVE-2016-8706)

* Thu Oct 13 2016 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.4.32-1
- update to 1.4.32

* Wed Sep 07 2016 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.4.31-1
- update to 1.4.31
- disable testing for now

* Fri Aug 12 2016 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.4.30-1
- update to 1.4.30

* Thu Jul 14 2016 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.4.29-1
- update to 1.4.29

* Tue Jul 12 2016 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.4.28-1
- update to 1.4.28
- listen only on loopback interface by default (#1182542)
- use upstream unit file (#1350939)
- remove obsolete macros and scriptlet

* Tue Jun 21 2016 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.4.26-1
- update to 1.4.26

* Tue Feb 23 2016 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.4.25-1
- update to 1.4.25
- enable SASL support (#815050)
- remove obsolete macros

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0:1.4.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.4.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.4.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.4.17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 15 2014 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.4.17-1
- update to 1.4.17
- fix building with -Werror=format-security in CFLAGS

* Wed Aug 07 2013 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.4.15-7
- buildrequire systemd-units (#992221)
- update memcached man page
- add memcached-tool man page

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.4.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 0:1.4.15-5
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.4.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 20 2012 Miroslav Lichvar <mlichvar@redhat.com> - 0:1.4.15-3
- compile with full RELRO

* Tue Nov 20 2012 Joe Orton <jorton@redhat.com> - 0:1.4.15-2
- BR perl(Test::Harness)

* Tue Nov 20 2012 Joe Orton <jorton@redhat.com> - 0:1.4.15-1
- update to 1.4.15 (#782395)
- switch to simple systemd service (#878198)
- use systemd scriptlet macros (Václav Pavlín, #850204)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.4.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 04 2012 Jon Ciesla <limburgher@gmail.com> - 0:1.4.13-2
- Migrate to systemd, 783112.

* Tue Feb  7 2012 Paul Lindner <lindner@mirth.inuus.com> - 0:1.4.13-1
- Upgrade to memcached 1.4.13
- http://code.google.com/p/memcached/wiki/ReleaseNotes1413
- http://code.google.com/p/memcached/wiki/ReleaseNotes1412
- http://code.google.com/p/memcached/wiki/ReleaseNotes1411

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.4.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  9 2011 Paul Lindner <lindner@mirth.inuus.com> - 0:1.4.10-1
- Upgrade to memcached 1.4.10 (http://code.google.com/p/memcached/wiki/ReleaseNotes1410)

* Tue Aug 16 2011 Paul Lindner <lindner@inuus.com> - 0:1.4.7-1
- Upgrade to memcached 1.4.7 (http://code.google.com/p/memcached/wiki/ReleaseNotes147)
- Fix some rpmlint errors/warnings.

* Tue Aug  2 2011 Paul Lindner <lindner@inuus.com> - 0:1.4.6-1
- Upgrade to memcached-1.4.6

* Wed Feb 16 2011 Joe Orton <jorton@redhat.com> - 0:1.4.5-7
- fix build

* Mon Feb 14 2011 Paul Lindner <lindner@inuus.com> - 0:1.4.5-6
- Rebuild for updated libevent

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0:1.4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Nov 28 2010 Paul Lindner <lindner@inuus.com> - 0:1.4.5-4
- Add code to deal with /var/run/memcached on tmpfs

* Wed Sep  8 2010 Paul Lindner <lindner@inuus.com> - 0:1.4.5-3
- Apply patch from memcached issue #60, solves Bugzilla 631051

* Wed May 26 2010 Joe Orton <jorton@redhat.com> - 0:1.4.5-2
- LSB compliance fixes for init script
- don't run the test suite as root
- ensure a constant timestamp on the sysconfig file

* Sun Apr  4 2010 Paul Lindner <lindner@inuus.com> - 0:1.4.5-1
- Upgrade to upstream memcached-1.4.5 (http://code.google.com/p/memcached/wiki/ReleaseNotes145)

* Wed Jan 20 2010 Paul Lindner <lindner@inuus.com> - 0:1.4.4-2
- Remove SELinux policies fixes Bugzilla 557073

* Sat Nov 28 2009 Paul Lindner <lindner@inuus.com> - 0:1.4.4-1
- Upgraded to upstream memcached-1.4.4 (http://code.google.com/p/memcached/wiki/ReleaseNotes144)
- Add explicit Epoch to fix issue with broken devel dependencies (resolves 542001)

* Thu Nov 12 2009 Paul Lindner <lindner@inuus.com> - 1.4.3-1
- Add explicit require on memcached for memcached-devel (resolves 537046)
- enable-threads option no longer needed
- Update web site address

* Wed Nov 11 2009 Paul Lindner <lindner@inuus.com> - 1.4.3-1
- Upgrade to memcached-1.4.3

* Mon Oct 12 2009 Paul Lindner <lindner@inuus.com> - 1.4.2-1
- Upgrade to memcached-1.4.2
- Addresses CVE-2009-2415

* Sat Aug 29 2009 Paul Lindner <lindner@inuus.com> - 1.4.1-1
- Upgrade to 1.4.1
- http://code.google.com/p/memcached/wiki/ReleaseNotes141

* Wed Apr 29 2009 Paul Lindner <lindner@inuus.com> - 1.2.8-1
- Upgrade to memcached-1.2.8
- Addresses CVE-2009-1255

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jul 29 2008 Paul Lindner <lindner@inuus.com> - 1.2.6-1
- Upgrade to memcached-1.2.6

* Tue Mar  4 2008 Paul Lindner <lindner@inuus.com> - 1.2.5-1
- Upgrade to memcached-1.2.5

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.4-4
- Autorebuild for GCC 4.3

* Sun Jan 27 2008 Paul Lindner <lindner@inuus.com> - 1.2.4-3
- Adjust libevent dependencies

* Sat Dec 22 2007 Paul Lindner <lindner@inuus.com> - 1.2.4-2
- Upgrade to memcached-1.2.4

* Fri Sep 07 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 1.2.3-8
- Add selinux policies
- Create our own system user

* Mon Aug  6 2007 Paul Lindner <lindner@inuus.com> - 1.2.3-7
- Fix problem with -P and -d flag combo on x86_64
- Fix init script for FC-6

* Fri Jul 13 2007 Paul Lindner <lindner@inuus.com> - 1.2.3-4
- Remove test that fails in fedora build system on ppc64

* Sat Jul  7 2007 root <lindner@inuus.com> - 1.2.3-2
- Upgrade to 1.2.3 upstream
- Adjust make install to preserve man page timestamp
- Conform with LSB init scripts standards, add force-reload

* Wed Jul  4 2007 Paul Lindner <lindner@inuus.com> - 1.2.2-5
- Use /var/run/memcached/ directory to hold PID file

* Sat May 12 2007 Paul Lindner <lindner@inuus.com> - 1.2.2-4
- Remove tabs from spec file, rpmlint reports no more errors

* Thu May 10 2007 Paul Lindner <lindner@inuus.com> - 1.2.2-3
- Enable build-time regression tests
- add dependency on initscripts
- remove memcached-debug (not needed in dist)
- above suggestions from Bernard Johnson

* Mon May  7 2007 Paul Lindner <lindner@inuus.com> - 1.2.2-2
- Tidyness improvements suggested by Ruben Kerkhof in bugzilla #238994

* Fri May  4 2007 Paul Lindner <lindner@inuus.com> - 1.2.2-1
- Initial spec file created via rpmdev-newspec
