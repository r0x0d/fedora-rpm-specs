# Generated by rust2rpm 23
%bcond_without check
%global debug_package %{nil}

%global crate freetype-sys

Name:           rust-freetype-sys0.13
Version:        0.13.1
Release:        %autorelease
Summary:        Low level binding for FreeType font library

License:        MIT
URL:            https://crates.io/crates/freetype-sys
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Low level binding for FreeType font library.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(freetype2) >= 18.5.12

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
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
%autosetup -n %{crate}-%{version_no_tilde} -p1
# remove the bundled copy to make sure we're linking against the system lib
rm -vr freetype2
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires
echo 'pkgconfig(freetype2) >= 18.5.12'

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