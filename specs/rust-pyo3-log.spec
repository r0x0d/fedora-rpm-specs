# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate pyo3-log

Name:           rust-pyo3-log
Version:        0.10.0
Release:        %autorelease
Summary:        Logging bridge from pyo3 native extension to python

License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/pyo3-log
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * relax stricter-than-SemVer requirement for the syn dev-dependency
Patch:          pyo3-log-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Logging bridge from pyo3 native extension to python.}

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