# Generated by rust2rpm 23
%bcond_without check
%global debug_package %{nil}

%global crate cursive_core

Name:           rust-cursive_core
Version:        0.3.7
Release:        %autorelease
Summary:        Core components for the Cursive TUI

License:        MIT
URL:            https://crates.io/crates/cursive_core
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop ansi and ansi-parser (missing deps include ufmt with test failures)
Patch:          cursive_core-fix-metadata.diff

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Core components for the Cursive TUI.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/Readme.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+doc-cfg-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+doc-cfg-devel %{_description}

This package contains library source intended for building other packages which
use the "doc-cfg" feature of the "%{crate}" crate.

%files       -n %{name}+doc-cfg-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+markdown-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+markdown-devel %{_description}

This package contains library source intended for building other packages which
use the "markdown" feature of the "%{crate}" crate.

%files       -n %{name}+markdown-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pulldown-cmark-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pulldown-cmark-devel %{_description}

This package contains library source intended for building other packages which
use the "pulldown-cmark" feature of the "%{crate}" crate.

%files       -n %{name}+pulldown-cmark-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+toml-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+toml-devel %{_description}

This package contains library source intended for building other packages which
use the "toml" feature of the "%{crate}" crate.

%files       -n %{name}+toml-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unstable_scroll-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable_scroll-devel %{_description}

This package contains library source intended for building other packages which
use the "unstable_scroll" feature of the "%{crate}" crate.

%files       -n %{name}+unstable_scroll-devel
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