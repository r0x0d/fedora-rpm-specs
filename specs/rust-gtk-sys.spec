# Generated by rust2rpm 24
# * tests are broken: https://github.com/gtk-rs/gtk-rs-core/issues/64
%bcond_with check
%global debug_package %{nil}

%global crate gtk-sys

Name:           rust-gtk-sys
Version:        0.18.0
Release:        %autorelease
Summary:        FFI bindings to libgtk-3

License:        MIT
URL:            https://crates.io/crates/gtk-sys
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
FFI bindings to libgtk-3.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gtk+-3.0) >= 3.22

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

%package     -n %{name}+v3_24-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gtk+-3.0) >= 3.24

%description -n %{name}+v3_24-devel %{_description}

This package contains library source intended for building other packages which
use the "v3_24" feature of the "%{crate}" crate.

%files       -n %{name}+v3_24-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v3_24_1-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gtk+-3.0) >= 3.24.1

%description -n %{name}+v3_24_1-devel %{_description}

This package contains library source intended for building other packages which
use the "v3_24_1" feature of the "%{crate}" crate.

%files       -n %{name}+v3_24_1-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v3_24_11-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gtk+-3.0) >= 3.24.11

%description -n %{name}+v3_24_11-devel %{_description}

This package contains library source intended for building other packages which
use the "v3_24_11" feature of the "%{crate}" crate.

%files       -n %{name}+v3_24_11-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v3_24_30-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gtk+-3.0) >= 3.24.30

%description -n %{name}+v3_24_30-devel %{_description}

This package contains library source intended for building other packages which
use the "v3_24_30" feature of the "%{crate}" crate.

%files       -n %{name}+v3_24_30-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v3_24_8-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gtk+-3.0) >= 3.24.8

%description -n %{name}+v3_24_8-devel %{_description}

This package contains library source intended for building other packages which
use the "v3_24_8" feature of the "%{crate}" crate.

%files       -n %{name}+v3_24_8-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+v3_24_9-devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gtk+-3.0) >= 3.24.9

%description -n %{name}+v3_24_9-devel %{_description}

This package contains library source intended for building other packages which
use the "v3_24_9" feature of the "%{crate}" crate.

%files       -n %{name}+v3_24_9-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'pkgconfig(gtk+-3.0) >= 3.22'

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