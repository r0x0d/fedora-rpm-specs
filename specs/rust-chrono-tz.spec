# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate chrono-tz

Name:           rust-chrono-tz
Version:        0.9.0
Release:        %autorelease
Summary:        TimeZone implementations for chrono from the IANA database

# * chrono-tz code is MIT OR Apache-2.0
# * bundled Olson timezone database is Public Domain
License:        (MIT OR Apache-2.0) AND LicenseRef-Fedora-Public-Domain
URL:            https://crates.io/crates/chrono-tz
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
TimeZone implementations for chrono from the IANA database.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Provides:       bundled(tzdata) = 2024a

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
%license %{crate_instdir}/tz/LICENSE
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

%package     -n %{name}+arbitrary-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+arbitrary-devel %{_description}

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%files       -n %{name}+arbitrary-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+case-insensitive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+case-insensitive-devel %{_description}

This package contains library source intended for building other packages which
use the "case-insensitive" feature of the "%{crate}" crate.

%files       -n %{name}+case-insensitive-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+filter-by-regex-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+filter-by-regex-devel %{_description}

This package contains library source intended for building other packages which
use the "filter-by-regex" feature of the "%{crate}" crate.

%files       -n %{name}+filter-by-regex-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
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