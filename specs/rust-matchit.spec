# Generated by rust2rpm 26
# * missing dev-dependencies: gonzales =0.0.3-beta
%bcond_with check
%global debug_package %{nil}

%global crate matchit

Name:           rust-matchit
Version:        0.8.4
Release:        %autorelease
Summary:        High performance, zero-copy URL router

License:        MIT AND BSD-3-Clause
URL:            https://crates.io/crates/matchit
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A high performance, zero-copy URL router.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%license %{crate_instdir}/LICENSE.httprouter
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