## NOTE: Lots of files in various subdirectories have the same name (such as
## "LICENSE") so this short macro allows us to distinguish them by using their
## directory names (from the source tree) as prefixes for the files.
%global add_to_license_files() \
        mkdir -p _license_files ; \
        cp -p %1 _license_files/$(echo '%1' | sed -e 's!/!.!g')

# Build documentation by default (use `rpmbuild --without docs` to override it).
# This is used by Coverity. Coverity injects custom compiler warnings, but
# any warning during WebKit docs build is fatal!
%bcond_without docs

# Clang is preferred: https://skia.org/docs/user/build/#supported-and-preferred-compilers
# But it is broken due to https://bugzilla.redhat.com/show_bug.cgi?id=2341532
#%%global toolchain clang

# We run out of memory if building with LTO enabled on i686.
%ifarch %{ix86}
%global _lto_cflags %{nil}
%endif

Name:           webkitgtk
Version:        2.47.3
Release:        %autorelease
Summary:        GTK web content engine library

# Source/bmalloc/bmalloc/*.h is BSD-2-Clause
# Source/bmalloc/bmalloc/CryptoRandom.cpp is ISC
# Source/bmalloc/bmalloc/valgrind.h is is bzip2-1.0.6
# Source/bmalloc/libpas/src/test/RedBlackTreeTests.cpp is BSD-3-Clause
# Source/JavaScriptCore/config.h is LGPL-2.0-or-later
# Source/JavaScriptCore/b3/B3ComputeDivisionMagic.h is NCSA
# Source/JavaScriptCore/disassembler/zydis/* is MIT
# Source/JavaScriptCore/runtime/JSDateMath.h is MPL 1.1/GPL 2.0/LGPL 2.1
# Source/JavaScriptCore/runtime/MathCommon.cpp is SunPro
# Source/JavaScriptCore/ucd/CaseFolding.txt is Unicode-TOU
# Source/ThirdParty/ANGLE/include/CL/cl_d3d10.h is Apache-2.0
# Source/ThirdParty/ANGLE/include/GLES/gl.h is MIT-Khronos (not on list see https://github.com/spdx/license-list-XML/issues/2017)
# Source/ThirdParty/ANGLE/src/compiler/preprocessor/preprocessor_tab_autogen.cpp is GPL-3.0-or-later WITH Bison-exception-2.2
# Source/ThirdParty/ANGLE/tools/flex-bison/third_party/m4sugar/m4sugar.m4 is GPL-3.0-only WITH Autoconf-exception-3.0
# Source/ThirdParty/pdfjs/web/images/annotation-paperclip.svg is MPL-2.0i
# Source/ThirdParty/pdfjs/web/standard_fonts/LICENSE_LIBERATION is OFL-1.1
# Source/ThirdParty/xdgmime/ is AFL-2.0 OR GPL-2.0-or-later
# Source/WebCore/dom/PseudoElement.h is BSD-Source-Code
# Source/WebCore/dom/SecurityContext.cpp is BSD-2-Clause-Views
# Source/WebKit/UIProcess/Launcher/glib/BubblewrapLauncher.cpp is LGPL-2.1-or-later
# Source/WTF/LICENSE-libc++.txt is NCSA OR MIT
# Source/WTF/LICENSE-LLVM.txt is Apache-2.0 WITH LLVM-exception
# Source/WTF/icu/LICENSE is ICU
# Source/WTF/wtf/Markable.h is BSL-1.0
# The license tag and above comment is up to date as of WebKitGTK 2.42.2.
License:        LGPL-2.1-only AND BSD-2-Clause AND BSD-3-Clause AND ISC AND bzip2-1.0.6 AND NCSA AND MIT AND GPL-2.0-only AND MPL-1.1 AND SunPro AND Unicode-TOU AND Apache-2.0 AND GPL-3.0-or-later WITH Bison-exception-2.2 AND GPL-3.0-only WITH Autoconf-exception-3.0 AND MPL-2.0 AND OFL-1.1 AND (AFL-2.0 OR GPL-2.0-or-later) AND BSD-Source-Code AND BSD-2-Clause-Views AND LGPL-2.1-or-later AND (NCSA OR MIT) AND Apache-2.0 WITH LLVM-exception AND ICU AND BSL-1.0
URL:            https://www.webkitgtk.org/
Source0:        https://webkitgtk.org/releases/webkitgtk-%{version}.tar.xz
Source1:        https://webkitgtk.org/releases/webkitgtk-%{version}.tar.xz.asc
# Use the keys from https://webkitgtk.org/verifying.html
# $ gpg --import aperez.key carlosgc.key
# $ gpg --export --export-options export-minimal 013A0127AC9C65B34FFA62526C1009B693975393 5AA3BC334FD7E3369E7C77B291C559DBE4C9123B > webkitgtk-keys.gpg
Source2:        webkitgtk-keys.gpg

