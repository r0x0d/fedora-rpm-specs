# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate multipart-rs

Name:           rust-multipart-rs
Version:        0.1.11
Release:        %autorelease
Summary:        Simple, zero-allocation, streaming, async multipart reader & writer for Rust

License:        MIT
URL:            https://crates.io/crates/multipart-rs
Source:         %{crates_source}
# add missing license text
# https://github.com/feliwir/multipart-rs/pull/2
Source:         https://raw.githubusercontent.com/michel-slm/multipart-rs/refs/heads/add-license/LICENSE

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A simple, zero-allocation, streaming, async multipart reader & writer
for Rust.}

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

%prep
%autosetup -n %{crate}-%{version} -p1
# copy in license file
cp -p %{SOURCE1} .
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
