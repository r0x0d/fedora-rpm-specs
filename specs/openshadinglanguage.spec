# Required for the plugin directory name, see https://github.com/OpenImageIO/oiio/issues/2583
%global oiio_major_minor_ver %(rpm -q --queryformat='%%{version}' OpenImageIO-devel | cut -d . -f 1-2)
#%%global prerelease -RC1
%bcond  qt5     1
%bcond  qt6     1
%bcond  ninja   1

#global llvm_compat 18

Name:           openshadinglanguage
Version:        1.13.11.0
Release:        %autorelease %{?prerelease: -p -e %{prerelease}}
Summary:        Advanced shading language for production GI renderers

# The entire source is BSD-3-Clause, except:
#
# BSD-3-Clause AND LicenseRef-Fedora-Public-Domain (see THIRD-PARTY.md):
#   src/include/OSL/oslnoise.h
#
# Additionally, the following are under other acceptable licenses but are
# removed in %%prep and not packaged in any binary RPM:
#
# Pixar (https://github.com/spdx/license-list-XML/issues/2225):
#   doc/build_install/windows/build_osl.py
# CC-BY-4.0:
#   ASWF/meetings/2020-04-02.md
#   ASWF/meetings/template.md
#   CHANGES.md
#   CONTRIBUTING.md
#   GOVERNANCE.md
#   INSTALL.md
#   doc/RELEASING.md
#   doc/build_install/README.md
#   doc/build_install/windows/Readme.md
#   src/doc/languagespec.tex
#   src/doc/osltoy.md.html
#   src/doc/techref.sty
#   src/doc/testshade.md.html
# BSD-2-Clause
#  src/doc/markdeep.min.js
# BSD-2-Clause OR LicenseRef-Fedora-Public-Domain:
#   src/doc/docs.css
License:        BSD-3-Clause AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/AcademySoftwareFoundation/OpenShadingLanguage
Source:         %{url}/archive/v%{version}/OpenShadingLanguage-%{version}%{?prerelease}.tar.gz

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

BuildRequires:  bison >= 2.7
BuildRequires:  boost-devel >= 1.55
BuildRequires:  clang%{?llvm_compat}-devel
BuildRequires:  cmake >= 3.12
BuildRequires:  flex >= 2.5.35
BuildRequires:  gcc-c++ >= 6.1
BuildRequires:  llvm%{?llvm_compat}-devel
%if %{with ninja}
BuildRequires:  ninja-build
%endif
# Needed for OSL pointclound functions
BuildRequires:  partio-devel
BuildRequires:  cmake(Imath) >= 2.3
BuildRequires:  cmake(OpenImageIO) >= 2.3
BuildRequires:  pkgconfig(pugixml)

# For osltoy
%if %{with qt5}
BuildRequires:  pkgconfig(Qt5) >= 5.6
%endif
%if %{with qt6}
BuildRequires:  pkgconfig(Qt6) >= 6.0
%endif
BuildRequires:  pkgconfig(zlib)

BuildRequires:  help2man

# 64 bit only
ExcludeArch:    %{ix86} %{arm}

# HTML documentation removed due to necessary pre-minified JavaScript:
Obsoletes:      %{name}-doc < 1.12.13.0-6

%global common_description %{expand:
Open Shading Language (OSL) is a small but rich language for programmable
shading in advanced renderers and other applications, ideal for describing
materials, lights, displacement, and pattern generation.}

%description %{common_description}

%package example-shaders-source
Summary:        OSL shader examples

# This subpackage doesn’t contain API headers or compiled libraries or executables;
# therefore, nothing in it is derived from src/include/OSL/oslnoise.h.
License:        BSD-3-Clause

BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-common-headers

%description example-shaders-source %{common_description}

This package contains some OSL example shaders.

%package common-headers
Summary:        OSL standard library and auxiliary headers
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description common-headers %{common_description}

This package contains the OSL standard library headers, as well
as some additional headers useful for writing shaders.

%package -n OpenImageIO-plugin-osl
Summary:        OpenImageIO input plugin

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description -n OpenImageIO-plugin-osl %{common_description}

This is a plugin to access OSL from OpenImageIO.

%package        libs
Summary:        OpenShadingLanguage's libraries

%description    libs %{common_description}


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel %{common_description}

The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        -n python3-%{name}
Summary:        %{summary}
BuildRequires:  cmake(pybind11)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(numpy)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    -n python3-%{name} %{common_description}

%prep
%autosetup -p1 -n OpenShadingLanguage-%{version}%{?prerelease}

# Use python3 binary instead of unversioned python
sed -i -e "s|COMMAND python|COMMAND python3|" $(find . -iname CMakeLists.txt)

# Fix all Python shebangs recursively in .
%py3_shebang_fix .

