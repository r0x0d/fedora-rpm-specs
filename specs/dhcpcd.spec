%global forgeurl0 https://github.com/NetworkConfiguration/dhcpcd

Name: dhcpcd
Version: 10.0.10
Release: %autorelease
Summary: A minimalistic network configuration daemon with DHCPv4, rdisc and DHCPv6 support
License: BSD-2-Clause AND ISC AND MIT
URL: http://roy.marples.name/projects/%{name}/
# Moved to github
VCS: git:%{forgeurl0}
Source0: %{forgeurl0}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1: %{forgeurl0}/releases/download/v%{version}/%{name}-%{version}.tar.xz.asc
Source2: https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xa785ed2755955d9e93ea59f6597f97ea9ad45549#/roy-marples.name.asc
Source3: %{name}.service
Source4: %{name}@.service
Source5: systemd-sysusers.conf
# Backport to work with the latest glibc getrandom() vDSO
# https://github.com/NetworkConfiguration/dhcpcd/commit/e9e40400003db2e4f12dba85acabbaf2212a520f
Patch: e9e40400003d-allow-the-__NR_rt_sigprocmask-syscall.patch

BuildRequires: gcc
BuildRequires: systemd-rpm-macros
BuildRequires: chrony
BuildRequires: systemd-devel
%if 0%{?fedora}
# Not in RHEL
BuildRequires: ypbind
%endif
BuildRequires: make
%if 0%{?fedora} || 0%{?rhel} > 8
BuildRequires: gnupg2
%endif
%{?systemd_requires}
%description
The dhcpcd package provides a minimalistic network configuration daemon
that supports IPv4 and IPv6 configuration including configuration discovery
through NDP, DHCPv4 and DHCPv6 protocols.

%prep
%if 0%{?fedora} || 0%{?rhel} > 8
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%autosetup -p1

%build
%configure \
    --dbdir=/var/lib/%{name} --runstatedir=%{_rundir}
%make_build

%check
%make_build test

%install
export BINMODE=755
%make_install
find %{buildroot} -name '*.la' -delete -print
install -D -m 644 %{SOURCE3} %{buildroot}%{_unitdir}/%{name}.service
install -D -m 644 %{SOURCE4} %{buildroot}%{_unitdir}/%{name}@.service
install -d %{buildroot}%{_sharedstatedir}/%{_name}

%pre
%sysusers_create_compat %{SOURCE5}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%license LICENSE
%config(noreplace) %{_sysconfdir}/%{name}.conf
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/hooks
%{_datadir}/%{name}/hooks/10-wpa_supplicant
%{_datadir}/%{name}/hooks/15-timezone
%{_datadir}/%{name}/hooks/29-lookup-hostname
%{_datadir}/%{name}/hooks/50-yp.conf
%{_libdir}/%{name}
%{_libexecdir}/%{name}-hooks
%{_libexecdir}/%{name}-run-hooks
%{_mandir}/man5/%{name}.conf.5.gz
%{_mandir}/man8/%{name}-run-hooks.8.gz
%{_mandir}/man8/%{name}.8.gz
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}@.service
%defattr(0644,root,dhcpcd,0755)
%{_sharedstatedir}/%{name}

%changelog
%autochangelog