# https://bugs.webkit.org/show_bug.cgi?id=286433
Patch:          ipint-linker-error.patch

BuildRequires:  bison
BuildRequires:  bubblewrap
BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  flite-devel
BuildRequires:  gettext
BuildRequires:  gi-docgen
BuildRequires:  git
BuildRequires:  gnupg2
BuildRequires:  gperf
BuildRequires:  hyphen-devel
BuildRequires:  libatomic
BuildRequires:  ninja-build
BuildRequires:  openssl-devel
BuildRequires:  perl(English)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(bigint)
BuildRequires:  python3
BuildRequires:  ruby
BuildRequires:  rubygems
BuildRequires:  rubygem(getoptlong)
BuildRequires:  rubygem-json
BuildRequires:  unifdef
BuildRequires:  xdg-dbus-proxy

BuildRequires:  pkgconfig(atspi-2)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libgcrypt)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libtasn1)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwoff2dec)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(manette-0.2)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(sysprof-capture-4)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(xt)

# Filter out provides for private libraries
%global __provides_exclude_from ^(%{_libdir}/webkit2gtk-4\\.0/.*\\.so|%{_libdir}/webkit2gtk-4\\.1/.*\\.so|%{_libdir}/webkitgtk-6\\.0/.*\\.so)$

%description
WebKitGTK is the port of the WebKit web rendering engine to the
GTK platform.

%package -n     webkitgtk6.0
Summary:        WebKitGTK for GTK 4
Requires:       javascriptcoregtk6.0%{?_isa} = %{version}-%{release}
Requires:       bubblewrap
Requires:       libGLES
Requires:       xdg-dbus-proxy
Recommends:     geoclue2
Recommends:     gstreamer1-plugins-bad-free
Recommends:     gstreamer1-plugins-good
Recommends:     xdg-desktop-portal-gtk
Provides:       bundled(angle)
Provides:       bundled(pdfjs)
Provides:       bundled(skia)
Provides:       bundled(xdgmime)
Obsoletes:      webkit2gtk5.0 < %{version}-%{release}

%description -n webkitgtk6.0
WebKitGTK is the port of the WebKit web rendering engine to the
GTK platform. This package contains WebKitGTK for GTK 4.

%package -n     webkit2gtk4.1
Summary:        WebKitGTK for GTK 3 and libsoup 3
Requires:       javascriptcoregtk4.1%{?_isa} = %{version}-%{release}
Requires:       bubblewrap
Requires:       libGLES
Requires:       xdg-dbus-proxy
Recommends:     geoclue2
Recommends:     gstreamer1-plugins-bad-free
Recommends:     gstreamer1-plugins-good
Recommends:     xdg-desktop-portal-gtk
Provides:       bundled(angle)
Provides:       bundled(pdfjs)
Provides:       bundled(skia)
Provides:       bundled(xdgmime)

%description -n webkit2gtk4.1
WebKitGTK is the port of the WebKit web rendering engine to the
GTK platform. This package contains WebKitGTK for GTK 3 and libsoup 3.

%package -n     webkitgtk6.0-devel
Summary:        Development files for webkitgtk6.0
Requires:       webkitgtk6.0%{?_isa} = %{version}-%{release}
Requires:       javascriptcoregtk6.0%{?_isa} = %{version}-%{release}
Requires:       javascriptcoregtk6.0-devel%{?_isa} = %{version}-%{release}
Obsoletes:      webkit2gtk5.0-devel < %{version}-%{release}

%description -n webkitgtk6.0-devel
The webkitgtk6.0-devel package contains libraries, build data, and header
files for developing applications that use webkitgtk6.0.

%package -n     webkit2gtk4.1-devel
Summary:        Development files for webkit2gtk4.1
Requires:       webkit2gtk4.1%{?_isa} = %{version}-%{release}
Requires:       javascriptcoregtk4.1%{?_isa} = %{version}-%{release}
Requires:       javascriptcoregtk4.1-devel%{?_isa} = %{version}-%{release}

