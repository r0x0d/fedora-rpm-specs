# generated by cabal-rpm-2.2.1
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name HaXml
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

Name:           ghc-%{pkg_name}
Version:        1.25.13
Release:        %autorelease
Summary:        Utilities for manipulating XML documents

# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/thread/VFYIDDBGTIGNG6IJBW2BVSJLIUZXFXKC/
License:        LGPL-2.1-or-later
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-polyparse-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-random-devel
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-polyparse-prof
BuildRequires:  ghc-pretty-prof
BuildRequires:  ghc-random-prof
%endif
# End cabal-rpm deps

%description
Haskell utilities for parsing, filtering, transforming and generating XML
documents.


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


%package -n %{pkg_name}
Summary:        Utilities for using XML documents with Haskell
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later

%description -n %{pkg_name}
This package provides the XML commandline tools for Haskell HaXml library.



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
%license COPYRIGHT
%license LICENCE-GPL
%license LICENCE-LGPL
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc Changelog.md README


%if %{with haddock}
%files doc -f %{name}-doc.files
%license COPYRIGHT
%license LICENCE-GPL
%license LICENCE-LGPL
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%files -n %{pkg_name}
%license COPYRIGHT
%license LICENCE-GPL
%{_bindir}/Canonicalise
%{_bindir}/CanonicaliseLazy
%{_bindir}/DtdToHaskell
%{_bindir}/FpMLToHaskell
%{_bindir}/MkOneOf
%{_bindir}/Validate
%{_bindir}/XsdToHaskell
%{_bindir}/Xtract


%changelog
%autochangelog