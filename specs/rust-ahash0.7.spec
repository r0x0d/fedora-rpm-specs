# Generated by rust2rpm 25
%bcond_without check
%global debug_package %{nil}

%global crate ahash

Name:           rust-ahash0.7
Version:        0.7.7
Release:        %autorelease
Summary:        Non-cryptographic hash function using AES-NI for high performance

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ahash
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          ahash-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
# * drop unused benchmarks and benchmark-only criterion dev-dependency
Patch:          ahash-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A non-cryptographic hash function using AES-NI for high performance.}

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
%doc %{crate_instdir}/FAQ.md
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

%package     -n %{name}+atomic-polyfill-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+atomic-polyfill-devel %{_description}

This package contains library source intended for building other packages which
use the "atomic-polyfill" feature of the "%{crate}" crate.

%files       -n %{name}+atomic-polyfill-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+compile-time-rng-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+compile-time-rng-devel %{_description}

This package contains library source intended for building other packages which
use the "compile-time-rng" feature of the "%{crate}" crate.

%files       -n %{name}+compile-time-rng-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+const-random-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+const-random-devel %{_description}

This package contains library source intended for building other packages which
use the "const-random" feature of the "%{crate}" crate.

%files       -n %{name}+const-random-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
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
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
# remove benchmark sources from non-standard path in tests/
rm tests/{bench.rs,map_tests.rs}

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