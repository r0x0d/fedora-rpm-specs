Name:		xerces-c
Version:	3.3.0
Release:	%autorelease
Summary:	Validating XML Parser

License:	Apache-2.0
URL:		https://xerces.apache.org/xerces-c/
Source0:	https://downloads.apache.org/xerces/c/3/sources/xerces-c-%{version}.tar.xz
Source1:	https://downloads.apache.org/xerces/c/3/sources/xerces-c-%{version}.tar.xz.asc
Source2:	https://downloads.apache.org/xerces/c/KEYS

BuildRequires:	dos2unix
BuildRequires:	gcc-c++
BuildRequires:	gnupg2
BuildRequires:	make

%description
Xerces-C is a validating XML parser written in a portable
subset of C++. Xerces-C makes it easy to give your application the
ability to read and write XML data. A shared library is provided for
parsing, generating, manipulating, and validating XML
documents. Xerces-C is faithful to the XML 1.0 recommendation and
associated standards: XML 1.0 (Third Edition), XML 1.1 (First
Edition), DOM Level 1, 2, 3 Core, DOM Level 2.0 Traversal and Range,
DOM Level 3.0 Load and Save, SAX 1.0 and SAX 2.0, Namespaces in XML,
Namespaces in XML 1.1, XML Schema, XML Inclusions).

%package	devel
Summary:	Header files, libraries and development documentation for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%package doc
Summary:	Documentation for Xerces-C++ validating XML parser
BuildArch:	noarch

%description doc
Documentation for Xerces-C++.

Xerces-C++ is a validating XML parser written in a portable subset of C++.
Xerces-C++ makes it easy to give your application the ability to read and
write XML data. A shared library is provided for parsing, generating,
manipulating, and validating XML documents.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup
# Copy samples before build to avoid including built binaries in -doc package
mkdir -p _docs
cp -a samples/ _docs/

%build
# --disable-sse2 makes sure explicit -msse2 isn't passed to gcc so
# the binaries would be compatible with non-SSE2 i686 hardware.
# This only affects i686, as on x86_64 the compiler uses SSE2 by default.
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
export CXXFLAGS="$CFLAGS"
%configure --disable-static \
  --disable-sse2
%make_build

%install
%make_install
# Correct errors in encoding
iconv -f iso8859-1 -t utf-8 CREDITS > CREDITS.tmp && mv -f CREDITS.tmp CREDITS
# Correct errors in line endings
pushd doc; dos2unix -k *.xml; popd
# Remove unwanted binaries
rm -rf $RPM_BUILD_ROOT%{_bindir}
# Remove .la files
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%files
%license LICENSE
%{_libdir}/libxerces-c-3.3.so

%files devel
%{_libdir}/libxerces-c.so
%{_libdir}/pkgconfig/xerces-c.pc
%{_includedir}/xercesc/

%files doc
%license LICENSE
%doc README NOTICE CREDITS doc _docs/*

%changelog
%autochangelog
