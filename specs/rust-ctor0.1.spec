# Generated by rust2rpm 24
# * no tests are shipped with the published crates
# * example code adds an unnecessary dependency on libc-print (not packaged)
%bcond_with check
%global debug_package %{nil}

%global crate ctor

Name:           rust-ctor0.1
Version:        0.1.26
Release:        %autorelease
Summary:        __attribute__((constructor)) for Rust

License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/ctor
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
__attribute__((constructor)) for Rust.}

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