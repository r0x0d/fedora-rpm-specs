%global apiver  6.0

Name:           libgda
Epoch:          1
Version:        6.0.0
Release:        11%{?dist}
Summary:        Library for writing gnome database programs

License:        LGPL-2.0-or-later
URL:            http://www.gnome-db.org/
Source:         http://ftp.gnome.org/pub/GNOME/sources/%{name}/6.0/%{name}-%{version}.tar.xz

Patch0:         mariadb.patch
Patch1:         signed-int.patch

BuildRequires:    gcc
BuildRequires:    gcc-c++
BuildRequires:    pkgconfig >= 0.8
BuildRequires:    glade-devel
BuildRequires:    glib2-devel >= 2.38.0
BuildRequires:    gtk3-devel >= 3.0.0
BuildRequires:    gtksourceview3-devel
BuildRequires:    goocanvas2-devel
BuildRequires:    graphviz-devel >= 2.26.0
BuildRequires:    iso-codes-devel
BuildRequires:    itstool
BuildRequires:    libxslt-devel >= 1.0.9
BuildRequires:    sqlite-devel >= 3.22.0
BuildRequires:    libgcrypt-devel
BuildRequires:    libgee-devel
BuildRequires:    gobject-introspection-devel >= 0.6.5
BuildRequires:    libxml2-devel readline-devel json-glib-devel
BuildRequires:    gtk-doc intltool gettext flex bison perl(XML::Parser)
BuildRequires:    libsecret-devel
BuildRequires:    libsoup-devel
BuildRequires:    openssl-devel
BuildRequires:    yelp-tools
BuildRequires:    vala
BuildRequires:    make
BuildRequires:    gnome-common
BuildRequires:    meson
BuildRequires:    valadoc
BuildRequires:    openldap-devel
BuildRequires:    mariadb-connector-c-devel
BuildRequires:    libpq-devel
BuildRequires:    sqlcipher-devel

Provides: %{name}-bdb%{?_isa} = 1:%{version}-%{release}
Obsoletes: %{name}-bdb <= 1:5.2.10-4

Provides: %{name}-ldap%{?_isa} = 1:%{version}-%{release}
Obsoletes: %{name}-ldap <= 1:5.2.10-4

Provides: %{name}-sqlcipher%{?_isa} = 1:%{version}-%{release}
Obsoletes: %{name}-sqlcipher <= 1:5.2.10-4

Provides: %{name}-mdb%{?_isa} = 1:%{version}-%{release}
Obsoletes: %{name}-mdb <= 1:5.2.10-4

Provides: %{name}-java%{?_isa} = 1:%{version}-%{release}
Obsoletes: %{name}-java <= 1:5.2.10-4

Provides: %{name}-web%{?_isa} = 1:%{version}-%{release}
Obsoletes: %{name}-web <= 1:5.2.10-4

%description
%{name} is a library that eases the task of writing Gtk3-based database
programs.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package ui
Summary:         UI extensions for %{name}
Requires:        %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description ui
%{name}-ui extends %{name} providing graphical widgets (Gtk+).

%package        ui-devel
Summary:        Development files for %{name}-ui
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-ui%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{epoch}:%{version}-%{release}
Requires:       gtk3-devel%{?_isa} >= 3.0.0

%description    ui-devel
The %{name}-ui-devel package contains libraries and header files for
developing applications that use %{name}-ui.

%package tools
Summary:         Graphical tools for %{name}
Requires:        %{name}-ui%{?_isa} = %{epoch}:%{version}-%{release}

%description tools
This %{name}-tools package provides graphical tools for %{name}.

%package sqlite
Summary:        SQLite provider for %{name}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}
Requires:       sqlite-libs%{?isa} >= 3.22.0

%description sqlite
This %{name}-sqlite includes the %{name} SQLite provider.

%package sqlcipher
Summary:        SQLiteCipher provider for %{name}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}

%description sqlcipher
This %{name}-sqlcipher includes the %{name} SQLiteCipher provider.

%package mysql
Summary:        Mysql provider for %{name}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}

%description mysql
This %{name}-mysql includes the %{name} Mysql provider.

%package postgres
Summary:        Postgres provider for %{name}
Requires:       %{name}%{?isa} = %{epoch}:%{version}-%{release}

%description postgres
This %{name}-postgres includes the %{name} PostgreSQL provider.

%prep
%autosetup -p1
NOCONFIGURE=1 srcdir=. gnome-autogen.sh

