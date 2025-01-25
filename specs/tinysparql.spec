%global systemd_units tinysparql-xdg-portal-3.service

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           tinysparql
Version:        3.8~rc
Release:        3%{?dist}
Summary:        Desktop-neutral metadata database and search tool

License:        GPL-2.0-or-later
URL:            https://gnome.pages.gitlab.gnome.org/tinysparql/
Source0:        https://download.gnome.org/sources/tinysparql/3.8/tinysparql-%{tarball_version}.tar.xz

BuildRequires:  asciidoc
BuildRequires:	gcc
BuildRequires:  gettext
BuildRequires:  gi-docgen
%if ! 0%{?rhel} || 0%{?rhel} < 10
# libstemmer is not part of RHEL 10
BuildRequires:  libstemmer-devel
%endif
BuildRequires:  meson
BuildRequires:  python3-gobject
BuildRequires:  systemd-rpm-macros
BuildRequires:  vala
BuildRequires:  pkgconfig(avahi-glib)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  /usr/bin/dbus-run-session

# renamed in F42
Obsoletes:      tracker < 3.7.3-4
Provides:       tracker = %{version}-%{release}
Provides:       tracker%{?_isa} = %{version}-%{release}

Requires: libtinysparql%{?_isa} = %{version}-%{release}

Recommends: localsearch%{?_isa}

%description
Tinysparql is a powerful desktop-neutral first class object database,
tag/metadata database and search tool.

It consists of a common object database that allows entities to have an
almost infinite number of properties, metadata (both embedded/harvested as
well as user definable), a comprehensive database of keywords/tags and
links to other entities.

It provides additional features for file based objects including context
linking and audit trails for a file object.

Metadata indexers are provided by the localsearch package.


%package -n     libtinysparql
Summary:        Libtinysparql library
License:        LGPL-2.1-or-later
Recommends:     %{name}%{?_isa} = %{version}-%{release}

%description -n libtinysparql
This package contains the libtinysparql library.

# renamed in F42
Obsoletes:      libtracker-sparql < 3.7.3-4
Provides:       libtracker-sparql = %{version}-%{release}
Provides:       libtracker-sparql%{?_isa} = %{version}-%{release}


%package        devel
Summary:        Development files for %{name}
License:        LGPL-2.1-or-later
Requires:       libtinysparql%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
# docs/reference/COPYING
License:        LicenceRef-Fedora-Public-Domain AND LGPL-2.1-or-later AND GPL-2.0-or-later

%description doc
This package contains the documentation for %{name}.


%prep
%autosetup -p1 -n %{name}-%{tarball_version}


%build
%meson \
  -Dunicode_support=icu \
  -Dsystemd_user_services_dir=%{_userunitdir} \
%if ! 0%{?rhel} || 0%{?rhel} >= 10
  -Dstemmer=disabled \
%endif
  %{nil}

%meson_build


%install
%meson_install

%find_lang tinysparql3


%post
%systemd_user_post tinysparql-xdg-portal-3.service

%preun
%systemd_user_preun tinysparql-xdg-portal-3.service

%postun
%systemd_user_postun_with_restart tinysparql-xdg-portal-3.service


%files -f tinysparql3.lang
%license COPYING COPYING.GPL
%doc AUTHORS NEWS README.md
%{_bindir}/tinysparql
%{_libexecdir}/tinysparql-sql
%{_libexecdir}/tinysparql-xdg-portal-3
%{_datadir}/dbus-1/services/org.freedesktop.portal.Tracker.service
%{_mandir}/man1/tinysparql*.1*
%{_userunitdir}/tinysparql-xdg-portal-3.service
%{bash_completions_dir}/tinysparql

%files -n libtinysparql
%license COPYING COPYING.LGPL
%{_libdir}/girepository-1.0/Tracker-3.0.typelib
%{_libdir}/girepository-1.0/Tsparql-3.0.typelib
%{_libdir}/libtinysparql-3.0.so.0*
%{_libdir}/libtracker-sparql-3.0.so*
%{_libdir}/tinysparql-3.0/
%{_datadir}/gir-1.0/Tracker-3.0.gir

%files devel
%license COPYING COPYING.LGPL
%{_includedir}/tinysparql-3.0/
%{_libdir}/libtinysparql-3.0.so
%{_libdir}/pkgconfig/tinysparql-3.0.pc
%{_libdir}/pkgconfig/tracker-sparql-3.0.pc
%{_datadir}/vala/vapi/tinysparql-3.0.deps
%{_datadir}/vala/vapi/tinysparql-3.0.vapi
%{_datadir}/gir-1.0/Tsparql-3.0.gir
%{_datadir}/vala/vapi/tracker-sparql-3.0.deps
%{_datadir}/vala/vapi/tracker-sparql-3.0.vapi

%files doc
%license docs/reference/COPYING
%{_docdir}/Tsparql-3.0/


%changelog
* Thu Jan 23 2025 Nieves Montero <nmontero@redhat.com> - 3.8.rc-3
- Minor change in %files

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.8~rc-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 03 2024 Nieves Montero <nmontero@redhat.com> - 3.8.rc-1
- Rename tracker to tinysparql
- Rename libtracker-sparql to libtinysparql
- Update to 3.8~rc