Name:       pure-ftpd
Version:    1.0.51
Release:    9%{?dist}
Summary:    Lightweight, fast and secure FTP server
# Automatically converted from old format: BSD - review is highly recommended.
License:    LicenseRef-Callaway-BSD
URL:        http://www.pureftpd.org

Source0:    http://download.pureftpd.org/pub/pure-ftpd/releases/pure-ftpd-%{version}.tar.bz2
Source1:    pure-ftpd.service
Source2:    pure-ftpd.logrotate
Source6:    pure-ftpd.README.SELinux
Source7:    pure-ftpd.pureftpd.te
Source8:    pure-ftpd-with-tls-init.service
Source9:    pure-ftpd-with-tls.service
Patch0:     0001-modify-pam.patch
Patch1:     0002-fedora-specific-config-file.patch

Provides:   ftpserver
BuildRequires: make
BuildRequires:  pam-devel, libcap-devel
BuildRequires:  libxcrypt-devel
%{!?_without_ldap:BuildRequires:  openldap-devel}
%{!?_without_mysql:BuildRequires: mariadb-connector-c-devel}
%{!?_without_pgsql:BuildRequires: libpq-devel}
%{!?_without_tls:BuildRequires: openssl-devel}
BuildRequires: checkpolicy, selinux-policy-devel
BuildRequires: systemd
BuildRequires: git
BuildRequires: gcc
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Requires:   logrotate
%{!?_without_tls:Requires: sscg}


%description
Pure-FTPd is a fast, production-quality, standard-comformant FTP server,
based upon Troll-FTPd. Unlike other popular FTP servers, it has no known
security flaw, it is really trivial to set up and it is especially designed
for modern Linux and FreeBSD kernels (setfsuid, sendfile, capabilities) .
Features include PAM support, IPv6, chroot()ed home directories, virtual
domains, built-in LS, anti-warez system, bandwidth throttling, FXP, bounded
ports for passive downloads, UL/DL ratios, native LDAP and SQL support,
Apache log files and more.
Rebuild switches:
--without ldap     disable ldap support
--without mysql    disable mysql support
--without pgsql    disable postgresql support
--without extauth  disable external authentication
--without tls      disable SSL/TLS


%package    selinux
Summary:    SELinux support for Pure-FTPD
Requires:   %{name} = %{version}
Requires(post): policycoreutils, %{name}
Requires(preun): policycoreutils, %{name}
Requires(postun): policycoreutils

%description selinux
This package adds SELinux enforcement to Pure-FTPD. Install it if you want
Pure-FTPd to be protected in the same way other FTP servers are in Fedora
(e.g. VSFTPd and ProFTPd)



%prep
%autosetup -S git
install -pm 644 %{SOURCE6} README.SELinux
mkdir selinux
cp -p %{SOURCE7} selinux/pureftpd.te


%build
%configure  \
            --sysconfdir=%{_sysconfdir}/%{name} \
            --with-capabilities \
            --with-sendfile \
            --with-paranoidmsg \
            --with-altlog \
            --with-puredb \
            %{!?_without_extauth:--with-extauth} \
            --with-pam \
            --with-cookie \
            --with-throttling \
            --with-ratios \
            --with-quotas \
            --with-ftpwho \
            --with-welcomemsg \
            --with-uploadscript \
            --with-virtualhosts \
            --with-virtualchroot \
            --with-diraliases \
            --with-peruserlimits \
            %{!?_without_ldap:--with-ldap} \
            %{!?_without_mysql:--with-mysql} \
            %{!?_without_pgsql:--with-pgsql} \
            --with-privsep \
            %{!?_without_tls:--with-tls --with-certfile=%{_sysconfdir}/pki/%{name}/%{name}.pem} \
            --with-rfc2640 \
            --without-bonjour \

%make_build

%install
%make_install

install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man8
install -d -m 755 $RPM_BUILD_ROOT%{_sbindir}
install -d -m 755 $RPM_BUILD_ROOT%{_unitdir}
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_localstatedir}/ftp
%{!?_without_tls:install -d -m 700 $RPM_BUILD_ROOT%{_sysconfdir}/pki/%{name}}

