Name:           gnome-desktop-sharp
Version:        2.26.0
Release:        52%{?dist}
Summary:        .NET language binding for mono

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            http://www.mono-project.com/GtkSharp
Source0:        http://ftp.gnome.org/pub/gnome/sources/%{name}/2.26/%{name}-%{version}.tar.bz2
Patch1:         %{name}-lib-target.patch

BuildRequires:  gcc-c++
BuildRequires:  mono-devel, gtk2-devel
BuildRequires:  librsvg2-devel, vte291-devel
BuildRequires:  libwnck-devel, gtksourceview2-devel
BuildRequires:  gnome-sharp-devel
BuildRequires:  gnome-desktop3-devel
BuildRequires:  vte-devel
BuildRequires:  gtk-sharp2-gapi >= 2.12.0
BuildRequires:  gtk-sharp2-devel >= 2.12.0
BuildRequires: make

Provides:       gtksourceview2-sharp = 2:%{version}-%{release}
Obsoletes:      gtksourceview2-sharp < 2:2.20.1-2

# Mono only available on these:
ExclusiveArch: %mono_arches


%description
GnomeDesktop is a .NET language binding for assorted
GNOME libraries from the desktop release.

%package         devel
Summary:         Developing files for gnome-Desktop-sharp
Requires:        %{name} = %{version}-%{release}
Requires:        pkgconfig

Provides:        gtksourceview2-sharp-devel = 2:%{version}-%{release}
Obsoletes:       gtksourceview2-sharp-devel < 2:2.20.1-2

%description     devel
Package %{name}-devel provides development files for writing
%{name} applications.


%prep
%setup -q
%patch -P1 -p1 -b .target
sed -i -e 's/gnome-desktop-2/gnome-desktop-3/g' configure
sed -i -e 's/VTE_REQUIRED_VERSION=.*/VTE_REQUIRED_VERSION=0.28.2/g' configure
sed -i -e 's!@libdir@!${exec_prefix}/lib/!g' gtksourceview/gtksourceview2-sharp.pc.in

# Fix permission
chmod 0644 HACKING

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

# Remove libttol archive
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'


%ldconfig_scriptlets


%files
%doc COPYING ChangeLog AUTHORS README
%{_libdir}/*.so
%{_prefix}/lib/mono/gac/gnomedesktop-sharp
%{_prefix}/lib/mono/gac/gtksourceview2-sharp
%{_prefix}/lib/mono/gac/rsvg2-sharp
%{_prefix}/lib/mono/gac/vte-sharp
%{_prefix}/lib/mono/gac/wnck-sharp
%{_prefix}/lib/mono/gnomedesktop-sharp-2.20
%{_prefix}/lib/mono/gtksourceview2-sharp-2.0
%{_prefix}/lib/mono/rsvg2-sharp-2.0
%{_prefix}/lib/mono/vte-sharp-0.16
%{_prefix}/lib/mono/wnck-sharp-2.20
%{_datadir}/gnomedesktop-sharp
%{_datadir}/gtksourceview2-sharp
%{_datadir}/rsvg2-sharp
%{_datadir}/vte-sharp
%{_datadir}/wnck-sharp

%files           devel
%doc HACKING
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.26.0-51
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-49
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-48
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-45
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-41
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 29 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.26.0-39
- switch from gnome-desktop to gnome-desktop3

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Oct 04 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 2.26.0-37
- switch from vte to vte291

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.0-29
- mono rebuild for aarch64 support

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.26.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Oct 24 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2.26.0-27
- Drop gnomeprintui

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 2.26.0-25
- Rebuild (mono4)

* Tue Mar 24 2015 Than Ngo <than@redhat.com> - 2.26.0-24
- use %%mono_arches

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Brent Baude <baude@us.ibm.com> - 2.26.0-21
- Fix type in macro

* Sat May 24 2014 Brent Baude <baude@us.ibm.com> - 2.26.0-20
- Change ppc64 to power64 macro

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.26.0-15
- Rebuild for new libpng

* Sun Oct 23 2011 Christian Krause <chkr@fedoraproject.org> - 2.26.0-14
- Change paths for mono assemblies according to updated packaging
  guidelines (http://fedoraproject.org/wiki/Packaging:Mono)

* Thu Feb 10 2011 Christian Krause <chkr@fedoraproject.org> - 2.26.0-13
- Disable gnome-panel bindings

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Dan Horák <dan[at]danny.cz> - 2.26.0-11
- updated the supported arch list

* Mon Dec 20 2010 Christian Krause <chkr@fedoraproject.org> - 2.26.0-10
- Rebuilt in rawhide (FTBFS BZ 660867)
- Disable gtkhtml3 support as directed in BZ 660867, comment #9

* Sun Oct 31 2010 Christian Krause <chkr@fedoraproject.org> - 2.26.0-9
- Rebuild again to create correct requires/provides capabilities

* Sat Oct 09 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> 2.26.0-8
- Rebuild

* Thu Jun 10 2010 Christian Krause <chkr@fedoraproject.org> - 2.26.0-7
- Rebuilt in rawhide (FTBFS BZ 600015)

* Thu Feb 11 2010 Xavier Lamien <laxathom@fedoraproject.org> - 2.26.0-6
- Fix libgnome-desktop target soname (BZ 563361)

* Mon Oct 26 2009 Dennis Gilmore <dennis@ausil.us> - 2.26.0-5
- Exclude sparc64

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.26.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 2.26.0-3
- Add support for ppc64

* Wed Apr 22 2009 Denis Leroy <denis@poolshark.org> - 2.26.0-2
- Rebuilt without nautilus-cd-burner (obsoleted)

* Mon Apr 06 2009 Xavier Lamien <lxtnow@gmail.com> - 2.26.0-1
- Update release.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.24.0-3
- and BR: libgnomeprintui22-devel

* Mon Oct 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.24.0-2
- add gnome-sharp-devel as BuildRequires

* Thu Oct 16 2008 Dan Winship <dwinship@redhat.com> - 2.24.0-1
- Update to 2.24.0

* Sat Jul 05 2008 Xavier Lamien <lxtnow[at]gmail.com> - 2.20.1-2
- Obsolete standalone package gtksourceview2-sharp.

* Sat Jul 05 2008 Xavier Lamien <lxtno[at]gmail.com> - 2.20.1-1
- Initial RPM Release.
