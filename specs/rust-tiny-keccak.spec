# Generated by rust2rpm 24
%bcond_without check
%global debug_package %{nil}

%global crate tiny-keccak

Name:           rust-tiny-keccak
Version:        2.0.2
Release:        %autorelease
Summary:        Implementation of Keccak derived functions

License:        CC0-1.0
URL:            https://crates.io/crates/tiny-keccak
Source:         %{crates_source}

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
An implementation of Keccak derived functions.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE
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

%package     -n %{name}+cshake-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cshake-devel %{_description}

This package contains library source intended for building other packages which
use the "cshake" feature of the "%{crate}" crate.

%files       -n %{name}+cshake-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+fips202-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fips202-devel %{_description}

This package contains library source intended for building other packages which
use the "fips202" feature of the "%{crate}" crate.

%files       -n %{name}+fips202-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+k12-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+k12-devel %{_description}

This package contains library source intended for building other packages which
use the "k12" feature of the "%{crate}" crate.

%files       -n %{name}+k12-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+keccak-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+keccak-devel %{_description}

This package contains library source intended for building other packages which
use the "keccak" feature of the "%{crate}" crate.

%files       -n %{name}+keccak-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+kmac-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+kmac-devel %{_description}

This package contains library source intended for building other packages which
use the "kmac" feature of the "%{crate}" crate.

%files       -n %{name}+kmac-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+parallel_hash-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+parallel_hash-devel %{_description}

This package contains library source intended for building other packages which
use the "parallel_hash" feature of the "%{crate}" crate.

%files       -n %{name}+parallel_hash-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+sha3-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sha3-devel %{_description}

This package contains library source intended for building other packages which
use the "sha3" feature of the "%{crate}" crate.

%files       -n %{name}+sha3-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+shake-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+shake-devel %{_description}

This package contains library source intended for building other packages which
use the "shake" feature of the "%{crate}" crate.

%files       -n %{name}+shake-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+sp800-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sp800-devel %{_description}

This package contains library source intended for building other packages which
use the "sp800" feature of the "%{crate}" crate.

%files       -n %{name}+sp800-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tuple_hash-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tuple_hash-devel %{_description}

This package contains library source intended for building other packages which
use the "tuple_hash" feature of the "%{crate}" crate.

%files       -n %{name}+tuple_hash-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -a

%build
%cargo_build -a

%install
%cargo_install -a

%if %{with check}
%check
%cargo_test -a
%endif

%changelog
%autochangelog
