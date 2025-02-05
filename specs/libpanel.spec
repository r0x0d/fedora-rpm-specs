%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           libpanel
Version:        1.9.0
Release:        %autorelease
Summary:        IDE paneling library for GTK

License:        LGPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/libpanel
Source0:        https://download.gnome.org/sources/libpanel/1.9/libpanel-%{tarball_version}.tar.xz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(gi-docgen)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)

Requires:       hicolor-icon-theme

%description
libpanel is a collection of GTK widgets for IDE-like applications targeting
GNOME using GTK and libadwaita.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n libpanel-%{tarball_version}


%build
%meson
%meson_build


%install
%meson_install

%find_lang libpanel


%files -f libpanel.lang
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libpanel-1.so.1*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/Panel-1.typelib
%{_datadir}/icons/hicolor/scalable/actions/panel-*-symbolic.svg

%files devel
%{_includedir}/libpanel-1/
%{_libdir}/libpanel-1.so
%{_libdir}/pkgconfig/libpanel-1.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/Panel-1.gir
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libpanel-1.deps
%{_datadir}/vala/vapi/libpanel-1.vapi
%doc %{_datadir}/doc/panel-1.0/


%changelog
%autochangelog
