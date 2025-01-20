%global commit 669d31c24a1c173581f7abc45e73516a6434b026
%global gittag v5.0.6
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           rudeconfig
Version:        5.0.6
Release:        16%{?dist}
Summary:        Library (C++ API) for reading and writing configuration/.ini files
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://www.rudeserver.com/config
Source0:        https://github.com/mflood/%{name}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Patch0:         %{name}-%{commit}-configure-c99.patch

BuildRequires: make
BuildRequires: gcc-c++

%description
%{name} is a library that allows applications to read, modify
and create configuration/.ini files.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
%{name} is a library that allows applications to read, modify
and create configuration/.ini files. The %{name}-devel package
contains libraries, header files, and documentation needed
to develop C++ applications using %{name}.

%prep
%autosetup -n %{name}-%{commit}

%build
%configure --disable-static
%make_build

%install
%make_install

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS README NEWS ChangeLog
%{_libdir}/librudeconfig.so.3
%{_libdir}/librudeconfig.so.3.2.1

%files devel
%dir %{_includedir}/rude
%{_includedir}/rude/config.h
%{_libdir}/librudeconfig.so
%{_mandir}/man3/*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 5.0.6-15
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Dec 19 2022 Peter Fordham <peter.fordham@gmail.com> - 5.0.6-10
- Port configure to C99.

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 21 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 5.0.6-1
- Update to latest release
- Remove patch

* Sat Oct 20 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 5.0.5-11
- Patch files to update FSF address

* Sat Oct 20 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 5.0.5-10
- Unretire

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar  5 2009 Caolรกn McNamara <caolanm@redhat.com> - 5.0.5-6
- include cstdio for EOF

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 5.0.5-4
- fix compile with gcc43

* Wed Sep  3 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 5.0.5-3
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.0.5-2
- Autorebuild for GCC 4.3

* Thu Feb 01 2007 Matt Flood <matt@rudeserver.com> 5.0.5-1
- Renamed header include guards in config.h
- From INCLUDED_CONFIG_H to INCLUDED_RUDE_CONFIG_H

* Thu Feb 01 2007 Matt Flood <matt@rudeserver.com> 5.0.4-3
- Minor amendments to build-related scripts
- Added missing include directory to specfile

* Thu Feb 01 2007 Matt Flood <matt@rudeserver.com> 5.0.4-2
- Minor amendments to build-related scripts
- Fixed minor typo in changelog (ChangeLog and rudeconfig.spec)
- Added --disable-static to configure directive in rudeconfig.spec

* Fri Jan 19 2007 Matt Flood <matt@rudeserver.com> 5.0.4-1
- Created rudeconfig.3 MAN page

* Mon Jul 31 2006 Matt Flood <matt@rudeserver.com> 5.0.3-1
- Minor changes to facilitate Windows builds
- changed #include's of  <cstring> to <string.h>
- added .c_str() to a string object to correct shorthand if statement ( a ? x : y )

* Thu Apr 10 2006 Matt Flood <matt@rudeserver.com> 5.0.2-1
- First RPM Release

* Fri Sep 2 2005 Matt Flood <matt@rudeserver.com> 5.0.2-0
- Modified source code for DataLine.cpp - removed 'using namespace std' which Visual Studio is too dumb to ignore.
- Fixed ParserJuly2004::chompEOL() - was not returning a value - (TODO: consider making the function void)
