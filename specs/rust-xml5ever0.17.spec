# Generated by rust2rpm 26
# * outdated dev-dependencies: rustc-test ^0.3
%bcond_with check
%global debug_package %{nil}

%global crate xml5ever

Name:           rust-xml5ever0.17
Version:        0.17.0
Release:        %autorelease
Summary:        Push based streaming parser for xml

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/xml5ever
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          xml5ever-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Push based streaming parser for xml.}

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
