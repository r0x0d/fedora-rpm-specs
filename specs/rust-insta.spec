# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate insta

Name:           rust-insta
Version:        1.40.0
Release:        %autorelease
Summary:        Snapshot testing library for Rust

License:        Apache-2.0
URL:            https://crates.io/crates/insta
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24
%if %{with check}
BuildRequires:  rustfmt
%endif

%global _description %{expand:
A snapshot testing library for Rust.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
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

%package     -n %{name}+_cargo_insta_internal-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+_cargo_insta_internal-devel %{_description}

This package contains library source intended for building other packages which
use the "_cargo_insta_internal" feature of the "%{crate}" crate.

%files       -n %{name}+_cargo_insta_internal-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+clap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+clap-devel %{_description}

This package contains library source intended for building other packages which
use the "clap" feature of the "%{crate}" crate.

%files       -n %{name}+clap-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+colors-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+colors-devel %{_description}

This package contains library source intended for building other packages which
use the "colors" feature of the "%{crate}" crate.

%files       -n %{name}+colors-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+console-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+console-devel %{_description}

This package contains library source intended for building other packages which
use the "console" feature of the "%{crate}" crate.

%files       -n %{name}+console-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+csv-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+csv-devel %{_description}

This package contains library source intended for building other packages which
use the "csv" feature of the "%{crate}" crate.

%files       -n %{name}+csv-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+filters-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+filters-devel %{_description}

This package contains library source intended for building other packages which
use the "filters" feature of the "%{crate}" crate.

%files       -n %{name}+filters-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+glob-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+glob-devel %{_description}

This package contains library source intended for building other packages which
use the "glob" feature of the "%{crate}" crate.

%files       -n %{name}+glob-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+globset-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+globset-devel %{_description}

This package contains library source intended for building other packages which
use the "globset" feature of the "%{crate}" crate.

%files       -n %{name}+globset-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+json-devel %{_description}

This package contains library source intended for building other packages which
use the "json" feature of the "%{crate}" crate.

%files       -n %{name}+json-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pest-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pest-devel %{_description}

This package contains library source intended for building other packages which
use the "pest" feature of the "%{crate}" crate.

%files       -n %{name}+pest-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pest_derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pest_derive-devel %{_description}

This package contains library source intended for building other packages which
use the "pest_derive" feature of the "%{crate}" crate.

%files       -n %{name}+pest_derive-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+redactions-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+redactions-devel %{_description}

This package contains library source intended for building other packages which
use the "redactions" feature of the "%{crate}" crate.

%files       -n %{name}+redactions-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+regex-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+regex-devel %{_description}

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%files       -n %{name}+regex-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ron-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ron-devel %{_description}

This package contains library source intended for building other packages which
use the "ron" feature of the "%{crate}" crate.

%files       -n %{name}+ron-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+toml-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+toml-devel %{_description}

This package contains library source intended for building other packages which
use the "toml" feature of the "%{crate}" crate.

%files       -n %{name}+toml-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+walkdir-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+walkdir-devel %{_description}

This package contains library source intended for building other packages which
use the "walkdir" feature of the "%{crate}" crate.

%files       -n %{name}+walkdir-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+yaml-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+yaml-devel %{_description}

This package contains library source intended for building other packages which
use the "yaml" feature of the "%{crate}" crate.

%files       -n %{name}+yaml-devel
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