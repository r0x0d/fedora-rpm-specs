%global         commit      a2f0f77effb5824690df1851d55754e0fd04cdd0
%global         shortcommit %(c=%{commit}; echo ${c:0:8})
%global         testcommit  1e565931348f15f3f9b654f46ab4bf5fa009ca4f
%global         testshortcommit  %(c=%{testcommit}; echo ${c:0:8})
%global         srcname muon
Name:           muon-meson
Version:        0.3.1^20240926.a2f0f77e
Release:        %{autorelease}
Summary:        C implementation of meson

# Main code is GPL-3.0-only
# MIT src/external/tinyjson.c
# MIT src/memmem.c
# unlicense src/sha_256
# MIT src/external/samurai/graph.c
# MIT src/external/samurai/parse.c
# MIT src/external/samurai/build.c
# MIT src/external/samurai/scan.c
# MIT src/external/samurai/env.c
# MIT src/external/samurai/tree.c
# MIT src/external/samurai/log.c
# MIT src/external/samurai/util.c
# MIT src/external/samurai/deps.c
# MIT src/external/samurai/tool.c
# MIT src/external/samurai/htab.c
# MIT src/external/samurai/samu.c

License:        Apache-2.0 AND GPL-3.0-only AND MIT AND Unlicense
URL:            https://muon.build
Source0:        https://git.sr.ht/~lattis/%{srcname}/archive/%{shortcommit}.tar.gz
Source1:        https://git.sr.ht/~lattis/meson-tests/archive/%{testshortcommit}.tar.gz
# Skip tests which fail due to fedora specific build flags
# These do not fail in normal operation
Patch:          skip-tests.patch

BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libarchive-devel
BuildRequires:  libcurl-devel
BuildRequires:  libpkgconf-devel
BuildRequires:  pkgconf
BuildRequires:  python3-devel
BuildRequires:  python3dist(pyyaml)
BuildRequires:  scdoc

# These are built in to provide needed
# functionality.
Provides:       bundled(memmem)
Provides:       bundled(samurai)
Provides:       bundled(sha_256)
Provides:       bundled(tiny_json)

%description
An implementation of the meson build system in c99 with minimal dependencies.

%prep
%autosetup -n %{srcname}-%{shortcommit} -p 1
tar xf %{SOURCE1}
mv meson-tests-%{testshortcommit} tests/project/meson-tests

%build
CFLAGS="-fPIE -DBOOTSTRAP_NO_TRACY %{optflags}" ./bootstrap.sh %{_vpath_builddir}
%{_vpath_builddir}/muon setup \
 -Dprefix=%{_prefix} \
 -Dwebsite=false \
 -Dstatic=false \
 -Ddocs=enabled \
 -Dsamurai=enabled \
 -Dlibarchive=enabled \
 -Dlibcurl=enabled \
 -Dlibpkgconf=enabled \
 %{_vpath_builddir}
%{_vpath_builddir}/muon -C %{_vpath_builddir} samu

%check
%{_vpath_builddir}/muon -C %{_vpath_builddir} test

%install
DESTDIR=%{buildroot} %{_vpath_builddir}/muon \
       -C %{_vpath_builddir} install

%files
%license LICENSES/Apache-2.0.txt
%license LICENSES/GPL-3.0-only.txt
%license LICENSES/MIT.txt
%license LICENSES/Unlicense.txt
%{_bindir}/muon
%{_mandir}/man1/muon.*
# Conflicts with meson documentation
%exclude %{_mandir}/man5/meson.*


%changelog
%autochangelog
