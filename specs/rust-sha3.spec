# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate sha3

Name:           rust-sha3
Version:        0.10.8
Release:        %autorelease
Summary:        SHA-3 (Keccak) hash function

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/sha3
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Pure Rust implementation of SHA-3, a family of Keccak-based hash
functions including the SHAKE family of eXtendable-Output Functions
(XOFs), as well as the accelerated variant TurboSHAKE.}

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
%doc %{crate_instdir}/CHANGELOG.md
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

%package     -n %{name}+asm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+asm-devel %{_description}

This package contains library source intended for building other packages which
use the "asm" feature of the "%{crate}" crate.

%files       -n %{name}+asm-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+oid-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+oid-devel %{_description}

This package contains library source intended for building other packages which
use the "oid" feature of the "%{crate}" crate.

%files       -n %{name}+oid-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+reset-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+reset-devel %{_description}

This package contains library source intended for building other packages which
use the "reset" feature of the "%{crate}" crate.

%files       -n %{name}+reset-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
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