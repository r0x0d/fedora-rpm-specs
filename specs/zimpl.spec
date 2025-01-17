%global giturl  https://github.com/scipopt/zimpl

Name:           zimpl
Version:        3.6.2
Release:        %autorelease
Summary:        Zuse Institut Mathematical Programming Language

%global upver   %(sed 's/\\.//g' <<< %{version})

# LGPL-3.0-or-later: the project as a whole
# Other licenses are due to fonts embedded in the PDF manual:
# OFL-1.1-RFN: AMS
# Knuth-CTAN: CM
# GPL-1.0-or-later: CM-Super
License:        LGPL-3.0-or-later AND OFL-1.1-RFN AND Knuth-CTAN AND GPL-1.0-or-later
URL:            https://zimpl.zib.de/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/v%{upver}/%{name}-%{version}.tar.gz
# Build a shared library instead of a static library.  ZIMPL leaves some symbols
# undefined, namely those listed in src/zimpl/xlpglue.h.  They take advantage of
# the fact that linking with a static library only pulls in the referenced
# symbols to avoid referring to the xlp symbols in certain cases, for example,
# in the scip test suite.  Since Fedora wants shared libraries, we have to give
# those symbols weak dummy definitions to avoid unresolved symbols at link time.
Patch:          %{name}-shared.patch
# This package and cddlib both have C functions named set_copy and set_free.
# This is a problem for polymake, which links both libraries.  Rename the
# zimpl functions to set_copy_zimpl and set_free_zimpl.
Patch:          %{name}-cddlib-set-clash.patch
# Use zlib-ng directly, rather than via the compatibility interface
Patch:          %{name}-zlib-ng.patch
# Fix a test failure that appears to be due to changes in bsearch behavior
# in newer glibc builds
Patch:          %{name}-test-bsearch.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(zlib-ng)

Requires:       libzimpl%{?_isa} = %{version}-%{release}

%global _desc %{expand:
Zimpl is a little language to translate the mathematical model of a
problem into a linear or nonlinear (mixed-) integer mathematical program
expressed in .lp or .mps file format which can be read and (hopefully)
solved by a LP or MIP solver.}

%description %_desc

This package contains a command-line tool to access ZIMPL
functionality.

%package -n     libzimpl
# LGPL-3.0-or-later: the project as a whole
# LGPL-2.0-or-later: src/zimpl/{mmlparse2.y,mmlscan.l}
# GPL-3.0-or-later WITH Bison-exception-2.2: mmlparse2.{c,h}
License:        LGPL-3.0-or-later AND LGPL-2.0-or-later AND GPL-3.0-or-later WITH Bison-exception-2.2
Summary:        Zuse Institut Mathematical Programming Language

%description -n libzimpl %_desc

This package contains a library interface to ZIMPL functionality.

%package -n     libzimpl-devel
# LGPL-3.0-or-later: the project as a whole
# GPL-3.0-or-later WITH Bison-exception-2.2: mmlparse2.h
License:        LGPL-3.0-or-later AND GPL-3.0-or-later WITH Bison-exception-2.2
Summary:        Headers and library links for libzimpl
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libzimpl%{?_isa} = %{version}-%{release}

%description -n libzimpl-devel
This package contains headers and library links for developing
applications that use libzimpl.

%prep
%autosetup -n %{name}-%{upver} -p1

%conf
# Fix installation directories
if [ "%{_lib}" != "lib" ]; then
  sed -i 's,\(DESTINATION \)lib,\1%{_lib},' src/CMakeLists.txt
fi

# Avoid warnings about obsolete invocations of grep
sed -i 's/fgrep/grep -F/' check/check.sh

%build
export CFLAGS='%{build_cflags} -DFREEMEM -DNO_MSHELL'
export CXXFLAGS='%{build_cxxflags} -DFREEMEM -DNO_MSHELL'
%cmake
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_mandir}/man1
cp -p doc/zimpl.man %{buildroot}%{_mandir}/man1/zimpl.1

# FIXME: Test qubo.zpl (qbo: lp) fails on ppc64le
%ifnarch ppc64le
%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
cd check
sh check.sh ../%{_vpath_builddir}/bin/zimpl
cd -
%endif

%files
%doc doc/zimpl.pdf
%{_bindir}/zimpl
%{_mandir}/man1/zimpl.1*

%files -n libzimpl
%doc CHANGELOG README
%license LICENSE
%{_libdir}/libzimpl.so.0*

%files -n libzimpl-devel
%{_includedir}/zimpl/
%{_libdir}/libzimpl.so
%{_libdir}/cmake/zimpl/

%changelog
%autochangelog
