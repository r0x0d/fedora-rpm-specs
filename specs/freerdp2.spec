# Can be rebuilt with FFmpeg support enabled by passing
# "--with=ffmpeg" to mock/rpmbuild; or by globally
# setting these variables:
# https://bugzilla.redhat.com/show_bug.cgi?id=2242028
#global _with_ffmpeg 1

# Can be rebuilt with OpenCL support enabled by passing # "--with=opencl"
# or by globally setting:
#global _opencl 1

# Momentarily disable GSS support
# https://github.com/FreeRDP/FreeRDP/issues/4348
#global _with_gss 1

# Disable server support in RHEL
# https://bugzilla.redhat.com/show_bug.cgi?id=1639165
%if 0%{?fedora} || 0%{?rhel} >= 10
%global _with_server 1
%endif

# Disable support for missing codecs in RHEL
%{!?rhel:%global _with_soxr 1}

# FIXME: GCC 14.x says there's lots of incompatible pointer casts going on...
%global build_type_safety_c 2

Name:           freerdp2
Version:        2.11.7
Release:        7%{?dist}
Summary:        Free implementation of the Remote Desktop Protocol (RDP)

# The effective license is Apache-2.0 but:
# uwac/libuwac/* is HPND
# winpr/libwinpr/utils/trio/* is ISC-Veillard
# uwac/protocols/server-decoration.xml is LGPL-2.1-or-later
License:        Apache-2.0 AND HPND AND ISC-Veillard AND LGPL-2.1-or-later
URL:            http://www.freerdp.com/

# The license of the winpr/libwinpr/crt/utf.[h|c] files is not allowed.
# See: https://gitlab.com/fedora/legal/fedora-license-data/-/issues/498
# Run the ./freerdp_download_and_repack.sh script to prepare tarball.
Source0:        FreeRDP-%{version}-repack.tar.gz
Source1:        freerdp_download_and_repack.sh

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake >= 2.8
BuildRequires:  cups-devel
BuildRequires:  gsm-devel
BuildRequires:  lame-devel
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libX11-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  libXrandr-devel
%{?_with_server:BuildRequires:  libXtst-devel}
BuildRequires:  libXv-devel
%{?_with_opencl:BuildRequires: opencl-headers >= 3.0}
%{?_with_opencl:BuildRequires: ocl-icd-devel}
BuildRequires:  pkgconfig(openh264)
%{?_with_x264:BuildRequires:  x264-devel}
%{?_with_server:BuildRequires:  pam-devel}
BuildRequires:  xmlto
BuildRequires:  zlib-devel
BuildRequires:  multilib-rpm-config

BuildRequires:  pkgconfig(cairo)
%{?_with_gss:BuildRequires:  pkgconfig(krb5) >= 1.13}
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(openssl)
%{?_with_soxr:BuildRequires:  pkgconfig(soxr)}
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(xkbcommon)

%{?_with_ffmpeg:
BuildRequires:  pkgconfig(libavcodec) >= 57.48.101
BuildRequires:  pkgconfig(libavutil)
}

%description
The xfreerdp & wlfreerdp Remote Desktop Protocol (RDP) clients from the FreeRDP
project.

xfreerdp & wlfreerdp can connect to RDP servers such as Microsoft Windows
machines, xrdp and VirtualBox.

%package        libs
Summary:        Core libraries implementing the RDP protocol
Requires:       libwinpr2%{?_isa} = %{version}-%{release}
%description    libs
libfreerdp-core can be embedded in applications.

libfreerdp-channels and libfreerdp-kbd might be convenient to use in X
applications together with libfreerdp-core.

libfreerdp-core can be extended with plugins handling RDP channels.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       cmake >= 2.8
Conflicts:      freerdp-devel

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}-libs.

%package -n     libwinpr2
Summary:        Windows Portable Runtime

%description -n libwinpr2
WinPR provides API compatibility for applications targeting non-Windows
environments. When on Windows, the original native API is being used instead of
the equivalent WinPR implementation, without having to modify the code using it.

%package -n     libwinpr2-devel
Summary:        Windows Portable Runtime development files
Requires:       libwinpr2%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
Requires:       cmake >= 2.8
Conflicts:      libwinpr-devel

%description -n libwinpr2-devel
The %{name}-libwinpr-devel package contains libraries and header files for
developing applications that use %{name}-libwinpr.

%prep
%autosetup -p1 -n FreeRDP-%{version}

