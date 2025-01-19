%{!?tcl_version: %define tcl_version %(echo 'puts $tcl_version' | tclsh)}
%{!?tcl_sitearch: %define tcl_sitearch %{_libdir}/tcl%{tcl_version}}

Name:           itcl
Version:        4.1.1
Release:        13%{?dist}
Summary:        Object oriented extensions to Tcl and Tk

License:        TCL
URL:            http://incrtcl.sourceforge.net/itcl/
Source0:        https://downloads.sourceforge.net/incrtcl/itcl%{version}.tar.gz
Patch1:         itcl-libdir.patch
Patch2:         itcl-soname.patch

Requires:       tcl(abi) = 8.6
BuildRequires:  gcc
BuildRequires:  tcl-devel >= 1:8.6
BuildRequires: make

%description
[incr Tcl] is Tcl extension that provides object-oriented features that are
missing from the Tcl language.

%package devel
Summary:  Development headers and libraries for linking against itcl
Requires:       %{name} = %{version}-%{release}
%description devel
Development headers and libraries for linking against itcl.

%prep
%setup -q -n %{name}%{version}
%patch -P1 -p1 -b .libdir
%patch -P2 -p1 -b .soname

%build
%configure
%make_build

%install
%make_install

# Patch the updated location of the stub library
sed -i -e "s#%{_libdir}/%{name}%{version}#%{tcl_sitearch}/%{name}%{version}#" \
        $RPM_BUILD_ROOT%{_libdir}/itclConfig.sh

%check
make test


%files
%dir %{tcl_sitearch}/%{name}%{version}
%{tcl_sitearch}/%{name}%{version}/*.tcl
%{_libdir}/*.so
%{_mandir}/mann/*.gz
%license license.terms
%doc README releasenotes.txt

%files devel
%{_includedir}/*.h
%{tcl_sitearch}/%{name}%{version}/*.a
%{_libdir}/itclConfig.sh

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 18 2019 Orion Poplawski <orion@nwra.com> - 4.1.1-1
- Update to 4.1.1

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 23 2018 Dmitrij S. Kryzhevich <kryzhev@ispms.ru> - 4.0.3-9
- Add patch that fix ptr count.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 7 2015 Orion Poplawski <orion@cora.nwra.com> - 4.0.3-2
- Fix library install permissions (bug #1219595)

* Tue May 5 2015 Orion Poplawski <orion@cora.nwra.com> - 4.0.3-1
- Update to 4.0.3 (bug #1209976)

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jun 4 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.0-2
- Drop extra namespace on import (bug #1104651)

* Tue May 27 2014 Orion Poplawski <orion@cora.nwra.com> - 4.0.0-1
- Update to 4.0.0 for Tcl 8.6
- Cleanup spec

* Wed May 21 2014 Jaroslav Škarvada <jskarvad@redhat.com> - 3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/f21tcl86

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 7 2009 Wart <wart@kobold.org> - 3.4-6
- Fix segfault during startup (BZ #539453)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Wart <wart@kobold.org> - 3.4-4
- Fix bad logic for locating itcl.tcl from the C bindings

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 9 2008 Wart <wart@kobold.org> - 3.4-2
- Rebuild for gcc 4.3
- Add patch for adding soname

* Thu Jan 10 2008 Wart <wart@kobold.org> - 3.4-1
- Update to latest CVS head for tcl 8.5 compatibility

* Wed Dec 19 2007 Wart <wart@kobold.org> - 3.3-0.11.RC1
- Move libitcl shared library to %%{_libdir} so that applications
  linked against itcl can find it. (BZ #372791)

* Sun Aug 19 2007 Wart <wart@kobold.org> - 3.3-0.10.RC1
- License tag clarification
- Better download URL
- Minor rpmlint cleanup

* Thu Mar 22 2007 Orion Poplawski <orion@cora.nwra.com> - 3.3-0.9.RC1
- Rebuild for tcl8.4 downgrade

* Thu Feb 8 2007 Wart <wart at kobold.org> - 3.3-0.8.RC1
- Rebuild for tcl8.5a5

* Mon Aug 28 2006 Wart <wart at kobold.org> - 3.3-0.7.RC1
- Rebuild for Fedora Extras

* Fri Jun 2 2006 Wart <wart at kobold.org> - 3.3-0.6.RC1
- Added upstream's patch to close a minor memory leak

* Thu Jun 1 2006 Wart <wart at kobold.org> - 3.3-0.5.RC1
- Fix BR: for -devel subpackage

* Thu Feb 16 2006 Wart <wart at kobold.org> - 3.3-0.4.RC1
- Rebuild for FC-5

* Fri Jan 27 2006 Wart <wart at kobold.org> - 3.3-0.3.RC1
- Remove duplicate in file list.

* Wed Jan 11 2006 Wart <wart at kobold.org> - 3.3-0.2.RC1
- Fix quoting bug that is exposed by bash >= 3.1

* Mon Jan 9 2006 Wart <wart at kobold.org> - 3.3-0.1.RC1
- Update to 3.3 upstream sources.  itk now uses a different source
  archive than itcl and has been moved to a separate spec file.

* Wed Dec 28 2005 Wart <wart at kobold.org> - 3.2.1-4
- Create itk as a subpackage.
- Rename patch to include version number.
- New source url.

* Fri Nov 25 2005 Wart <wart at kobold.org> - 3.2.1-3
- Minor fixes to remove rpmlint warnings.
- Move DSOs to itcl library directory instead of polluting /usr/lib.

* Sat Oct 22 2005 Wart <wart at kobold.org> - 3.2.1-2
- Look for itk.tcl in the lib64 directory for x86_64 platforms.

* Fri Oct 21 2005 Wart <wart at kobold.org> - 3.2.1-1
- Intial spec file for Fedora Extras
