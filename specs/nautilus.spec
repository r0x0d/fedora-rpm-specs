%bcond cloudproviders %{undefined rhel}

%global glib2_version 2.79.0
%global gnome_autoar_version 0.4.4
%global gtk4_version 4.15.2
%global libadwaita_version 1.6~beta

Name:           nautilus
Version:        47.2

%global tarball_version %%(echo %{version} | tr '~' '.')
%global major_version %%(cut -d "." -f 1 <<<%{tarball_version})

Release:        %autorelease
Summary:        File manager for GNOME

# Sources are GPL-3.0-or-later and Appdata is CC0-1.0.
License:        GPL-3.0-or-later AND CC0-1.0
URL:            https://apps.gnome.org/Nautilus/
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz
# https://pagure.io/fedora-workstation/issue/442
Patch:          default-terminal.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  meson
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(glib-2.0) >= %{glib2_version}
BuildRequires:  pkgconfig(gnome-autoar-0) >= %{gnome_autoar_version}
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gtk4) >= %{gtk4_version}
BuildRequires:  pkgconfig(libadwaita-1) >= %{libadwaita_version}
%if %{with cloudproviders}
BuildRequires:  pkgconfig(cloudproviders)
%endif
BuildRequires:  pkgconfig(libportal)
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(tracker-sparql-3.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  /usr/bin/appstream-util
# needed by test/automated/displayless
BuildRequires:  localsearch

Requires:       glib2%{_isa} >= %{glib2_version}
Requires:       gnome-autoar%{_isa} >= %{gnome_autoar_version}
Requires:       gsettings-desktop-schemas%{_isa}
Requires:       gtk4%{_isa} >= %{gtk4_version}
Requires:       gvfs%{_isa}
Requires:       libadwaita%{_isa} >= %{libadwaita_version}
# the main binary links against libnautilus-extension.so
# don't depend on soname, rather on exact version
Requires:       %{name}-extensions%{_isa} = %{version}-%{release}
# For the org.freedesktop.Tracker3.Miner.Files GSettings schema
Requires:       localsearch

Provides:       bundled(libgd)

%description
Nautilus is the file manager and graphical shell for the GNOME desktop
that makes it easy to manage your files and the rest of your system.
It allows to browse directories on local and remote filesystems, preview
files and launch applications associated with them.
It is also responsible for handling the icons on the GNOME desktop.

%package extensions
Summary:        Nautilus extensions library
License:        LGPL-2.1-or-later

%description extensions
This package provides the libraries used by nautilus extensions.

%package devel
Summary:        Support for developing nautilus extensions
License:        LGPL-2.1-or-later
Requires:       %{name}%{_isa} = %{version}-%{release}
Requires:       %{name}-extensions%{_isa} = %{version}-%{release}

%description devel
This package provides libraries and header files needed
for developing nautilus extensions.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

# Remove -Werror from compiler flags
sed -i '/-Werror/d' meson.build

%build
%meson \
  -Ddocs=true \
  -Dextensions=true \
  -Dintrospection=true \
  -Dselinux=true \
  -Dcloudproviders=%{?with_cloudproviders:true}%{?!with_cloudproviders:false}
  %{nil}
%meson_build

%install
%meson_install

%find_lang %{name}

%check
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/org.gnome.Nautilus.metainfo.xml
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop

%files  -f %{name}.lang
%doc NEWS README.md
%license LICENSE
%{_datadir}/applications/*
%{_bindir}/*
%{_datadir}/dbus-1/services/org.freedesktop.FileManager1.service
%{_datadir}/dbus-1/services/org.gnome.Nautilus.service
%exclude %{_datadir}/dbus-1/services/org.gnome.Nautilus.Tracker3.Miner.Extract.service
%exclude %{_datadir}/dbus-1/services/org.gnome.Nautilus.Tracker3.Miner.Files.service
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/search-providers
%{_datadir}/gnome-shell/search-providers/org.gnome.Nautilus.search-provider.ini
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Nautilus.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Nautilus-symbolic.svg
%{_mandir}/man1/nautilus.1*
%{_mandir}/man1/nautilus-autorun-software.1*
%{_datadir}/glib-2.0/schemas/org.gnome.nautilus.gschema.xml
%{_datadir}/nautilus/
%exclude %{_datadir}/localsearch3/domain-ontologies/org.gnome.Nautilus.domain.rule
%{_libdir}/nautilus/extensions-4/libnautilus-image-properties.so
%{_libdir}/nautilus/extensions-4/libtotem-properties-page.so
%{_metainfodir}/org.gnome.Nautilus.metainfo.xml

%files extensions
%license libnautilus-extension/LICENSE
%{_libdir}/libnautilus-extension.so.4*
%{_libdir}/girepository-1.0/Nautilus-4.0.typelib
%dir %{_libdir}/nautilus
%dir %{_libdir}/nautilus/extensions-4

%files devel
%{_includedir}/nautilus
%{_libdir}/pkgconfig/libnautilus-extension-4.pc
%{_libdir}/libnautilus-extension.so
%{_datadir}/gir-1.0/Nautilus-4.0.gir
%doc %{_datadir}/doc/nautilus/

%changelog
%autochangelog
