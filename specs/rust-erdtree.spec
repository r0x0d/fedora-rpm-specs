# Generated by rust2rpm 24
%bcond_without check

%global crate erdtree

Name:           rust-erdtree
Version:        3.1.2
Release:        %autorelease
Summary:        Cross-platform multi-threaded filesystem and disk usage analysis tool

License:        MIT
URL:            https://crates.io/crates/erdtree
Source:         %{crates_source}
# Automatically generated patch to strip foreign dependencies
Patch:          erdtree-fix-metadata-auto.diff

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Erdtree (erd) is a cross-platform, multi-threaded, and general purpose
filesystem and disk usage utility that is aware of .gitignore and hidden
file rules.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# Output of "cargo_license_summary" macro
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# MPL-2.0
# Unlicense OR MIT
License:        MIT AND Unicode-DFS-2016 AND (Apache-2.0 OR MIT) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND MPL-2.0 AND (Unlicense OR MIT)

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc CHANGELOG.md
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc README.md
%doc SECURITY.md
%{_bindir}/erd

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog