# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate xkeysym

Name:           rust-xkeysym
Version:        0.2.1
Release:        %autorelease
Summary:        Library for working with X11 keysyms

License:        MIT OR Apache-2.0 OR Zlib
URL:            https://crates.io/crates/xkeysym
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * relax x11rb dependency from ^0.12 to >=0.12,<0.14
Patch:          xkeysym-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A library for working with X11 keysyms.}

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
%license %{crate_instdir}/LICENSE-ZLIB
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

%package     -n %{name}+bytemuck-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bytemuck-devel %{_description}

This package contains library source intended for building other packages which
use the "bytemuck" feature of the "%{crate}" crate.

%files       -n %{name}+bytemuck-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
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