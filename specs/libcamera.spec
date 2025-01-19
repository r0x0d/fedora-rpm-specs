Name:    libcamera
Version: 0.4.0
Release: 3%{?dist}
Summary: A library to support complex camera ISPs
# see .reuse/dep5 and COPYING for details
License: LGPL-2.1-or-later
URL:     http://libcamera.org/

# Upstream is still under development and does not release tarballs,
# but they do tag releases (https://git.libcamera.org/libcamera/libcamera.git/)
#
# For use the following to do generate a tarball from a git tag:
#
# git archive --format=tar --prefix=%%{name}-%%{version}/ %%{version} | xz > %%{name}-%%{version}.tar.xz
Source0: %{name}-%{version}.tar.xz
Source1: qcam.desktop
Source2: qcam.metainfo.xml
Source3: 70-libcamera.rules

# libcamera does not currently build on these architectures
ExcludeArch: s390x ppc64le

BuildRequires: doxygen
BuildRequires: gcc-c++
BuildRequires: gtest-devel
BuildRequires: desktop-file-utils
BuildRequires: meson
BuildRequires: openssl
BuildRequires: ninja-build
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: gnutls-devel
BuildRequires: pkgconfig(gstreamer-video-1.0)
BuildRequires: pkgconfig(gstreamer-allocators-1.0)
BuildRequires: libatomic
BuildRequires: libevent-devel
BuildRequires: libtiff-devel
BuildRequires: libyaml-devel
BuildRequires: lttng-ust-devel
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6OpenGL)
BuildRequires: pkgconfig(Qt6OpenGLWidgets)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pybind11-devel
BuildRequires: python3-devel
BuildRequires: python3-jinja2
BuildRequires: python3-ply
BuildRequires: python3-pyyaml
BuildRequires: python3-sphinx
BuildRequires: SDL2-devel
BuildRequires: systemd-devel
# libcamera is not really usable without its IPA plugins
Recommends: %{name}-ipa%{?_isa}

%description
libcamera is a library that deals with heavy hardware image processing
operations of complex camera devices that are shared between the linux
host all while allowing offload of certain aspects to the control of
complex camera hardware such as ISPs.

Hardware support includes USB UVC cameras, libv4l cameras as well as more
complex ISPs (Image Signal Processor).

%package     devel
Summary:     Development package for %{name}
Requires:    %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with %{name}.

%package     doc
Summary:     Documentation for %{name}
License:     LGPL-2.1-or-later AND CC-BY-4.0

%description doc
HTML based documentation for %{name} including getting started and API.

%package     ipa
Summary:     ISP Image Processing Algorithm Plugins for %{name}
License:     LGPL-2.1-or-later AND BSD-2-Clause
Requires:    %{name}%{?_isa} = %{version}-%{release}

%description ipa
Image Processing Algorithms plugins for interfacing with device
ISPs for %{name}

%package     tools
Summary:     Tools for %{name}
License:     LGPL-2.1-or-later AND BSD-3-Clause
Requires:    %{name}%{?_isa} = %{version}-%{release}

%description tools
Command line tools for %{name}

%package     qcam
Summary:     Graphical QCam application for %{name}
License:     GPL-2.0-or-later AND MIT
Requires:    %{name}%{?_isa} = %{version}-%{release}

%description qcam
Graphical QCam application for %{name}

%package     gstreamer
Summary:     GSTreamer plugin for %{name}
Requires:    %{name}%{?_isa} = %{version}-%{release}

%description gstreamer
GSTreamer plugins for %{name}

%package     v4l2
Summary:     V4L2 compatibility layer for %{name}
Requires:    %{name}%{?_isa} = %{version}-%{release}

%description v4l2
V4L2 compatibility layer for %{name}

%package     -n python3-%{name}
Summary:     Python bindings for %{name}
Requires:    %{name}%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
Python bindings for %{name}

%prep
%autosetup -p1

%build
# cam/qcam crash with LTO
%global _lto_cflags %{nil}
export CFLAGS="%{optflags} -Wno-deprecated-declarations"
export CXXFLAGS="%{optflags} -Wno-deprecated-declarations"

%meson -Dv4l2=true
%meson_build