# Rpmlint fixes
find . -name "*.h" -exec chmod 664 {} \;
find . -name "*.c" -exec chmod 664 {} \;

%build
%cmake %{?_cmake_skip_rpath} \
    -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
    -DWITH_ALSA=ON \
    -DWITH_CAIRO=ON \
    -DWITH_CUPS=ON \
    -DWITH_CHANNELS=ON -DBUILTIN_CHANNELS=OFF \
    -DWITH_CLIENT=OFF \
    -DWITH_DIRECTFB=OFF \
    -DWITH_DSP_FFMPEG=%{?_with_ffmpeg:ON}%{?!_with_ffmpeg:OFF} \
    -DWITH_FFMPEG=%{?_with_ffmpeg:ON}%{?!_with_ffmpeg:OFF} \
    -DWITH_GSM=ON \
    -DWITH_GSSAPI=%{?_with_gss:ON}%{?!_with_gss:OFF} \
    -DWITH_ICU=ON \
    -DWITH_IPP=OFF \
    -DWITH_JPEG=ON \
    -DWITH_LAME=ON \
    -DWITH_MANPAGES=OFF \
    -DWITH_OPENCL=%{?_with_opencl:ON}%{?!_with_opencl:OFF} \
    -DWITH_OPENH264=ON \
    -DWITH_OPENSSL=ON \
    -DWITH_PCSC=ON \
    -DWITH_PULSE=ON \
    -DWITH_SERVER=%{?_with_server:ON}%{?!_with_server:OFF} \
    -DWITH_SERVER_INTERFACE=%{?_with_server:ON}%{?!_with_server:OFF} \
    -DWITH_SHADOW_X11=%{?_with_server:ON}%{?!_with_server:OFF} \
    -DWITH_SHADOW_MAC=%{?_with_server:ON}%{?!_with_server:OFF} \
    -DWITH_SOXR=%{?_with_soxr:ON}%{?!_with_soxr:OFF} \
    -DWITH_WAYLAND=ON \
    -DWITH_X11=ON \
    -DWITH_XCURSOR=ON \
    -DWITH_XEXT=ON \
    -DWITH_XKBFILE=ON \
    -DWITH_XI=ON \
    -DWITH_XINERAMA=ON \
    -DWITH_XRENDER=ON \
    -DWITH_XTEST=%{?_with_server:ON}%{?!_with_server:OFF} \
    -DWITH_XV=ON \
    -DWITH_ZLIB=ON \
%ifarch x86_64
    -DWITH_SSE2=ON \
    -DWITH_VAAPI=%{?_with_ffmpeg:ON}%{?!_with_ffmpeg:OFF} \
%else
    -DWITH_SSE2=OFF \
%endif
%ifarch armv7hl
    -DARM_FP_ABI=hard \
    -DWITH_NEON=OFF \
%endif
%ifarch armv7hnl
    -DARM_FP_ABI=hard \
    -DWITH_NEON=ON \
%endif
%ifarch armv5tel armv6l armv7l
    -DARM_FP_ABI=soft \
    -DWITH_NEON=OFF \
%endif
    %{nil}

%cmake_build

%install
%cmake_install

find %{buildroot} -name "*.a" -delete

%multilib_fix_c_header --file %{_includedir}/freerdp2/freerdp/build-config.h

# Delete executables we do not need
rm -rfv %{buildroot}%{_bindir}


%files libs
%license LICENSE
%doc README.md ChangeLog
%{_libdir}/freerdp2/
%{_libdir}/libfreerdp-client2.so.*
%{?_with_server:
%{_libdir}/libfreerdp-server2.so.*
%{_libdir}/libfreerdp-shadow2.so.*
%{_libdir}/libfreerdp-shadow-subsystem2.so.*
}
%{_libdir}/libfreerdp2.so.*
%{_libdir}/libuwac0.so.*

%files devel
%{_includedir}/freerdp2/
%{_includedir}/uwac0/
%{_libdir}/cmake/FreeRDP2/
%{_libdir}/cmake/FreeRDP-Client2/
%{?_with_server:
%{_libdir}/cmake/FreeRDP-Server2/
%{_libdir}/cmake/FreeRDP-Shadow2/
}
%{_libdir}/cmake/uwac0/
%{_libdir}/libfreerdp-client2.so
%{?_with_server:
%{_libdir}/libfreerdp-server2.so
%{_libdir}/libfreerdp-shadow2.so
%{_libdir}/libfreerdp-shadow-subsystem2.so
}
%{_libdir}/libfreerdp2.so
%{_libdir}/libuwac0.so
%{_libdir}/pkgconfig/freerdp2.pc
%{_libdir}/pkgconfig/freerdp-client2.pc
%{?_with_server:
%{_libdir}/pkgconfig/freerdp-server2.pc
%{_libdir}/pkgconfig/freerdp-shadow2.pc
}
%{_libdir}/pkgconfig/uwac0.pc

