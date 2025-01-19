Name:           mm-common
Version:        1.0.6
Release:        6%{?dist}
Summary:        Common build files of the C++ bindings

BuildArch:      noarch
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://gtkmm.org
Source0:        https://download.gnome.org/sources/%{name}/1.0/%{name}-%{version}.tar.xz

BuildRequires:  meson

Requires:       doxygen
Requires:       graphviz
Requires:       libxslt
Requires:       pkgconfig

%description
The mm-common module provides the build infrastructure and utilities
shared among the GNOME C++ binding libraries.  It is a required dependency
to build glibmm and gtkmm from git.

%package docs
Summary:        Documentation for %{name}, includes example mm module skeleton
Requires:       %{name} = %{version}-%{release}

%description docs
Package contains short documentation for %{name} and example skeleton module,
which could be used as a base for new mm module.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc NEWS OVERVIEW.md README.md
%{_mandir}/man1/*
%{_bindir}/*
%{_datadir}/aclocal/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/pkgconfig/*.pc

%files docs
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.6-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Kalev Lember <klember@redhat.com> - 1.0.6-1
- Update to 1.0.6

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 06 2022 David King <amigadave@amigadave.com> - 1.0.5-1
- Update to 1.0.5

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Mar 25 2022 David King <amigadave@amigadave.com> - 1.0.4-1
- Update to 1.0.4

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed May 26 2021 Kalev Lember <klember@redhat.com> - 1.0.3-1
- Update to 1.0.3

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 25 19:29:53 CEST 2020 Kalev Lember <klember@redhat.com> - 1.0.2-1
- Update to 1.0.2

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun 05 2020 Kalev Lember <klember@redhat.com> - 1.0.1-1
- Update to 1.0.1
- Switch to the meson build system

* Wed Apr 15 2020 Kalev Lember <klember@redhat.com> - 1.0.0-1
- Update to 1.0.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Apr 08 2018 Kalev Lember <klember@redhat.com> - 0.9.12-1
- Update to 0.9.12

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug 28 2017 Kalev Lember <klember@redhat.com> - 0.9.11-1
- Update to 0.9.11

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Mar 03 2016 Kalev Lember <klember@redhat.com> - 0.9.10-1
- Update to 0.9.10

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 28 2015 Kalev Lember <klember@redhat.com> - 0.9.9-1
- Update to 0.9.9

* Tue Sep 22 2015 Kalev Lember <klember@redhat.com> - 0.9.8-1
- Update to 0.9.8
- Use make_install macro
- Mark COPYING as %%license
- Drop large ChangeLog file from docs
- Don't require automake for /usr/share/aclocal dir

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 15 2014 Kalev Lember <kalevlember@gmail.com> - 0.9.7-1
- Update to 0.9.7

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jul 18 2013 Petr Pisar <ppisar@redhat.com> - 0.9.6-3
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 16 2012 Kalev Lember <kalevlember@gmail.com> - 0.9.6-1
- Update to 0.9.6

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 11 2011 Krzesimir Nowak <qdlacz@gmail.com>
- Fix description.

* Wed Apr 6 2011 Krzesimir Nowak <qdlacz@gmail.com> - 0.9.5-1
- New upstream release.
- Fixes distributing doctools.

* Mon Mar 21 2011 Krzesimir Nowak <qdlacz@gmail.com> - 0.9.4-1
- New upstream release.
- Fixes placement of mm-common-util.pc, so no hacks are needed in spec.

* Thu Mar 17 2011 Krzesimir Nowak <qdlacz@gmail.com> - 0.9.3-2
- Move a pkgconfig file from libdir to datadir, so it will remain a Noarch.

* Thu Mar 17 2011 Krzesimir Nowak <qdlacz@gmail.com> - 0.9.3-1
- New upstream release.
- Becomes a required dependency to build glibmm-2.27.97.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 10 2010 Krzesimir Nowak <qdlacz@gmail.com> - 0.9.2-1
- New upstream release.

* Tue Jan 5 2010 Krzesimir Nowak <qdlacz@gmail.com> - 0.9.1-1
- New upstream release.
- Removed GFDL from license - doxygen docs have the same license as source code.

* Mon Sep 21 2009 Krzesimir Nowak <qdlacz@gmail.com> - 0.8-1
- New upstream release.

* Sun Sep 13 2009 Krzesimir Nowak <qdlacz@gmail.com> - 0.7.3-2
- Added automake to `Requires:'.
- Fixed some directory ownerships.
- Preserve timestamps during install.

* Thu Sep 10 2009 Krzesimir Nowak <qdlacz@gmail.com> - 0.7.3-1
- Initial RPM release.
