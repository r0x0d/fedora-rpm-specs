# Disable tests which need the Internet
# <https://github.com/gbxyz/perl-net-rdap/issues/9>
%bcond_with network_tests

Name:           perl-Net-RDAP
Version:        0.33
Release:        1%{?dist}
Summary:        Interface to the Registration Data Access Protocol (RDAP)
# LICENSE:      BSD-2-Clause
License:        BSD-2-Clause
URL:            https://metacpan.org/dist/Net-RDAP
Source0:        https://cpan.metacpan.org/authors/id/G/GB/GBROWN/Net-RDAP-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(DateTime::Format::ISO8601)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(JSON)
BuildRequires:  perl(List::Util)
%if %{with network_tests}
BuildRequires:  perl(LWP::Protocol::https)
%endif
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::Type)
BuildRequires:  perl(Mozilla::CA)
BuildRequires:  perl(Net::ASN)
BuildRequires:  perl(Net::DNS::Domain)
BuildRequires:  perl(Net::DNS::RR::DNSKEY)
BuildRequires:  perl(Net::DNS::RR::DS)
BuildRequires:  perl(Net::IP)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Storable)
BuildRequires:  perl(URI)
BuildRequires:  perl(vars)
BuildRequires:  perl(vCard)
BuildRequires:  perl(XML::LibXML)
# Tests:
BuildRequires:  perl(Cwd)
%if %{with network_tests}
BuildRequires:  perl(LWP::Online)
BuildRequires:  perl(Net::DNS)
%endif
BuildRequires:  perl(Test::More)
Requires:       perl(LWP::Protocol::https)

%description
Net::RDAP provides an interface to the Registration Data Access Protocol.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Net-RDAP-%{version}
%if %{without network_tests}
for T in t/chain.t t/document_url.t t/objects.t t/search.t; do
    rm "$T"
    perl -i -ne 'print $_ unless m{\A\Q'"$T"'\E}' MANIFEST
done
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/Net/RDAP
%{perl_vendorlib}/Net/RDAP.pm
%{_mandir}/man3/Net::RDAP.*
%{_mandir}/man3/Net::RDAP::*

%files tests
%{_libexecdir}/%{name}

%changelog
* Wed Oct 16 2024 Petr Pisar <ppisar@redhat.com> - 0.33-1
- 0.33 bump

* Wed Oct 16 2024 Petr Pisar <ppisar@redhat.com> 0.32-1
- Specfile autogenerated by cpanspec 1.78.