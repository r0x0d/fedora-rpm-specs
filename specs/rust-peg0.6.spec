# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate peg

Name:           rust-peg0.6
Version:        0.6.3
Release:        %autorelease
Summary:        Simple Parsing Expression Grammar (PEG) parser generator

License:        MIT
URL:            https://crates.io/crates/peg
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
A simple Parsing Expression Grammar (PEG) parser generator.}

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

%package     -n %{name}+trace-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+trace-devel %{_description}

This package contains library source intended for building other packages which
use the "trace" feature of the "%{crate}" crate.

%files       -n %{name}+trace-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep
# drop test that fails harmlessly with Rust 1.69.0 and newer
rm tests/compile-fail/rust_action_type_error.{rs,stderr}
# drop test that fails harmlessly with Rust 1.78.0 and newer
rm tests/compile-fail/rule_args_errors.{rs,stderr}

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