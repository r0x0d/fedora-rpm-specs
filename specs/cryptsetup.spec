Summary: Utility for setting up encrypted disks
Name: cryptsetup
Version: 2.7.5
Release: 2%{?dist}
License: GPL-2.0-or-later WITH cryptsetup-OpenSSL-exception AND LGPL-2.1-or-later WITH cryptsetup-OpenSSL-exception
URL: https://gitlab.com/cryptsetup/cryptsetup
BuildRequires: autoconf, automake, libtool, gettext-devel,
BuildRequires: openssl-devel, popt-devel, device-mapper-devel
BuildRequires: libuuid-devel, gcc, json-c-devel
BuildRequires: libpwquality-devel, libblkid-devel
BuildRequires: make libssh-devel
BuildRequires: asciidoctor
Requires: cryptsetup-libs = %{version}-%{release}
Requires: libpwquality >= 1.2.0
Obsoletes: %{name}-reencrypt <= %{version}
Provides: %{name}-reencrypt = %{version}

%global upstream_version %{version_no_tilde}
Source0: https://www.kernel.org/pub/linux/utils/cryptsetup/v2.7/cryptsetup-%{upstream_version}.tar.xz

%description
The cryptsetup package contains a utility for setting up
disk encryption using dm-crypt kernel module.

%package devel
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Summary: Headers and libraries for using encrypted file systems

%description devel
The cryptsetup-devel package contains libraries and header files
used for writing code that makes use of disk encryption.

%package libs
Summary: Cryptsetup shared library

%description libs
This package contains the cryptsetup shared library, libcryptsetup.

%package ssh-token
Summary: Cryptsetup LUKS2 SSH token
Requires: cryptsetup-libs = %{version}-%{release}

%description ssh-token
This package contains the LUKS2 SSH token.

%package -n veritysetup
Summary: A utility for setting up dm-verity volumes
Requires: cryptsetup-libs = %{version}-%{release}

%description -n veritysetup
The veritysetup package contains a utility for setting up
disk verification using dm-verity kernel module.

%package -n integritysetup
Summary: A utility for setting up dm-integrity volumes
Requires: cryptsetup-libs = %{version}-%{release}

%description -n integritysetup
The integritysetup package contains a utility for setting up
disk integrity protection using dm-integrity kernel module.

%prep
%autosetup -n cryptsetup-%{upstream_version} -p 1

