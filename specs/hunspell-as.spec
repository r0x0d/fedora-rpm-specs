%if 0%{?fedora} >= 36 || 0%{?rhel} > 9
%global dict_dirname hunspell
%else
%global dict_dirname myspell
%endif

Name: hunspell-as
Summary: Assamese hunspell dictionaries
Version: 1.0.3
Release: 33%{?dist}
Source: https://downloads.sourceforge.net/project/aoo-extensions/2318/4/as_in.oxt
URL: https://extensions.openoffice.org/en/project/assamese-dictionaryspell-checker
License: GPL-2.0-or-later OR LGPL-2.1-or-later OR MPL-1.1
BuildArch: noarch

Requires: hunspell-filesystem
Supplements: (hunspell and langpacks-as)

%description
Assamese hunspell dictionaries.

%prep
%autosetup -c -n hunspell-as

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}
cp -p as_IN.* $RPM_BUILD_ROOT/%{_datadir}/%{dict_dirname}/

%files
%doc README_as_IN.txt
%license COPYING COPYING.MPL COPYING.GPL COPYING.LGPL
%{_datadir}/%{dict_dirname}/*

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 23 2022 Parag Nemade <pnemade AT redhat DOT com> - 1.0.3-28
- Update license tag to SPDX format

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Mar 22 2022 Parag Nemade <pnemade AT redhat DOT com> - 1.0.3-26
- Add conditional for new hunspell dir path and update to Requires:
  hunspell-filesystem

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Parag Nemade <pnemade AT fedoraproject DOT org> - 1.0.3-17
- Update Source and URL tags
- Added %%license and %%autosetup

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 19 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.0.3-13
- Add Supplements: tag for langpacks naming guidelines
- Clean the specfile to follow current packaging guidelines

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 28 2012 Parag <pnemade@redhat.com> - 1.0.3-6
- spec cleanup

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 29 2009 Parag <pnemade@redhat.com> - 1.0.3-2
- Fix source issue in cvs

* Tue Apr 28 2009 Caolan McNamara <caolanm@redhat.com> - 1.0.3-1
- initial version