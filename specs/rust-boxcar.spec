# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate boxcar

Name:           rust-boxcar
Version:        0.2.5
Release:        %autorelease
Summary:        Concurrent, append-only vector

License:        MIT
URL:            https://crates.io/crates/boxcar
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * Exclude benchmarks and other unnecessary files from published crates:
#   https://github.com/ibraheemdev/boxcar/pull/8/commits/0a4ffbad2486a902ac251664e7ce1a64b286e39c
Patch:          boxcar-fix-metadata.diff
# * Include MIT license text for sharded-slab in bench.rs
# * From https://github.com/ibraheemdev/boxcar/pull/8
Patch10:       https://github.com/ibraheemdev/boxcar/pull/8/commits/74c3f316c23d419bc97054c017b94d07bec21b34.patch#/boxcar-sharded-slab-license.patch

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  tomcli

%global _description %{expand:
A concurrent, append-only vector.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/DESIGN.md
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
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
# Do not depend on criterion; it is needed only for benchmarks.
tomcli set Cargo.toml del dev-dependencies.criterion

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