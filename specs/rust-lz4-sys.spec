# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate lz4-sys
%global upstream_version 1.11.1+lz4-1.10.0

Name:           rust-lz4-sys
Version:        1.11.1
Release:        %autorelease
Summary:        Rust LZ4 sys package

License:        MIT
URL:            https://crates.io/crates/lz4-sys
Source:         %{crates_source %{crate} %{upstream_version}}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          lz4-sys-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
# * Depend on pkg-config unconditionally
Patch:          lz4-sys-fix-metadata.diff
# * Link system liblz4 when available
# * https://github.com/10XGenomics/lz4-rs/pull/39
# * Squashed (to omit reverted changes to the top-level Cargo.toml) and adjusted
#   to apply to the released crate; remaining changes to Cargo.toml are applied
#   with “rust2rpm -p” and appear in lz4-sys-fix-metadata.diff.
Patch10:       lz4-sys-1.11.0-system-liblz4.patch

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  pkgconfig(liblz4)

%global _description %{expand:
Rust LZ4 sys package.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(liblz4)

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/CHANGELOG.md
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
%autosetup -n %{crate}-%{upstream_version} -p1
# Remove the bundled copy of liblz4.
rm -rv liblz4
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