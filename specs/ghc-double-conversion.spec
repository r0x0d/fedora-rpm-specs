# generated by cabal-rpm-2.2.1
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name double-conversion
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}

# testsuite missing deps: test-framework test-framework-hunit test-framework-quickcheck2

Name:           ghc-%{pkg_name}
Version:        2.0.5.0
Release:        %autorelease
Summary:        Fast conversion between single and double precision floating point and text

# License file is BSD2, though .cabal file says BSD3
License:        BSD-2-Clause
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources
# tweaked https://salsa.debian.org/haskell-team/DHG_packages/-/raw/master/p/haskell-double-conversion/debian/patches/
Patch0:         use-system-lib.diff

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-text-devel
%if %{with ghc_prof}
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-text-prof
%endif
BuildRequires:  double-conversion-devel
BuildRequires:  gcc-c++
# End cabal-rpm deps

%description
A library that performs fast, accurate conversion between floating point and
text.

This library is implemented as bindings to the C++ 'double-conversion' library
written by Florian Loitsch at Google:
<https://github.com/floitsch/double-conversion>.

Now it can convert single precision numbers, and also it can create Builder,
instead of bytestring or text.

The 'Text' versions of these functions are about 30 times faster than the
default 'show' implementation for the 'Double' type.

The 'ByteString' versions are have very close speed to the 'Text' versions;

Builder versions (both for Text and Bytestring) are slower on single value, but
they are much faster on large number of values (up to 20x faster on list with
20000 doubles).

As a final note, be aware that the 'bytestring-show' package is about 50%
slower than simply using 'show'.


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
# Begin cabal-rpm deps:
Requires:       double-conversion-devel%{?_isa}
# End cabal-rpm deps
# missing from double-conversion-devel (#2068103)
Requires:       gcc-c++

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
%autopatch -p1
# End cabal-rpm setup
cabal-tweak-flag embedded_double_conversion False

# remove bundled library
rm -r double-conversion


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
%doc README.markdown


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
%autochangelog