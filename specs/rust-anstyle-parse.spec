# Generated by rust2rpm 26
# * missing dev-dependencies: codegenrs
%bcond_with check
%global debug_package %{nil}

%global crate anstyle-parse

Name:           rust-anstyle-parse
Version:        0.2.5
Release:        %autorelease
Summary:        Parse ANSI Style Escapes

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/anstyle-parse
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Parse ANSI Style Escapes.}

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

%package     -n %{name}+core-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+core-devel %{_description}

This package contains library source intended for building other packages which
use the "core" feature of the "%{crate}" crate.

%files       -n %{name}+core-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+utf8-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+utf8-devel %{_description}

This package contains library source intended for building other packages which
use the "utf8" feature of the "%{crate}" crate.

%files       -n %{name}+utf8-devel
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