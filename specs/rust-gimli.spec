# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate gimli

Name:           rust-gimli
Version:        0.31.1
Release:        %autorelease
Summary:        Library for reading and writing the DWARF debugging format

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/gimli
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * remove dependencies on compiler internals
Patch:          gimli-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A library for reading and writing the DWARF debugging format.}

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

%package     -n %{name}+endian-reader-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+endian-reader-devel %{_description}

This package contains library source intended for building other packages which
use the "endian-reader" feature of the "%{crate}" crate.

%files       -n %{name}+endian-reader-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+fallible-iterator-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fallible-iterator-devel %{_description}

This package contains library source intended for building other packages which
use the "fallible-iterator" feature of the "%{crate}" crate.

%files       -n %{name}+fallible-iterator-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+read-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+read-devel %{_description}

This package contains library source intended for building other packages which
use the "read" feature of the "%{crate}" crate.

%files       -n %{name}+read-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+read-all-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+read-all-devel %{_description}

This package contains library source intended for building other packages which
use the "read-all" feature of the "%{crate}" crate.

%files       -n %{name}+read-all-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+read-core-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+read-core-devel %{_description}

This package contains library source intended for building other packages which
use the "read-core" feature of the "%{crate}" crate.

%files       -n %{name}+read-core-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+write-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+write-devel %{_description}

This package contains library source intended for building other packages which
use the "write" feature of the "%{crate}" crate.

%files       -n %{name}+write-devel
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