# AUTHORS not in UTF-8
iconv --from=ISO-8859-1 --to=UTF-8 AUTHORS > AUTHORS.new && \
touch -r AUTHORS AUTHORS.new && mv AUTHORS.new AUTHORS

%build
%meson -Djson=true -Dldap=true -Ddoc=true -Dexperimental=true -Dhelp=true -Dui=true -Dlibsoup=true -Dlibsecret=true -Dflatpak=false -Dsqlcipher=true -Dgraphviz=true
#-Dtools=true
#        -Dexamples=false \

%meson_build


%install
%meson_install
mkdir -p %{buildroot}%{_sysconfdir}/%{name}-%{apiver}/
install data/config %{buildroot}%{_sysconfdir}/%{name}-%{apiver}/config
install libgda-ui/data/import_encodings.xml %{buildroot}%{_datadir}/%{name}-%{apiver}/import_encodings.xml

%find_lang libgda-6.0

%files -f libgda-6.0.lang
%license COPYING
%doc AUTHORS ChangeLog README NEWS
%dir %{_sysconfdir}/%{name}-%{apiver}/
%config(noreplace) %{_sysconfdir}/%{name}-%{apiver}/config
%{_libdir}/%{name}-%{apiver}.so.*
%{_libdir}/%{name}-report-%{apiver}.so.*
%{_libdir}/%{name}-xslt-%{apiver}.so.*
%dir %{_libdir}/%{name}-%{apiver}/
%dir %{_libdir}/%{name}-%{apiver}/providers/
%{_libdir}/libgda-%{apiver}/providers/libgda-ldap-%{apiver}.so
%{_libdir}/girepository-1.0/Gda-%{apiver}.typelib
%dir %{_datadir}/%{name}-%{apiver}/
%dir %{_datadir}/%{name}-%{apiver}/dtd/
%{_datadir}/%{name}-%{apiver}/dtd/libgda-*.dtd
%{_datadir}/%{name}-%{apiver}/import_encodings.xml
%{_datadir}/%{name}-%{apiver}/information_schema.xml

%files devel
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%doc %{_datadir}/gtk-doc/html/%{name}-%{apiver}
%{_datadir}/gir-1.0/Gda-%{apiver}.gir
%dir %{_includedir}/%{name}-%{apiver}/
%{_includedir}/%{name}-%{apiver}/%{name}
%{_includedir}/%{name}-%{apiver}/%{name}-report
%{_libdir}/%{name}-%{apiver}.so
%{_libdir}/%{name}-report-%{apiver}.so
%{_libdir}/%{name}-xslt-%{apiver}.so
%{_libdir}/pkgconfig/%{name}-%{apiver}.pc
%{_libdir}/pkgconfig/%{name}-*-%{apiver}.pc
%exclude %{_libdir}/pkgconfig/%{name}-ui-%{apiver}.pc
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libgda-%{apiver}.vapi
%{_datadir}/vala/vapi/libgda-%{apiver}.deps
%{_datadir}/devhelp/books/Gda-%{apiver}/
%{_datadir}/devhelp/books/Gdaui-%{apiver}/
%{_includedir}/%{name}-%{apiver}/providers/


%files ui
%{_libdir}/%{name}-ui-%{apiver}.so.*
%{_libdir}/%{name}-%{apiver}/plugins/%{name}-ui-plugins-%{name}-%{apiver}.so
%{_libdir}/girepository-1.0/Gdaui-%{apiver}.typelib
%{_datadir}/%{name}-%{apiver}/ui/

%files ui-devel
%{_includedir}/%{name}-%{apiver}/%{name}-ui
%{_libdir}/%{name}-ui-%{apiver}.so
%{_libdir}/pkgconfig/%{name}-ui-%{apiver}.pc
%{_datadir}/%{name}-%{apiver}/demo/
%{_datadir}/gir-1.0/Gdaui-%{apiver}.gir
%{_datadir}/glade/
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/libgdaui-%{apiver}.vapi

%files tools
%doc %{_datadir}/gtk-doc/html/libgdaui-%{apiver}/
%{_bindir}/gda-*
%{_bindir}/org.gnome.gda.*
%{_bindir}/trml2html.py
%{_bindir}/trml2pdf.py
%{_datadir}/%{name}-%{apiver}/gda_trml2html
%{_datadir}/%{name}-%{apiver}/gda_trml2pdf

