# Generated by rust2rpm 23
# * dev-dependencies are outdated
%bcond_with check
%global debug_package %{nil}

%global crate bzip2

Name:           rust-bzip2
Version:        0.4.4
Release:        %autorelease
Summary:        Bindings to libbzip2 exposed as Reader/Writer streams

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/bzip2
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Bindings to libbzip2 for bzip2 compression and decompression exposed as
Reader/Writer streams.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
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

%package     -n %{name}+futures-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-devel %{_description}

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%files       -n %{name}+futures-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tokio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-devel %{_description}

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%files       -n %{name}+tokio-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tokio-io-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-io-devel %{_description}

This package contains library source intended for building other packages which
use the "tokio-io" feature of the "%{crate}" crate.

%files       -n %{name}+tokio-io-devel
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