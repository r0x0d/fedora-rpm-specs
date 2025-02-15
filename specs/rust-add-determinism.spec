# Generated by rust2rpm 26
%bcond_without check

# prevent library files from being installed
%global cargo_install_lib 0

%global crate add-determinism

Name:           rust-add-determinism
Version:        0.6.0
Release:        %autorelease
Summary:        RPM buildroot helper to strip nondeterministic bits in files

License:        GPL-3.0-or-later
URL:            https://crates.io/crates/add-determinism
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 26

%global _description %{expand:
RPM buildroot helper to strip nondeterministic bits in files.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# GPL-3.0-or-later
# MIT
# MIT OR Apache-2.0
# MIT OR Zlib OR Apache-2.0
# Unlicense OR MIT
License:        GPL-3.0-or-later AND MIT AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE.GPL3
%license LICENSE.dependencies
%doc README.md
%{_bindir}/add-determinism

%package     -n build-reproducibility-srpm-macros
Summary:     Configuration to integrate add-determinism in package builds
BuildArch:   noarch
Requires:    add-determinism = %{version}-%{release}

%description -n build-reproducibility-srpm-macros
%{summary}.

This package is intended to be pulled in by redhat-rpm-config.

%files       -n build-reproducibility-srpm-macros
%{rpmmacrodir}/macros.build-reproducibility

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} >LICENSE.dependencies

%install
%cargo_install
install -m0644 -Dt %{buildroot}%{rpmmacrodir} rpm/macros.build-reproducibility

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
