# Generated by rust2rpm 27
%bcond check 1

%global crate yubibomb

Name:           rust-yubibomb
Version:        0.2.14
Release:        %autorelease
Summary:        Rust command line tool that prints out a 6-digit random number

License:        GPL-3.0-only
URL:            https://crates.io/crates/yubibomb
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * migrate away from deprecated SPDX license identifier:
#   https://github.com/bowlofeggs/yubibomb/pull/44
Patch:          yubibomb-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Don't you love when you accidentally tap your Yubikey when you have your
IRC client in focus and you send 987947 into Libera? Want to be able to
have that experience without having to reach all the way over to your
laptop's USB port? Now you can!}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# BSD-2-Clause OR Apache-2.0 OR MIT
# GPL-3.0-only
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        GPL-3.0-only AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc CHANGELOG.md
%doc README.md
%{_bindir}/yubibomb

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
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

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
