# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate remain

Name:           rust-remain
Version:        0.2.14
Release:        %autorelease
Summary:        Compile-time checks that an enum, struct, or match is written in sorted order

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/remain
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Compile-time checks that an enum, struct, or match is written in sorted
order.}

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