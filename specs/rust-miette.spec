# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate miette

Name:           rust-miette
Version:        7.2.0
Release:        %autorelease
Summary:        Fancy diagnostic reporting library and protocol for us mere mortals

License:        Apache-2.0
URL:            https://crates.io/crates/miette
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Fancy diagnostic reporting library and protocol for us mere mortals who
aren't compiler hackers.}

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
%doc %{crate_instdir}/CODE_OF_CONDUCT.md
%doc %{crate_instdir}/CONTRIBUTING.md
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

%package     -n %{name}+backtrace-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+backtrace-devel %{_description}

This package contains library source intended for building other packages which
use the "backtrace" feature of the "%{crate}" crate.

%files       -n %{name}+backtrace-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+backtrace-ext-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+backtrace-ext-devel %{_description}

This package contains library source intended for building other packages which
use the "backtrace-ext" feature of the "%{crate}" crate.

%files       -n %{name}+backtrace-ext-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+derive-devel %{_description}

This package contains library source intended for building other packages which
use the "derive" feature of the "%{crate}" crate.

%files       -n %{name}+derive-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+fancy-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fancy-devel %{_description}

This package contains library source intended for building other packages which
use the "fancy" feature of the "%{crate}" crate.

%files       -n %{name}+fancy-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+fancy-base-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fancy-base-devel %{_description}

This package contains library source intended for building other packages which
use the "fancy-base" feature of the "%{crate}" crate.

%files       -n %{name}+fancy-base-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+fancy-no-backtrace-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fancy-no-backtrace-devel %{_description}

This package contains library source intended for building other packages which
use the "fancy-no-backtrace" feature of the "%{crate}" crate.

%files       -n %{name}+fancy-no-backtrace-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+fancy-no-syscall-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fancy-no-syscall-devel %{_description}

This package contains library source intended for building other packages which
use the "fancy-no-syscall" feature of the "%{crate}" crate.

%files       -n %{name}+fancy-no-syscall-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+miette-derive-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+miette-derive-devel %{_description}

This package contains library source intended for building other packages which
use the "miette-derive" feature of the "%{crate}" crate.

%files       -n %{name}+miette-derive-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+no-format-args-capture-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+no-format-args-capture-devel %{_description}

This package contains library source intended for building other packages which
use the "no-format-args-capture" feature of the "%{crate}" crate.

%files       -n %{name}+no-format-args-capture-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+owo-colors-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+owo-colors-devel %{_description}

This package contains library source intended for building other packages which
use the "owo-colors" feature of the "%{crate}" crate.

%files       -n %{name}+owo-colors-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+supports-color-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+supports-color-devel %{_description}

This package contains library source intended for building other packages which
use the "supports-color" feature of the "%{crate}" crate.

%files       -n %{name}+supports-color-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+supports-hyperlinks-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+supports-hyperlinks-devel %{_description}

This package contains library source intended for building other packages which
use the "supports-hyperlinks" feature of the "%{crate}" crate.

%files       -n %{name}+supports-hyperlinks-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+supports-unicode-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+supports-unicode-devel %{_description}

This package contains library source intended for building other packages which
use the "supports-unicode" feature of the "%{crate}" crate.

%files       -n %{name}+supports-unicode-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+syntect-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+syntect-devel %{_description}

This package contains library source intended for building other packages which
use the "syntect" feature of the "%{crate}" crate.

%files       -n %{name}+syntect-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+syntect-highlighter-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+syntect-highlighter-devel %{_description}

This package contains library source intended for building other packages which
use the "syntect-highlighter" feature of the "%{crate}" crate.

%files       -n %{name}+syntect-highlighter-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+terminal_size-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+terminal_size-devel %{_description}

This package contains library source intended for building other packages which
use the "terminal_size" feature of the "%{crate}" crate.

%files       -n %{name}+terminal_size-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+textwrap-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+textwrap-devel %{_description}

This package contains library source intended for building other packages which
use the "textwrap" feature of the "%{crate}" crate.

%files       -n %{name}+textwrap-devel
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