# Conf
install -p -m 644 pure-ftpd.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -p -m 644 pureftpd-ldap.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -p -m 644 pureftpd-mysql.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}
install -p -m 644 pureftpd-pgsql.conf $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

# Man
install -p -m 644 man/pure-ftpd.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 644 man/pure-ftpwho.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 644 man/pure-mrtginfo.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 644 man/pure-uploadscript.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 644 man/pure-pw.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 644 man/pure-pwconvert.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 644 man/pure-statsdecode.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 644 man/pure-quotacheck.8 $RPM_BUILD_ROOT%{_mandir}/man8
install -p -m 644 man/pure-authd.8 $RPM_BUILD_ROOT%{_mandir}/man8

# Systemd services
%if 0%{!?_without_tls:1}
install -p -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{_unitdir}/pure-ftpd-init.service
install -p -m 644 %{SOURCE9} $RPM_BUILD_ROOT%{_unitdir}/pure-ftpd.service
%else
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/pure-ftpd.service
%endif

# Pam 
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
install -p -m 644 pam/pure-ftpd $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/

# Logrotate
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/logrotate.d/%{name}

# SELinux support
pushd selinux
echo "%{_sbindir}/pure-ftpd    system_u:object_r:ftpd_exec_t:s0" > pureftpd.fc
echo '%{_localstatedir}/log/pureftpd.log    system_u:object_r:xferlog_t:s0' >> pureftpd.fc
touch pureftpd.if
make -f %{_datadir}/selinux/devel/Makefile
install -p -m 644 -D pureftpd.pp $RPM_BUILD_ROOT%{_datadir}/selinux/packages/%{name}/pureftpd.pp
popd

# Remove unnecessary docs
rm $RPM_BUILD_ROOT%{_docdir}/%{name}/README.MacOS-X

%post
%systemd_post pure-ftpd.service

%preun
%systemd_preun pure-ftpd.service

%postun
%systemd_postun_with_restart pure-ftpd.service


%post selinux
if [ "$1" -le "1" ]; then # Fist install
    semodule -i %{_datadir}/selinux/packages/%{name}/pureftpd.pp 2>/dev/null || :
    fixfiles -R pure-ftpd restore || :
    /bin/systemctl condrestart pure-ftpd > /dev/null 2>&1  || :
fi

%preun selinux
if [ "$1" -lt "1" ]; then # Final removal
    semodule -r pureftpd 2>/dev/null || :
    fixfiles -R pure-ftpd restore || :
    /bin/systemctl condrestart pure-ftpd > /dev/null 2>&1  || :
fi

%postun selinux
if [ "$1" -ge "1" ]; then # Upgrade
    # Replaces the module if it is already loaded
    semodule -i %{_datadir}/selinux/packages/%{name}/pureftpd.pp 2>/dev/null || :
    # no need to restart the daemon
fi