%description -n webkit2gtk4.1-devel
The webkit2gtk4.1-devel package contains libraries, build data, and header
files for developing applications that use webkit2gtk4.1.

%if %{with docs}
%package -n     webkitgtk6.0-doc
Summary:        Documentation files for webkit2gtk5.0
BuildArch:      noarch
Requires:       webkitgtk6.0 = %{version}-%{release}
Obsoletes:      webkit2gtk5.0-doc < %{version}-%{release}
Recommends:     gi-docgen-fonts

# Documentation/jsc-glib-4.1/fzy.js is MIT
# Documentation/jsc-glib-4.1/*.js and *css is Apache-2.0 OR GPL-3.0-or-later
# Documentation/jsc-glib-4.1/*html is BSD, LGPL-2.1
# Documentation/webkit2gtk-4.1/*html is  BSD, LGPL-2.1
# Documentation/webkit2gtk-web-extension-4.1/*html is BSD, LGPL-2.1
# Documentation/webkit2gtk-web-extension-4.1/solarized* is MIT
# Documentation/webkit2gtk-web-extension-4.1/style.css is Apache-2.0 OR GPL-3.0-or-later
License:        MIT AND LGPL-2.1-only AND BSD-3-Clause AND (Apache-2.0 OR GPL-3.0-or-later)

%description -n webkitgtk6.0-doc
This package contains developer documentation for webkitgtk6.0.

%package -n     webkit2gtk4.1-doc
Summary:        Documentation files for webkit2gtk4.1
BuildArch:      noarch
Requires:       webkit2gtk4.1 = %{version}-%{release}
Recommends:     gi-docgen-fonts

# Documentation/jsc-glib-4.1/fzy.js is MIT
# Documentation/jsc-glib-4.1/*.js and *css is Apache-2.0 OR GPL-3.0-or-later
# Documentation/jsc-glib-4.1/*html is BSD, LGPL-2.1
# Documentation/webkit2gtk-4.1/*html is  BSD, LGPL-2.1
# Documentation/webkit2gtk-web-extension-4.1/*html is BSD, LGPL-2.1
# Documentation/webkit2gtk-web-extension-4.1/solarized* is MIT
# Documentation/webkit2gtk-web-extension-4.1/style.css is Apache-2.0 OR GPL-3.0-or-later
License:        MIT AND LGPL-2.1-only AND BSD-3-Clause AND (Apache-2.0 OR GPL-3.0-or-later)

%description -n webkit2gtk4.1-doc
This package contains developer documentation for webkit2gtk4.1.
%endif

%package -n     javascriptcoregtk6.0
Summary:        JavaScript engine from webkitgtk6.0
Provides:       bundled(simde)
Provides:       bundled(simdutf)
Obsoletes:      javascriptcoregtk5.0 < %{version}-%{release}

%description -n javascriptcoregtk6.0
This package contains the JavaScript engine from webkitgtk6.0.

%package -n     javascriptcoregtk4.1
Summary:        JavaScript engine from webkit2gtk4.1
Provides:       bundled(simde)
Provides:       bundled(simdutf)
Obsoletes:      webkit2gtk4.1-jsc < %{version}-%{release}

%description -n javascriptcoregtk4.1
This package contains the JavaScript engine from webkit2gtk4.1.

%package -n     javascriptcoregtk6.0-devel
Summary:        Development files for JavaScript engine from webkitgtk6.0
Requires:       javascriptcoregtk6.0%{?_isa} = %{version}-%{release}
Obsoletes:      javascriptcoregtk5.0-devel < %{version}-%{release}

%description -n javascriptcoregtk6.0-devel
The javascriptcoregtk6.0-devel package contains libraries, build data, and header
files for developing applications that use JavaScript engine from webkitgtk-6.0.

%package -n     javascriptcoregtk4.1-devel
Summary:        Development files for JavaScript engine from webkit2gtk4.1
Requires:       javascriptcoregtk4.1%{?_isa} = %{version}-%{release}
Obsoletes:      webkit2gtk4.1-jsc-devel < %{version}-%{release}

%description -n javascriptcoregtk4.1-devel
The javascriptcoregtk4.1-devel package contains libraries, build data, and header
files for developing applications that use JavaScript engine from webkit2gtk-4.1.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n webkitgtk-%{version}

