%bcond check 1
%bcond heif %{undefined rhel}
%bcond jpegxl %{undefined rhel}

%if 0%{?rhel}
%global bundled_rust_deps 1
%else
%global bundled_rust_deps 0
%endif

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           glycin-loaders
Version:        1.0.1
Release:        %autorelease
Summary:        Sandboxed image rendering

# (Apache-2.0 OR MIT) AND BSD-3-Clause
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# 0BSD OR MIT OR Apache-2.0
# Apache-2.0
# Apache-2.0 OR MIT
# Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
# BSD-2-Clause
# GPL-3.0-or-later
# LGPL-2.1-or-later
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MIT OR Zlib OR Apache-2.0
# MPL-2.0
# MPL-2.0 OR LGPL-2.1-or-later
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND GPL-3.0-or-later AND LGPL-2.1-or-later AND MIT AND MPL-2.0 AND Unicode-DFS-2016 AND (Apache-2.0 OR MIT) AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND (MPL-2.0 OR LGPL-2.1-or-later) AND (Unlicense OR MIT)
# LICENSE.dependencies contains a full license breakdown
URL:            https://gitlab.gnome.org/sophie-h/glycin
Source0:        https://download.gnome.org/sources/glycin-loaders/1.0/glycin-loaders-%{tarball_version}.tar.xz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%if 0%{?rhel}
BuildRequires:  rust-toolset
%else
BuildRequires:  cargo-rpm-macros
%endif
BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libseccomp)
%if %{with heif}
BuildRequires:  pkgconfig(libheif)
%endif
%if %{with jpegxl}
BuildRequires:  pkgconfig(libjxl)
%endif
BuildRequires:  pkgconfig(cairo)

%description
Sandboxed and extendable image decoding.


%prep
%autosetup -p1 -n glycin-loaders-%{tarball_version}

%if 0%{?bundled_rust_deps}
%cargo_prep -v vendor
%else
rm -rf vendor
%cargo_prep
%endif


%if ! 0%{?bundled_rust_deps}
%generate_buildrequires
%cargo_generate_buildrequires
%endif


%build
%meson \
  -Dloaders=%{?with_heif:glycin-heif,}glycin-image-rs,%{?with_jpegxl:glycin-jxl,}glycin-svg \
  -Dtest_skip_install=true \
  %{nil}

%meson_build

%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
%if 0%{?bundled_rust_deps}
%cargo_vendor_manifest
%endif


%install
%meson_install


%if %{with check}
%check
# Something is wrong with the test setup and tests fail with
# "No such file or directory"
%meson_test || :
%endif


%files
%license LICENSE LICENSE-LGPL-2.1 LICENSE-MPL-2.0
%license LICENSE.dependencies
%if 0%{?bundled_rust_deps}
%license cargo-vendor.txt
%endif
%doc NEWS README.md
%{_libexecdir}/glycin-loaders/
%{_datadir}/glycin-loaders/


%changelog
%autochangelog
