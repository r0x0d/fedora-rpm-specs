%undefine __cmake_in_source_build
%global _vpath_builddir build

Name: yajl
Version: 2.1.0
Release: 25%{?dist}
Summary: Yet Another JSON Library (YAJL)

License: ISC
URL: http://lloyd.github.com/yajl/

#
# NB, upstream does not provide pre-built tar.gz downloads. Instead
# they make you use the 'on the fly' generated tar.gz from GITHub's
# web interface
#
# The Source0 for any version is obtained by a URL
#
#   https://github.com/lloyd/yajl/releases/tag/2.1.0
#
Source0: %{name}-%{version}.tar.gz

# Patches managed at https://github.com/berrange/yajl/tree/fedora-dist-git
Patch: 0001-pkg-config-file-should-be-in-lib-dir-not-shared-data.patch
Patch: 0002-pkg-config-include-dir-should-not-have-the-yajl-suff.patch
Patch: 0003-fix-patch-to-test-files-to-take-account-of-vpath.patch
Patch: 0004-drop-bogus-_s-suffix-from-yajl-dynamic-library.patch
Patch: 0005-Fix-for-CVE-2017-16516.patch
Patch: 0006-Fix-CVE-2022-24795.patch
Patch: 0007-yajl-fix-memory-leak-problem.patch
Patch: 0008-fix-memory-leaks.patch

BuildRequires: gcc
BuildRequires: cmake
BuildRequires: git

%package devel
Summary: Libraries, includes, etc to develop with YAJL
Requires: %{name} = %{version}-%{release}

%description
Yet Another JSON Library. YAJL is a small event-driven
(SAX-style) JSON parser written in ANSI C, and a small
validating JSON generator.

%description devel
Yet Another JSON Library. YAJL is a small event-driven
(SAX-style) JSON parser written in ANSI C, and a small
validating JSON generator.

This sub-package provides the libraries and includes
necessary for developing against the YAJL library

%prep
%autosetup -S git_am

%build
# NB, we are not using upstream's 'configure'/'make'
# wrapper, instead we use cmake directly to better
# align with Fedora standards
%cmake
%cmake_build


%install
%cmake_install


# No static libraries
rm -f $RPM_BUILD_ROOT%{_libdir}/libyajl_s.a


%check
cd test
(cd parsing && ./run_tests.sh)
(cd api && ./run_tests.sh)

%ldconfig_scriptlets

%files
%license COPYING
%doc ChangeLog README TODO
%{_bindir}/json_reformat
%{_bindir}/json_verify
%{_libdir}/libyajl.so.2
%{_libdir}/libyajl.so.2.*

%files devel
%dir %{_includedir}/yajl
%{_includedir}/yajl/yajl_common.h
%{_includedir}/yajl/yajl_gen.h
%{_includedir}/yajl/yajl_parse.h
%{_includedir}/yajl/yajl_tree.h
%{_includedir}/yajl/yajl_version.h
%{_libdir}/libyajl.so
%{_libdir}/pkgconfig/yajl.pc


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 10 2023 Daniel P. Berrangé <berrange@redhat.com> - 2.1.0-21
- Switch to using git for managing patches
- Fix potential buffer overread (CVE-2017-16516)
- Fix integer overflow leading to heap corruption (CVE-2022-24795)
- Fix multiple memory leaks (CVE-2023-33460)

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Feb 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.0-9
- Switch to %%ldconfig_scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Daniel P. Berrange <berrange@redhat.com> - 2.1.0-1
- Update to 2.1.0 release (rhbz #1080935)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug  6 2012 Daniel P. Berrange <berrange@redhat.com> - 2.0.4-1
- Update to 2.0.4 release (rhbz #845777)
- Fix License tag to reflect change in 2.0.0 series from BSD to ISC

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Daniel P. Berrange <berrange@redhat.com> - 2.0.1-1
- Update to 2.0.1 release

* Tue May  3 2011 Daniel P. Berrange <berrange@redhat.com> - 1.0.12-1
- Update to 1.0.12 release

* Fri Dec 17 2010 Daniel P. Berrange <berrange@redhat.com> - 1.0.11-1
- Update to 1.0.11 release

* Mon Jan 11 2010 Daniel P. Berrange <berrange@redhat.com> - 1.0.7-3
- Fix ignoring of cflags (rhbz #547500)

* Tue Dec  8 2009 Daniel P. Berrange <berrange@redhat.com> - 1.0.7-2
- Change use of 'define' to 'global'

* Mon Dec  7 2009 Daniel P. Berrange <berrange@redhat.com> - 1.0.7-1
- Initial Fedora package
