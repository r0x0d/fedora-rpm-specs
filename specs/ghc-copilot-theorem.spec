# generated by cabal-rpm-2.2.1
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name copilot-theorem
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

# testsuite missing deps: test-framework test-framework-quickcheck2

Name:           ghc-%{pkg_name}
Version:        3.19.1
Release:        %autorelease
Summary:        K-induction for Copilot

License:        BSD-3-Clause
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bimap-devel
BuildRequires:  ghc-bv-sized-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-copilot-core-devel
BuildRequires:  ghc-copilot-prettyprinter-devel
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-libBF-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-panic-devel
BuildRequires:  ghc-parameterized-utils-devel
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-what4-devel
BuildRequires:  ghc-xml-devel
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bimap-prof
BuildRequires:  ghc-bv-sized-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-copilot-core-prof
BuildRequires:  ghc-copilot-prettyprinter-prof
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-libBF-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-panic-prof
BuildRequires:  ghc-parameterized-utils-prof
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-pretty-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-what4-prof
BuildRequires:  ghc-xml-prof
%endif
# End cabal-rpm deps

%description
Some tools to prove properties on Copilot programs with k-induction model
checking.

Copilot is a stream (i.e., infinite lists) domain-specific language (DSL) in
Haskell that compiles into embedded C. Copilot contains an interpreter,
multiple back-end compilers, and other verification tools.

A tutorial, examples, and other information are available at
<https://copilot-language.github.io>.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development
files.


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


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
# End cabal-rpm setup


%build
# Begin cabal-rpm build:
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install
# End cabal-rpm install


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc CHANGELOG README.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
%autochangelog