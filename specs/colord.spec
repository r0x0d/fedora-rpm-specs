# Building the extra print profiles requires colprof, +4Gb of RAM and
# quite a lot of time. Don't enable this for test builds.
%define enable_print_profiles 0

# SANE is pretty insane when it comes to handling devices, and we get AVCs
# popping up all over the place.
%define enable_sane 0

Summary:   Color daemon
Name:      colord
Version:   1.4.7
Release:   %autorelease
License:   GPL-2.0-or-later AND LGPL-2.1-or-later
URL:       https://www.freedesktop.org/software/colord/
Source0:   https://www.freedesktop.org/software/colord/releases/%{name}-%{version}.tar.xz
Source1:   colord.sysusers

Patch0:    0001-Fix-writing-to-the-database-with-ProtectSystem-stric.patch

%if !0%{?rhel}
BuildRequires:  pkgconfig(bash-completion)
%endif
BuildRequires: color-filesystem
BuildRequires: docbook5-style-xsl
BuildRequires: gettext
BuildRequires: gtk-doc
BuildRequires: gobject-introspection-devel
BuildRequires: libxslt
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(gusb) >= 0.2.7
BuildRequires: pkgconfig(lcms2) >= 2.6
BuildRequires: pkgconfig(libsystemd)
BuildRequires: pkgconfig(polkit-gobject-1) >= 0.103
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(systemd)

# for SANE support
%if 0%{?enable_sane}
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(sane-backends)
%endif

Requires: color-filesystem
BuildRequires: systemd, systemd-rpm-macros
%{?systemd_requires}
Requires: colord-libs%{?_isa} = %{version}-%{release}

# Self-obsoletes to fix the multilib upgrade path
Obsoletes: colord < 0.1.27-3

# obsolete separate profiles package
Obsoletes: shared-color-profiles <= 0.1.6-2
Provides: shared-color-profiles

%description
colord is a low level system activated daemon that maps color devices
to color profiles in the system context.

%package libs
Summary: Color daemon library

%description libs
colord is a low level system activated daemon that maps color devices
to color profiles in the system context.

%package devel
Summary: Development package for %{name}
Requires: %{name} = %{version}-%{release}
Requires: %{name}-libs = %{version}-%{release}
Obsoletes: colorhug-client-devel <= 0.1.13

%description devel
Files for development with %{name}.

%package devel-docs
Summary: Developer documentation package for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description devel-docs
Documentation for development with %{name}.

%package extra-profiles
Summary: More color profiles for color management that are less commonly used
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

# obsolete separate profiles package
Obsoletes: shared-color-profiles-extra <= 0.1.6-2
Provides: shared-color-profiles-extra

%description extra-profiles
More color profiles for color management that are less commonly used.
This may be useful for CMYK soft-proofing or for extra device support.

%package tests
Summary: Data files for installed tests

%description tests
Data files for installed tests.

%prep
%autosetup -p1

%build
# Set ~2 GiB limit so that colprof is forced to work in chunks when
# generating the print profile rather than trying to allocate a 3.1 GiB
# chunk of RAM to put the entire B-to-A tables in.
ulimit -Sv 2000000

%meson \
    -Dvapi=true \
    -Dinstalled_tests=true \
    -Dprint_profiles=false \
%if 0%{?enable_sane}
    -Dsane=true \
%endif
%if 0%{?rhel}
    -Dbash_completion=false \
    -Dargyllcms_sensor=false \
%endif
%if !0%{?rhel}
    -Dlibcolordcompat=true \
%endif
    -Ddaemon_user=colord

%meson_build

%install
%meson_install
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/colord.conf

# databases
touch $RPM_BUILD_ROOT%{_localstatedir}/lib/colord/mapping.db
touch $RPM_BUILD_ROOT%{_localstatedir}/lib/colord/storage.db

%find_lang %{name}


%post
%systemd_post colord.service

%preun
%systemd_preun colord.service

%postun
%systemd_postun colord.service

%ldconfig_scriptlets libs

