ExcludeArch: %{ix86}
# Generated by rust2rpm 26
%bcond_without check


%global crate cosmic-screenshot


%global commit 031eb6686196e3dd4d7876ae30572522edc110b9
%global shortcommit %{sub %{commit} 1 7}
%global commitdatestring 2024-07-25 16:39:25 -0400
%global commitdate 20240725

Name:           cosmic-screenshot
Version:        1.0.0~alpha.2
Release:        %autorelease
Summary:        Screenshot utility for the COSMIC Desktop Environment

License:        BSD-3-Clause AND (MIT OR Apache-2.0) AND (Apache-2.0 OR MIT) AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (MIT OR Zlib OR Apache-2.0) AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND MIT AND MPL-2.0

URL:            https://github.com/pop-os/cosmic-screenshot

Source0:        https://github.com/pop-os/cosmic-screenshot/archive/%{commit}/cosmic-screenshot-%{shortcommit}.tar.gz
# To create the below sources:
# * git clone https://github.com/pop-os/cosmic-screenshot at the specified commit
# * cargo vendor > vendor-config-%%{shortcommit}.toml
# * tar -pczf vendor-%%{shortcommit}.tar.gz vendor
Source1:        vendor-%{shortcommit}.tar.gz
# * mv vendor-config-%%{shortcommit}.toml ..
Source2:        vendor-config-%{shortcommit}.toml


BuildRequires:  cargo-rpm-macros >= 26
BuildRequires:  rustc
BuildRequires:  lld
BuildRequires:  cargo
BuildRequires:  just
BuildRequires:  desktop-file-utils

%global _description %{expand:
%{summary}.}

%description %{_description}

%prep
%autosetup -n %{crate}-%{commit} -p1 -a1
%cargo_prep -N
# Check if .cargo/config.toml exists
if [ -f .cargo/config.toml ]; then
  # If it exists, append the contents of %%{SOURCE2} to .cargo/config.toml
  cat %{SOURCE2} >> .cargo/config.toml
  echo "Appended %{SOURCE2} to .cargo/config.toml"
else
  # If it does not exist, append the contents of %%{SOURCE2} to .cargo/config
  cat %{SOURCE2} >> .cargo/config
  echo "Appended %{SOURCE2} to .cargo/config"
fi

%build
# Set vergen environment variables
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}
sed 's/\(.*\) (.*#\(.*\))/\1+git\2/' -i cargo-vendor.txt

%install
# Set vergen environment variables
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
just rootdir=%{buildroot} prefix=%{_prefix} install

# COSMIC is not a valid category pre-fedora 41
%if %{defined fedora} && 0%{?fedora} < 41
desktop-file-install \
--remove-category COSMIC \
--add-category X-COSMIC \
--delete-original \
--dir %{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/com.system76.CosmicScreenshot.desktop
%endif

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/com.system76.CosmicScreenshot.desktop
%if %{with check}
# Set vergen environment variables
export VERGEN_GIT_COMMIT_DATE="date --utc '%{commitdatestring}'"
export VERGEN_GIT_SHA="%{commit}"
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md
%{_bindir}/cosmic-screenshot
%{_datadir}/applications/com.system76.CosmicScreenshot.desktop
%{_datadir}/icons/hicolor/*/apps/com.system76.CosmicScreenshot.svg

%changelog
%autochangelog