# Stripping requires the re-signing of IPA libraries, manually
# copy standard definition of __spec_install_post and re-sign.
%define __spec_install_post \
    %{?__debug_package:%{__debug_install_post}} \
    %{__arch_install_post} \
    %{__os_install_post} \
    %{_builddir}/%{name}-%{version}/src/ipa/ipa-sign-install.sh %{_builddir}/%{name}-%{version}/%{_vpath_builddir}/src/ipa-priv-key.pem %{buildroot}/%{_libdir}/libcamera/ipa_*.so \
%{nil}

%install
%meson_install

# Install Desktop Entry file
desktop-file-install --dir=%{buildroot}%{_datadir}/applications \
                     %SOURCE1

# Install AppStream metainfo file
mkdir -p %{buildroot}/%{_metainfodir}/
cp -a %SOURCE2 %{buildroot}/%{_metainfodir}/

# Install udev rules
mkdir -p %{buildroot}/%{_udevrulesdir}/
install -D -m 644 %SOURCE3 %{buildroot}/%{_udevrulesdir}/

# Remove the Sphinx build leftovers
rm -rf ${RPM_BUILD_ROOT}/%{_docdir}/%{name}-*/html/.buildinfo
rm -rf ${RPM_BUILD_ROOT}/%{_docdir}/%{name}-*/html/.doctrees

%files
%license COPYING.rst LICENSES/LGPL-2.1-or-later.txt
# We leave the version here explicitly to know when it bumps
%{_libdir}/libcamera*.so.0.4
%{_libdir}/libcamera*.so.%{version}
%{_udevrulesdir}/70-libcamera.rules

%files devel
%{_includedir}/%{name}/
%{_libdir}/libcamera*.so
%{_libdir}/pkgconfig/libcamera-base.pc
%{_libdir}/pkgconfig/libcamera.pc

%files doc
%doc %{_docdir}/%{name}-*/

%files ipa
%{_datadir}/libcamera/
%{_libdir}/libcamera/
%{_libexecdir}/libcamera/
%exclude %{_libexecdir}/libcamera/v4l2-compat.so

%files gstreamer
%{_libdir}/gstreamer-1.0/libgstlibcamera.so

%files qcam
%{_bindir}/qcam
%{_datadir}/applications/qcam.desktop
%{_metainfodir}/qcam.metainfo.xml

%files tools
%license LICENSES/GPL-2.0-only.txt
%{_bindir}/cam
%{_bindir}/lc-compliance

%files v4l2
%{_bindir}/libcamerify
%{_libexecdir}/libcamera/v4l2-compat.so

%files -n python3-%{name}
%{python3_sitearch}/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 10 2025 Milan Zamazal <mzamazal@redhat.com> - 0.4.0-2
- Rebuilt with a side tag, to rebuilt pipewire against the new .so version.

* Thu Jan 09 2025 Milan Zamazal <mzamazal@redhat.com> - 0.4.0-1
- Update to version 0.4.0
- Resolves: rhbz#2333913

* Wed Sep 25 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.2-1
- Update to 0.3.2

* Fri Sep 20 2024 Hans de Goede <hdegoede@redhat.com> - 0.3.1-4
- Add Recommends: libcamera-ipa to the main package

* Sun Sep 15 2024 Hans de Goede <hdegoede@redhat.com> - 0.3.1-3
- Add patches to fix pipewire keeping UVC cameras open all the time causing
  significant laptop battery drain:
  https://gitlab.freedesktop.org/pipeawire/pipewire/-/issues/2669

* Thu Aug 01 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.1-2
- Enable simple pipeline everywhere

* Mon Jul 29 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.1-1
- Update to 0.3.1

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Peter Robinson <pbrobinson@fedoraproject.org> - 0.3.0-3
- Add udev rules file, minor package cleanups

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.3.0-2
- Rebuilt for Python 3.13

* Thu May 23 2024 Javier Martinez Canillas <javierm@redhat.com> - 0.3.0-1
- Update to version 0.3.0
- Resolves: rhbz#2282075

* Sun Jan 21 2024 Neal Gompa <ngompa@fedoraproject.org> - 0.2.0-3
- Add patch to port qcam to Qt6 and re-enable for RHEL 10+

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 10 2024 Javier Martinez Canillas <javierm@redhat.com> - 0.2.0-1
- Update to version 0.2.0
- Resolves: rhbz#2257601

