# Generated by rust2rpm 24
# * most tests require a running user and / or system bus
%bcond_with check
%global debug_package %{nil}

%global crate dbus

Name:           rust-dbus
Version:        0.9.7
Release:        %autorelease
Summary:        Bindings to D-Bus

# Upstream license specification: Apache-2.0/MIT
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/dbus
Source:         %{crates_source}
# Automatically generated patch to strip foreign dependencies
Patch:          dbus-fix-metadata-auto.diff
# Manually created patch for downstream crate metadata changes
# * drop feature for building with and statically linking vendored libdbus
Patch:          dbus-fix-metadata.diff

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Bindings to D-Bus, which is a bus commonly used on Linux for inter-
process communication.}

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
%doc %{crate_instdir}/changes-in-0.7.md
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

%package     -n %{name}+futures-channel-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-channel-devel %{_description}

This package contains library source intended for building other packages which
use the "futures-channel" feature of the "%{crate}" crate.

%files       -n %{name}+futures-channel-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures-executor-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-executor-devel %{_description}

This package contains library source intended for building other packages which
use the "futures-executor" feature of the "%{crate}" crate.

%files       -n %{name}+futures-executor-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures-util-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-util-devel %{_description}

This package contains library source intended for building other packages which
use the "futures-util" feature of the "%{crate}" crate.

%files       -n %{name}+futures-util-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+no-string-validation-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no-string-validation-devel %{_description}

This package contains library source intended for building other packages which
use the "no-string-validation" feature of the "%{crate}" crate.

%files       -n %{name}+no-string-validation-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+stdfd-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+stdfd-devel %{_description}

This package contains library source intended for building other packages which
use the "stdfd" feature of the "%{crate}" crate.

%files       -n %{name}+stdfd-devel
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