# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate trust-dns-recursor

Name:           rust-trust-dns-recursor
Version:        0.23.2
Release:        %autorelease
Summary:        Safe and secure DNS recursive resolver with DNSSEC support

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/trust-dns-recursor
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * remove unused tracing-subscriber dev-dependency
Patch:          trust-dns-recursor-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Trust-DNS Recursor is a safe and secure DNS recursive resolver with
DNSSEC support. Trust-DNS is based on the Tokio and Futures libraries,
which means it should be easily integrated into other software that also
use those libraries. This library can be used as in the server and
binary for performing recursive lookups.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dns-over-native-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dns-over-native-tls-devel %{_description}

This package contains library source intended for building other packages which
use the "dns-over-native-tls" feature of the "%{crate}" crate.

%files       -n %{name}+dns-over-native-tls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dns-over-openssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dns-over-openssl-devel %{_description}

This package contains library source intended for building other packages which
use the "dns-over-openssl" feature of the "%{crate}" crate.

%files       -n %{name}+dns-over-openssl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dns-over-tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dns-over-tls-devel %{_description}

This package contains library source intended for building other packages which
use the "dns-over-tls" feature of the "%{crate}" crate.

%files       -n %{name}+dns-over-tls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dnssec-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dnssec-devel %{_description}

This package contains library source intended for building other packages which
use the "dnssec" feature of the "%{crate}" crate.

%files       -n %{name}+dnssec-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+dnssec-openssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+dnssec-openssl-devel %{_description}

This package contains library source intended for building other packages which
use the "dnssec-openssl" feature of the "%{crate}" crate.

%files       -n %{name}+dnssec-openssl-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-config-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-config-devel %{_description}

This package contains library source intended for building other packages which
use the "serde-config" feature of the "%{crate}" crate.

%files       -n %{name}+serde-config-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+testing-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+testing-devel %{_description}

This package contains library source intended for building other packages which
use the "testing" feature of the "%{crate}" crate.

%files       -n %{name}+testing-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tls-devel %{_description}

This package contains library source intended for building other packages which
use the "tls" feature of the "%{crate}" crate.

%files       -n %{name}+tls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tls-openssl-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tls-openssl-devel %{_description}

This package contains library source intended for building other packages which
use the "tls-openssl" feature of the "%{crate}" crate.

%files       -n %{name}+tls-openssl-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog