%global apiver 1.6
# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

%global glibmm24_version 2.46.2

Name:           atkmm
Version:        2.28.4
Release:        3%{?dist}
Summary:        C++ interface for the ATK library

License:        LGPL-2.1-or-later
URL:            https://www.gtkmm.org/
Source0:        https://download.gnome.org/sources/atkmm/%{release_version}/atkmm-%{version}.tar.xz

BuildRequires:  atk-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(glibmm-2.4) >= %{glibmm24_version}
BuildRequires:  libxslt
BuildRequires:  m4
BuildRequires:  meson
BuildRequires:  mm-common

Requires:       glibmm24%{?_isa} >= %{glibmm24_version}

%description
atkmm provides a C++ interface for the ATK library. Highlights
include typesafe callbacks, widgets extensible via inheritance and a
comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Developer's documentation for the atkmm library
BuildArch:      noarch
License:        LGPL-2.1-or-later AND MIT AND GPL-2.0-or-later AND (MIT OR GPL-2.0-or-later)
Requires:       %{name} = %{version}-%{release}
Requires:       glibmm24-doc

%description    doc
This package contains developer's documentation for the atkmm
library. Atkmm is the C++ API for the ATK accessibility toolkit library.

The documentation can be viewed either through the devhelp
documentation browser or through a web browser.


%prep
%setup -q


%build
%meson -Dbuild-documentation=true
%meson_build


%install
%meson_install


%files
%license COPYING
%doc NEWS README.md
%{_libdir}/libatkmm-%{apiver}.so.1*

%files devel
%{_includedir}/atkmm-%{apiver}/
%{_libdir}/libatkmm-%{apiver}.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/atkmm-%{apiver}/

%files doc
%doc %{_docdir}/atkmm-%{apiver}/
%doc %{_datadir}/devhelp/


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 David King <amigadave@amigadave.com> - 2.28.4-1
- Update to 2.28.4

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 10 2022 Kalev Lember <klember@redhat.com> - 2.28.3-1
- Update to 2.28.3

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 26 2021 Kalev Lember <klember@redhat.com> - 2.28.2-1
- Update to 2.28.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.28.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec 14 2020 Kalev Lember <klember@redhat.com> - 2.28.1-1
- Update to 2.28.1
- Switch to meson build system
- Update source URLs
- Tighten -devel subpackage deps
- Tighten soname globs

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 14 2020 Tom Stellard <tstellar@redhat.com> - 2.24.3-5
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jan 23 2019 Kalev Lember <klember@redhat.com> - 2.24.3-1
- Update to 2.24.3

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.24.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 30 2015 Kalev Lember <klember@redhat.com> - 2.24.2-1
- Update to 2.24.2

* Tue Sep 22 2015 Kalev Lember <klember@redhat.com> - 2.24.1-1
- Update to 2.24.1
- Drop conflicts with old gtkmm24 versions
- Use make_install macro

* Tue Sep 15 2015 Richard Hughes <rhughes@redhat.com> - 2.23.3-1
- Update to 2.23.3

* Tue Jun 30 2015 Kalev Lember <klember@redhat.com> - 2.23.1-1
- Update to 2.23.1
- Set minimum required glibmm24 version
- Use license macro for COPYING

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.22.7-5
- Rebuilt for GCC 5 C++11 ABI change

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 29 2013 Kalev Lember <kalevlember@gmail.com> - 2.22.7-1
- Update to 2.22.7
- Drop -devel package deps that rpmbuild takes care of automatically

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 27 2012 Kalev Lember <kalevlember@gmail.com> - 2.22.6-1
- Update to 2.22.6
- Switch to .xz tarballs

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Mar 31 2011 Kalev Lember <kalev@smartlink.ee> - 2.22.5-1
- Update to 2.22.5

* Fri Mar 25 2011 Kalev Lember <kalev@smartlink.ee> - 2.22.4-1
- Update to 2.22.4

* Tue Mar 01 2011 Kalev Lember <kalev@smartlink.ee> - 2.22.2-4
- Spec cleanup
- Actually co-own /usr/share/devhelp/ directory
- Require base package from -doc subpackage

* Mon Feb 21 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 2.22.2-3
- split doc into subpackage
- fix documentation location
- co-own /usr/share/devhelp

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 13 2011 Kalev Lember <kalev@smartlink.ee> - 2.22.2-1
- Update to 2.22.2

* Tue Sep 28 2010 Kalev Lember <kalev@smartlink.ee> - 2.22.0-1
- Update to 2.22.0

* Tue Sep 14 2010 Kalev Lember <kalev@smartlink.ee> - 2.21.2-2
- Co-own /usr/share/gtk-doc/ directory (#604169)

* Wed Jun 30 2010 Kalev Lember <kalev@smartlink.ee> - 2.21.2-1
- Update to 2.21.2

* Sat Jun 26 2010 Kalev Lember <kalev@smartlink.ee> - 2.21.1-2
- added missing Conflicts: gtkmm24-devel to -devel subpackage
- calculate two-digit download directory from three-digit package version

* Wed Jun 23 2010 Kalev Lember <kalev@smartlink.ee> - 2.21.1-1
- Initial RPM release
