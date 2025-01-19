%global api_ver 2.0

Name:             gtksourceviewmm
Version:          2.10.3
Release:          30%{?dist}
Summary:          A C++ wrapper for the gtksourceview widget library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:          LicenseRef-Callaway-LGPLv2+
URL:              http://projects.gnome.org/gtksourceviewmm/
Source0:          http://ftp.gnome.org/pub/GNOME/sources/gtksourceviewmm/2.10/%{name}-%{version}.tar.xz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:    gtkmm24-devel >= 2.12
BuildRequires:    gtksourceview2-devel >= 2.10.0
BuildRequires: make


%description
gtksourceviewmm is a C++ wrapper for the gtksourceview widget
library. It offers all the power of gtksourceview with an interface
familiar to c++ developers, including users of the gtkmm library


%package          devel
Summary:          Development files for %{name}
Requires:         %{name} = %{version}-%{release}
Requires:         gtkmm24-devel
Requires:         gtksourceview2-devel
Requires:         pkgconfig


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package          doc
Summary:          Developer's documentation for the gtksourceviewmm library
BuildArch:        noarch
Requires:         gtkmm24-docs

%description      doc
This package contains developer's documentation for the Gtksourceviewmm
library. Gtksourceviewmm is the C++ API for the Gtksourceview library.

The documentation can be viewed either through the devhelp
documentation browser or through a web browser.

%prep
%setup -q


%build
%configure --disable-static
# removing rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv && mv -f ChangeLog.conv ChangeLog


%install
rm -rf $RPM_BUILD_ROOT
make INSTALL="install -c -p" DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'



%ldconfig_scriptlets


%files
%doc README AUTHORS COPYING ChangeLog NEWS
%{_libdir}/*.so.*


%files devel
%{_includedir}/%{name}-2.0
%{_libdir}/*.so
%{_libdir}/%{name}-2.0
%{_libdir}/pkgconfig/*.pc


%files doc
%doc COPYING
%doc %{_datadir}/devhelp/
%doc %{_docdir}/%{name}-%{api_ver}


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 2.10.3-29
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.10.3-8
- Rebuilt for GCC 5 C++11 ABI change

* Fri May 01 2015 Kalev Lember <kalevlember@gmail.com> - 2.10.3-7
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 17 2012 Kalev Lember <kalevlember@gmail.com> - 2.10.3-1
- Update to 2.10.3

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.10.2-3
- Rebuild for new libpng

* Sat Jun 25 2011 Krzesimir Nowak <qdlacz@gmail.com> - 2.10.2-2
- Co-own devhelp directory.
- Dropped unneeded doxygen and graphviz BuildRequires.

* Fri Jun 24 2011 Krzesimir Nowak <qdlacz@gmail.com> - 2.10.2-1
- New upstream release.
- Fixes several reference counting problems, mostly in completion stuff.
- Fixes building with newer glibmm.

* Tue Feb 22 2011 Haïkel Guémar <hguemar@fedoraproject.org> - 2.10.1-3
- split doc into subpackage

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 08 2010  <hguemar@fedoraproject.org> - 2.10.1-1
- Update to upstream 2.10.1
- Add missing header gtksourceviewmmconfig.h (RHBZ #650727)

* Sun Apr 11 2010 Haïkel Guémar <hguemar@fedoraproject.org> - 2.10.0-1
- Update to upstream 2.10.0
- Improved documentation
- Fixes a bug with regexxer

* Wed Jan 20 2010 Denis Leroy <denis@poolshark.org> - 2.9.1-1
- Update to upstream 2.9.1, to follow gtksourceview2
- Packaged devhelp book, fixed doc path

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 15 2009 Denis Leroy <denis@poolshark.org> - 2.2.0-2
- Fixed BRs

* Tue Jan 13 2009 Denis Leroy <denis@poolshark.org> - 2.2.0-1
- Initial draft, based on 1.0 version

