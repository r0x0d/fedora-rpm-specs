# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate tracing_facade

Name:           rust-tracing_facade
Version:        0.1.0
Release:        %autorelease
Summary:        Facade for tracing

License:        0BSD
URL:            https://crates.io/crates/tracing_facade
Source:         %{crates_source}
# * PR to include license text: https://github.com/jmgao/tracing/pull/4
Source1:        https://raw.githubusercontent.com/jmgao/tracing/master/LICENSE
# Manually created patch for downstream crate metadata changes
# * remove reference to readme file that is not included in published crates
Patch:          tracing_facade-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Facade for tracing.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
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
cp -pav %{SOURCE1} .

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