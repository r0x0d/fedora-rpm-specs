# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate glycin

Name:           rust-glycin
Version:        2.0.1
Release:        %autorelease
Summary:        Sandboxed image decoding

License:        MPL-2.0 OR LGPL-2.1-or-later
URL:            https://crates.io/crates/glycin
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Sandboxed image decoding.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%license %{crate_instdir}/LICENSE-LGPL-2.1
%license %{crate_instdir}/LICENSE-MPL-2.0
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

%package     -n %{name}+async-io-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-io-devel %{_description}

This package contains library source intended for building other packages which
use the "async-io" feature of the "%{crate}" crate.

%files       -n %{name}+async-io-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+gdk4-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gdk4-devel %{_description}

This package contains library source intended for building other packages which
use the "gdk4" feature of the "%{crate}" crate.

%files       -n %{name}+gdk4-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+gobject-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+gobject-devel %{_description}

This package contains library source intended for building other packages which
use the "gobject" feature of the "%{crate}" crate.

%files       -n %{name}+gobject-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tokio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-devel %{_description}

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%files       -n %{name}+tokio-devel
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
# * skip a doctest that doesn't compile
%cargo_test -- -- --skip 'src/lib.rs'
%endif

%changelog
%autochangelog