%files -n libwinpr2
%license LICENSE
%doc README.md ChangeLog
%{_libdir}/libwinpr2.so.*
%{_libdir}/libwinpr-tools2.so.*

%files -n libwinpr2-devel
%{_libdir}/cmake/WinPR2/
%{_includedir}/winpr2/
%{_libdir}/libwinpr2.so
%{_libdir}/libwinpr-tools2.so
%{_libdir}/pkgconfig/winpr2.pc
%{_libdir}/pkgconfig/winpr-tools2.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Pete Walter <pwalter@fedoraproject.org> - 2.11.7-6
- Rebuild for ICU 76

* Tue Jul 23 2024 Neal Gompa <ngompa@fedoraproject.org> - 2.11.7-5
- Enable OpenH264 support

* Tue Jul 23 2024 Neal Gompa <ngompa@fedoraproject.org> - 2.11.7-4
- Include freerdp source download script in SRPM

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.11.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 21 2024 Ondrej Holy <oholy@redhat.com> - 2:2.11.7-2
- Remove files with non-allowed license from the tarball

* Tue Apr 23 2024 Ondrej Holy <oholy@redhat.com> - 2:2.11.7-1
- Update to 2.11.7

* Thu Feb 01 2024 Ondrej Holy <oholy@redhat.com> - 2:2.11.5-1
- Update to 2.11.5.

* Wed Jan 31 2024 Pete Walter <pwalter@fedoraproject.org> - 2.11.4-5
- Rebuild for ICU 74

* Fri Jan 26 2024 Neal Gompa <ngompa@fedoraproject.org> - 2.11.4-4
- Fix dependency in libs subpackage

* Wed Jan 24 2024 Neal Gompa <ngompa@fedoraproject.org> - 2.11.4-3
- Split out as a compatibility package

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.11.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 12 2024 Ondrej Holy <oholy@redhat.com> - 2:2.11.4-1
- Update to 2.11.4.

