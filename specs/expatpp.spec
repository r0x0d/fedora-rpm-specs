Name:		expatpp
Version:	0
Release:	31.20121019gitd8c1bf8%{?dist}
Summary:	C++ layer for expat
# Automatically converted from old format: MPLv1.1 - review is highly recommended.
License:	LicenseRef-Callaway-MPLv1.1
URL:		http://sourceforge.net/projects/expatpp/
# svn export -r 6 https://expatpp.svn.sourceforge.net/svnroot/expatpp/trunk/src_pp/ expatpp
# tar cjf  expatpp.tar.bz2 expatpp
Source0:	expatpp.tar.bz2
Patch1:		0001-Added-CMake-config-file.patch
Patch2:		0002-Fix-case-of-required-arg.patch
Patch3:		0003-Include-string-header.patch
Patch4:		0004-Converted-to-lib-standalone-program-layout.patch
Patch5:		0005-Added-test-code.patch
Patch6:		0006-Build-testexpatpp1.patch
Patch7:		0007-Fix-subdir-command.patch
Patch8:		0008-Added-cPack.patch
Patch9:		0009-Install-library.patch
Patch10:	0010-Use-lib-or-lib64-automatically.patch
Patch11:	0011-added-soname-info.patch
Patch12:	0012-Fixed-missing-api-version.patch
Patch13:	0013-Install-header-file.patch
Patch14:	0014-Removed-windows-static-lib-header.patch
Patch15:	0015-Reworked-documentation.patch
Patch16:	0016-Quick-fix-for-FTBFS.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	cmake
BuildRequires:	expat-devel


%description
Expatpp is a simple C++ layer to make using the open source expat XML parsing
library vastly easier for complex schemas. It has been used widely in industry
including the Valve Steam project.


%package	devel
Summary:	Headers and development libraries for expatpp
Requires:	%{name}%{?_isa} = %{version}-%{release}


%description devel
You should install this package if you would like to
develop code based on expatpp.


%prep
%autosetup -p1 -n %{name}


%build
%{cmake} -DCMAKE_VERBOSE_MAKEFILE=ON \
       -DBUILD_SHARED_LIBS:BOOL=ON \
       -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" .
%{cmake_build}


%install
%{cmake_install}


%check
%{ctest}


%files
%doc CHANGELOG EXTEND TODO
%{_libdir}/*.so.*


%files devel
%{_includedir}/%{name}.h
%{_libdir}/*.so


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0-31.20121019gitd8c1bf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 0-30.20121019gitd8c1bf8
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-29.20121019gitd8c1bf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-28.20121019gitd8c1bf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0-27.20121019gitd8c1bf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-26.20121019gitd8c1bf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0-25.20121019gitd8c1bf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-24.20121019gitd8c1bf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-23.20121019gitd8c1bf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-22.20121019gitd8c1bf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-21.20121019gitd8c1bf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 27 2020 Peter Lemenkov <lemenkov@gmail.com> - 0-20.20121019gitd8c1bf8
- Fix FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-19.20121019gitd8c1bf8
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-18.20121019gitd8c1bf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-17.20121019gitd8c1bf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-16.20121019gitd8c1bf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-15.20121019gitd8c1bf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-14.20121019gitd8c1bf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-13.20121019gitd8c1bf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jul 31 2017 Florian Weimer <fweimer@redhat.com> - 0-12.20121019gitd8c1bf8
- Rebuild with binutils fix for ppc64le (#1475636)

* Wed Jul 26 2017 Peter Lemenkov <lemenkov@gmail.com> - 0-11.20121019gitd8c1bf8
- Fix FTBFS

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-10.20121019gitd8c1bf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-9.20121019gitd8c1bf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-8.20121019gitd8c1bf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-7.20121019gitd8c1bf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0-6.20121019gitd8c1bf8
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-5.20121019gitd8c1bf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-4.20121019gitd8c1bf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-3.20121019gitd8c1bf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-2.20121019gitd8c1bf8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Oct 28 2012 Mario Ceresa mrceresa fedoraproject org expatpp 0-1.20121019gitd8c1bf8%{?dist}
- Included revision in svn export directive
- Fixed tab/spaces issue
- Fixed revision tag
- Shorted Source tag



* Fri Oct 19 2012 Mario Ceresa mrceresa fedoraproject org expatpp 0.6-20121019gitd8c1bf8%{?dist}
- Added patches and fixed release tag
- Fixed license and doc files

* Thu Oct 18 2012 Mario Ceresa mrceresa fedoraproject org expatpp 0.6-1%{?dist}
- Initial SPEC
