Name:           libXcm
Version:        0.5.3
Release:        28%{?dist}
Summary:        X Color Management Library
License:        MIT
URL:            http://www.oyranos.org
Source0:        http://downloads.sourceforge.net/oyranos/libXcm-%{version}.tar.bz2
BuildRequires:  make
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  libXfixes-devel
BuildRequires:  libXmu-devel
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  xorg-x11-util-macros

%description
The libXcm library is a reference implementation of the net-color spec.
It allows to attach color regions to X windows to communicate with color
servers.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libX11-devel%{?_isa}
Requires:       xorg-x11-proto-devel

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
autoreconf -vif
%configure --disable-static --enable-shared
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete -print

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/*.so.*

%files devel
%doc docs/*.txt
%{_libdir}/cmake/Xcm/
%{_includedir}/X11/Xcm/
%{_libdir}/*.so
%{_libdir}/pkgconfig/xcm*.pc
%{_mandir}/man3/*.3*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Aug 16 2021 Nicolas Chauvet <kwizart@gmail.com> - 0.5.3-20
- Fix FTBFS

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov  5 11:14:26 AEST 2020 Peter Hutterer <peter.hutterer@redhat.com> - 0.5.3-17
- Add BuildRequires for make

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 21 2019 Adam Jackson <ajax@redhat.com> - 0.5.3-13
- Remove unnecessary BuildRequires: xorg-x11-xtrans-devel

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 08 2014 Christopher Meng <rpm@cicku.me> - 0.5.3-2
- Correct the arched requires in -devel package since the requested one is noarch.

* Sat Mar 08 2014 Christopher Meng <rpm@cicku.me> - 0.5.3-1
- Update to 0.5.3

* Tue Jan 07 2014 Christopher Meng <rpm@cicku.me> - 0.5.2-1
- Update to 0.5.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> - 0.5.1-3
- autoreconf for aarch64

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 18 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.5.1-1
- Update to 0.5.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.5.0-2
- Bump release

* Sat Mar 10 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.5.0-1
- Update to 0.5.0

* Sun Feb 26 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.4.2-3
- Enable PIC in build. Fixes FTBFS on ARM

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 08 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.4.2-1
- Update to 0.4.2

* Sat Jul 23 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.4.1-1
- Update to 0.4.1

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 07 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.4.0-1
- Update to 0.4.0

* Fri Nov 05 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.3.0-1
- Update to 0.3.0

* Sun Aug 22 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.2.7-1
- Update to 0.27

* Fri Jul 16 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.2.6-2
- Fix X11 directory ownership for header.
- Improve description

* Wed Jul 14 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.2.6-1
- Initial spec file