%build
# force regeneration of manual pages from AsciiDoc
rm -f man/*.8

./autogen.sh
%configure --enable-fips --enable-pwquality --enable-asciidoc --enable-internal-sse-argon2
%make_build

%install
%make_install
rm -rf %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_libdir}/%{name}/*.la

%find_lang cryptsetup

%ldconfig_scriptlets -n cryptsetup-libs

%files
%license COPYING
%doc AUTHORS FAQ.md docs/*ReleaseNotes
%{_mandir}/man8/cryptsetup.8.gz
%{_mandir}/man8/cryptsetup-*.8.gz
%{_sbindir}/cryptsetup

%files -n veritysetup
%license COPYING
%{_mandir}/man8/veritysetup.8.gz
%{_sbindir}/veritysetup

%files -n integritysetup
%license COPYING
%{_mandir}/man8/integritysetup.8.gz
%{_sbindir}/integritysetup

%files devel
%doc docs/examples/*
%{_includedir}/libcryptsetup.h
%{_libdir}/libcryptsetup.so
%{_libdir}/pkgconfig/libcryptsetup.pc

%files libs -f cryptsetup.lang
%license COPYING COPYING.LGPL
%{_libdir}/libcryptsetup.so.*
%dir %{_libdir}/%{name}/
%{_tmpfilesdir}/cryptsetup.conf
%ghost %attr(700, -, -) %dir /run/cryptsetup

%files ssh-token
%license COPYING COPYING.LGPL
%{_libdir}/%{name}/libcryptsetup-token-ssh.so
%{_mandir}/man8/cryptsetup-ssh.8.gz
%{_sbindir}/cryptsetup-ssh

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Sep 03 2024 Ondrej Kozina <okozina@redhat.com> - 2.7.5-1
- Update to cryptsetup 2.7.5.

* Tue Jul 30 2024 Ondrej Kozina <okozina@redhat.com> - 2.7.4-1
- Update to cryptsetup 2.7.4.

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Ondrej Kozina <okozina@redhat.com> - 2.7.3-1
- Update to cryptsetup 2.7.3.

* Tue Apr 09 2024 Ondrej Kozina <okozina@redhat.com> - 2.7.2-1
- Update to cryptsetup 2.7.2.

* Thu Mar 07 2024 Ondrej Kozina <okozina@redhat.com> - 2.7.1-1
- Update to cryptsetup 2.7.1.

* Fri Feb 09 2024 Ondrej Kozina <okozina@redhat.com> - 2.7.0-2
- Rebuild for OpenSSL Argon2 implementation (OpenSSL 3.2)
- patch: Do not compile unused internal argon2 implementation

* Wed Jan 24 2024 Ondrej Kozina <okozina@redhat.com> - 2.7.0-1
- Update to cryptsetup 2.7.0.

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0~rc1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0~rc1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 20 2023 Milan Broz <gmazyland@gmail.com> - 2.7.0~rc1-1
- Update to cryptsetup 2.7.0-rc1.

* Wed Nov 29 2023 Ondrej Kozina <okozina@redhat.com> - 2.7.0~rc0-1
- Update to cryptsetup 2.7.0-rc0.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 2.6.1-2
- Drop libargon2 dependency in RHEL builds

* Fri Feb 10 2023 Ondrej Kozina <okozina@redhat.com> - 2.6.1-1
- Update to cryptsetup 2.6.1.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Nov 28 2022 Ondrej Kozina <okozina@redhat.com> - 2.6.0-1
- Update to cryptsetup 2.6.0.

* Mon Nov 21 2022 Ondrej Kozina <okozina@redhat.com> - 2.6.0~rc0-1
- Update to cryptsetup 2.6.0-rc0.

* Thu Jul 28 2022 Ondrej Kozina <okozina@redhat.com> - 2.5.0-1
- Update to cryptsetup 2.5.0.

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0~rc1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jul 14 2022 Ondrej Kozina <okozina@redhat.com> - 2.5.0~rc1-1
- Update to cryptsetup 2.5.0-rc1.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jan 12 2022 Ondrej Kozina <okozina@redhat.com> - 2.4.3-1
- Update to cryptsetup 2.4.3.

* Thu Nov 18 2021 Milan Broz <gmazyland@gmail.com> - 2.4.2-1
- Update to cryptsetup 2.4.2.

* Fri Sep 17 2021 Ondrej Kozina <okozina@redhat.com> - 2.4.1-1
- Update to cryptsetup 2.4.1.

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2.4.0-2
- Rebuilt with OpenSSL 3.0.0

* Wed Aug 18 2021 Ondrej Kozina <okozina@redhat.com> - 2.4.0-1
- Update to cryptsetup 2.4.0.

* Fri Jul 30 2021 Milan Broz <gmazyland@gmail.com> - 2.4.0~rc1-1
- Update to cryptsetup 2.4.0-rc1.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.4.0~rc0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Björn Esser <besser82@fedoraproject.org> - 2.4.0~rc0-2
- Rebuild for versioned symbols in json-c

* Fri Jul 02 2021 Ondrej Kozina <okozina@redhat.com> - 2.4.0~rc0-1
- Update to cryptsetup 2.4.0-rc0.
- add experimental cryptsetup-ssh token subpackage
- spec file cleanup

* Fri May 28 2021 Milan Broz <gmazyland@gmail.com> - 2.3.6-1
- Update to cryptsetup 2.3.6.

* Thu Mar 11 2021 Milan Broz <gmazyland@gmail.com> - 2.3.5-2
- Update to cryptsetup 2.3.5.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Sep 03 2020 Milan Broz <gmazyland@gmail.com> - 2.3.4-1
- Update to cryptsetup 2.3.4.
- Fix for CVE-2020-14382 (#1874712)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Ondrej Kozina <okozina@redhat.com> - 2.3.3-1
- Update to cryptsetup 2.3.3.

* Thu Apr 30 2020 Milan Broz <gmazyland@gmail.com> - 2.3.2-1
- Update to cryptsetup 2.3.2.

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 2.3.1-4
- Rebuild (json-c)

* Thu Apr 16 2020 Milan Broz <gmazyland@gmail.com> - 2.3.1-3
- Fix broken json-c patch (#1824878).

* Tue Apr 14 2020 Björn Esser <besser82@fedoraproject.org> - 2.3.1-2
- Add support for upcoming json-c 0.14.0
- Use %%make_build, %%make_install and %%autosetup macros

* Thu Mar 12 2020 Ondrej Kozina <okozina@redhat.com> - 2.3.1-1
- Update to cryptsetup 2.3.1.

* Sun Feb 02 2020 Milan Broz <gmazyland@gmail.com> - 2.3.0-1
- Update to cryptsetup 2.3.0.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 12 2020 Milan Broz <gmazyland@gmail.com> - 2.3.0-0.1
- Update to cryptsetup 2.3.0-rc0.

* Fri Nov 01 2019 Ondrej Kozina <okozina@redhat.com> - 2.2.2-1
- Update to cryptsetup 2.2.2.

* Fri Sep 06 2019 Ondrej Kozina <okozina@redhat.com> - 2.2.1-1
- Update to cryptsetup 2.2.1.

* Thu Aug 15 2019 Milan Broz <gmazyland@gmail.com> - 2.2.0-1
- Update to cryptsetup 2.2.0.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jun 14 2019 Ondrej Kozina <okozina@redhat.com> - 2.2.0-0.2
- Update to cryptsetup 2.2.0-rc1.

* Fri May 03 2019 Ondrej Kozina <okozina@redhat.com> - 2.2.0-0.1
- Update to cryptsetup 2.2.0-rc0.

* Thu Apr 04 2019 Kalev Lember <klember@redhat.com> - 2.1.0-3
- Add back python2-cryptsetup and cryptsetup-python3 obsoletes

* Mon Mar 18 2019 Milan Broz <gmazyland@gmail.com> - 2.1.0-2
- Rebuild for new libargon2 soname.

* Fri Feb 08 2019 Ondrej Kozina <okozina@redhat.com> - 2.1.0-1
- Update to cryptsetup 2.1.0.
- Drop python specific bits from spec file (python was removed
  from upstream project)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 22 2019 Ondrej Kozina <okozina@redhat.com> - 2.0.6-2
- Switch default metadata format to LUKS2.
- Resolves: #1668013

* Mon Dec 03 2018 Ondrej Kozina <okozina@redhat.com> - 2.0.6-1
- Update to cryptsetup 2.0.6.

* Mon Oct 29 2018 Ondrej Kozina <okozina@redhat.com> - 2.0.5-1
- Update to cryptsetup 2.0.5.

* Fri Aug 03 2018 Ondrej Kozina <okozina@redhat.com> - 2.0.4-1
- Update to cryptsetup 2.0.4.
- patch: Add Fedora system library paths in configure.

* Tue Jul 17 2018 Ondrej Kozina <okozina@redhat.com> - 2.0.3-6
- Remove libgcrypt dependency from cryptsetup-libs package.

* Tue Jul 17 2018 Ondrej Kozina <okozina@redhat.com> - 2.0.3-5
- Replace sed script with --disable-rpath configure option.
- Switch cryptsetup to openssl crypto backend.
- Spec file cleanup.

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 04 2018 Ondrej Kozina <okozina@redhat.com> - 2.0.3-3
- Fix obsolete macro for python3 subpackage.

* Fri May 04 2018 Ondrej Kozina <okozina@redhat.com> - 2.0.3-2
- Add missing 'Obsoletes' macros for python subpackages.

* Fri May 04 2018 Milan Broz <gmazyland@gmail.com> - 2.0.3-1
- Update to cryptsetup 2.0.3.

* Wed Apr 25 2018 Ondrej Kozina <okozina@redhat.com> - 2.0.2-3
- Add conditions for python sub-packages

* Tue Mar 27 2018 Björn Esser <besser82@fedoraproject.org> - 2.0.2-2
- Rebuilt for libjson-c.so.4 (json-c v0.13.1) on fc28

* Wed Mar 07 2018 Milan Broz <gmazyland@gmail.com> - 2.0.2-1
- Update to cryptsetup 2.0.2.

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 2.0.1-3
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 21 2018 Milan Broz <gmazyland@gmail.com> - 2.0.1-1
- Update to cryptsetup 2.0.1.

* Thu Jan 04 2018 Ondrej Kozina <okozina@redhat.com> - 2.0.0-3
- Override locking path to /run/cryptsetup (going to be new default)
- Claim ownership of the locking directory

* Fri Dec 15 2017 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.0-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Tue Dec 12 2017 Ondrej Kozina <okozina@redhat.com> - 2.0.0-1
- Update to cryptsetup 2.0.0 (final).

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 2.0.0-0.6
- Rebuilt for libjson-c.so.3

* Mon Nov 20 2017 Milan Broz <gmazyland@gmail.com> - 2.0.0-0.5
- Link to system libargon2 instead of using bundled code.

* Thu Nov 09 2017 Ondrej Kozina <okozina@redhat.com> - 2.0.0-0.4
- Drop the legacy library.

* Wed Nov 08 2017 Ondrej Kozina <okozina@redhat.com> - 2.0.0-0.3
- Temporary build providing legacy library.

* Tue Nov 07 2017 Ondrej Kozina <okozina@redhat.com> - 2.0.0-0.2
- Update to cryptsetup 2.0.0-rc1 (with libcryptsetup soname bump).
- Added integritysetup subpackage.

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.7.5-5
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.7.5-4
- Python 2 binary package renamed to python2-cryptsetup
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Apr 27 2017 Milan Broz <gmazyland@gmail.com> - 1.7.5-1
- Update to cryptsetup 1.7.5.

* Wed Mar 15 2017 Milan Broz <gmazyland@gmail.com> - 1.7.4-1
- Update to cryptsetup 1.7.4.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.7.3-2
- Rebuild for Python 3.6

* Sun Oct 30 2016 Milan Broz <gmazyland@gmail.com> - 1.7.3-1
- Update to cryptsetup 1.7.3.

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.2-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jun 13 2016 Milan Broz <gmazyland@gmail.com> - 1.7.2-2
- Rebuilt for compatible symbol changes in glibc.

* Sat Jun 04 2016 Milan Broz <gmazyland@gmail.com> - 1.7.2-1
- Update to cryptsetup 1.7.2.

* Sun Feb 28 2016 Milan Broz <gmazyland@gmail.com> - 1.7.1-1
- Update to cryptsetup 1.7.1.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Nov 03 2015 Milan Broz <gmazyland@gmail.com> - 1.7.0-1
- Update to cryptsetup 1.7.0.
- Switch to sha256 as default hash.
- Increase default PBKDF2 iteration time to 2 seconds.

* Tue Sep 08 2015 Milan Broz <gmazyland@gmail.com> - 1.6.8-2
- Update to cryptsetup 1.6.8.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 23 2015 Milan Broz <gmazyland@gmail.com> - 1.6.7-1
- Update to cryptsetup 1.6.7.
- Remove no longer needed fipscheck library dependence.
- Change URL to new homepage.

* Sat Aug 16 2014 Milan Broz <gmazyland@gmail.com> - 1.6.6-1
- Update to cryptsetup 1.6.6.

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jul 11 2014 Tom Callaway <spot@fedoraproject.org> - 1.6.5-2
- fix license handling

* Sun Jun 29 2014 Milan Broz <gmazyland@gmail.com> - 1.6.5-1
- Update to cryptsetup 1.6.5.
- Add cryptsetup-python3 subpackage.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Mar 02 2014 Milan Broz <gmazyland@gmail.com> - 1.6.4-2
- Require libgcrypt 1.6.1 (with fixed PBKDF2 and Whirlpool hash).

* Thu Feb 27 2014 Milan Broz <gmazyland@gmail.com> - 1.6.4-1
- Update to cryptsetup 1.6.4.

* Tue Jan 07 2014 Ondrej Kozina <okozina@redhat.com> - 1.6.3-2
- remove useless hmac checksum

* Fri Dec 13 2013 Milan Broz <gmazyland@gmail.com> - 1.6.3-1
- Update to cryptsetup 1.6.3.

* Sun Aug 04 2013 Milan Broz <gmazyland@gmail.com> - 1.6.2-1
- Update to cryptsetup 1.6.2.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 31 2013 Milan Broz <gmazyland@gmail.com> - 1.6.1-1
- Update to cryptsetup 1.6.1.
- Install ReleaseNotes files instead of empty Changelog file.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jan 14 2013 Milan Broz <mbroz@redhat.com> - 1.6.0-1
- Update to cryptsetup 1.6.0.
- Change default LUKS encryption mode to aes-xts-plain64 (AES128).
- Force use of gcrypt PBKDF2 instead of internal implementation.

* Sat Dec 29 2012 Milan Broz <mbroz@redhat.com> - 1.6.0-0.1
- Update to cryptsetup 1.6.0-rc1.
- Relax license to GPLv2+ according to new release.
- Compile cryptsetup with libpwquality support.

* Tue Oct 16 2012 Milan Broz <mbroz@redhat.com> - 1.5.1-1
- Update to cryptsetup 1.5.1.

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Milan Broz <mbroz@redhat.com> - 1.5.0-1
- Update to cryptsetup 1.5.0.

* Wed Jun 20 2012 Milan Broz <mbroz@redhat.com> - 1.5.0-0.2
- Update to cryptsetup 1.5.0-rc2.
- Add cryptsetup-reencrypt subpackage.

* Mon Jun 11 2012 Milan Broz <mbroz@redhat.com> - 1.5.0-0.1
- Update to cryptsetup 1.5.0-rc1.
- Add veritysetup subpackage.
- Move localization files to libs subpackage.

* Thu May 31 2012 Milan Broz <mbroz@redhat.com> - 1.4.3-2
- Build with fipscheck (verification in fips mode).
- Clean up spec file, use install to /usr.

* Thu May 31 2012 Milan Broz <mbroz@redhat.com> - 1.4.3-1
- Update to cryptsetup 1.4.3.

* Thu Apr 12 2012 Milan Broz <mbroz@redhat.com> - 1.4.2-1
- Update to cryptsetup 1.4.2.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 09 2011 Milan Broz <mbroz@redhat.com> - 1.4.1-1
- Update to cryptsetup 1.4.1.
- Add Python cryptsetup bindings.
- Obsolete separate python-cryptsetup package.

* Wed Oct 26 2011 Milan Broz <mbroz@redhat.com> - 1.4.0-1
- Update to cryptsetup 1.4.0.

* Mon Oct 10 2011 Milan Broz <mbroz@redhat.com> - 1.4.0-0.1
- Update to cryptsetup 1.4.0-rc1.
- Rename package back from cryptsetup-luks to cryptsetup.

* Wed Jun 22 2011 Milan Broz <mbroz@redhat.com> - 1.3.1-2
- Fix return code for status command when device doesn't exist.

* Tue May 24 2011 Milan Broz <mbroz@redhat.com> - 1.3.1-1
- Update to cryptsetup 1.3.1.

* Tue Apr 05 2011 Milan Broz <mbroz@redhat.com> - 1.3.0-1
- Update to cryptsetup 1.3.0.

* Tue Mar 22 2011 Milan Broz <mbroz@redhat.com> - 1.3.0-0.2
- Update to cryptsetup 1.3.0-rc2

* Mon Mar 14 2011 Milan Broz <mbroz@redhat.com> - 1.3.0-0.1
- Update to cryptsetup 1.3.0-rc1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Milan Broz <mbroz@redhat.com> - 1.2.0-1
- Update to cryptsetup 1.2.0

* Thu Nov 25 2010 Milan Broz <mbroz@redhat.com> - 1.2.0-0.2
- Fix crypt_activate_by_keyfile() to work with PLAIN devices.

* Tue Nov 16 2010 Milan Broz <mbroz@redhat.com> - 1.2.0-0.1
- Add FAQ to documentation.
- Update to cryptsetup 1.2.0-rc1

* Sat Jul 03 2010 Milan Broz <mbroz@redhat.com> - 1.1.3-1
- Update to cryptsetup 1.1.3

* Mon Jun 07 2010 Milan Broz <mbroz@redhat.com> - 1.1.2-2
- Fix alignment ioctl use.
- Fix API activation calls to handle NULL device name.

* Sun May 30 2010 Milan Broz <mbroz@redhat.com> - 1.1.2-1
- Update to cryptsetup 1.1.2
- Fix luksOpen handling of new line char on stdin.

* Sun May 23 2010 Milan Broz <mbroz@redhat.com> - 1.1.1-1
- Update to cryptsetup 1.1.1
- Fix luksClose for stacked LUKS/LVM devices.

* Mon May 03 2010 Milan Broz <mbroz@redhat.com> - 1.1.1-0.2
- Update to cryptsetup 1.1.1-rc2.

* Sat May 01 2010 Milan Broz <mbroz@redhat.com> - 1.1.1-0.1
- Update to cryptsetup 1.1.1-rc1.

* Sun Jan 17 2010 Milan Broz <mbroz@redhat.com> - 1.1.0-1
- Update to cryptsetup 1.1.0.

* Fri Jan 15 2010 Milan Broz <mbroz@redhat.com> - 1.1.0-0.6
- Fix gcrypt initialisation.
- Fix backward compatibility for hash algorithm (uppercase).

* Wed Dec 30 2009 Milan Broz <mbroz@redhat.com> - 1.1.0-0.5
- Update to cryptsetup 1.1.0-rc4

* Mon Nov 16 2009 Milan Broz <mbroz@redhat.com> - 1.1.0-0.4
- Update to cryptsetup 1.1.0-rc3

* Thu Oct 01 2009 Milan Broz <mbroz@redhat.com> - 1.1.0-0.3
- Update to cryptsetup 1.1.0-rc2
- Fix libcryptsetup to properly export only versioned symbols.

* Tue Sep 29 2009 Milan Broz <mbroz@redhat.com> - 1.1.0-0.2
- Update to cryptsetup 1.1.0-rc1
- Add luksHeaderBackup and luksHeaderRestore commands.

* Fri Sep 11 2009 Milan Broz <mbroz@redhat.com> - 1.1.0-0.1
- Update to new upstream testing version with new API interface.
- Add luksSuspend and luksResume commands.
- Introduce pkgconfig.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Milan Broz <mbroz@redhat.com> - 1.0.7-1
- Update to upstream final release.
- Split libs subpackage.
- Remove rpath setting from cryptsetup binary.

* Wed Jul 15 2009 Till Maas <opensource@till.name> - 1.0.7-0.2
- update BR because of libuuid splitout from e2fsprogs

* Mon Jun 22 2009 Milan Broz <mbroz@redhat.com> - 1.0.7-0.1
- Update to new upstream 1.0.7-rc1.

- Wipe old fs headers to not confuse blkid (#468062)
* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 30 2008 Milan Broz <mbroz@redhat.com> - 1.0.6-6
- Wipe old fs headers to not confuse blkid (#468062)

* Tue Sep 23 2008 Milan Broz <mbroz@redhat.com> - 1.0.6-5
- Change new project home page.
- Print more descriptive messages for initialization errors.
- Refresh patches to versions commited upstream.

* Sat Sep 06 2008 Milan Broz <mbroz@redhat.com> - 1.0.6-4
- Fix close of zero decriptor.
- Fix udevsettle delays - use temporary crypt device remapping.

* Wed May 28 2008 Till Maas <opensource till name> - 1.0.6-3
- remove a duplicate sentence from the manpage (RH #448705)
- add patch metadata about upstream status

* Tue Apr 15 2008 Bill Nottinghm <notting@redhat.com> - 1.0.6-2
- Add the device to the luksOpen prompt (#433406)
- Use iconv, not recode (#442574)

* Thu Mar 13 2008 Till Maas <opensource till name> - 1.0.6-1
- Update to latest version
- remove patches that have been merged upstream

* Mon Mar 03 2008 Till Maas <opensource till name> - 1.0.6-0.1.pre2
- Update to new version with several bugfixes
- remove patches that have been merged upstream
- add patch from cryptsetup newsgroup
- fix typo / missing luksRemoveKey in manpage (patch)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.0.5-9
- Autorebuild for GCC 4.3

* Sat Jan 19 2008 Peter Jones <pjones@redhat.com> - 1.0.5-8
- Rebuild for broken deps.

* Thu Aug 30 2007 Till Maas <opensource till name> - 1.0.5-7
- update URL
- update license tag
- recode ChangeLog from latin1 to uf8
- add smp_mflags to make

* Fri Aug 24 2007 Till Maas <opensource till name> - 1.0.5-6
- cleanup BuildRequires:
- removed versions, packages in Fedora are new enough
- changed popt to popt-devel

* Thu Aug 23 2007 Till Maas <opensource till name> - 1.0.5-5
- fix devel subpackage requires
- remove empty NEWS README
- remove uneeded INSTALL
- remove uneeded ldconfig requires
- add readonly detection patch

* Wed Aug 08 2007 Till Maas <opensource till name> - 1.0.5-4
- disable patch2, libsepol is now detected by configure
- move libcryptsetup.so to %%{_libdir} instead of /%%{_lib}

* Fri Jul 27 2007 Till Maas <opensource till name> - 1.0.5-3
- Use /%%{_lib} instead of /lib to use /lib64 on 64bit archs

* Thu Jul 26 2007 Till Maas <opensource till name> - 1.0.5-2
- Use /lib as libdir (#243228)
- sync header and library (#215349)
- do not use %%makeinstall (recommended by PackageGuidelines)
- select sbindir with %%configure instead with make
- add TODO

* Wed Jun 13 2007 Jeremy Katz <katzj@redhat.com> - 1.0.5-1
- update to 1.0.5

* Mon Jun 04 2007 Peter Jones <pjones@redhat.com> - 1.0.3-5
- Don't build static any more.

* Mon Feb 05 2007 Alasdair Kergon <agk@redhat.com> - 1.0.3-4
- Add build dependency on new device-mapper-devel package.
- Add preun and post ldconfig requirements.
- Update BuildRoot.

* Wed Nov  1 2006 Peter Jones <pjones@redhat.com> - 1.0.3-3
- Require newer libselinux (#213414)

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1.0.3-2.1
- rebuild

* Wed Jun  7 2006 Jeremy Katz <katzj@redhat.com> - 1.0.3-2
- put shared libs in the right subpackages

* Fri Apr  7 2006 Bill Nottingham <notting@redhat.com> 1.0.3-1
- update to final 1.0.3

* Mon Feb 27 2006 Bill Nottingham <notting@redhat.com> 1.0.3-0.rc2
- update to 1.0.3rc2, fixes bug with HAL & encrypted devices (#182658)

* Wed Feb 22 2006 Bill Nottingham <notting@redhat.com> 1.0.3-0.rc1
- update to 1.0.3rc1, reverts changes to default encryption type

* Tue Feb 21 2006 Bill Nottingham <notting@redhat.com> 1.0.2-1
- update to 1.0.2, fix incompatiblity with old cryptsetup (#176726)

* Mon Feb 20 2006 Karsten Hopp <karsten@redhat.de> 1.0.1-5
- BuildRequires: libselinux-devel

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.0.1-4.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.0.1-4.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Dec  5 2005 Bill Nottingham <notting@redhat.com> 1.0.1-4
- rebuild against new libdevmapper

* Thu Oct 13 2005 Florian La Roche <laroche@redhat.com>
- add -lsepol to rebuild on current fc5

* Mon Aug 22 2005 Karel Zak <kzak@redhat.com> 1.0.1-2
- fix cryptsetup help for isLuks action

* Fri Jul  1 2005 Bill Nottingham <notting@redhat.com> 1.0.1-1
- update to 1.0.1 - fixes incompatiblity with previous cryptsetup for
  piped passwords

* Thu Jun 16 2005 Bill Nottingham <notting@redhat.com> 1.0-2
- add patch for 32/64 bit compatibility (#160445, <redhat@paukstadt.de>)

* Tue Mar 29 2005 Bill Nottingham <notting@redhat.com> 1.0-1
- update to 1.0

* Thu Mar 10 2005 Bill Nottingham <notting@redhat.com> 0.993-1
- switch to cryptsetup-luks, for LUKS support

* Tue Oct 12 2004 Bill Nottingham <notting@redhat.com> 0.1-4
- oops, make that *everything* static (#129926)

* Tue Aug 31 2004 Bill Nottingham <notting@redhat.com> 0.1-3
- link some things static, move to /sbin (#129926)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Apr 16 2004 Bill Nottingham <notting@redhat.com> 0.1-1
- initial packaging
