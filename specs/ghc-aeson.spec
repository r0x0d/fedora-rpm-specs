# generated by cabal-rpm-2.2.1 --subpackage
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name aeson
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

%global OneTuple OneTuple-0.4.2
%global generically generically-0.1.1
%global indexedtraversableinstances indexed-traversable-instances-0.1.2
%global semialign semialign-1.3.1
%global witherable witherable-0.4.2

%global subpkgs %{OneTuple} %{generically} %{indexedtraversableinstances} %{semialign} %{witherable}

# testsuite missing deps: tasty-golden

Name:           ghc-%{pkg_name}
Version:        2.1.2.1
# can only be reset when all subpkgs bumped
Release:        7%{?dist}
Summary:        Fast JSON parsing and encoding

License:        BSD-3-Clause
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{OneTuple}/%{OneTuple}.tar.gz
Source2:        https://hackage.haskell.org/package/%{generically}/%{generically}.tar.gz
Source3:        https://hackage.haskell.org/package/%{indexedtraversableinstances}/%{indexedtraversableinstances}.tar.gz
Source4:        https://hackage.haskell.org/package/%{semialign}/%{semialign}.tar.gz
Source5:        https://hackage.haskell.org/package/%{witherable}/%{witherable}.tar.gz
Source6:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros-extra
#BuildRequires:  ghc-OneTuple-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-compat-batteries-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-data-fix-devel
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-dlist-devel
BuildRequires:  ghc-exceptions-devel
#BuildRequires:  ghc-generically-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-indexed-traversable-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-scientific-devel
#BuildRequires:  ghc-semialign-devel
BuildRequires:  ghc-strict-devel
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-short-devel
BuildRequires:  ghc-th-abstraction-devel
BuildRequires:  ghc-these-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-compat-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-uuid-types-devel
BuildRequires:  ghc-vector-devel
#BuildRequires:  ghc-witherable-devel
%if %{with ghc_prof}
#BuildRequires:  ghc-OneTuple-prof
BuildRequires:  ghc-QuickCheck-prof
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base-compat-batteries-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-data-fix-prof
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-dlist-prof
BuildRequires:  ghc-exceptions-prof
#BuildRequires:  ghc-generically-prof
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-indexed-traversable-prof
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-scientific-prof
#BuildRequires:  ghc-semialign-prof
BuildRequires:  ghc-strict-prof
BuildRequires:  ghc-tagged-prof
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-text-short-prof
BuildRequires:  ghc-th-abstraction-prof
BuildRequires:  ghc-these-prof
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-time-compat-prof
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-uuid-types-prof
BuildRequires:  ghc-vector-prof
#BuildRequires:  ghc-witherable-prof
%endif
# for missing dep 'semialign':
BuildRequires:  ghc-semigroupoids-devel
BuildRequires:  ghc-transformers-devel
%if %{with ghc_prof}
BuildRequires:  ghc-semigroupoids-prof
BuildRequires:  ghc-transformers-prof
%endif
# for missing dep 'witherable':
BuildRequires:  ghc-base-orphans-devel
BuildRequires:  ghc-transformers-devel
%if %{with ghc_prof}
BuildRequires:  ghc-base-orphans-prof
BuildRequires:  ghc-transformers-prof
%endif
# End cabal-rpm deps

%description
A JSON parsing and encoding library optimized for ease of use and
high performance.  Aeson was the father of Jason in Greek mythology.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch
Requires:       ghc-filesystem

%description doc
This package provides the Haskell %{pkg_name} library documentation.
%endif


%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-devel and ghc-prof)

%description prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%global main_version %{version}

%if %{defined ghclibdir}
%ghc_lib_subpackage -l BSD-3-Clause %{OneTuple}
%ghc_lib_subpackage -l BSD-3-Clause %{generically}
%ghc_lib_subpackage -l BSD-2-Clause %{indexedtraversableinstances}
%ghc_lib_subpackage -l BSD-3-Clause %{semialign}
%ghc_lib_subpackage -l BSD-3-Clause %{witherable}
%endif

