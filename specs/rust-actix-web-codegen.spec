# Generated by rust2rpm 26
# * tests can only be run in-tree
%bcond_with check
%global debug_package %{nil}

%global crate actix-web-codegen

Name:           rust-actix-web-codegen
Version:        4.3.0
Release:        %autorelease
Summary:        Routing and runtime macros for Actix Web

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/actix-web-codegen
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Routing and runtime macros for Actix Web.}

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
%doc %{crate_instdir}/CHANGES.md
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

%package     -n %{name}+compat-routing-macros-force-pub-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+compat-routing-macros-force-pub-devel %{_description}

This package contains library source intended for building other packages which
use the "compat-routing-macros-force-pub" feature of the "%{crate}" crate.

%files       -n %{name}+compat-routing-macros-force-pub-devel
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