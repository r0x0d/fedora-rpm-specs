# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate prettytable-rs

Name:           rust-prettytable-rs
Version:        0.10.0
Release:        %autorelease
Summary:        Library for printing pretty formatted tables in terminal

License:        BSD-3-Clause
URL:            https://crates.io/crates/prettytable-rs
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * prevent useless executable from being built and shipped
Patch:          prettytable-rs-fix-metadata.diff

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
A library for printing pretty formatted tables in terminal.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE.txt
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

%package     -n %{name}+csv-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+csv-devel %{_description}

This package contains library source intended for building other packages which
use the "csv" feature of the "%{crate}" crate.

%files       -n %{name}+csv-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+evcxr-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+evcxr-devel %{_description}

This package contains library source intended for building other packages which
use the "evcxr" feature of the "%{crate}" crate.

%files       -n %{name}+evcxr-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+win_crlf-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+win_crlf-devel %{_description}

This package contains library source intended for building other packages which
use the "win_crlf" feature of the "%{crate}" crate.

%files       -n %{name}+win_crlf-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
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