* Tue Oct 31 2023 Terje Rosten <terje.rosten@ntnu.no> - 0.1.0-3
- Rebuild for gtest 1.14.0

* Sun Jul 30 2023 Javier Martinez Canillas <javierm@redhat.com> - 0.1.0-1
- Update to version 0.1.0
- Resolves: rhbz#2192455

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed May 17 2023 Javier Martinez Canillas <javierm@redhat.com> - 0.0.5-3
- Fix path of key for IPA modules re-sign and drop unused env var

* Wed May 17 2023 Javier Martinez Canillas <javierm@redhat.com> - 0.0.5-2
- Re-sign IPA modules for real now

* Wed May 17 2023 Javier Martinez Canillas <javierm@redhat.com> - 0.0.5-1
- Update to version 0.0.5
- Build again for s390x and ppc64le
- Drop boost-devel build requires
- Drop workaround patch to fix a GCC13 build issue
- Add a libcamera-v4l2-devel sub-package for the V4L2 compatibility layer
- Re-sign IPA modules after debug symbol stripping

* Wed Feb 01 2023 Javier Martinez Canillas <javierm@redhat.com> - 0.0.4-1
- Update to version 0.0.4
- Add ExcludeArch tag to avoid building libcamera for s390x and ppc64le.

* Tue Jan 24 2023 Wim Taymans <wtaymans@redhat.com> - 0.0.3-3
- Rebuild for gtest .so bump rhbz#2161870
- Add patch for gcc13

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 22 2022 Javier Martinez Canillas <javierm@redhat.com> - 0.0.3-1
- Update to version 0.0.3

* Thu Dec 01 2022 Javier Martinez Canillas <javierm@redhat.com> - 0.0.2-1
- Update to version 0.0.2

* Wed Aug 31 2022 Javier Martinez Canillas <javierm@redhat.com> - 0.0.0~git.20220831.68683d3-1
- Update to snapshot 68683d3

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0~git.20220126.bb84fc6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 10 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.0~git.20220126.bb84fc6-4
- Rebuild for new gtest

* Thu Jun 23 2022 Javier Martinez Canillas <javierm@redhat.com> - 0.0.0~git.20220623.bb84fc6-1
- Update to snapshot bb84fc6

* Wed Feb 02 2022 Javier Martinez Canillas <javierm@redhat.com> - 0.0.0~git.20220128.7ea52d2-3
- Re-enable lc-compliance build

* Wed Feb 02 2022 Eric Curtin <ecurtin@redhat.com> - 0.0.0~git.20220128.7ea52d2-2
- Build with lc-compliance disabled

* Fri Jan 28 2022 Eric Curtin <ecurtin@redhat.com> - 0.0.0~git.20220128.7ea52d2-1
- Update to snapshot 7ea52d2

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.0~git.20210928.e00149f-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 02 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.0.0~git.20210928.e00149f-2
- rebuild against new liblttng-ust

* Tue Sep 28 2021 Javier Martinez Canillas <javierm@redhat.com> - 0.0.0~git.20210928.e00149f-1
- Update to snapshot e00149f

* Wed Sep 08 2021 Javier Martinez Canillas <javierm@redhat.com> - 0.0.0~git.20210908.39c2d5d-1
- Update to snapshot 39c2d5d
- Add snapshot date information to follow the Fedora packaging guidelines
- Use correct license short names to follow the Fedora licensing guidelines
- Remove %%ldconfig_scriptlets that are not needed
- Add a downstream SONAME versioning
- Use %%global instead of %%define
- Fix ppc64le build error caused by not using the IEEE long double ABI
- Remove the Sphinx build leftovers
- Add only the needed license files instead of the whole LICENSE dir
- Ship only the .so.0.n and the .so in the devel sub-package
- Add Desktop and AppStream metainfo files
- Rename docs sub-package to libcamera-doc to silence a package review warning

* Mon Apr 05 2021 Peter Robinson <pbrobinson@fedoraproject.org> 0.0.0-0.1.76a5861
- Update to snapshot 76a5861
- Enable gstreamer plugin and QCam tool
- More granular packaging

* Sat Jul 27 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.0.0-0.1.36d6229
- Initial package
