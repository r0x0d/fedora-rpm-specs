# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate bigdecimal

Name:           rust-bigdecimal
Version:        0.4.5
Release:        %autorelease
Summary:        Arbitrary precision decimal numbers

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/bigdecimal
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * relax serde_test dev-dependency to allow building with version >=1.0.176
# * exclude files that are only useful for upstream development
Patch:          bigdecimal-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Arbitrary precision decimal numbers.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/COPYRIGHT
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

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-json-devel %{_description}

This package contains library source intended for building other packages which
use the "serde-json" feature of the "%{crate}" crate.

%files       -n %{name}+serde-json-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde_json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_json-devel %{_description}

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%files       -n %{name}+serde_json-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+string-only-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+string-only-devel %{_description}

This package contains library source intended for building other packages which
use the "string-only" feature of the "%{crate}" crate.

%files       -n %{name}+string-only-devel
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