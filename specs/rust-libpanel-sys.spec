# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate libpanel-sys

Name:           rust-libpanel-sys
Version:        0.5.0
Release:        %autorelease
Summary:        FFI bindings for GNOME libpanel

License:        MIT
URL:            https://crates.io/crates/libpanel-sys
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  pkgconfig(libpanel-1)

%global _description %{expand:
FFI bindings for GNOME libpanel.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(libpanel-1)

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/COPYING
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v1_2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v1_2-devel %{_description}

This package contains library source intended for building other packages which
use the "v1_2" feature of the "%{crate}" crate.

%files       -n %{name}+v1_2-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v1_4-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v1_4-devel %{_description}

This package contains library source intended for building other packages which
use the "v1_4" feature of the "%{crate}" crate.

%files       -n %{name}+v1_4-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v1_8-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+v1_8-devel %{_description}

This package contains library source intended for building other packages which
use the "v1_8" feature of the "%{crate}" crate.

%files       -n %{name}+v1_8-devel
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
# * Skipped tests due to differences in GIR
%cargo_test -- -- --exact --skip cross_validate_constants_with_c --skip cross_validate_layout_with_c
%endif

%changelog
%autochangelog