%build
# Increase the DIE limit so our debuginfo packages can be size-optimized.
# This previously decreased the size for x86_64 from ~5G to ~1.1G, but as of
# 2022 it's more like 850 MB -> 675 MB. This requires lots of RAM on the
# builders, so only do this for x86_64 and aarch64 to avoid overwhelming
# builders with less RAM.
# https://bugzilla.redhat.com/show_bug.cgi?id=1456261
%global _dwz_max_die_limit_x86_64 250000000
%global _dwz_max_die_limit_aarch64 250000000

# Require 32 GB of RAM per vCPU for debuginfo processing. 16 GB is not enough.
%global _find_debuginfo_opts %limit_build -m 32768

# Reduce debuginfo verbosity 32-bit builds to reduce memory consumption even more.
# https://bugs.webkit.org/show_bug.cgi?id=140176
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/I6IVNA52TXTBRQLKW45CJ5K4RA4WNGMI/
%ifarch %{ix86}
%global optflags %(echo %{optflags} | sed 's/-g /-g1 /')
%endif

# JIT is broken on ARM systems with new ARMv8.5 BTI extension at the moment
# Cf. https://bugzilla.redhat.com/show_bug.cgi?id=2130009
# Cf. https://bugs.webkit.org/show_bug.cgi?id=245697
# Disable BTI until this is fixed upstream.
%ifarch aarch64
%global optflags %(echo %{optflags} | sed 's/-mbranch-protection=standard /-mbranch-protection=pac-ret /')
%endif

%define _vpath_builddir %{_vendor}-%{_target_os}-build/webkitgtk-6.0
%cmake \
  -GNinja \
  -DPORT=GTK \
  -DCMAKE_BUILD_TYPE=Release \
  -DUSE_GTK4=ON \
  -DUSE_LIBBACKTRACE=OFF \
%if %{without docs}
  -DENABLE_DOCUMENTATION=OFF \
%endif
  %{nil}

%define _vpath_builddir %{_vendor}-%{_target_os}-build/webkit2gtk-4.1
%cmake \
  -GNinja \
  -DPORT=GTK \
  -DCMAKE_BUILD_TYPE=Release \
  -DUSE_GTK4=OFF \
  -DUSE_LIBBACKTRACE=OFF \
  -DENABLE_WEBDRIVER=OFF \
%if %{without docs}
  -DENABLE_DOCUMENTATION=OFF \
%endif
  %{nil}

%define _vpath_builddir %{_vendor}-%{_target_os}-build/webkitgtk-6.0
export NINJA_STATUS="[1/2][%f/%t %es] "
%cmake_build %limit_build -m 3072

%define _vpath_builddir %{_vendor}-%{_target_os}-build/webkit2gtk-4.1
export NINJA_STATUS="[2/2][%f/%t %es] "
%cmake_build %limit_build -m 3072

%install
%define _vpath_builddir %{_vendor}-%{_target_os}-build/webkitgtk-6.0
%cmake_install

%define _vpath_builddir %{_vendor}-%{_target_os}-build/webkit2gtk-4.1
%cmake_install

%find_lang WebKitGTK-6.0
%find_lang WebKitGTK-4.1

# Finally, copy over and rename various files for %%license inclusion
%add_to_license_files Source/JavaScriptCore/COPYING.LIB
%add_to_license_files Source/ThirdParty/ANGLE/LICENSE
%add_to_license_files Source/ThirdParty/ANGLE/src/third_party/libXNVCtrl/LICENSE
%add_to_license_files Source/WebCore/LICENSE-APPLE
%add_to_license_files Source/WebCore/LICENSE-LGPL-2
%add_to_license_files Source/WebCore/LICENSE-LGPL-2.1
%add_to_license_files Source/WebInspectorUI/UserInterface/External/CodeMirror/LICENSE
%add_to_license_files Source/WebInspectorUI/UserInterface/External/Esprima/LICENSE
%add_to_license_files Source/WebInspectorUI/UserInterface/External/three.js/LICENSE
%add_to_license_files Source/WTF/icu/LICENSE
%add_to_license_files Source/WTF/wtf/dtoa/COPYING
%add_to_license_files Source/WTF/wtf/dtoa/LICENSE

