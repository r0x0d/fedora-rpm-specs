%global __cmake_in_source_build 1

Name:      spatialindex
Version:   1.9.3
Release:   13%{?dist}
Summary:   Spatial index library 
License:   MIT
URL:       http://libspatialindex.org
Source0:   https://github.com/libspatialindex/libspatialindex/releases/download/%{version}/%{name}-src-%{version}.tar.bz2

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
Spatialindex provides a general framework for developing spatial indices.
Currently it defines generic interfaces, provides simple main memory and
disk based storage managers and a robust implementation of an R*-tree,
an MVR-tree and a TPR-tree.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%autosetup -n %{name}-src-%{version} -p1


%build
%cmake .
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


# Tests must be run manually and seemingly are not built yet
# See changelog 2011-10-11


%ldconfig_scriptlets


%files 
%license COPYING
%doc AUTHORS ChangeLog
%{_libdir}/lib%{name}*.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}*.so


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 24 2020 Jeff Law <law@redhat.com> - 1.9.3-3
- Use __cmake_in_source_build

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 24 2019 Volker Fröhlich <volker27@gmx.at> - 1.9.3-1
- New upstream release

* Tue Oct 22 2019 Volker Fröhlich <volker27@gmx.at> - 1.9.2-1
- New upstream release
- Use github as source
- Use license macro and remove the now-gone README
- Remove merged patch

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 08 2018 Volker Fröhlich <volker27@gmx.at> - 1.8.5-9
- Remove Group keyword

* Fri Dec 01 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.8.5-8
- Patch to fix out-of-bounds crash

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.8.5-2
- Rebuilt for GCC 5 C++11 ABI change

* Sat Dec 20 2014 Dave Johansen <davejohansen@gmail.com> - 1.8.5-1
- New upstream release

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Sep 18 2013 Volker Fröhlich <volker27@gmx.at> - 1.8.1-1
- New upstream release

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Volker Fröhlich <volker27@gmx.at> - 1.8.0-1
- New upstream release
- New URL
- License is now MIT

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr  9 2012 Volker Fröhlich <volker27@gmx.at> - 1.7.1-2
- Patch build system to install to the expected include dir
  and produce proper soname symlinks and fully versioned C
  API library

* Sun Apr  8 2012 Volker Fröhlich <volker27@gmx.at> - 1.7.1-1
- Update for new release
- Drop 64 bit patch
- Header permissions are correct now
- Move header files to spatialindex sub-directory
- Correct FSF address in all files
- Update URL
- Upstream switched to Cmake
- No more issues with rpath, libtool archives or undefined symbols

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-5
- Rebuilt for c++ ABI breakage

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 04 2011 Volker Fröhlich <volker27@gmx.at> - 1.6.1-3
- Preserve timestamps by using install -p

* Thu Aug 04 2011 Volker Fröhlich <volker27@gmx.at> - 1.6.1-2
- Generalized file list to avoid specifying so-version
- Adapt Require in sub-package to guidelines
- Removed BR chrpath; using approach from
  http://fedoraproject.org/wiki/Packaging:Guidelines#Removing_Rpath
- Correct FSF postal address

* Thu Jun 02 2011 Volker Fröhlich <volker27@gmx.at> - 1.6.1-1
- Initial packaging
