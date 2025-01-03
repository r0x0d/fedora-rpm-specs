# Generated by rust2rpm 26
%bcond_without check

%global crate desed

Name:           rust-desed
Version:        1.2.2
Release:        %autorelease
Summary:        Sed script debugger

License:        GPL-3.0-or-later
URL:            https://crates.io/crates/desed
Source:         %{crates_source}
# Automatically generated patch to strip dependencies and normalize metadata
Patch:          desed-fix-metadata-auto.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Sed script debugger. Debug and demystify your sed scripts with TUI
debugger.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause OR Apache-2.0 OR MIT
# GPL-3.0-or-later
# ISC
# MIT
# MIT OR Apache-2.0
License:        GPL-3.0-or-later AND ISC AND MIT AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (BSD-2-Clause OR Apache-2.0 OR MIT)
# LICENSE.dependencies contains a full license breakdown
Requires:       sed >= 4.6

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/desed

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
