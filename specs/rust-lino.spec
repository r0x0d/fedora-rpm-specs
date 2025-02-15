# Generated by rust2rpm 27
%bcond check 1

%global crate lino

Name:           rust-lino
Version:        0.10.0
Release:        %autorelease
Summary:        Command line text editor with notepad like key bindings

License:        MIT
URL:            https://crates.io/crates/lino
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * bump copypasta dependency from 0.7 to 0.10
# * bump crossterm dependency from 0.22 to 0.28
Patch:          lino-fix-metadata.diff
Patch:          0001-port-from-crossterm-0.23-to-0.28.patch

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A command line text editor with notepad like key bindings.}

%description %{_description}

%package     -n %{crate}
Summary:        %{summary}
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# ISC
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MIT OR Zlib OR Apache-2.0
# Unlicense OR MIT
License:        %{shrink:
    MIT AND
    ISC AND
    Unicode-DFS-2016 AND
    (0BSD OR MIT OR Apache-2.0) AND
    (Apache-2.0 OR BSL-1.0) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND
    (MIT OR Apache-2.0 OR Zlib) AND
    (Unlicense OR MIT)
}
# LICENSE.dependencies contains a full license breakdown

%description -n %{crate} %{_description}

%files       -n %{crate}
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%doc TODO.md
%{_bindir}/lino

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
