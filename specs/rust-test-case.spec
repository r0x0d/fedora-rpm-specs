# Generated by rust2rpm 25
%bcond_without check
%global debug_package %{nil}

%global crate test-case

Name:           rust-test-case
Version:        3.3.1
Release:        %autorelease
Summary:        Procedural macro attribute for generating parametrized test cases

License:        MIT
URL:            https://crates.io/crates/test-case
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop acceptance tests that are not included in published crates
# * exclude some files that are only useful for upstream development
Patch:          test-case-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Provides #[test_case(...)] procedural macro attribute for generating
parametrized test cases easily.}

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

%package     -n %{name}+regex-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+regex-devel %{_description}

This package contains library source intended for building other packages which
use the "regex" feature of the "%{crate}" crate.

%files       -n %{name}+regex-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+with-regex-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-regex-devel %{_description}

This package contains library source intended for building other packages which
use the "with-regex" feature of the "%{crate}" crate.

%files       -n %{name}+with-regex-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
# integration tests rely on files that are not included in published crates
rm tests/acceptance_tests.rs

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