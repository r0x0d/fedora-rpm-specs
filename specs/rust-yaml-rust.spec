# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate yaml-rust

Name:           rust-yaml-rust
Version:        0.4.5
Release:        %autorelease
Summary:        Missing YAML 1.2 parser for rust

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/yaml-rust
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
The missing YAML 1.2 parser for rust.}

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
%autosetup -n %{crate}-%{version_no_tilde} -p1
# prevent dependency on /usr/bin/ruby from being generated
chmod -x tests/specs/cpp2rust.rb
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