%global         srcname         dnspython
%global         forgeurl        https://github.com/rthalley/dnspython
Version:        2.7.0
%global         tag             v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        DNS toolkit for python

License:        ISC
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
# Needed for documentation
BuildRequires:  make
BuildRequires:  python3dist(sphinx)
# Needed for additional functionality
BuildRequires:  python3dist(cryptography)
BuildRequires:  python3dist(httpcore)
BuildRequires:  python3dist(httpx)
BuildRequires:  python3dist(h2)
BuildRequires:  python3dist(aioquic)
BuildRequires:  python3dist(idna)
BuildRequires:  python3dist(trio)
# Change end of line encoding
BuildRequires:  dos2unix
# Not packaged for Fedora needed for wmi subpackage
#BuildRequires:  python3dist(wmi)
BuildArch: noarch

%global _description %{expand:
dnspython is a DNS toolkit for Python. It supports almost all record types.
It can be used for queries, zone transfers, and dynamic updates. It supports
TSIG-authenticated messages and EDNS0.

dnspython provides both high- and low-level access to DNS. The high-level
classes perform queries for data of a given name, type, and class, and
return an answer set. The low-level classes allow direct manipulation of
DNS zones, messages, names, and records.

dnspython is a utility to work with DNS, /etc/hosts is thus not used. For
simple forward DNS lookups, it's better to use socket.getaddrinfo() or
socket.gethostbyname().

dnspython originated at Nominum where it was developed to facilitate the
testing of DNS software.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%pyproject_extras_subpkg -n python3-%{srcname} dnssec

%pyproject_extras_subpkg -n python3-%{srcname} doh

%pyproject_extras_subpkg -n python3-%{srcname} doq

%pyproject_extras_subpkg -n python3-%{srcname} idna

%pyproject_extras_subpkg -n python3-%{srcname} trio

%prep
%forgesetup

pushd examples
for f in *.py;
do
    sed -i 's|/usr/bin/env python3|/usr/bin/python3|g' $f
    chmod -x $f
done
popd
# Fix end of line encoding
dos2unix examples/dot.py

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

# Build Documentation
pushd doc
make man
popd

%install
%pyproject_install
%pyproject_save_files dns

mkdir -p %{buildroot}/%{_mandir}/man1
install -m 644 doc/_build/man/dnspython.1 %{buildroot}/%{_mandir}/man1/


%check
%pyproject_check_import

# Do not run test that depend on sha1
k="${k-}${k+ and }not (DNSSECValidatorTestCase and testAbsoluteRSABad)"
k="${k-}${k+ and }not (DNSSECValidatorTestCase and testAbsoluteRSAGood)"
k="${k-}${k+ and }not (DNSSECValidatorTestCase and testAlternateParameterFormats)"
k="${k-}${k+ and }not (DNSSECValidatorTestCase and testDuplicateKeytag)"
k="${k-}${k+ and }not (DNSSECValidatorTestCase and testRelativeRSABad)"
k="${k-}${k+ and }not (DNSSECValidatorTestCase and testRelativeRSAGood)"
k="${k-}${k+ and }not (DNSSECValidatorTestCase and testWildcardGoodAndBad)"
k="${k-}${k+ and }not (DNSSECSignatureTestCase and testSignatureRSASHA1)"
k="${k-}${k+ and }not (DNSSECAlgorithm and test_rsa)"

%pytest -k "${k-}"

%files -n python3-%{srcname} -f %{pyproject_files}
%doc SECURITY.md
%doc README.md
%doc examples/
%{_mandir}/man1/dnspython.1*
%license LICENSE

%changelog
%autochangelog
