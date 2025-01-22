Name:           libsigc++
Version:        1.2.7
Release:        43%{?dist}
Summary:        Typesafe signal framework for C++
License:        LGPL-2.1-or-later
URL:            http://libsigc.sourceforge.net/
Source0:        http://ftp.gnome.org/pub/GNOME/sources/libsigc++/1.2/%{name}-%{version}.tar.bz2
BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  m4
BuildRequires:  doxygen
BuildRequires:  libxslt docbook-style-xsl
BuildRequires: make

Patch1:         libsigc++-1.2.5-stylesheet.patch
Patch2:         libsigc++-1.2.5-configure.patch
%description
This library implements a full callback system for use in widget libraries,
abstract interfaces, and general programming. Originally part of the Gtk--
widget set, %name is now a separate library to provide for more general
use. It is the most complete library of its kind with the ablity to connect
an abstract callback to a class method, function, or function object. It
contains adaptor classes for connection of dissimilar callbacks and has an
ease of use unmatched by other C++ callback libraries.

Package gtkmm (previously gtk--), which is a C++ binding to the GTK+
library, starting with version 1.1.2, uses %name.

%package        devel
Summary:        Development tools for the typesafe signal framework for C++
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
The %name-devel package contains the static libraries and header files
needed for development with %name.

%package        doc
Summary:        Documentation for %{name}, includes full API docs
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains the full API documentation for %{name}.


%prep
%setup -q
%patch -P1 -p1 -b .stylesheet
%patch -P2 -p1 -b .configure



%build
%configure %{!?_with_static: --disable-static}
%make_build
cd doc/manual
make
cd -



%install
rm -rf ${RPM_BUILD_ROOT}
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'
# Clean up a temporary doc dir prior to including files from it.
rm -rf _doc ; cp -a doc _doc
find _doc -type f -name "Makefile*" -exec rm -f {} ';'
find _doc -type f -empty -exec rm -f {} ';'
find _doc -type d -empty -print0 | xargs -0r rmdir





%ldconfig_scriptlets



%files
%doc AUTHORS COPYING.LIB README IDEAS NEWS ChangeLog TODO
%{_libdir}/lib*.so.*


%files devel
%{_libdir}/sigc++-1.2/
%{?_with_static: %{_libdir}/*.a}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/sigc++-1.2/

%files doc
%doc _doc/*


%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Mar 05 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.2.7-38
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 06 2023 Peter Fordham <peter.fordham@gmail.com> - 1.2.7-36
- Port configure script to C99.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-31
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Tom Stellard <tstellar@redhat.com> - 1.2.7-29
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.2.7-24
- Escape macros in %%changelog

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.2.7-17
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 03 2011 Jon Ciesla <limb@jcomserv.net> - 1.2.7-10
- Added doc subpackage to resolve arch conflict, BZ 710611.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.7-6
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Denis Leroy <denis@poolshark.org> - 1.2.7-5
- Updated License tag

* Tue Oct 10 2006 Denis Leroy <denis@poolshark.org> - 1.2.7-4
- Added dist tag

* Mon Aug 28 2006 Denis Leroy <denis@poolshark.org> - 1.2.7-3
- FE6 Rebuild

* Tue Feb 28 2006 Denis Leroy <denis@poolshark.org> 1.2.7-2
- Fixed sources file

* Tue Feb 28 2006 Denis Leroy <denis@poolshark.org> 1.2.7-1
- Upgrade to version 1.2.7.
- Removed obsolete patches.
- Disabled static libs by default. Enabled with '--with static'.

* Tue Apr 12 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 1.2.5-8
- Add BR docbook-style-xsl and patch doc/manual to use it instead of
  an external http stylesheet.
- Replace libtool/autofoo calls with ~145KiB patch.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Tue Jul 13 2004 Michael Schwendt <mschwendt[AT]users.sf.net> 0:1.2.5-0.fdr.5
- Don't run autogen.sh, but --force rerun autotools/libtoolize.

* Tue Jul 13 2004 Michael Schwendt <mschwendt[AT]users.sf.net> 0:1.2.5-0.fdr.4
- Rerun autogen.sh for x86_64,
  patch pkgconfig template. (#1420) (Nicholas Miell)

* Sun Nov 16 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:1.2.5-0.fdr.3
- BuildReq libxslt.

* Thu Sep 18 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:1.2.5-0.fdr.2
- Spec patch from Michael Schwendt.
- BuildReq doxygen.
- BuildReq m4.
- devel Req pkgconfig.
- Changed path for Source0.
- Cleanup of doc directory.

* Tue Sep 16 2003 Phillip Compton <pcompton[AT]proteinmedia.com> 0:1.2.5-0.fdr.1
- Initial Fedora Release..1

* Sat Nov 02 2002 Morten Brix Pedersen <morten@wtf.dk>
- Fixed RPM build with final libsigc++-1.2 release.
- Distribute pc (pkg-config) file with tarball.

* Sun Dec 31 2000 Karl E. Nelson <kenelson@sourceforge.net>
- Initial cut for 1.1

* Sat Apr 15 2000 Dmitry V. Levin <ldv@fandra.org>
- updated Url and Source fileds
- 1.0.0 stable release

* Sat Jan 22 2000 Dmitry V. Levin <ldv@fandra.org>
- filtering out -fno-rtti and -fno-exceptions options from $RPM_OPT_FLAGS
- minor install section cleanup

* Wed Jan 19 2000 Allan Rae <rae@lyx.org>
- autogen just creates configure, not runs it, so cleaned that up too.

* Wed Jan 19 2000 Dmitry V. Levin <ldv@fandra.org>
- minor attr fix
- removed unnecessary curly braces
- fixed Herbert's adjustement

* Sat Jan 15 2000 Dmitry V. Levin <ldv@fandra.org>
- minor package dependence fix

* Sat Dec 25 1999 Herbert Valerio Riedel <hvr@gnu.org>
- fixed typo of mine
- added traditional CUSTOM_RELEASE stuff
- added SMP support

* Thu Dec 23 1999 Herbert Valerio Riedel <hvr@gnu.org>
- adjusted spec file to get tests.Makefile and examples.Makefile from scripts/

* Fri Oct 22 1999 Dmitry V. Levin <ldv@fandra.org>
- split into three packages: %%name, %%name-devel and %%name-examples

* Thu Aug 12 1999 Karl Nelson <kenelson@ece.ucdavis.edu>
- updated source field and merged conflicts between revisions.

* Tue Aug 10 1999 Dmitry V. Levin <ldv@fandra.org>
- updated Prefix and BuildRoot fields

* Thu Aug  5 1999 Herbert Valerio Riedel <hvr@hvrlab.dhs.org>
- made sure configure works on all alphas

* Wed Jul  7 1999 Karl Nelson <kenelson@ece.ucdavis.edu>
- Added autoconf macro for sigc.

* Fri Jun 11 1999 Karl Nelson <kenelson@ece.ucdavis.edu>
- Made into a .in to keep version field up to date
- Still need to do release by hand

* Mon Jun  7 1999 Dmitry V. Levin <ldv@fandra.org>
- added Vendor and Packager fields

* Sat Jun  5 1999 Dmitry V. Levin <ldv@fandra.org>
- updated to 0.8.0

* Tue Jun  1 1999 Dmitry V. Levin <ldv@fandra.org>
- initial revision