%files sqlite
%{_libdir}/%{name}-%{apiver}/providers/%{name}-sqlite-%{apiver}.so

%files mysql
%{_libdir}/libgda-%{apiver}/providers/libgda-mysql-%{apiver}.so

%files postgres
%{_libdir}/libgda-%{apiver}/providers/libgda-postgres-%{apiver}.so

%files sqlcipher
%{_libdir}/libgda-%{apiver}/providers/libgda-sqlcipher-%{apiver}.so

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Sep 28 2023 Gwyn Ciesla <gwync@protonmail.com> -1:6.0.0-7
- mariadb rebuild.

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Mar 04 2023 Gwyn Ciesla <gwync@protonmail.com> - 1:6.0.0-5
- migrated to SPDX license

* Tue Feb 21 2023 Gwyn Ciesla <gwync@protonmail.com> -1:6.0.0-4
- Update glib and sqlite dependencies

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 29 2022 Carl George <carl@george.computer> - 1:6.0.0-2
- Rebuild for sqlcipher soname bump

* Thu Aug 04 2022 Gwyn Ciesla <gwync@protonmail.com> - 1:6.0.0-1
- 6.0.0
- Only ship supported providers: PostgreSQL, MySQL, SQLite.

* Fri Feb 11 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1:5.2.10-7
- Workaround to detect JRE 17 (java 17)

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1:5.2.10-6
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 22 2021 Gwyn Ciesla <gwync@protonmail.com> - 1:5.2.10-4
- Patch for CVE-2021-39359

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1:5.2.10-3
- Rebuilt with OpenSSL 3.0.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Hans de Goede <hdegoede@redhat.com> - 1:5.2.10-1
- New upstream bugfix release 5.2.10
- gda_trml2html/2pdf scripts have been ported to python3, restore them
- Rebuild against new mdbtools-libs

* Mon Feb 08 2021 Pavel Raiskup <praiskup@redhat.com> - 1:5.2.9-8
- rebuild for libpq ABI fix rhbz#1908268

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1:5.2.9-5
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 12 2019 Fabio Valentini <decathorpe@gmail.com> - 1:5.2.9-3
- Remove report converter functionality that relies on ancient python2 scripts.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed May 08 2019 Kalev Lember <klember@redhat.com> - 1:5.2.9-1
- Update to 5.2.9

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1:5.2.8-4
- Rebuild for readline 8.0

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 06 2019 Björn Esser <besser82@fedoraproject.org> - 1:5.2.8-2
- Add patch to use explicit python2 shebangs, fixes FTBFS

