# Generated by rust2rpm 24
# * tests fail to compile with recent versions of Rust:
#   https://github.com/reem/rust-mac/issues/15
%bcond_with check
%global debug_package %{nil}

%global crate mac

Name:           rust-mac
Version:        0.1.1
Release:        %autorelease
Summary:        Collection of great and ubiqutitous macros

# Upstream license specification: MIT/Apache-2.0
# https://github.com/reem/rust-mac/issues/14
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/mac
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
A collection of great and ubiqutitous macros.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
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