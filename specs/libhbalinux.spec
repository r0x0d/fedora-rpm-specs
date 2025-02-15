Name:               libhbalinux
Version:            1.0.17
Release:            22%{?dist}
Summary:            FC-HBAAPI implementation using scsi_transport_fc interfaces
License:            LGPL-2.1-only
URL:                http://www.open-fcoe.org
Source0:            %{name}-%{version}.tar.gz
Patch0:             libhbalinux-1.0.13-conf.patch
Patch1:             libhbalinux-fix-non-pci-netdev.patch
BuildRequires:      libhbaapi-devel >= 2.2.9-6
BuildRequires:      libpciaccess-devel libtool automake systemd-devel
BuildRequires: make
Requires:           libhbaapi >= 2.2.9-6
Requires(post):     grep
Requires(postun):   grep

%description
SNIA HBAAPI vendor library built on top of the scsi_transport_fc interfaces.

%package devel
Summary:            A file needed for libhbalinux application development
Requires:           %{name}%{?_isa} = %{version}-%{release}
Requires:           pkgconfig

%description devel
The libhbalinux-devel package contains the library pkgconfig file.

%prep
%autosetup -p1

%build
./bootstrap.sh
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post
/sbin/ldconfig
ORG=org.open-fcoe.libhbalinux
LIB=%{_libdir}/libhbalinux.so.2.0.2
STR="$ORG	$LIB"
CONF=%{_sysconfdir}/hba.conf
if test -f $CONF; then
  grep -E -q ^[[:space:]]*$ORG[[:space:]]+$LIB $CONF
  if test $? -ne 0; then
    echo $STR >> $CONF;
  fi
fi

%postun
/sbin/ldconfig
ORG=org.open-fcoe.libhbalinux
CONF=%{_sysconfdir}/hba.conf
if test -f $CONF; then
  grep -v $ORG $CONF > %{_sysconfdir}/hba.conf.new
  mv %{_sysconfdir}/hba.conf.new %{_sysconfdir}/hba.conf
fi

%files
%doc README COPYING
%{_libdir}/%{name}.so.*

%files devel
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 06 2015 Chris Leech <cleech@redhat.com> - 1.0.17-2
- fix for non-PCI netdevs

* Tue Jun 16 2015 Chris Leech <cleech@redhat.com> - 1.0.17-1
- rebase to upstream v1.0.17

* Tue Oct 07 2014 Chris Leech <cleech@redhat.com> - 1.0.16-5
- sync with upstream, extends portspeed support up to 40 Gbit

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.16-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.16-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jul 26 2013 Petr Šabata <contyk@redhat.com> - 1.0.16-2
- Fix a bogus date in changelog

* Tue Jun 04 2013 Petr Šabata <contyk@redhat.com> - 1.0.16-1
- 1.0.16 bump

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 03 2012 Petr Šabata <contyk@redhat.com> - 1.0.14-4
- Require grep for the post/postun scriptlets (#859397)

* Thu Aug 16 2012 Petr Šabata <contyk@redhat.com> - 1.0.14-3
- Include the unversioned library in the devel subpackage.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 25 2012 Petr Šabata <contyk@redhat.com> - 1.0.14-1
- 1.0.14 bump (really just a version bump, removing the need for
  the previous patch)

* Tue Jan 31 2012 Petr Šabata <contyk@redhat.com> - 1.0.13-3
- Set SerialNumber to "Unknown" if not found (47d8dca41)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 24 2011 Petr Šabata <contyk@redhat.com> - 1.0.13-1
- 1.0.13 bump
- Creating the devel subpackage with a pkgconfig file

* Thu Jul 07 2011 Petr Sabata <contyk@redhat.com> - 1.0.12-1
- 1.0.12 bump
- Remove now obsolete Buildroot and defattr

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May 24 2010 Jan Zeleny <jzeleny@redhat.com> - 1.0.10-1
- rebased to 1.0.10, bugfix release (see git changelog for more info)

* Fri Dec 04 2009 Jan Zeleny <jzeleny@redhat.com> - 1.0.9-20091204git
- rebased to the latest version in upstream git

* Thu Jul 30 2009 Jan Zeleny <jzeleny@redhat.com> - 1.0.8-1
- rebase of libhbalinux, spec file adjusted to match changes

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 01 2009 Jan Zeleny <jzeleny@redhat.com> - 1.0.7-3
- replaced unofficial 1.0.7 source tarball with official one
- update of Makefile, part of it moved to postinstall section
  of spec file

* Tue Mar 31 2009 Jan Zeleny <jzeleny@redhat.com> - 1.0.7-2
- minor changes in spec file

* Mon Mar 2 2009 Chris Leech <christopher.leech@intel.com> - 1.0.7-1
- initial build

