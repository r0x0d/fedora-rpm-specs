# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

# prevent executables from being installed
%global cargo_install_bin 0

%global crate minicbor

Name:           rust-minicbor
Version:        0.25.1
Release:        %autorelease
Summary:        Small CBOR codec suitable for no_std environments

License:        BlueOak-1.0.0
URL:            https://crates.io/crates/minicbor
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 26

%global _description %{expand:
A small CBOR codec suitable for no_std environments.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE.md
%doc %{crate_instdir}/CONTRIBUTING.md
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

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+derive-devel %{_description}

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%files       -n %{name}+derive-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+full-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+full-devel %{_description}

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

%files       -n %{name}+full-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+half-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+half-devel %{_description}

This package contains library source intended for building other packages which
use the "half" feature of the "%{crate}" crate.

%files       -n %{name}+half-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+minicbor-derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+minicbor-derive-devel %{_description}

This package contains library source intended for building other packages which
use the "minicbor-derive" feature of the "%{crate}" crate.

%files       -n %{name}+minicbor-derive-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -f half,std

%build
%cargo_build -f half,std

%install
%cargo_install -f half,std

%if %{with check}
%check
%cargo_test -f half,std
%endif

%changelog
%autochangelog