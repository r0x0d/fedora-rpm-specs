# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate jwalk

Name:           rust-jwalk0.6
Version:        0.6.2
Release:        %autorelease
Summary:        Filesystem walk performed in parallel with streamed and sorted results

License:        MIT
URL:            https://crates.io/crates/jwalk
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * bump rayon dependency from 1.5 to 1.6.1 to fix a deadlock in parallel code
# * drop unused, benchmark-only criterion dev-dependency to speed up builds
Patch:          jwalk-fix-metadata.diff

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Filesystem walk performed in parallel with streamed and sorted results.}

%description %{_description}

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