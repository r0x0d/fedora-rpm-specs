# Generated by rust2rpm 24
# * tests require pre-releases of various tokio crates
# * tests are unreliable: https://github.com/seanmonstar/want/issues/2
%bcond_with check
%global debug_package %{nil}

%global crate want

Name:           rust-want
Version:        0.3.1
Release:        %autorelease
Summary:        Detect when another Future wants a result

License:        MIT
URL:            https://crates.io/crates/want
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Detect when another Future wants a result.}

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