%global version %{main_version}


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1 -a2 -a3 -a4 -a5
cp -bp %{SOURCE6} %{pkg_name}.cabal
# End cabal-rpm setup
(
cd %{generically}
cabal-tweak-dep-ver base '<4.18' '<4.19'
)
(
cd %{witherable}
cabal-tweak-dep-ver base-orphans '<0.9' '<0.10'
cabal-tweak-dep-ver hashable '<1.4' '<1.5'
cabal-tweak-dep-ver transformers '<0.6' '<0.7'
cabal-tweak-dep-ver vector '<0.13' '<0.14'
)


%build
# Begin cabal-rpm build:
%ghc_libs_build %{subpkgs}
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
# End cabal-rpm install


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc README.markdown changelog.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
* Sat Aug  3 2024 Jens Petersen <petersen@redhat.com> - 2.1.2.1-7
- OneTuple-0.4.2, indexed-traversable-instances-0.1.2, semialign-1.3.1

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jul 23 2023 Jens Petersen <petersen@redhat.com> - 2.1.2.1-3
- https://hackage.haskell.org/package/aeson-2.1.2.1/changelog

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jan 22 2023 Jens Petersen <petersen@redhat.com> - 2.0.3.0-1
- https://hackage.haskell.org/package/aeson-2.0.3.0/changelog
- refresh to cabal-rpm-2.1.0 with SPDX migration

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 17 2022 Jens Petersen <petersen@redhat.com> - 1.5.6.0-3
- rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug  5 2021 Jens Petersen <petersen@redhat.com> - 1.5.6.0-1
- update to 1.5.6.0

* Thu Aug  5 2021 Jens Petersen <petersen@redhat.com> - 1.5.5.1-1
- update to 1.5.5.1

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 07 2020 Jens Petersen <petersen@redhat.com> - 1.4.7.1-1
- update to 1.4.7.1

* Sun Feb 09 2020 Jens Petersen <petersen@redhat.com> - 1.4.6.0-1
- update to 1.4.6.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Jens Petersen <petersen@redhat.com> - 1.4.2.0-1
- update to 1.4.2.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Jens Petersen <petersen@redhat.com> - 1.3.1.1-1
- update to 1.3.1.1

* Sun Feb 17 2019 Jens Petersen <petersen@redhat.com> - 1.2.4.0-3
- refresh to cabal-rpm-0.13

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 28 2018 Jens Petersen <petersen@redhat.com> - 1.2.4.0-1
- update to 1.2.4.0

* Mon Jul 23 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.3.0-4
- Rebuilt for #1607054

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 Jens Petersen <petersen@redhat.com> - 1.2.3.0-1
- update to 1.2.3.0

* Fri Jan 12 2018 Jens Petersen <petersen@redhat.com> - 1.0.2.1-8
- time-locale-compat is now packaged

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Feb 21 2017 Jens Petersen <petersen@redhat.com> - 1.0.2.1-5
- update to 1.0.2.1
- subpackage time-locale-compat

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Aug 31 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.8.0.2-3
- Rebuild (aarch64 vector hashes)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 Jens Petersen <petersen@redhat.com> - 0.8.0.2-1
- update to 0.8.0.2

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 20 2014 Jens Petersen <petersen@redhat.com> - 0.6.2.1-2
- disable TH module on arch's without ghci

* Wed Jan 22 2014 Jens Petersen <petersen@redhat.com> - 0.6.2.1-1
- update to 0.6.2.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Jens Petersen <petersen@redhat.com> - 0.6.1.0-2
- update to new simplified Haskell Packaging Guidelines

* Mon Mar 11 2013 Jens Petersen <petersen@redhat.com> - 0.6.1.0-1
- update to 0.6.1.0

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Nov 17 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.2-5
- update with cabal-rpm

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.2-3
- rebuild

* Fri Jun 15 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.2-2
- rebuild

* Sun May  6 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.2-1
- update to 0.6.0.2
- build needs ghci

* Sat Mar 24 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.0-2
- depends on dlist for ghc > 7.2

* Mon Feb 27 2012 Jens Petersen <petersen@redhat.com> - 0.6.0.0-1
- BSD license
- doc files

* Mon Feb 27 2012 Fedora Haskell SIG <haskell-devel@lists.fedoraproject.org>
- spec file template generated by cabal2spec-0.25.4