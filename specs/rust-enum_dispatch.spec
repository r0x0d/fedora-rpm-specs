# Generated by rust2rpm 26
# * It is not practical to run the tests:
# * - custom_derive and enum_derive are unpackaged and unmaintained for 7+ years
# * - smol is unpackaged
%bcond_with check
%global debug_package %{nil}

%global crate enum_dispatch

Name:           rust-enum_dispatch
Version:        0.3.13
Release:        %autorelease
Summary:        Near drop-in replacement for dynamic-dispatched method calls

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/enum_dispatch
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Near drop-in replacement for dynamic-dispatched method calls with up to
10x the speed.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
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