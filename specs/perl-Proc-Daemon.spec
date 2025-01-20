# Fedora spec file for perl-Proc-Daemon
#
# Copyright (c) 2006-2016 Remi Collet
# License: CC-BY-SA
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#
%global perlname Proc-Daemon

Name:      perl-Proc-Daemon
Version:   0.23
Release:   29%{?dist}
Summary:   Run Perl program as a daemon process 

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:   GPL-1.0-or-later OR Artistic-1.0-Perl
URL:       https://metacpan.org/release/Proc-Daemon
Source:    https://cpan.metacpan.org/authors/id/A/AK/AKREAL/%{perlname}-%{version}.tar.gz

BuildArch: noarch
# build requirements
BuildRequires: coreutils
BuildRequires: make
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires: perl(warnings)
BuildRequires: sed
# runtime requirements
BuildRequires: perl(POSIX)
BuildRequires: perl(Proc::ProcessTable)
# test requirements
BuildRequires: perl(Cwd)
BuildRequires: perl(Test::More)
Requires:  perl(Proc::ProcessTable)

%{?perl_default_filter}


%description
This is version %{version} of Proc::Daemon

This module contains the routine Init which can be called by a Perl 
program to initialize itself as a daemon. A daemon is a process that
runs in the background with no controlling terminal. Generally servers
(like FTP and HTTP servers) run as daemon processes.


%prep
%setup -q -n %{perlname}-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}


%install
%{make_install}
%{_fixperms} %{buildroot}/*


%check
%{make_build} test


%files
%doc Changes README.md
%{_mandir}/man3/Proc*
%{perl_vendorlib}/Proc


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 06 2024 Miroslav Suchý <msuchy@redhat.com> - 0.23-28
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-21
- Perl 5.36 rebuild

* Wed Mar 09 2022 Emmanuel Seyman <emmanuel@seyman.fr> - 0.23-20
- Replace %%{__perl} with /usr/bin/perl
- Use %%{make_build} and %%{make_install} where appropriate
- Pass NO_PACKLIST and NO_PERLLOCAL to Makefile.PL
- Update and order dependencies
- No longer convert Changes to UTF-8

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-17
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-14
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-11
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-8
- Perl 5.28 rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.23-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan  7 2016 Remi Collet <remi@fedoraproject.org> - 0.23-1
- update to 0.22 (test suite only)

* Thu Oct 29 2015 Remi Collet <remi@fedoraproject.org> - 0.22-1
- update to 0.22 (test suite only)

* Fri Aug  7 2015 Remi Collet <remi@fedoraproject.org> - 0.21-1
- update to 0.21 (test suite only)

* Sat Jun 27 2015 Remi Collet <remi@fedoraproject.org> - 0.20-1
- update to 0.20 (test suite only)
- enable the test suite

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.19-3
- Perl 5.22 rebuild

* Fri Apr  3 2015 Remi Collet <remi@fedoraproject.org> - 0.19-2
- ignore test results for now as not reliable
  https://rt.cpan.org/Public/Bug/Display.html?id=103130

* Sun Mar 22 2015 Remi Collet <remi@fedoraproject.org> - 0.19-1
- update to 0.19
  http://cpansearch.perl.org/src/AKREAL/Proc-Daemon-0.19/Changes

* Tue Feb  3 2015 Remi Collet <remi@fedoraproject.org> - 0.18-1
- update to 0.18
  http://cpansearch.perl.org/src/AKREAL/Proc-Daemon-0.18/Changes

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.14-11
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Dec 18 2013 Remi Collet <remi@fedoraproject.org> 0.14-9
- fix pidfile with mode 666, patch from debian, CVE-2013-7135

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.14-7
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.14-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.14-2
- Perl mass rebuild

* Sat Jun 11 2011 Remi Collet <Fedora@famillecollet.com> 0.14-1
- update to 0.14
  http://cpansearch.perl.org/src/DETI/Proc-Daemon-0.14/Changes

* Wed Jun 01 2011 Remi Collet <Fedora@famillecollet.com> 0.13-1
- update to 0.13

* Mon May 30 2011 Remi Collet <Fedora@famillecollet.com> 0.12-1
- update to 0.12 (bugfix)
- fix wrong-file-end-of-line-encoding and file-not-utf8

* Mon Apr 11 2011 Remi Collet <Fedora@famillecollet.com> 0.10-1
- update to 0.10

* Sat Mar 19 2011 Remi Collet <Fedora@famillecollet.com> 0.09-1
- update to 0.09

* Sat Feb 19 2011 Remi Collet <Fedora@famillecollet.com> 0.07-1
- update to 0.07 (bugfix)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.06-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 19 2011 Remi Collet <Fedora@famillecollet.com> 0.06-1
- update to 0.06

* Fri Oct 29 2010 Remi Collet <Fedora@famillecollet.com> 0.05-1
- update to 0.05
- add BR: perl(Proc::ProcessTable) and BR: perl(Test::More)

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.03-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.03-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.03-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.03-2.2
Rebuild for new perl

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> 0.03-1.2
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Sat Feb 11 2006 Remi Collet <Fedora@famillecollet.com> 0.03-1
- initial spec for Extras