* Mon Dec 03 2018 Kalev Lember <klember@redhat.com> - 5.2.8-1
- Update to 5.2.8
- Move libgda-ui-plugins to correct subpackage
- Drop appdata override as the appdata file is now upstream
- Drop various rpm scriptlets that are no longer needed these days
- Use make_build and make_install macros
- Use license macro for COPYING
- Enable vala vapi generation
- BR mariadb-connector-c-devel instead of mysql-devel (#1494068)
- Drop bdbsql provider that doesn't build

* Sun Sep 16 2018 Haïkel Guémar <hguemar@fedoraproject.org> - 1:5.2.4-1
- Upstream 5.2.4

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 1:5.2.2-12
- Rebuild for readline 7.x

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 02 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 1:5.2.2-10
- Add libgda-5.2.2-geninclude.pl.patch (Fix FTBFS).

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 1:5.2.2-8
- Add an AppData file for the software center

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 22 2014 Kalev Lember <kalevlember@gmail.com> - 1:5.2.2-6
- Rebuilt for gobject-introspection 1.41.4

* Mon Jun 16 2014 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 1:5.2.2-5
- Handle AArch64 as well

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Brent Baude <baude@us.ibm.com> - 1:5.2.2-3
- Adding ppc64le arch description to spec

* Sun May 18 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1:5.2.2-2
- Rebuild (mdbtools)

* Sat May 17 2014 Kalev Lember <kalevlember@gmail.com> - 1:5.2.2-1
- Update to 5.2.2
- Fix FTBFS with -Werror=format-security (#1037160)
- Fix the build with JRE 1.8
- Install the gdaui Glade catalog

* Wed Apr 23 2014 Tomáš Mráz <tmraz@redhat.com> - 1:5.1.2-5
- Rebuild for new libgcrypt

* Tue Aug  6 2013 Haïkel Guémar <hguemar@fedoraproject.org> - 1:5.1.2-4
- fix FTBFS (RHBZ #992077)
- cleanup rpm conditionals

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 26 2013 Kalev Lember <kalevlember@gmail.com> - 1:5.1.2-2
- Rebuilt for gtksourceview3 soname bump

* Tue Mar 19 2013 Haïkel Guémar <hguemar@fedoraproject.org> - 1:5.1.2-1
- upstream 5.1.2
- dropped upstreamed patches

* Sun Feb 24 2013 Haïkel Guémar <hguemar@fedoraproject.org> - 1:5.1.1-6
- rebuilt against newer graphviz (RHBZ #914131)
- remove deprecated graphviz API calls in gda-browser
- build system workaround (RHBZ #904790)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:5.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 25 2012 Dan Horák <dan[at]danny.cz> - 1:5.1.1-4
- fix Java detection on secondary arches

* Wed Oct 24 2012 Kalev Lember <kalevlember@gmail.com> - 1:5.1.1-3
- Enable introspection (#869072)

* Mon Oct 22 2012 Kalev Lember <kalevlember@gmail.com> - 1:5.1.1-2
- Add back the epoch
- Build without scrollkeeper support
- Properly obsolete subpackages that got removed in v4->v5 transition
- Fix some rpm directory ownership issues
- Add icon cache scriptlets

* Sun Oct 21 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 5.1.1-1
- upstream 5.1.1 based on libgda5 review (RHBZ #788569)

* Sun Aug  5 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.2.13-1
- upstream 4.2.13
- bug fixes to MySQL and MDB providers and various minor issues

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.2.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat May 05 2012 Kalev Lember <kalevlember@gmail.com> - 1:4.2.12-3
- switch to libdb-devel
- fix the build with OpenJDK7

* Sun Jan 22 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.2.12-2
- fix gobject-introspection support
- clean up spec (removed old obsoletes)

* Sun Jan 22 2012 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.2.12-1
- upstream 4.2.12

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Nov 26 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.2.11-1
- upstream 4.1.11
- sqlite provider can load sqlite extensions using "SELECT load_extension ('xxx')"
- remove unused BR

* Thu Aug 25 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.2.8-1
- upstream 4.2.8
- ldap read-only support is back

* Mon Jul  4 2011 Mark Chappell <tremble@fedoraproject.org> - 1:4.2.5-2
- Rebuild for graphviz so name bump.

* Sun Apr 10 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.2.5-1
- upstream 4.2.5

* Wed Mar 23 2011 Dan Horák <dan@danny.cz> - 1:4.2.4-3
- rebuilt for mysql 5.5.10 (soname bump in libmysqlclient)

* Tue Feb 22 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.2.4-2
- fix sqlite loading (RHBZ #673809)

* Thu Feb 17 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.2.4-1
- upstream 4.2.4

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan  8 2011  <builder@zangetsu.seireitei> - 1:4.2.2-2
- drop sqlite patch: should be fixed in latest xulrunner package

* Tue Nov 30 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.2.2-1
- Upstream 4.2.2
- Cleaned spec from deprecated providers support
- Fix sqlite3 shared library loading (RHBZ #658471)

* Tue Oct 26 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.2.0-1
- Update to upstream 4.2.0
- New provider: sqlcipher (SQLite encryption extension)
- New patch fixing 4.2.0 build issue
- Disable GObject introspection since it's broken

* Wed Jun 16 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.1.6-1
- Update to upstream 4.1.6
- Add new BR: gnome-doc-utils
- Dropped BR: gir-repository

* Tue Apr 27 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.1.4-1
- Update to upstream 4.1.4 (required by Glom)
- Added web provider and ui subpackages
- Added new BR (gtk2, unique, goocanvas, graphviz) for libgda-ui

* Thu Apr 22 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.0.8-2
- add gir descriptions files

* Thu Apr 22 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 1:4.0.8-1
- Update to upstream 4.0.8

* Thu Feb 18 2010 Denis Leroy <denis@poolshark.org> - 1:4.0.7-1
- Update to upstream 4.0.7

* Mon Jan 18 2010 Denis Leroy <denis@poolshark.org> - 1:4.0.6-1
- Update to upstream 4.0.6
- Added Java JDBC provider subpackage

* Sat Nov  7 2009 Denis Leroy <denis@poolshark.org> - 1:4.0.5-1
- Update to upstream 4.0.5
- Source URL fix

* Tue Sep 15 2009 Denis Leroy <denis@poolshark.org> - 1:4.0.4-1
- Update to upstream version 4.0.4

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 1:4.0.2-3
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 25 2009 Denis Leroy <denis@poolshark.org> - 1:4.0.2-1
- Update to upstream 4.0.2
- Use system sqlite library

* Mon Mar 23 2009  <denis@poolshark.org> - 1:4.0.0-1
- Update to upstream 4.0.0

* Wed Mar  4 2009 Denis Leroy <denis@poolshark.org> - 1:3.99.12-1
- Update to upstream 3.99.12

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.99.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 14 2009 Denis Leroy <denis@poolshark.org> - 1:3.99.11-1
- Update to 3.99.11 (many bug fixes)

* Fri Jan 16 2009 Denis Leroy <denis@poolshark.org> - 1:3.99.8-1
- Switch to 4.0 ABI
- Update to upstream 3.99.8
- Patch updates (upstreamed and ported)
- Added JAVA package flag, currently disabled

* Mon Oct 27 2008 Denis Leroy <denis@poolshark.org> - 1:3.1.2-6
- Added patch to fix providers path on x86_64 (#468510)

* Thu Jul 10 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1:3.1.2-5
- Rebuild against new db4-4.7

* Tue Jun 17 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1:3.1.2-4
- Rebuild against new freetds

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:3.1.2-3
- Autorebuild for GCC 4.3

* Sat Jan 26 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1:3.1.2-2
- Rebuid now that the system sqlite has column metadata enabled, so that we
  use the system version instead of our own private copy (bz 430258)

* Fri Jan 25 2008 Hans de Goede <j.w.r.degoede@hhs.nl> 1:3.1.2-1
- New upstream release 3.1.2 (needed for new gnumeric)
- Drop upstreamed / no longer needed patches

* Thu Dec 06 2007 Release Engineering <rel-eng at fedoraproject dot org> - 3.0.1-6
- Rebuild for deps

* Sun Oct 21 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1:3.0.1-5
- Rebuild to fix untranslated strings on x86_64 in
  /usr/share/libgda-3.0/sqlite_specs_drop_index.xml
  which caused multilib problems (bz 342101)

* Fri Aug 17 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1:3.0.1-4
- Fix building on ppc64 again (patch configure not configure.in, now we are
  no longer running autoconf)

* Wed Aug 15 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1:3.0.1-3
- Enable microsoft access (mdb) support now that mdbtools is in Fedora
- Enable xBase (dBase, Clipper, FoxPro) support, it seems that xbase has been
  available for quite a while now
- Switch from using mysqlclient10 to using mysql-libs for the msql provider

* Wed Aug  8 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1:3.0.1-2
- Build against system sqlite instead of own private copy (this is possible now
  that the system sqlite is of a high enough version)
- Enable FreeTDS provider (FreeTDS is in Fedora now)
- Update License tag for new Licensing Guidelines compliance

* Sun May 27 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1:3.0.1-1
- New upstream release 3.0.1
- Remove mono bindings sub-package as upstream no longer includes them

* Thu May 10 2007 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.9.100-12
- Don't build mono/sharp bits on ppc64
- Fixup packaging of sharp bindings to match the mono packaging guidelines

* Fri Dec 15 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.9.100-11
- Rebuild for new postgres

* Mon Aug 28 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.9.100-10
- FE6 Rebuild

* Tue Jun 20 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.9.100-9
- Add BuildRequires: libtool hopefully _really_ fixing building with the new
  stripped mock config. (Drop BR: autoconf which is implied by BR: automake).

* Thu Jun 15 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.9.100-8
- Add BuildRequires: automake, autoconf to fix building with the new even more
  stripped mock config.

* Sat Jun 10 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.9.100-7
- Add BuildRequires: gettext, bison, flex, gamin-devel to fix building with
  new stripped mock config.

* Thu May 11 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.9.100-6
- Move Obsoletes and Provides for plugins out of the plugins %%description,
  so that they actually Obsolete and Provide instead of showing up in rpm -qi
  (bug 191213).

* Thu May  4 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.9.100-5
- Add patch3 fixing a couple of x86_64 bugs (bz 190366)

* Mon Feb 13 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.9.100-4
- Bump release and rebuild for new gcc4.1 and glibc.
- Make sqlite plugin use system sqlite not build in version
- Make sqlite plugin a seperate package again
- Attempt to properly install C-sharp/mono bindings
- Add %%{?dist} for consistency with my other packages
- Remove static lib from -devel package

* Tue Jan 17 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.9.100-3
- Make -sharp package Require the main package.

* Mon Jan 16 2006 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.9.100-2
- Remove unneeded requires (.so reqs are automaticly picked up by rpm).
- Add BuildRequires for building libgda-sharp

* Sun Nov 27 2005 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.9.100-1
- New upstream version
- Drop 4 intergrated patches
- Removed sqlite configurability, it is now an internal part of the upstream
  sources.

* Fri Aug  5 2005 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.2.0-8
- Remove libgda.la file from devel package.

* Sat Jun 25 2005 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.2.0-7
- Added Patch4: libgda-1.2.0-libdir.patch which fixes loading of
  database providers on platforms with a lib64 dir. Thanks to:
  Bas Driessen <bas.driessen@xobas.com> for the patch.
- Enabled building of libgda-ldap and libgda-sqlite by default.

* Tue Jun 21 2005 Hans de Goede <j.w.r.degoede@hhs.nl> 1:1.2.0-6
- rebuild so that we depend on the proper version of libpq.so (#160917)
- change names of database providers from gda-xxx to libgda-xxx (#160917)

* Wed Mar  2 2005 Caolan McNamara <caolanm@redhat.com> 1:1.2.0-5
- rebuild with gcc4

* Fri Feb 11 2005 Caolan McNamara <caolanm@redhat.com> 1:1.2.0-4
- well, that was moronic

* Thu Feb 10 2005 Caolan McNamara <caolanm@redhat.com> 1:1.2.0-3
- bandaid

* Wed Feb  9 2005 Jeremy Katz <katzj@redhat.com> - 1:1.2.0-2
- rebuild to try to fix broken dep

* Fri Feb 4 2005 Caolan McNamara <caolanm@redhat.com> 1:1.2.0-1
- bump to latest version
- drop integrated break warning patch
- update configure patch

* Wed Jan 12 2005 Tim Waugh <twaugh@redhat.com> 1:1.0.4-5
- Rebuilt for new readline.

* Sat Oct 30 2004 Caolan McNamara <caolanm@redhat.com> 1:1.0.4-4
- Use mysqlclient10

* Fri Oct  8 2004 Caolan McNamara <caolanm@redhat.com> 1:1.0.4-3
- #rh135043# Extra BuildRequires

* Thu Sep  9 2004 Bill Nottingham <notting@redhat.com> 1:1.0.4-2
- %%defattr

* Thu Aug 12 2004 Caolan McNamara <caolanm@redhat.com> 1:1.0.4-1
- Initial Red Hat import
- patch for missing break statement
- fixup devel package requirement pickiness
- autoconf patch to pick up correct mysql path from mysql_config (e.g. x64)
- autoconf patch to just look in the normal place for postgres first

* Tue Mar 11 2003 David Hollis <dhollis@davehollis.com>
- Fix --with-tds & --without-tds to match what configure wants

* Tue Jan 28 2003 Yanko Kaneti <yaneti@declera.com>
- Remove the idl path
- Include gda-config man page
- add --without-* for disabled providers
- package and use the omf/scrollkeeper bits

* Tue Dec 31 2002 David Hollis <dhollis@davehollis.com>
- Added sqlite-devel buildreq
- Include gda-config-tool man page

* Mon Aug 19 2002 Ben Liblit <liblit@acm.org>
- Fixed version number substitutions

- Removed some explicit "Requires:" prerequisites that RPM will figure
  out on its own.  Removed explicit dependency on older MySQL client
  libraries

- Required that the ODBC development package be installed if we are
  building the ODBC provider

- Created distinct subpackages for each provider, conditional on that
  provider actually being enabled; some of these will need to be
  updated as the family of available providers changes

- Updated files list to match what "make install" actually installs

- Added URL tag pointing to GNOME-DB project's web site

* Tue Feb 26 2002 Chris Chabot <chabotc@reviewboard.com>
- Added defines and configure flags for all supported DB types

* Mon Feb 25 2002 Chris Chabot <chabotc@reviewboard.com>
- Cleaned up formatting
- Added Requirements
- Added defines for postgres, mysql, odbc support

* Thu Feb 21 2002 Chris Chabot <chabotc@reviewboard.com>
- Initial spec file
