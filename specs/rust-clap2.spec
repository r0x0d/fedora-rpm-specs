# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate clap

Name:           rust-clap2
Version:        2.34.0
Release:        %autorelease
Summary:        Simple to use, efficient, and full-featured Command Line Argument Parser

License:        MIT
URL:            https://crates.io/crates/clap
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * exclude files that are only useful for upstream development
# * bump strsim dependency from 0.8 to 0.10
Patch:          clap-fix-metadata.diff

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
A simple to use, efficient, and full-featured Command Line Argument
Parser.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/CONTRIBUTORS.md
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/SPONSORS.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ansi_term-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ansi_term-devel %{_description}

This package contains library source intended for building other packages which
use the "ansi_term" feature of the "%{crate}" crate.

%files       -n %{name}+ansi_term-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+atty-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+atty-devel %{_description}

This package contains library source intended for building other packages which
use the "atty" feature of the "%{crate}" crate.

%files       -n %{name}+atty-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+color-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+color-devel %{_description}

This package contains library source intended for building other packages which
use the "color" feature of the "%{crate}" crate.

%files       -n %{name}+color-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+debug-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+debug-devel %{_description}

This package contains library source intended for building other packages which
use the "debug" feature of the "%{crate}" crate.

%files       -n %{name}+debug-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+doc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+doc-devel %{_description}

This package contains library source intended for building other packages which
use the "doc" feature of the "%{crate}" crate.

%files       -n %{name}+doc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+no_cargo-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no_cargo-devel %{_description}

This package contains library source intended for building other packages which
use the "no_cargo" feature of the "%{crate}" crate.

%files       -n %{name}+no_cargo-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+strsim-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+strsim-devel %{_description}

This package contains library source intended for building other packages which
use the "strsim" feature of the "%{crate}" crate.

%files       -n %{name}+strsim-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+suggestions-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+suggestions-devel %{_description}

This package contains library source intended for building other packages which
use the "suggestions" feature of the "%{crate}" crate.

%files       -n %{name}+suggestions-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+term_size-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+term_size-devel %{_description}

This package contains library source intended for building other packages which
use the "term_size" feature of the "%{crate}" crate.

%files       -n %{name}+term_size-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%files       -n %{name}+unstable-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+vec_map-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+vec_map-devel %{_description}

This package contains library source intended for building other packages which
use the "vec_map" feature of the "%{crate}" crate.

%files       -n %{name}+vec_map-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+wrap_help-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wrap_help-devel %{_description}

This package contains library source intended for building other packages which
use the "wrap_help" feature of the "%{crate}" crate.

%files       -n %{name}+wrap_help-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+yaml-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+yaml-devel %{_description}

This package contains library source intended for building other packages which
use the "yaml" feature of the "%{crate}" crate.

%files       -n %{name}+yaml-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+yaml-rust-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+yaml-rust-devel %{_description}

This package contains library source intended for building other packages which
use the "yaml-rust" feature of the "%{crate}" crate.

%files       -n %{name}+yaml-rust-devel
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