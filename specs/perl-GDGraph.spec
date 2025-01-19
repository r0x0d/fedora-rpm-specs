Name:           perl-GDGraph
Epoch:          1
Version:        1.56
Release:        8%{?dist}
Summary:        Graph generation package for Perl
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND GPL-2.0-or-later
URL:            https://metacpan.org/release/GDGraph
Source0:        https://cpan.metacpan.org/modules/by-module/GD/GDGraph-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(GD) >= 1.18
BuildRequires:  perl(GD::Text) >= 0.80
BuildRequires:  perl(GD::Text::Align)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(warnings)
# Dependencies
Requires:       perl(Data::Dumper)
Requires:       perl(GD) >= 1.18
Requires:       perl(GD::Text) >= 0.80
Requires:       perl(Text::ParseWords)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(GD\\)

%description
%{summary}.

%prep
%setup -q -n GDGraph-%{version}

# Fix shellbangs
perl -pi -e 's{^#!/usr/local/bin/perl\b}{#!%{__perl}}' \
  samples/sample1A.pl \
  samples/make_index.pl

# Fix line endings
perl -pi -e 's/\r\n/\n/' samples/sample64.pl

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
# Dustismo_Sans.ttf is GPL-2.0-or-later, everything else is GPL-1.0-or-later OR Artistic-1.0-Perl
%license Dustismo.LICENSE
%doc CHANGES README Dustismo_Sans.ttf samples/
%{perl_vendorlib}/GD/
%{_mandir}/man3/GD::Graph.3*
%{_mandir}/man3/GD::Graph::Data.3*
%{_mandir}/man3/GD::Graph::Error.3*
%{_mandir}/man3/GD::Graph::FAQ.3*
%{_mandir}/man3/GD::Graph::colour.3*
%{_mandir}/man3/GD::Graph::hbars.3*

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.56-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.56-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.56-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.56-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.56-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.56-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Paul Howarth <paul@city-fan.org> - 1:1.56-1
- Update to 1.56
  - Improve language in documentation

* Fri Jan 13 2023 Paul Howarth <paul@city-fan.org> - 1:1.55-1
- Update to 1.55
  - Fix failing XBM test resulting from some upstream changes (CPAN RT#140940)
  - Skip samples tests if libgd has image support disabled, which is the
    default starting with version 2.3.3
    (see https://github.com/libgd/libgd/issues/428)
- Use SPDX-format license tag
- Drop perl(:MODULE_COMPAT_XXX) dependency
  (https://fedoraproject.org/wiki/Changes/Perl_replace_MODULE_COMPAT_by_generator)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.54-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.54-20
- Perl 5.36 rebuild

* Tue Feb  1 2022 Paul Howarth <paul@city-fan.org> - 1:1.54-19
- Fix logo_xbm_noext test (GH#1)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.54-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.54-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.54-16
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.54-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.54-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.54-13
- Perl 5.32 rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.54-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 29 2019 Paul Howarth <paul@city-fan.org> - 1:1.54-11
- Spec tidy-up
  - Use author-independent source URL
  - Use %%{make_build} and %%{make_install}
  - Make %%files list more explicit

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.54-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.54-9
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.54-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.54-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.54-6
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.54-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.54-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.54-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 21 2016 Paul Howarth <paul@city-fan.org> - 1:1.54-1
- Update to 1.54
  - Disable two Y axes alignment when any y[12]_{min,max}_value is defined
    (CPAN RT#62665)

* Fri Jul  8 2016 Paul Howarth <paul@city-fan.org> - 1:1.53-1
- Update to 1.53
  - Fix 'Illegal division by zero' when x_min_value and x_max_value are
    defined and x_tick_number set to 'auto' (CPAN RT#73185,
    https://github.com/ruz/GDGraph/pull/12)
- Don't use macros for commands
- Upstream now wants EU:MM ≥ 6.76 so take advantage of being able to
  use NO_PACKLIST and NO_PERLLOCAL
- Bump Test::More version requirement to 0.88 due to use of done_testing()

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.52-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.52-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 29 2016 Paul Howarth <paul@city-fan.org> - 1:1.52-1
- Update to 1.52
  - y1_min_range and y2_min_range instead of min_range_1 and min_range_2;
    neither were previously documented
  - Update documentation in regards to all *_min_range options available

* Mon Dec 28 2015 Paul Howarth <paul@city-fan.org> - 1:1.51-1
- Update to 1.51
  - Run samples as part of test suite to make sure no sample crashes
  - Properly define test requirements using newer MakeMaker
  - Fix shadows rendering on cumulative bar charts
    (https://github.com/ruz/GDGraph/pull/4)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.49-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 05 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.49-2
- Perl 5.22 rebuild

* Thu Mar 12 2015 Paul Howarth <paul@city-fan.org> - 1:1.49-1
- Update to 1.49
  - Fix to Z-axis color filling in 3D pie charts (Debian Bug #489184)
  - Bump ExtUtils::MakeMaker dependency
  - Tiny improvement in the code of the samples
- Include Dustismo_Sans.ttf with documentation as it's used by the samples

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1:1.48-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.48-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 18 2014 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:1.48-1
- Upstream update.
- Reflect Source0: having changed.
- Modernize spec.
- Fix bogus %%changelog entry.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.44-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Petr Pisar <ppisar@redhat.com> - 1:1.44-16
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.44-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.44-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 12 2012 Petr Pisar <ppisar@redhat.com> - 1:1.44-13
- Perl 5.16 rebuild
- Specify all dependencies

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.44-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 21 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:1.44-11
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.44-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:1.44-9
- 661697 rebuild for fixing problems with vendorach/lib

* Sun May 02 2010 Marcela Maslanova <mmaslano@redhat.com> - 1:1.44-8
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1:1.44-7
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.44-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.44-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1:1.44-4
- Rebuild for perl 5.10 (again)

* Thu Jan 24 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1:1.44-3
- rebuild for new perl

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1:1.44-2.2
- add BR: perl(Test::More)

* Mon Oct 15 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1:1.44-2.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Sat Jun  9 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1:1.44-2
- Bumping release (due to dist tag mismatches).

* Sat May  5 2007 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1:1.44-1
- Update to 1.44.

* Thu May 18 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4308-1
- Update to 1.4308.

* Mon Feb 20 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4307-1
- Update to 1.4307.

* Mon Feb  6 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4306-1
- Update to 1.4306.

* Thu Dec 22 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.4305-1
- Update to 1.4305.

* Wed Apr  6 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.43-4
- rebuilt

* Sun Jul 11 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.43-0.fdr.3
- Unowned directory: %%{perl_vendorlib}/GD (see bug 1800 comment #1).

* Wed Jun 30 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.43-0.fdr.2
- Bring up to date with current fedora.us perl spec template.
- Added the samples directory to the documentation files.

* Sun Oct 12 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:1.43-0.fdr.1
- First build.
