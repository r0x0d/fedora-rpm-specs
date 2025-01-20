Name:           perl-Proc-ProcessTable
Version:        0.636
Release:        6%{?dist}
Summary:        Perl extension to access the Unix process table
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Proc-ProcessTable
Source0:        https://cpan.metacpan.org/modules/by-module/Proc/Proc-ProcessTable-%{version}.tar.gz
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(subs)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More)
BuildRequires:  procps-ng
# Dependencies
Requires:       perl(File::Temp)
Requires:       perl(Storable)

# Avoid provides for private objects
%{?perl_default_filter}

%description
Perl interface to the Unix process table.

%prep
%setup -q -n Proc-ProcessTable-%{version}

chmod -c 644 contrib/*

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README README.linux contrib/pswait
%{perl_vendorarch}/auto/Proc/
%{perl_vendorarch}/Proc/
%{_mandir}/man3/Proc::ProcessTable.3*
%{_mandir}/man3/Proc::Killall.3*
%{_mandir}/man3/Proc::Killfam.3*
%{_mandir}/man3/Proc::ProcessTable::Process.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.636-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.636-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Jitka Plesnikova <jplesnik@redhat.com> - 0.636-4
- Perl 5.40 rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.636-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.636-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 30 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.636-1
- 0.636 bump (rhbz#2216486)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.635-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.635-2
- Perl 5.38 rebuild

* Wed Jun 07 2023 Jitka Plesnikova <jplesnik@redhat.com> - 0.635-1
- 0.635 bump
- Update license to SPDX format

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.634-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.634-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.634-2
- Perl 5.36 rebuild

* Thu May 19 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.634-1
- 0.634 bump

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.59-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.59-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.59-8
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.59-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.59-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.59-5
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.59-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 2019 Paul Howarth <paul@city-fan.org> - 0.59-3
- Spec tidy-up
  - Classify buildreqs by usage
  - Use %%{make_build} and %%{make_install}
  - Simplify find command using -empty
  - Make %%files list more explicit

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.59-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.59-1
- 0.59 bump

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.56-2
- Perl 5.30 rebuild

* Thu Feb 28 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.56-1
- 0.56 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.55-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.55-3
- Perl 5.28 rebuild

* Thu Mar  1 2018 Florian Weimer <fweimer@redhat.com> - 0.55-2
- Rebuild with new redhat-rpm-config/perl build flags

* Thu Mar 01 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.55-1
- 0.55 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.53-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 11 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.53-1
- 0.53 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-5
- Perl 5.22 rebuild

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.50-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 08 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.50-1
- 0.50 bump

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 0.48-2
- Perl 5.18 rebuild

* Wed Jul 24 2013 Paul Howarth <paul@city-fan.org> - 0.48-1
- Update to 0.48
  - Make module thread-safe on linux (CPAN RT#38709)
  - New constructor flag enable_ttys, which when set to 0 disables traversing
    the device tree
  - New maintainer JSWARTZ
  - Fix reading process command lines (CPAN RT#51470)
  - Fixes for non-threaded perls (CPAN RT#41397, CPAN RT#46861, CPAN RT#58236)
  - Fix file descriptor leak (CPAN RT#69397)
  - Fix unsafe use of /tmp (CPAN RT#72862, CVE-2011-4363)
  - Various fixes for non-linux operating systems
  - Fix byte order tag in cache file (CPAN RT#72862)
  - Fixes to stay accurate on machines with many CPUs (CPAN RT#82175), to
    include system time into calculations (CPAN RT#80391) and others
    (CPAN RT#81312, CPAN RT#82175 and CPAN RT#80391)
  - Fix unknown process states for debian kernels (CPAN RT#71976)
  - Added tests
- Drop ARG_MAX patch, no longer needed
- Don't use macros for commands
- Don't need to remove empty directories from the buildroot
- Don't ship empty TODO file
- Drop %%defattr, redundant since rpm 4.4
- Specify all dependencies
- Add %%{?perl_default_filter}

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.44-14
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.44-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.44-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 0.44-11
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.44-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 0.44-9
- Perl mass rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.44-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.44-7
- Rebuild to fix problems with vendorarch/lib (#661697)

* Thu May 06 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.44-6
- Mass rebuild with perl-5.12.0

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.44-5
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.44-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 05 2009 Caolán McNamara <caolanm@redhat.com> - 0.44-3
- defuzz patches to build

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.44-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug  1 2008 Andreas Thienemnan <athienem@redhat.com> 0.44-1
- Update to 0.44

* Sat Apr  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.42-1
- update to 0.42
- patch to define ARG_MAX (since for some unknown reason, it isn't defined anymore)

* Mon Mar  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.41-4
- rebuild for new perl (again)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.41-3
- Autorebuild for GCC 4.3

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.41-2
- rebuild for new perl

* Thu Mar 15 2007 Andreas Thienemann <andreas@bawue.net> 0.41-1
- Specfile autogenerated by cpanspec 1.69.1.
- Cleaned up for FE
