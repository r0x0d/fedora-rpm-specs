# Generated by rust2rpm 24
# * missing dev-dependency: rand_hc ^0.2
%bcond_with check
%global debug_package %{nil}

%global crate rand

Name:           rust-rand0.7
Version:        0.7.3
Release:        %autorelease
Summary:        Random number generators and other randomness functionality

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rand
Source:         %{crates_source}
# Automatically generated patch to strip foreign dependencies
Patch:          rand-fix-metadata-auto.diff

BuildRequires:  rust-packaging >= 21

%global _description %{expand:
Random number generators and other randomness functionality.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/COPYRIGHT
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/SECURITY.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+getrandom-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+getrandom-devel %{_description}

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%files       -n %{name}+getrandom-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+getrandom_package-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+getrandom_package-devel %{_description}

This package contains library source intended for building other packages which
use the "getrandom_package" feature of the "%{crate}" crate.

%files       -n %{name}+getrandom_package-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+libc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+libc-devel %{_description}

This package contains library source intended for building other packages which
use the "libc" feature of the "%{crate}" crate.

%files       -n %{name}+libc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+log-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+log-devel %{_description}

This package contains library source intended for building other packages which
use the "log" feature of the "%{crate}" crate.

%files       -n %{name}+log-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rand_pcg-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rand_pcg-devel %{_description}

This package contains library source intended for building other packages which
use the "rand_pcg" feature of the "%{crate}" crate.

%files       -n %{name}+rand_pcg-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde1-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde1-devel %{_description}

This package contains library source intended for building other packages which
use the "serde1" feature of the "%{crate}" crate.

%files       -n %{name}+serde1-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+small_rng-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+small_rng-devel %{_description}

This package contains library source intended for building other packages which
use the "small_rng" feature of the "%{crate}" crate.

%files       -n %{name}+small_rng-devel
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