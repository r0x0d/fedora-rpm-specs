# Generated by rust2rpm 26
# * tests can only be run in-tree
%bcond_with check
%global debug_package %{nil}

%global crate hyper-util

Name:           rust-hyper-util
Version:        0.1.8
Release:        %autorelease
Summary:        Hyper utilities

License:        MIT
URL:            https://crates.io/crates/hyper-util
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Hyper utilities.}

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

%package     -n %{name}+client-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+client-devel %{_description}

This package contains library source intended for building other packages which
use the "client" feature of the "%{crate}" crate.

%files       -n %{name}+client-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+client-legacy-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+client-legacy-devel %{_description}

This package contains library source intended for building other packages which
use the "client-legacy" feature of the "%{crate}" crate.

%files       -n %{name}+client-legacy-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+full-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+full-devel %{_description}

This package contains library source intended for building other packages which
use the "full" feature of the "%{crate}" crate.

%files       -n %{name}+full-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+http1-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+http1-devel %{_description}

This package contains library source intended for building other packages which
use the "http1" feature of the "%{crate}" crate.

%files       -n %{name}+http1-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+http2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+http2-devel %{_description}

This package contains library source intended for building other packages which
use the "http2" feature of the "%{crate}" crate.

%files       -n %{name}+http2-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+server-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+server-devel %{_description}

This package contains library source intended for building other packages which
use the "server" feature of the "%{crate}" crate.

%files       -n %{name}+server-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+server-auto-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+server-auto-devel %{_description}

This package contains library source intended for building other packages which
use the "server-auto" feature of the "%{crate}" crate.

%files       -n %{name}+server-auto-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+server-graceful-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+server-graceful-devel %{_description}

This package contains library source intended for building other packages which
use the "server-graceful" feature of the "%{crate}" crate.

%files       -n %{name}+server-graceful-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+service-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+service-devel %{_description}

This package contains library source intended for building other packages which
use the "service" feature of the "%{crate}" crate.

%files       -n %{name}+service-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tokio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-devel %{_description}

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%files       -n %{name}+tokio-devel
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