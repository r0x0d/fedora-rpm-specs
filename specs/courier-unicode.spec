Summary: A library implementing algorithms related to the Unicode Standard
Name: courier-unicode
Version: 2.2.6
Release: 6%{?dist}
License: GPL-3.0-only
URL: http://www.courier-mta.org/unicode/
Source0: https://downloads.sourceforge.net/project/courier/%{name}/%{version}/%{name}-%{version}.tar.bz2
Source1: https://downloads.sourceforge.net/project/courier/%{name}/%{version}/%{name}-%{version}.tar.bz2.sig
Source2: pubkey.maildrop

BuildRequires: gcc-c++
BuildRequires: gcc
BuildRequires: gnupg
BuildRequires: perl-interpreter
BuildRequires: make

%description
This library implements several algorithms related to the Unicode Standard:

* Look up uppercase, lowercase, and titlecase equivalents of a unicode character.
* Implementation of grapheme and work breaking rules.
* Implementation of line breaking rules.

Several ancillary functions, like looking up the unicode character that
corresponds to some HTML 4.0 entity (such as “&amp;”, for example), and
determining the normal width or a double-width status of a unicode character.
Also, an adaptation of the iconv(3) API for this unicode library.

This library also implements C++ bindings for these algorithms.
The current release of the Courier Unicode library is based on the Unicode 8.0.0 standard.

%package devel
Summary: Development tools for programs which will use the libcourier-unicode library
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The courier-unicode-devel package includes the header files and documentation
necessary for developing programs which will use the libcourier-unicode library.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%install
%makeinstall

# We don't ship .la files.
rm %{buildroot}%{_libdir}/*.la

%check
%{__make} check

%files
%license COPYING
%doc README ChangeLog AUTHORS
%{_libdir}/libcourier-unicode.so.7
%{_libdir}/libcourier-unicode.so.7.0.0

%files devel
%{_includedir}/courier-unicode.h
%{_includedir}/courier-unicode-categories-tab.h
%{_includedir}/courier-unicode-script-tab.h
%{_libdir}/libcourier-unicode.so
%{_datadir}/aclocal/courier-unicode.m4
%{_datadir}/aclocal/courier-unicode-version.m4
%{_mandir}/man3/*
%{_mandir}/man7/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jan 30 2023 Brian C. Lane <bcl@redhat.com> - 2.2.6-1
- New upstream v2.2.6
- SPDX migration

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jun 03 2022 Brian C. Lane <bcl@redhat.com> - 2.2.4-1
- New upstream v2.2.4

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 01 2020 Brian C. Lane <bcl@redhat.com> - 2.1-4
- Add make to BuildRequires

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 22 2019 Brian C. Lane <bcl@redhat.com> - 2.1-1
- New upstream v2.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 19 2018 Brian C. Lane <bcl@redhat.com> - 2.0-5
- Remove ldconfig, it no longer needs to be called on un/installs

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Brian C. Lane <bcl@redhat.com> - 2.0-3
- Add gcc and gcc-c++ BuildRequires for future minimal buildroot support

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 26 2017 Brian C. Lane <bcl@redhat.com> - 2.0-1
- Upstream v2.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 16 2017 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.4-4
- Add BR: perl (Fix F26FTBS).

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 23 2016 Brian C. Lane <bcl@redhat.com> - 1.4-1
- Update description -- based on the Unicode 8.0.0 standard.

* Thu Feb 04 2016 Brian C. Lane <bcl@redhat.com> 1.4-1
- Upstream v1.4
  Note that the library name changed to libcourier-unicode

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1-4
- Rebuilt for GCC 5 C++11 ABI change

* Wed Feb 18 2015 Brian C. Lane <bcl@redhat.com> 1.1-3
- Update with suggestions from the review
- Run make check

* Tue Feb 17 2015 Brian C. Lane <bcl@redhat.com> 1.1-2
- Changed package name to courier-unicode

* Wed Jan 28 2015 Brian C. Lane <bcl@redhat.com> 1.1-1
- Initial build