%files -n webkitgtk6.0 -f WebKitGTK-6.0.lang
%license _license_files/*ThirdParty*
%license _license_files/*WebCore*
%license _license_files/*WebInspectorUI*
%license _license_files/*WTF*
%{_libdir}/libwebkitgtk-6.0.so.4*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/WebKit-6.0.typelib
%{_libdir}/girepository-1.0/WebKitWebProcessExtension-6.0.typelib
%{_libdir}/webkitgtk-6.0/
%{_libexecdir}/webkitgtk-6.0/
%exclude %{_libexecdir}/webkitgtk-6.0/MiniBrowser
%exclude %{_libexecdir}/webkitgtk-6.0/jsc
%{_bindir}/WebKitWebDriver

%files -n webkit2gtk4.1 -f WebKitGTK-4.1.lang
%license _license_files/*ThirdParty*
%license _license_files/*WebCore*
%license _license_files/*WebInspectorUI*
%license _license_files/*WTF*
%{_libdir}/libwebkit2gtk-4.1.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/WebKit2-4.1.typelib
%{_libdir}/girepository-1.0/WebKit2WebExtension-4.1.typelib
%{_libdir}/webkit2gtk-4.1/
%{_libexecdir}/webkit2gtk-4.1/
%exclude %{_libexecdir}/webkit2gtk-4.1/MiniBrowser
%exclude %{_libexecdir}/webkit2gtk-4.1/jsc

%files -n webkitgtk6.0-devel
%{_libexecdir}/webkitgtk-6.0/MiniBrowser
%{_includedir}/webkitgtk-6.0/
%exclude %{_includedir}/webkitgtk-6.0/jsc
%{_libdir}/libwebkitgtk-6.0.so
%{_libdir}/pkgconfig/webkitgtk-6.0.pc
%{_libdir}/pkgconfig/webkitgtk-web-process-extension-6.0.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/WebKit-6.0.gir
%{_datadir}/gir-1.0/WebKitWebProcessExtension-6.0.gir

%files -n webkit2gtk4.1-devel
%{_libexecdir}/webkit2gtk-4.1/MiniBrowser
%{_includedir}/webkitgtk-4.1/
%exclude %{_includedir}/webkitgtk-4.1/JavaScriptCore
%exclude %{_includedir}/webkitgtk-4.1/jsc
%{_libdir}/libwebkit2gtk-4.1.so
%{_libdir}/pkgconfig/webkit2gtk-4.1.pc
%{_libdir}/pkgconfig/webkit2gtk-web-extension-4.1.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/WebKit2-4.1.gir
%{_datadir}/gir-1.0/WebKit2WebExtension-4.1.gir

%files -n javascriptcoregtk6.0
%license _license_files/*JavaScriptCore*
%{_libdir}/libjavascriptcoregtk-6.0.so.1*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/JavaScriptCore-6.0.typelib

%files -n javascriptcoregtk4.1
%license _license_files/*JavaScriptCore*
%{_libdir}/libjavascriptcoregtk-4.1.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/JavaScriptCore-4.1.typelib

%files -n javascriptcoregtk6.0-devel
%{_libexecdir}/webkitgtk-6.0/jsc
%dir %{_includedir}/webkitgtk-6.0
%{_includedir}/webkitgtk-6.0/jsc/
%{_libdir}/libjavascriptcoregtk-6.0.so
%{_libdir}/pkgconfig/javascriptcoregtk-6.0.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/JavaScriptCore-6.0.gir

%files -n javascriptcoregtk4.1-devel
%{_libexecdir}/webkit2gtk-4.1/jsc
%dir %{_includedir}/webkitgtk-4.1
%{_includedir}/webkitgtk-4.1/JavaScriptCore/
%{_includedir}/webkitgtk-4.1/jsc/
%{_libdir}/libjavascriptcoregtk-4.1.so
%{_libdir}/pkgconfig/javascriptcoregtk-4.1.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/JavaScriptCore-4.1.gir

%if %{with docs}
%files -n webkitgtk6.0-doc
%dir %{_datadir}/doc
%{_datadir}/doc/javascriptcoregtk-6.0/
%{_datadir}/doc/webkitgtk-6.0/
%{_datadir}/doc/webkitgtk-web-process-extension-6.0/

%files -n webkit2gtk4.1-doc
%dir %{_datadir}/doc
%{_datadir}/doc/javascriptcoregtk-4.1/
%{_datadir}/doc/webkit2gtk-4.1/
%{_datadir}/doc/webkit2gtk-web-extension-4.1/
%endif

%changelog
%autochangelog
