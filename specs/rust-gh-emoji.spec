# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate gh-emoji

Name:           rust-gh-emoji
Version:        1.0.8
Release:        %autorelease
Summary:        Convert :emoji: to Unicode using GitHub's emoji names

License:        MIT
URL:            https://crates.io/crates/gh-emoji
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Convert `:emoji:` to Unicode using GitHub's emoji names.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

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