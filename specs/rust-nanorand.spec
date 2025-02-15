# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate nanorand

Name:           rust-nanorand
Version:        0.7.0
Release:        %autorelease
Summary:        Tiny, fast, zero-dep library for random number generation

License:        Zlib
URL:            https://crates.io/crates/nanorand
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * drop WASM-specific getrandom/js feature
Patch:          nanorand-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
A tiny, fast, zero-dep library for random number generation.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE.md
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

%package     -n %{name}+alloc-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+alloc-devel %{_description}

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%files       -n %{name}+alloc-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+chacha-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+chacha-devel %{_description}

This package contains library source intended for building other packages which
use the "chacha" feature of the "%{crate}" crate.

%files       -n %{name}+chacha-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+getrandom-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+getrandom-devel %{_description}

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%files       -n %{name}+getrandom-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+pcg64-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+pcg64-devel %{_description}

This package contains library source intended for building other packages which
use the "pcg64" feature of the "%{crate}" crate.

%files       -n %{name}+pcg64-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rdseed-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rdseed-devel %{_description}

This package contains library source intended for building other packages which
use the "rdseed" feature of the "%{crate}" crate.

%files       -n %{name}+rdseed-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tls-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tls-devel %{_description}

This package contains library source intended for building other packages which
use the "tls" feature of the "%{crate}" crate.

%files       -n %{name}+tls-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+wyrand-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wyrand-devel %{_description}

This package contains library source intended for building other packages which
use the "wyrand" feature of the "%{crate}" crate.

%files       -n %{name}+wyrand-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+zeroize-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+zeroize-devel %{_description}

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

%files       -n %{name}+zeroize-devel
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
