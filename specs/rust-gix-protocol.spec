# Generated by rust2rpm 26
# * Deactivate tests because of a missing dev-dependency (gix-testtools)
# * See https://github.com/Byron/gitoxide/discussions/900 for more information
%bcond_with check
%global debug_package %{nil}

%global crate gix-protocol

Name:           rust-gix-protocol
Version:        0.45.3
Release:        %autorelease
Summary:        Git protocols implementation

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gix-protocol
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A crate of the gitoxide project for implementing git protocols.}

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
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async-client-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-client-devel %{_description}

This package contains library source intended for building other packages which
use the "async-client" feature of the "%{crate}" crate.

%files       -n %{name}+async-client-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async-trait-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-trait-devel %{_description}

This package contains library source intended for building other packages which
use the "async-trait" feature of the "%{crate}" crate.

%files       -n %{name}+async-trait-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+blocking-client-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+blocking-client-devel %{_description}

This package contains library source intended for building other packages which
use the "blocking-client" feature of the "%{crate}" crate.

%files       -n %{name}+blocking-client-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+document-features-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+document-features-devel %{_description}

This package contains library source intended for building other packages which
use the "document-features" feature of the "%{crate}" crate.

%files       -n %{name}+document-features-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures-io-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-io-devel %{_description}

This package contains library source intended for building other packages which
use the "futures-io" feature of the "%{crate}" crate.

%files       -n %{name}+futures-io-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures-lite-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-lite-devel %{_description}

This package contains library source intended for building other packages which
use the "futures-lite" feature of the "%{crate}" crate.

%files       -n %{name}+futures-lite-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
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