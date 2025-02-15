# Generated by rust2rpm 26
%bcond_without check

# prevent library files from being installed
%global cargo_install_lib 0

%global crate rublk

Name:           rust-rublk
Version:        0.2.3
Release:        %autorelease
Summary:        Rust ublk generic targets

License:        GPL-2.0-or-later
URL:            https://crates.io/crates/rublk
Source:         %{crates_source}
Source:         rublk-0.2.3-vendor.tar.xz

BuildRequires:  cargo-rpm-macros >= 26
# dependency for vendored bindgen crate
BuildRequires:  clang-libs

%global _description %{expand:
Rust ublk generic targets.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# rublk and crate dependencies:
# =============================
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-3-Clause
# GPL-2.0-or-later
# MIT
# MIT OR Zlib OR Apache-2.0
# MPL-2.0+
# Unlicense OR MIT
# code derived from Unicode data:
# Unicode-DFS-2016 (in regex-syntax)
License:        (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND BSD-3-Clause AND GPL-2.0-or-later AND MIT AND (MIT OR Zlib OR Apache-2.0) AND MPL-2.0+ AND (Unlicense OR MIT) AND Unicode-DFS-2016
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%files       -n %{crate}
%license COPYING
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/rublk

%prep
%autosetup -n %{crate}-%{version} -p1 -a1
%cargo_prep -v vendor

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