# Remove files that are under licenses that are acceptable in Fedora, but which
# we haven’t included in any License field, so we want to make sure that the
# files bearing them aren’t installed.
#
# Pixar (https://github.com/spdx/license-list-XML/issues/2225):
rm -v doc/build_install/windows/build_osl.py
# CC-BY-4.0 (documentation):
rm -v \
    ASWF/meetings/2020-04-02.md \
    ASWF/meetings/template.md \
    CHANGES.md \
    CONTRIBUTING.md \
    GOVERNANCE.md \
    INSTALL.md \
    doc/RELEASING.md \
    doc/build_install/README.md \
    doc/build_install/windows/Readme.md \
    src/doc/languagespec.tex \
    src/doc/osltoy.md.html \
    src/doc/techref.sty \
    src/doc/testshade.md.html
# BSD-2-Clause
rm -v src/doc/markdeep.min.js
# BSD-2-Clause OR LicenseRef-Fedora-Public-Domain:
rm -v src/doc/docs.css

# Make sure we didn’t miss any bundled and pre-minified JavaScript
# https://docs.fedoraproject.org/en-US/packaging-guidelines/JavaScript/#_compilationminification
find . -type f -name '*.min.js' -print -delete

%build
%cmake \
%if %{with ninja}
   -G Ninja \
%endif
   -DCMAKE_CXX_STANDARD=17 \
   -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name} \
   -DCMAKE_SKIP_RPATH=TRUE \
   -DCMAKE_SKIP_INSTALL_RPATH=YES \
   -DLLVM_STATIC=0 \
   -DLLVM_CONFIG=$(which llvm-config%{?llvm_compat:-%{llvm_compat}}) \
   -DOSL_SHADER_INSTALL_DIR:PATH=%{_datadir}/%{name}/shaders/ \
   -Dpartio_DIR=%{_prefix} \
   -DPARTIO_INCLUDE_DIR=%{_includedir} \
   -DPARTIO_LIBRARIES=%{_libdir}/libpartio.so \
   -DPYTHON_VERSION=%{python3_version} \
   -DSTOP_ON_WARNING=OFF \
   -DINSTALL_DOCS=OFF
%cmake_build

mkdir -p %{_vpath_builddir}/man/man1
for cmd in oslc oslinfo osltoy testrender testshade testshade_dso
do
  cmdpath="%{_vpath_builddir}/bin/${cmd}"
  summary="$(
    LD_LIBRARY_PATH='%{_vpath_builddir}/lib' "${cmdpath}" --help |
    head -n 1 |
    sed -r 's/.* -- //'
  )"
  LD_LIBRARY_PATH='%{_vpath_builddir}/lib' help2man \
      --no-info \
      --version-string='%{version}' \
      --name="${summary}" \
      --output="%{_vpath_builddir}/man/man1/${cmd}.1" \
      "${cmdpath}"
done

%install
%cmake_install

# Move the OpenImageIO plugin into its default search path
mkdir %{buildroot}%{_libdir}/OpenImageIO-%{oiio_major_minor_ver}
mv %{buildroot}%{_libdir}/osl.imageio.so %{buildroot}%{_libdir}/OpenImageIO-%{oiio_major_minor_ver}/

# Install manual files
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    %{_vpath_builddir}/man/man1/*.1
    
# Remove unneeded files
rm -fr %{buildroot}%{_prefix}/build-scripts
rm -fr %{buildroot}%{_prefix}/cmake/llvm_macros.cmake

%files
%license LICENSE.md
%doc README.md
%{_bindir}/oslc
%{_bindir}/oslinfo
%if %{with qt5} || %{with qt6}
%{_bindir}/osltoy
%endif
%{_bindir}/testrender
%{_bindir}/testshade
%{_bindir}/testshade_dso

%{_mandir}/man1/oslc.1*
%{_mandir}/man1/oslinfo.1*
%if %{with qt5}
%{_mandir}/man1/osltoy.1*
%endif
%{_mandir}/man1/testrender.1*
%{_mandir}/man1/testshade.1*
%{_mandir}/man1/testshade_dso.1*

%files example-shaders-source
%{_datadir}/%{name}/shaders/*.osl
%{_datadir}/%{name}/shaders/*.oso

%files common-headers
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/shaders
%{_datadir}/%{name}/shaders/*.h

%files -n OpenImageIO-plugin-osl
%license LICENSE.md
%dir %{_libdir}/OpenImageIO-%{oiio_major_minor_ver}/
%{_libdir}/OpenImageIO-%{oiio_major_minor_ver}/osl.imageio.so
   
%files libs
%license LICENSE.md
%{_libdir}/libosl*.so.1*
%{_libdir}/libtestshade.so.1*

%files devel
%{_includedir}/OSL/
%{_libdir}/libosl*.so
%{_libdir}/libtestshade.so
%{_libdir}/cmake/OSL/
%{_libdir}/pkgconfig/osl*.pc


%files -n python3-%{name}
%{python3_sitearch}/oslquery.so

%changelog
%autochangelog