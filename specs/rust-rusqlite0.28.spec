# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate rusqlite

Name:           rust-rusqlite0.28
Version:        0.28.0
Release:        %autorelease
Summary:        Ergonomic wrapper for SQLite

License:        MIT
URL:            https://crates.io/crates/rusqlite
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * bump fallible-iterator dependency from 0.2 to 0.3
# * drop features for building with bundled dependencies
# * drop Windows- and WASM-specific features and dependencies
Patch:          rusqlite-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Ergonomic wrapper for SQLite.}

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

%package     -n %{name}+array-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+array-devel %{_description}

This package contains library source intended for building other packages which
use the "array" feature of the "%{crate}" crate.

%files       -n %{name}+array-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+backup-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+backup-devel %{_description}

This package contains library source intended for building other packages which
use the "backup" feature of the "%{crate}" crate.

%files       -n %{name}+backup-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+blob-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+blob-devel %{_description}

This package contains library source intended for building other packages which
use the "blob" feature of the "%{crate}" crate.

%files       -n %{name}+blob-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+buildtime_bindgen-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+buildtime_bindgen-devel %{_description}

This package contains library source intended for building other packages which
use the "buildtime_bindgen" feature of the "%{crate}" crate.

%files       -n %{name}+buildtime_bindgen-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+chrono-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+chrono-devel %{_description}

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%files       -n %{name}+chrono-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+collation-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+collation-devel %{_description}

This package contains library source intended for building other packages which
use the "collation" feature of the "%{crate}" crate.

%files       -n %{name}+collation-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+column_decltype-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+column_decltype-devel %{_description}

This package contains library source intended for building other packages which
use the "column_decltype" feature of the "%{crate}" crate.

%files       -n %{name}+column_decltype-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+csv-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+csv-devel %{_description}

This package contains library source intended for building other packages which
use the "csv" feature of the "%{crate}" crate.

%files       -n %{name}+csv-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+csvtab-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+csvtab-devel %{_description}

This package contains library source intended for building other packages which
use the "csvtab" feature of the "%{crate}" crate.

%files       -n %{name}+csvtab-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+extra_check-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+extra_check-devel %{_description}

This package contains library source intended for building other packages which
use the "extra_check" feature of the "%{crate}" crate.

%files       -n %{name}+extra_check-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+functions-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+functions-devel %{_description}

This package contains library source intended for building other packages which
use the "functions" feature of the "%{crate}" crate.

%files       -n %{name}+functions-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+hooks-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+hooks-devel %{_description}

This package contains library source intended for building other packages which
use the "hooks" feature of the "%{crate}" crate.

%files       -n %{name}+hooks-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+i128_blob-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+i128_blob-devel %{_description}

This package contains library source intended for building other packages which
use the "i128_blob" feature of the "%{crate}" crate.

%files       -n %{name}+i128_blob-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+lazy_static-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+lazy_static-devel %{_description}

This package contains library source intended for building other packages which
use the "lazy_static" feature of the "%{crate}" crate.

%files       -n %{name}+lazy_static-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+limits-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+limits-devel %{_description}

This package contains library source intended for building other packages which
use the "limits" feature of the "%{crate}" crate.

%files       -n %{name}+limits-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+load_extension-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+load_extension-devel %{_description}

This package contains library source intended for building other packages which
use the "load_extension" feature of the "%{crate}" crate.

%files       -n %{name}+load_extension-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+modern-full-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+modern-full-devel %{_description}

This package contains library source intended for building other packages which
use the "modern-full" feature of the "%{crate}" crate.

%files       -n %{name}+modern-full-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+modern_sqlite-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+modern_sqlite-devel %{_description}

This package contains library source intended for building other packages which
use the "modern_sqlite" feature of the "%{crate}" crate.

%files       -n %{name}+modern_sqlite-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+release_memory-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+release_memory-devel %{_description}

This package contains library source intended for building other packages which
use the "release_memory" feature of the "%{crate}" crate.

%files       -n %{name}+release_memory-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde_json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_json-devel %{_description}

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%files       -n %{name}+serde_json-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+series-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+series-devel %{_description}

This package contains library source intended for building other packages which
use the "series" feature of the "%{crate}" crate.

%files       -n %{name}+series-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+session-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+session-devel %{_description}

This package contains library source intended for building other packages which
use the "session" feature of the "%{crate}" crate.

%files       -n %{name}+session-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+sqlcipher-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+sqlcipher-devel %{_description}

This package contains library source intended for building other packages which
use the "sqlcipher" feature of the "%{crate}" crate.

%files       -n %{name}+sqlcipher-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+time-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+time-devel %{_description}

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%files       -n %{name}+time-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+trace-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+trace-devel %{_description}

This package contains library source intended for building other packages which
use the "trace" feature of the "%{crate}" crate.

%files       -n %{name}+trace-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unlock_notify-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unlock_notify-devel %{_description}

This package contains library source intended for building other packages which
use the "unlock_notify" feature of the "%{crate}" crate.

%files       -n %{name}+unlock_notify-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+url-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+url-devel %{_description}

This package contains library source intended for building other packages which
use the "url" feature of the "%{crate}" crate.

%files       -n %{name}+url-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+uuid-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+uuid-devel %{_description}

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

%files       -n %{name}+uuid-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+vtab-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+vtab-devel %{_description}

This package contains library source intended for building other packages which
use the "vtab" feature of the "%{crate}" crate.

%files       -n %{name}+vtab-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+window-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+window-devel %{_description}

This package contains library source intended for building other packages which
use the "window" feature of the "%{crate}" crate.

%files       -n %{name}+window-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+with-asan-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+with-asan-devel %{_description}

This package contains library source intended for building other packages which
use the "with-asan" feature of the "%{crate}" crate.

%files       -n %{name}+with-asan-devel
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