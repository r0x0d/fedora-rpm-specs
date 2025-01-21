%global tarball xf86-video-qxl
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir %{moduledir}/drivers

%undefine _hardened_build

# Xspice is x86_64 and ARM only since spice-server is x86_64 / ARM only
%ifarch %{ix86} x86_64 %{arm} aarch64
%define with_xspice 1
%else
%define with_xspice 0
%endif

Summary:    Xorg X11 qxl video driver
Name:       xorg-x11-drv-qxl
Version:    0.1.6
Release:    7%{?dist}
URL:        http://www.x.org
License:    MIT

Source0:    http://xorg.freedesktop.org/releases/individual/driver/%{tarball}-%{version}.tar.xz
Patch1:     0001-worst-hack-of-all-time-to-qxl-driver.patch
# This shebang patch is currently downstream-only
Patch2:     0005-Xspice-Adjust-shebang-to-explicitly-mention-python3.patch

ExcludeArch: s390 s390x

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  libtool
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libdrm) >= 2.4.46
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(xfont2)
BuildRequires:  pkgconfig(xorg-server) >= 1.0.99.901
BuildRequires:  pkgconfig(pciaccess) >= 0.10
BuildRequires:  pkgconfig(spice-protocol) >= 0.12.0
%if %{with_xspice}
BuildRequires:  pkgconfig(libcacard)
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(spice-server) >= 0.6.3
%endif

Requires: Xorg %(xserver-sdk-abi-requires ansic)
Requires: Xorg %(xserver-sdk-abi-requires videodrv)

%description
X.Org X11 qxl video driver.

%if %{with_xspice}
%package -n     xorg-x11-server-Xspice
Summary:        XSpice is an X server that can be accessed by a Spice client
Requires:       Xorg %(xserver-sdk-abi-requires ansic)
Requires:       Xorg %(xserver-sdk-abi-requires videodrv)
Requires:       xorg-x11-server-Xorg
Requires:       pcsc-lite-ccid

%description -n xorg-x11-server-Xspice
XSpice is both an X and a Spice server.
%endif

%prep
%autosetup -S git_am -n %{tarball}-%{version}

%build
autoreconf -vif
%if %{with_xspice}
%define enable_xspice --enable-ccid --enable-xspice
%endif
%configure --disable-static %{?enable_xspice}
%make_build

%install
%make_install

find %{buildroot} -name "*.la" -delete
rm -f %{buildroot}/usr/share/doc/xf86-video-qxl/spiceqxl.xorg.conf.example

%if %{with_xspice}
mkdir -p %{buildroot}%{_sysconfdir}/X11
install -p -m 644 examples/spiceqxl.xorg.conf.example \
    %{buildroot}%{_sysconfdir}/X11/spiceqxl.xorg.conf
%endif


%files
%doc COPYING README.md
%{driverdir}/qxl_drv.so

%if %{with_xspice}
%files -n xorg-x11-server-Xspice
%doc COPYING README.xspice README.md examples/spiceqxl.xorg.conf.example
%config(noreplace) %{_sysconfdir}/X11/spiceqxl.xorg.conf
%{_bindir}/Xspice
%{driverdir}/spiceqxl_drv.so
%{_libdir}/pcsc/drivers/serial/libspiceccid.so*
%endif


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 30 2024 Simone Caronni <negativo17@gmail.com> - 0.1.6-6
- Clean up SPEC file.
- Enable Spice Smart Card support.
- Trim changelog.

* Fri Sep 27 2024 Sérgio Basto <sergio@serjux.com> - 0.1.6-5
- Rebuild for rebase of xorg-server to versions 21.1.x

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jan 24 2023 Peter Hutterer <peter.hutterer@redhat.com> - 0.1.6-1
- qxl 0.1.6

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 11 2023 Olivier Fourdan <ofourdan@redhat.com> - 0.1.5-23
- Fix build with recent Xorg (#2047132)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild
