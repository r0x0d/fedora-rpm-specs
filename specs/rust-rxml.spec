# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate rxml

Name:           rust-rxml
Version:        0.9.1
Release:        %autorelease
Summary:        Minimalistic, restricted XML 1.0 parser which does not include dangerous XML features

License:        MIT
URL:            https://crates.io/crates/rxml
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop unused, benchmark-only criterion dev-dependency to speed up builds
Patch:          rxml-fix-metadata.diff

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Minimalistic, restricted XML 1.0 parser which does not include dangerous
XML features.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/COPYING
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

%package     -n %{name}+async-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-devel %{_description}

This package contains library source intended for building other packages which
use the "async" feature of the "%{crate}" crate.

%files       -n %{name}+async-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures-core-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-core-devel %{_description}

This package contains library source intended for building other packages which
use the "futures-core" feature of the "%{crate}" crate.

%files       -n %{name}+futures-core-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+macros-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+macros-devel %{_description}

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%files       -n %{name}+macros-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+mt-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+mt-devel %{_description}

This package contains library source intended for building other packages which
use the "mt" feature of the "%{crate}" crate.

%files       -n %{name}+mt-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pin-project-lite-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pin-project-lite-devel %{_description}

This package contains library source intended for building other packages which
use the "pin-project-lite" feature of the "%{crate}" crate.

%files       -n %{name}+pin-project-lite-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rxml_proc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rxml_proc-devel %{_description}

This package contains library source intended for building other packages which
use the "rxml_proc" feature of the "%{crate}" crate.

%files       -n %{name}+rxml_proc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+shared_ns-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+shared_ns-devel %{_description}

This package contains library source intended for building other packages which
use the "shared_ns" feature of the "%{crate}" crate.

%files       -n %{name}+shared_ns-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+stream-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+stream-devel %{_description}

This package contains library source intended for building other packages which
use the "stream" feature of the "%{crate}" crate.

%files       -n %{name}+stream-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tokio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-devel %{_description}

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%files       -n %{name}+tokio-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+weak-table-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+weak-table-devel %{_description}

This package contains library source intended for building other packages which
use the "weak-table" feature of the "%{crate}" crate.

%files       -n %{name}+weak-table-devel
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
