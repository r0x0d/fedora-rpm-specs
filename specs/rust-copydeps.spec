# Generated by rust2rpm 24
%bcond_without check

%global crate copydeps

Name:           rust-copydeps
Version:        5.0.1
Release:        %autorelease
Summary:        Find and copy all the .so / .dll files needed by an executable

License:        GPL-3.0-or-later
URL:            https://crates.io/crates/copydeps
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 23

%global _description %{expand:
Find and copy all the .so / .dll files needed by an executable.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# GPL-3.0-or-later
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
License:        GPL-3.0-or-later AND MIT AND Unicode-DFS-2016 AND (MIT OR Apache-2.0) AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENCE.txt
%license LICENSE.dependencies
%doc README.md
%{_bindir}/copydeps
%{_mandir}/man1/%{crate}.1*
%{bash_completions_dir}/%{crate}

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install
install -m 644 -Dp misc/%{crate}.man %{buildroot}%{_mandir}/man1/%{crate}.1
install -m 644 -Dp misc/%{crate}.bash-completion %{buildroot}%{bash_completions_dir}/%{crate}

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
