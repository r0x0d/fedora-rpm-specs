%global tarball xf86-video-vesa
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir	%{moduledir}/drivers

%undefine _hardened_build

Summary:   Xorg X11 vesa video driver
Name:      xorg-x11-drv-vesa
Version:   2.6.0
Release:   1%{?dist}
URL:       https://www.x.org
Source0:   https://xorg.freedesktop.org/releases/individual/driver/%{tarball}-%{version}.tar.xz
License:   MIT

ExclusiveArch: %{ix86} x86_64

BuildRequires: make
BuildRequires: xorg-x11-server-devel >= 1.10.99.902
BuildRequires: autoconf automake libtool

Requires: Xorg %([ -e /usr/bin/xserver-sdk-abi-requires ] && xserver-sdk-abi-requires ansic)
Requires: Xorg %([ -e /usr/bin/xserver-sdk-abi-requires ] && xserver-sdk-abi-requires videodrv)
Requires: xorg-x11-server-wrapper

%description 
X.Org X11 vesa video driver.

%prep
%autosetup -p1 -n %{tarball}-%{version}

%build
autoreconf -vif
%configure --disable-static
%make_build

%install
%make_install

find %{buildroot} -name "*.la" -delete

%files
%{driverdir}/vesa_drv.so
%{_mandir}/man4/vesa.4*

%changelog
* Fri Sep 27 2024 Simone Caronni <negativo17@gmail.com> - 2.6.0-1
- Update to 2.6.0.
- Clean up SPEC file.
- Trim changelog.

* Fri Sep 27 2024 Sérgio Basto <sergio@serjux.com> - 2.5.0-9
- Rebuild for rebase of xorg-server to versions 21.1.x

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Apr 19 2022 Jocelyn Falempe <jfalempe@redhat.com> - 2.5.0-3
- Fix vesa crash with simpledrm driver (#2074789)

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jan 07 2022 Adam Jackson <ajax@redhat.com> - 2.5.0-1
- vesa 2.5.0