%files
%doc FAQ THANKS AUTHORS HISTORY NEWS
%doc README README.Authentication-Modules README.Configuration-File
%doc README.Donations README.LDAP README.MySQL README.SELinux
%doc README.PGSQL README.TLS README.Virtual-Users
%doc pureftpd.schema
%doc %{_docdir}/%{name}/*.conf
%{_bindir}/pure-*
%{_sbindir}/pure-*
%if 0%{!?_without_tls:1}
%{_unitdir}/pure-ftpd-init.service
%{_unitdir}/pure-ftpd.service
%else
%{_unitdir}/pure-ftpd.service
%endif
%config(noreplace) %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%{!?_without_tls:%{_sysconfdir}/pki/%{name}}
%{_mandir}/man8/*
%dir /var/ftp/


%files selinux
%doc README.SELinux
%{_datadir}/selinux/packages/%{name}/pureftpd.pp


%changelog
* Sat Feb 01 2025 Björn Esser <besser82@fedoraproject.org> - 1.0.51-9
- Add explicit BR: libxcrypt-devel

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.51-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.51-7
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.51-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.51-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.51-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.51-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.51-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Jonathan Wright <jonathan@almalinux.org> - 1.0.51-1
- New version
- Resolves: rhbz#2026153
- Remove usermode dependency and non-root "ftpwho"
- Resolves: rhbz#502754

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.49-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.0.49-11
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.49-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.49-9
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 1.0.49-8
- rebuild for libpq ABI fix rhbz#1908268

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.49-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.49-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 06 2020 Ondřej Lysoněk <olysonek@redhat.com> - 1.0.49-5
- Fix CVE-2020-9365 and CVE-2020-9274
- Resolves: rhbz#1828688
- Resolves: rhbz#1831059

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.49-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Ondřej Lysoněk <olysonek@redhat.com> - 1.0.49-3
- Fix potential stack exhaustion in function listdir (CVE-2019-20176)
- Resolves: rhbz#1795152

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.49-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 03 2019 Ondřej Lysoněk <olysonek@redhat.com> - 1.0.49-1
- New version
- Resolves: rhbz#1695561

* Fri Mar 29 2019 Ondřej Lysoněk <olysonek@redhat.com> - 1.0.48-1
- New version
- Resolves: rhbz#1692539
- Resolves: rhbz#1672494
- Resolves: rhbz#1654838

* Tue Feb 12 2019 Ondřej Lysoněk <olysonek@redhat.com> - 1.0.47-10
- Temporarily disable TLSv1.3 support until it's fully fixed

* Tue Feb 05 2019 Ondřej Lysoněk <olysonek@redhat.com> - 1.0.47-9
- Fixed TLSv1.3 support
- Resolves: rhbz#1654838
- Fixed postgresql authentication

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.47-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.0.47-7
- Rebuilt for libcrypt.so.2 (#1666033)

* Mon Nov 19 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.47-6
- Fix for oversight in previous change

* Sun Nov 18 2018 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.47-5
- Drop sysv legacy bits

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.47-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Ondřej Lysoněk <olysonek@redhat.com> - 1.0.47-3
- Apply upstream patch to increase the size limit of the process's data segment
- https://github.com/jedisct1/pure-ftpd/issues/82
- Resolves: rhbz#1490354

* Mon Feb 19 2018 Ondřej Lysoněk <olysonek@redhat.com> - 1.0.47-2
- Add gcc to BuildRequires

* Tue Feb 13 2018 Ondřej Lysoněk <olysonek@redhat.com> - 1.0.47-1
- New version
- Dropped patch 0003-Allow-having-both-options-and-config-file-on-command.patch
  as it was rejected by upstream
- Complain when invalid or excessive arguments are given on the command line

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.46-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1.0.46-5
- Rebuilt for switch to libxcrypt

* Wed Oct 25 2017 Ondřej Lysoněk <olysonek@redhat.com> - 1.0.46-4
- Depend on mariadb-connector-c-devel instead of mysql-devel
- Resolves: rhbz#1493658

* Wed Oct 25 2017 Ondřej Lysoněk <olysonek@redhat.com> - 1.0.46-3
- Generate the TLS certificate using sscg in an initialization systemd service
- This is required by
- https://fedoraproject.org/wiki/Packaging:Initial_Service_Setup

* Thu Sep 14 2017 Ondřej Lysoněk <olysonek@redhat.com> - 1.0.46-2
- Fix loading the configuration file
- Drop unsupported UseFtpUsers option from configuration file

* Mon Aug 14 2017 Martin Sehnoutka <msehnout@redhat.com> - 1.0.46-1
- Rebase to 1.0.46

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.42-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.42-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.42-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.42-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 23 2015 Robert Scheck <robert@fedoraproject.org> - 1.0.42-3
- Remove executable permission bits from pure-ftpd systemd unit

* Wed Aug 05 2015 Jaromir Capik <jcapik@redhat.com> - 1.0.42-2
- Making mysql/postgresql policies optional (#1249109)

* Mon Jul 27 2015 Jaromir Capik <jcapik@redhat.com> - 1.0.42-1
- Updating to 1.0.42 (#1236253)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Jaromir Capik <jcapik@redhat.com> - 1.0.40-1
- Updating to 1.0.40 (#1231498)

* Mon Jun 01 2015 Jaromir Capik <jcapik@redhat.com> - 1.0.39-1
- Updating to 1.0.39 (#1224479)

* Fri Feb 27 2015 Jaromir Capik <jcapik@redhat.com> - 1.0.37-1
- Updating to 1.0.37

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.36-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.0.36-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 23 2012 Jaromir Capik <jcapik@redhat.com> - 1.0.36-1
- Update to 1.0.36

* Mon Aug 27 2012 Jaromir Capik <jcapik@redhat.com> - 1.0.35-4
- Migration to new systemd scriptlet macros

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 13 2012 Jaromir Capik <jcapik@redhat.com> - 1.0.35-2
- Changing MinUID from 500 to 1000

* Fri Jan 13 2012 Jaromir Capik <jcapik@redhat.com> - 1.0.35-1
- Update to 1.0.35

* Mon Sep 12 2011 Tom Callaway <spot@fedoraproject.org> - 1.0.32-2
- convert to systemd

* Thu May 19 2011 Michal Ingeli <mi@v3.sk> - 1.0.32-1
- version 1.0.32
- security bug fix #704283 by upstream (CVE-2011-0418)

* Sat Mar 26 2011 Michal Ingeli <mi@v3.sk> - 1.0.30-2
- bug fix for mysql passwords #690346
- version 1.0.30
- security bug fix #683221 by upstream

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 1.0.29-4
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Apr 28 2010 Aurelien Bompard <abompard@fedoraproject.org> -  1.0.29-2
- fix bug #586513

* Tue Mar 16 2010 Aurelien Bompard <abompard@fedoraproject.org> -  1.0.29-1
- version 0.1.29

* Fri Dec 04 2009 Aurelien Bompard <abompard@fedoraproject.org> -  1.0.27-1
- version 1.0.27

* Wed Sep 16 2009 Tomas Mraz <tmraz@redhat.com> - 1.0.22-4
- use password-auth common PAM configuration instead of system-auth

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1.0.22-3
- rebuilt with new openssl

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 27 2009 Aurelien Bompard <abompard@fedoraproject.org> 1.0.22-1
- version 1.0.22

* Wed Mar 04 2009 Aurelien Bompard <abompard@fedoraproject.org> 1.0.21-20
- make pam and consolehelper's conf files noreplace

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.21-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 24 2009 Aurelien Bompard <abompard@fedoraproject.org> 1.0.21-18
- Rebuild for mysql

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0.21-17
- Rebuild for Python 2.6

* Thu Jun 05 2008 Aurelien Bompard <abompard@fedoraproject.org> 1.0.21-16
- Rebuild for libcap.so.2 (bug 450086)

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.21-15
- Autorebuild for GCC 4.3

* Thu Dec 06 2007 Release Engineering <rel-eng at fedoraproject dot org> - 1.0.21-14
- Rebuild for deps

* Sun Aug 26 2007 Aurelien Bompard <abompard@fedoraproject.org> 1.0.21-13
- rebuild for BuildID

* Sat Dec 09 2006 Aurelien Bompard <abompard@fedoraproject.org> 1.0.21-12
- rebuild

* Sat Dec 09 2006 Aurelien Bompard <abompard@fedoraproject.org> 1.0.21-11
- rebuild

* Wed Aug 30 2006 Aurelien Bompard <abompard@fedoraproject.org> 1.0.21-9
- rebuild

* Fri Aug 04 2006 Aurelien Bompard <abompard@fedoraproject.org> 1.0.21-8
- BuildRequire selinux-policy-devel for FC6 onwards

* Fri Aug 04 2006 Aurelien Bompard <abompard@fedoraproject.org> 1.0.21-7
- install README.SELinux with perms 644 to avoid depending on the
  buildsys' umask (bug 200844)

* Fri Jun 16 2006 Aurelien Bompard <gauret[AT]free.fr> 1.0.21-6
- add missing m4 BuildRequires

* Sun May 14 2006 Aurelien Bompard <gauret[AT]free.fr> 1.0.21-5
- add missing BuildRequires

* Sun May 14 2006 Aurelien Bompard <gauret[AT]free.fr> 1.0.21-4
- add SELinux support
- prevent the init script from displaying the config on startup

* Sun Apr 09 2006 Aurelien Bompard <gauret[AT]free.fr> 1.0.21-3
- fix mysql socket location (bug 188426)

* Wed Feb 22 2006 Aurelien Bompard <gauret[AT]free.fr> 1.0.21-2
- build option rendezvous has been renamed to bonjour
- add --with-cork
- see bug 182314 for more info, thanks to Jose Pedro Oliveira

* Tue Feb 21 2006 Aurelien Bompard <gauret[AT]free.fr> 1.0.21-1
- version 1.0.21

* Sun Nov 13 2005 Aurelien Bompard <gauret[AT]free.fr> 1.0.20-4
- rebuild
- i18n in init script

* Mon Aug 01 2005 Aurelien Bompard <gauret[AT]free.fr> 1.0.20-3
- build feature-complete by default
- add TLS support
- see bug #162849

* Wed Mar 23 2005 Aurelien Bompard <gauret[AT]free.fr> 1.0.20-2.fc4
- implement Jose's RFE in bug 151337: pure-ftpwho can be run
  by a normal user.
- change release tag for FC4

* Sun Mar 13 2005 Aurelien Bompard <gauret[AT]free.fr> 1.0.20-1
- adapt to Fedora Extras (drop Epoch, change Release tag)

* Wed Feb 16 2005 Aurelien Bompard <gauret[AT]free.fr> 0:1.0.20-0.fdr.9
- license is BSD, not GPL

* Mon Feb 14 2005 Aurelien Bompard <gauret[AT]free.fr> 0:1.0.20-0.fdr.8
- various fixes. See bug 1573 (fedora.us) for more info.

* Fri Feb 11 2005 Aurelien Bompard <gauret[AT]free.fr> 0:1.0.20-0.fdr.7
- fix init script
- require logrotate
- add rebuild switches to lower dependancies
- see bug 1573 (fedora.us) for more info.

* Fri Feb 04 2005 Aurelien Bompard <gauret[AT]free.fr> 0:1.0.20-0.fdr.6
- Add the "UseFtpUsers no" directive in the config file since we don't
  use it anymore

* Wed Feb 02 2005 Aurelien Bompard <gauret[AT]free.fr> 0:1.0.20-0.fdr.5
- various spec file improvements

* Mon Jan 31 2005 Aurelien Bompard <gauret[AT]free.fr> 0:1.0.20-0.fdr.4
- add patch for x86_64 support
- implement wishes in bug 1573 from Jose Pedro Oliveira
- don't use the ftpusers file, and thus remove conflicts with other FTP servers
- rediff config patch

* Tue Nov 02 2004 Aurelien Bompard <gauret[AT]free.fr> 0:1.0.20-0.fdr.3
- add large file support

* Fri Sep 24 2004 Aurelien Bompard <gauret[AT]free.fr> 0:1.0.20-0.fdr.2
- redirect %%preun output to /dev/null
- add requirements to chkconfig for the scriptlets

* Sun Aug 01 2004 Aurelien Bompard <gauret[AT]free.fr> 0:1.0.20-0.fdr.1
- version 1.0.20 (bugfixes)

* Mon Jun 28 2004 Aurelien Bompard <gauret[AT]free.fr> 0:1.0.19-0.fdr.1
- version 1.0.19

* Tue May 04 2004 Aurelien Bompard <gauret[AT]free.fr> 0:1.0.18-0.fdr.1
- version 1.0.18
- spec file cleanups

* Sun Oct 19 2003 Aurelien Bompard <gauret[AT]free.fr> 1.0.16a-1
- Redhatize the Mandrake RPM
- version 1.0.16a
- improve ftpusers creation script