* Wed Oct 25 2023 Ondrej Holy <oholy@redhat.com> - 2:2.11.2-3
- Disable FFmpeg support (#2242028).

* Mon Oct 09 2023 John Wiele <jwiele@redhat.com> - 2:2.11.2-2
- Enable optional build with OpenCL support.

* Wed Sep 27 2023 Ondrej Holy <oholy@redhat.com> - 2:2.11.1-2
- Update to 2.11.2.

* Tue Sep 05 2023 Ondrej Holy <oholy@redhat.com> - 2:2.11.1-1
- Update to 2.11.1.

* Fri Sep 01 2023 Ondrej Holy <oholy@redhat.com> - 2:2.11.0-1
- Update to 2.11.0 (CVE-2023-39350, CVE-2023-39351, CVE-2023-39352,
  CVE-2023-39353, CVE-2023-39354, CVE-2023-39356, CVE-2023-40181,
  CVE-2023-40186, CVE-2023-40188, CVE-2023-40567, CVE-2023-40569 and
  CVE-2023-40589).

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 František Zatloukal <fzatlouk@redhat.com> - 2:2.10.0-3
- Rebuilt for ICU 73.2

* Thu May 11 2023 Ondrej Holy <oholy@redhat.com> - 2:2.10.0-2
- Enable recommended FFmpeg support.

* Tue Feb 21 2023 Ondrej Holy <oholy@redhat.com> - 2:2.10.0-1
- Update to 2.10.0.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Dec 31 2022 Pete Walter <pwalter@fedoraproject.org> - 2:2.9.0-2
- Rebuild for ICU 72

* Wed Nov 30 2022 Ondrej Holy <oholy@redhat.com> - 2:2.9.0-1
- Update to 2.9.0 (CVE-2022-39316, CVE-2022-39317, CVE-2022-39318,
CVE-2022-39319, CVE-2022-39320, CVE-2022-41877, CVE-2022-39347).

* Mon Nov 14 2022 Ondrej Holy <oholy@redhat.com> - 2:2.8.1-1
- Update to 2.8.1 (CVE-2022-39282, CVE-2022-39283).

* Mon Aug 15 2022 Simone Caronni <negativo17@gmail.com> - 2:2.8.0-1
- Update to 2.8.0.

* Wed Aug 03 2022 Ondrej Holy <oholy@redhat.com> - 2:2.7.0-4
- Enable server support in ELN.

* Mon Aug 01 2022 Frantisek Zatloukal <fzatlouk@redhat.com> - 2:2.7.0-3
- Rebuilt for ICU 71.1

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Apr 25 2022 Ondrej Holy <oholy@redhat.com> - 2:2.7.0-1
- Update to 2.7.0.

* Fri Mar 11 2022 Ondrej Holy <oholy@redhat.com> - 2:2.6.1-1
- Update to 2.6.1.

* Thu Feb 03 2022 Ondrej Holy <oholy@redhat.com> - 2:2.5.0-1
- Update to 2.5.0.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 26 2021 Ondrej Holy <oholy@redhat.com> - 2:2.4.1-2
- Fix datatype mismatch / big-endian breakage
- Load legacy provider when initializing OpenSSL 3.0

* Wed Nov 10 2021 Ondrej Holy <oholy@redhat.com> - 2:2.4.1-1
- Update to 2.4.1 (CVE-2021-41159, CVE-2021-41160).

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 2:2.4.0-3
- Rebuilt with OpenSSL 3.0.0

* Wed Aug 11 2021 Ondrej Holy <oholy@redhat.com> - 2:2.4.0-2
- Preparation for OpenSSL 3.0

* Thu Jul 29 2021 Ondrej Holy <oholy@redhat.com> - 2:2.4.0-1
- Update to 2.4.0.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 19 2021 Pete Walter <pwalter@fedoraproject.org> - 2:2.3.2-2
- Rebuild for ICU 69

* Thu Apr 15 2021 Simone Caronni <negativo17@gmail.com> - 2:2.3.2-1
- Update to 2.3.2.

* Tue Mar 23 2021 Simone Caronni <negativo17@gmail.com> - 2:2.2.0-6
- Explicitly enable Cairo support (#1938393).

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 11 2020 Ondrej Holy <oholy@redhat.com> - 2:2.2.0-4
- Use %%cmake_ macros to fix out-of-source builds (#1863586)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.2.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 23 2020 Simone Caronni <negativo17@gmail.com> - 2:2.2.0-1
- Update to 2.2.0.

* Tue Jun 30 2020 Simone Caronni <negativo17@gmail.com> - 2:2.1.2-1
- Update to 2.1.2.

* Thu May 21 2020 Ondrej Holy <oholy@redhat.com> - 2:2.1.1-1
- Update to 2.1.1.

* Fri May 15 2020 Ondrej Holy <oholy@redhat.com> - 2:2.1.0-1
- Update to 2.1.0 (#1833540).

* Fri May 15 2020 Pete Walter <pwalter@fedoraproject.org> - 2:2.0.0-57.20200207git245fc60
- Rebuild for ICU 67

* Fri Feb 07 2020 Simone Caronni <negativo17@gmail.com> - 2:2.0.0-56.20200207git245fc60
- Update to latest snapshot.

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.0-55.20190820git6015229
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 2:2.0.0-54.20190820git6015229
- Rebuild for ICU 65

* Tue Aug 20 2019 Simone Caronni <negativo17@gmail.com> - 2:2.0.0-53.20190820git6015229
- Update to latest snapshot.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.0-52.20190918git5e672d4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 21 2019 Simone Caronni <negativo17@gmail.com> - 2:2.0.0-51.20190918git5e672d4
- Update to latest snapshot.

* Sat May 18 2019 Simone Caronni <negativo17@gmail.com> - 2:2.0.0-50.20190517gitb907324
- Update to latest snapshot.

* Wed Mar 06 2019 Simone Caronni <negativo17@gmail.com> - 2:2.0.0-49.20190304git435872b
- Fix for GFX color depth (Windows 10).

* Thu Feb 28 2019 Simone Caronni <negativo17@gmail.com> - 2:2.0.0-48.20190228gitce386c8
- Update to latest snapshot post rc4.
- CVE-2018-1000852 (#1661642).

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.0-47.rc4.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 29 2018 Ondrej Holy <oholy@redhat.com> - 2:2.0.0-47.rc4
- Update to 2.0.0-rc4

* Mon Oct 15 2018 Simone Caronni <negativo17@gmail.com> - 2:2.0.0-46.20181008git00af869
- Enable Xtest option (#1559606).

* Mon Oct 15 2018 Simone Caronni <negativo17@gmail.com> - 2:2.0.0-45.20181008git00af869
- Update to last snapshot post 2.0.0-rc3.

* Mon Aug 20 2018 Simone Caronni <negativo17@gmail.com> - 2:2.0.0-44.rc3
- Update SPEC file.

* Sat Aug 04 2018 Mike DePaulo <mikedep333@fedoraproject.org> - 2:2.0.0-43.20180801.rc3
- Update to 2.0.0-rc3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.0-42.20180405gita9ecd6a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 09 2018 Simone Caronni <negativo17@gmail.com> - 2:2.0.0-41.20180405gita9ecd6a
- Update to latest snapshot.

* Wed Mar 21 2018 Simone Caronni <negativo17@gmail.com> - 2:2.0.0-40.20180320gitde83f4d
- Add PAM support (fixes freerdp-shadow-cli). Thanks Paolo Zeppegno.
- Update to latest snapshot.

* Thu Mar 15 2018 Simone Caronni <negativo17@gmail.com> - 2:2.0.0-39.20180314gitf8baeb7
- Update to latest snapshot.
- Fixes connection to RDP servers with the latest Microsoft patches:
  https://github.com/FreeRDP/FreeRDP/issues/4449

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.0-38.20180115git8f52c7e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Karsten Hopp <karsten@redhat.com> - 2.0.0-37git}
- use versioned build requirement on pkgconfig(openssl) to prevent using
  compat-openssl10-devel instead of openssl-devel

* Tue Jan 16 2018 Simone Caronni <negativo17@gmail.com> - 2:2.0.0-36.20180115git8f52c7e
- Update to latest snapshot.
- Make GSS support optional and disable it for now (#1534094 and FreeRDP #4348,
  #1435, #4363).

* Wed Dec 20 2017 Simone Caronni <negativo17@gmail.com> - 2:2.0.0-35.20171220gitbfe8359
- Update to latest snapshot post 2.0.0rc1.

* Mon Sep 11 2017 Simone Caronni <negativo17@gmail.com> - 2:2.0.0-34.20170831git3b83526
- Update to latest snapshot.
- Trim changelog.

* Mon Aug 07 2017 Björn Esser <besser82@fedoraproject.org> - 2:2.0.0-33.20170724gitf8c9f43
- Rebuilt for AutoReq cmake-filesystem

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.0-32.20170724gitf8c9f43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Simone Caronni <negativo17@gmail.com> - 2:2.0.0-31.20170724gitf8c9f43
- Update to latest snapshot, Talos security fixes.

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.0-30.20170710gitf580bea
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 12 2017 Simone Caronni <negativo17@gmail.com> - 2:2.0.0-29.20170710gitf580bea
- Update to latest snapshot.

* Mon Jun 26 2017 Simone Caronni <negativo17@gmail.com> - 2:2.0.0-28.20170623git9904c32
- Update to latest snapshot.

* Mon May 15 2017 Simone Caronni <negativo17@gmail.com> - 2:2.0.0-27.20170512gitb1df835
- Update to latest snapshot.

* Thu Apr 20 2017 Simone Caronni <negativo17@gmail.com> - 2:2.0.0-26.20170419gitbfcf8e7
- Update to latest 2.0 snapshot.

* Thu Apr 13 2017 Orion Poplawski <orion@cora.nwra.com> - 2:2.0.0-25.20170317git8c68761
- Install tools via make install

* Wed Mar 22 2017 Simone Caronni <negativo17@gmail.com> - 2:2.0.0-24.20170317git8c68761
- Update to latest snapshot.

* Mon Mar 06 2017 Simone Caronni <negativo17@gmail.com> - 2:2.0.0-23.20170302git210de68
- Remove shared libxfreerdp-client shared library.

* Thu Mar 02 2017 Simone Caronni <negativo17@gmail.com> - 2:2.0.0-22.20170302git210de68
- Move libxfreerdp-client shared object into devel subpackage.

* Thu Mar 02 2017 Simone Caronni <negativo17@gmail.com> - 2:2.0.0-21.20170302git210de68
- Update to latest snapshot.
- Update build requirements, tune build options.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.0-20.20161228git90877f5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 Simone Caronni <negativo17@gmail.com> - 2:2.0.0-19.20161228git90877f5
- Update to latest snapshot.
