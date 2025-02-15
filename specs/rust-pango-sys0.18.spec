# Generated by rust2rpm 26
# * tests are broken: https://github.com/gtk-rs/gtk-rs-core/issues/64
%bcond_with check
%global debug_package %{nil}

%global crate pango-sys

Name:           rust-pango-sys0.18
Version:        0.18.0
Release:        %autorelease
Summary:        FFI bindings to libpango-1.0

License:        MIT
URL:            https://crates.io/crates/pango-sys
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
FFI bindings to libpango-1.0.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(pango) >= 1.40

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

%package     -n %{name}+v1_42-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(pango) >= 1.42

%description -n %{name}+v1_42-devel %{_description}

This package contains library source intended for building other packages which
use the "v1_42" feature of the "%{crate}" crate.

%files       -n %{name}+v1_42-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v1_44-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(pango) >= 1.44

%description -n %{name}+v1_44-devel %{_description}

This package contains library source intended for building other packages which
use the "v1_44" feature of the "%{crate}" crate.

%files       -n %{name}+v1_44-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v1_46-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(pango) >= 1.46

%description -n %{name}+v1_46-devel %{_description}

This package contains library source intended for building other packages which
use the "v1_46" feature of the "%{crate}" crate.

%files       -n %{name}+v1_46-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v1_48-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(pango) >= 1.48

%description -n %{name}+v1_48-devel %{_description}

This package contains library source intended for building other packages which
use the "v1_48" feature of the "%{crate}" crate.

%files       -n %{name}+v1_48-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v1_50-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(pango) >= 1.50

%description -n %{name}+v1_50-devel %{_description}

This package contains library source intended for building other packages which
use the "v1_50" feature of the "%{crate}" crate.

%files       -n %{name}+v1_50-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v1_52-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(pango) >= 1.51

%description -n %{name}+v1_52-devel %{_description}

This package contains library source intended for building other packages which
use the "v1_52" feature of the "%{crate}" crate.

%files       -n %{name}+v1_52-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'pkgconfig(pango) >= 1.40'

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
