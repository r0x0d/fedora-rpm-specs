Name:           paperkey
Version:        1.6
Release:        16%{?dist}
Summary:        An OpenPGP key archiver

License:        GPL-2.0-or-later
URL:            https://www.jabberwocky.com/software/paperkey/
Source0:        https://www.jabberwocky.com/software/%{name}/%{name}-%{version}.tar.gz
Source1:        https://www.jabberwocky.com/software/%{name}/%{name}-%{version}.tar.gz.sig
Source2:        gpgkey-DB698D7199242560.asc

BuildRequires:  coreutils
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  grep
BuildRequires:  make

%description
A reasonable way to achieve a long term backup of OpenPGP (PGP, GnuPG,
etc) keys is to print them out on paper.  Paper and ink have amazingly
long retention qualities - far longer than the magnetic or optical
means that are generally used to back up computer data.  A paper
backup isn't a replacement for the usual machine readable (tape, CD-R,
DVD-R, etc) backups, but rather as an if-all-else-fails method of
restoring a key.

%prep
%gpgverify -d0 -s1 -k2
%autosetup -p1


%build
%configure
%make_build


%install
%make_install


%check
%make_build check


%files
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 01 2022 Todd Zullinger <tmz@pobox.com> - 1.6-10
- convert license to SPDX

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 30 2020 Todd Zullinger <tmz@pobox.com> - 1.6-5
- add make to BuildRequires
- use https for package URL and sources
- miscellaneous spec file cleanups and improvements

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Todd Zullinger <tmz@pobox.com> - 1.6-1
- Update to 1.6
- Run self-tests
- Remove obsolete buildroot cleanup from %%install

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 Todd Zullinger <tmz@pobox.com> - 1.5-3
- Update BuildRequires
- Use %%make_build and %%make_install macros

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 07 2018 Todd Zullinger <tmz@pobox.com> - 1.5-1
- Update to 1.5
- Remove EL-5 conditionals

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Sep 07 2016 Fabio Alessandro Locati <fale@redhat.com> - 1.4-1
- Update to 1.4

* Sun Aug 28 2016 Todd Zullinger <tmz@pobox.com> - 1.3-3
- Check upstream GPG signature in %%prep

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Dec 31 2015 Todd Zullinger <tmz@pobox.com> - 1.3-1
- Update to 1.3
- Use %%license for COPYING file

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 10 2009 Todd Zullinger <tmz@pobox.com> - 1.1-1
- Update to 1.1
- Replace $RPM_BUILD_ROOT with %%{buildroot}

* Tue Feb 12 2008 Todd Zullinger <tmz@pobox.com> - 0.8-1
- update to 0.8
- update %%description from upstream spec file

* Sun Oct 14 2007 Todd Zullinger <tmz@pobox.com> - 0.7-1
- update to 0.7

* Mon Sep 24 2007 Todd Zullinger <tmz@pobox.com> - 0.6-1
- initial package