%files -f %{name}.lang
%doc README.md AUTHORS NEWS
%license COPYING
%{_libexecdir}/colord
%attr(755,colord,colord) %dir %{_localstatedir}/lib/colord
%attr(755,colord,colord) %dir %{_localstatedir}/lib/colord/icc
%{_bindir}/*
%{_datadir}/glib-2.0/schemas/org.freedesktop.ColorHelper.gschema.xml
%{_datadir}/dbus-1/system.d/org.freedesktop.ColorManager.conf
%{_datadir}/dbus-1/interfaces/org.freedesktop.ColorManager*.xml
%{_datadir}/polkit-1/actions/org.freedesktop.color.policy
%{_datadir}/dbus-1/system-services/org.freedesktop.ColorManager.service
%{_mandir}/man1/*.1*
%{_datadir}/colord
%if !0%{?rhel}
%{_datadir}/bash-completion/completions/colormgr
%endif
/usr/lib/udev/rules.d/*.rules
/usr/lib/tmpfiles.d/colord.conf
%{_libdir}/colord-sensors
%{_libdir}/colord-plugins
%ghost %attr(-,colord,colord) %{_localstatedir}/lib/colord/*.db
%{_unitdir}/colord.service
%{_sysusersdir}/colord.conf

# session helper
%{_libexecdir}/colord-session
%{_datadir}/dbus-1/interfaces/org.freedesktop.ColorHelper.xml
%{_datadir}/dbus-1/services/org.freedesktop.ColorHelper.service
%{_userunitdir}/colord-session.service

# sane helper
%if 0%{?enable_sane}
%{_libexecdir}/colord-sane
%endif

# common colorspaces
%dir %{_icccolordir}/colord
%{_icccolordir}/colord/AdobeRGB1998.icc
%{_icccolordir}/colord/ProPhotoRGB.icc
%{_icccolordir}/colord/Rec709.icc
%{_icccolordir}/colord/SMPTE-C-RGB.icc
%{_icccolordir}/colord/sRGB.icc

# monitor test profiles
%{_icccolordir}/colord/Bluish.icc

# named color profiles
%{_icccolordir}/colord/x11-colors.icc

%files libs
%doc COPYING
%{_libdir}/libcolord.so.2*
%{_libdir}/libcolordprivate.so.2*
%{_libdir}/libcolorhug.so.2*
%if !0%{?rhel}
%{_libdir}/libcolordcompat.so
%endif

%{_libdir}/girepository-1.0/*.typelib

%files extra-profiles
# other colorspaces not often used
%{_icccolordir}/colord/AppleRGB.icc
%{_icccolordir}/colord/BestRGB.icc
%{_icccolordir}/colord/BetaRGB.icc
%{_icccolordir}/colord/BruceRGB.icc
%{_icccolordir}/colord/CIE-RGB.icc
%{_icccolordir}/colord/ColorMatchRGB.icc
%{_icccolordir}/colord/DonRGB4.icc
%{_icccolordir}/colord/ECI-RGBv1.icc
%{_icccolordir}/colord/ECI-RGBv2.icc
%{_icccolordir}/colord/EktaSpacePS5.icc
%{_icccolordir}/colord/Gamma*.icc
%{_icccolordir}/colord/NTSC-RGB.icc
%{_icccolordir}/colord/PAL-RGB.icc
%{_icccolordir}/colord/SwappedRedAndGreen.icc
%{_icccolordir}/colord/WideGamutRGB.icc

# other named color profiles not generally useful
%{_icccolordir}/colord/Crayons.icc

%files devel
%{_includedir}/colord-1
%{_libdir}/libcolord.so
%{_libdir}/libcolordprivate.so
%{_libdir}/libcolorhug.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%{_datadir}/vala/vapi/colord.vapi
%{_datadir}/vala/vapi/colord.deps

%files devel-docs
%dir %{_datadir}/gtk-doc/html/colord
%{_datadir}/gtk-doc/html/colord/*

%files tests
%dir %{_libexecdir}/installed-tests/colord
%{_libexecdir}/installed-tests/colord/*
%dir %{_datadir}/installed-tests/colord
%{_datadir}/installed-tests/colord/*

%changelog	
%autochangelog
