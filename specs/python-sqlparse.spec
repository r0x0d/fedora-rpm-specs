# tests need internet connection, see similar case here:
# https://bugzilla.redhat.com/show_bug.cgi?id=864464#c15
# To build with tests, run rpmbuild --with tests -ba <spec>
%bcond_with     tests

%global         shortname sqlparse

Name:           python-%{shortname}
Version:        0.4.2
Release:        13%{?dist}
Summary:        Non-validating SQL parser for Python

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/andialbrecht/%{shortname}
Source0:        https://github.com/andialbrecht/%{shortname}/archive/%{version}/%{shortname}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-tools
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-py

%if %{with tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-pytest-cov
%endif # with_tests

%global _description\
sqlparse is a tool for parsing SQL strings.  It can generate pretty-printed\
renderings of SQL in various formats.\
\
It is a python module, together with a command-line tool.

%description %_description

%package -n     python%{python3_pkgversion}-%{shortname}
Summary:        Non-validating SQL parser for Python

%description -n python%{python3_pkgversion}-%{shortname}
sqlparse is a tool for parsing SQL strings.  It can generate pretty-printed
renderings of SQL in various formats.

It is a python module, together with a command-line tool.


%prep
%setup -q -n %{shortname}-%{version}


%build
%{__python3} setup.py build


%install
%{__python3} setup.py install --skip-build --root %{buildroot}


%if %{with tests}
%check
tox -e py%{python3_version_nodots}
%endif # with_tests


%files -n python%{python3_pkgversion}-%{shortname}
%license LICENSE
%doc AUTHORS CHANGELOG README.rst
%{python3_sitelib}/*

%{_bindir}/sqlformat

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.4.2-12
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.4.2-10
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.4.2-6
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.4.2-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 17 2021 Honza Horak <hhorak@redhat.com> - 0.4.2-1
- Update to 0.4.2
  Also fixes CVE-2021-32839

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 0.4.1-2
- Rebuilt for Python 3.10

* Fri Jan 29 2021 Joel Capitao <jcapitao@redhat.com> - 0.4.1-1
- Update to 0.4.1 (#1886093)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-2
- Rebuilt for Python 3.9

* Sun Mar 01 2020 Terje Rosten <terje.rosten@ntnu.no> - 0.3.1-1
- Update to 0.3.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-9
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-8
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 18 2019 Marc Dequènes (Duck) <duck@redhat.com> - 0.2.4-6
- Adaptations to build Python 3 on EPEL

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-4
- Subpackage python2-sqlparse has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.4-2
- Rebuilt for Python 3.7

* Sun Apr 15 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 0.2.4-1
- new version

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.2.2-6
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.2-4
- Python 2 binary package renamed to python2-sqlparse
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.2.2-1
- Uodate to 0.2.2

* Mon Dec 12 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.2.1-2
- Rebuild for Python 3.6

* Sat Aug 27 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.2.1-1
- Uodate to 0.2.1
- Simplify a little bit the SPEC

* Sun Jul 31 2016 Honza Horak <hhorak@redhat.com> - 0.2-1
- Update to 0.2 (rhbx#1360756)

* Fri Jul 08 2016 Honza Horak <hhorak@redhat.com> - 0.1.19-1
- Update to 0.1.19 (#1315292)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.18-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Nov  5 2015 Toshio Kuratomi <toshio@fedoraproject.org> - 0.1.18-3
- Do not include the sqlformat script in the python-sqlparse package, only in
  the python3-sqlparse package.  This will fix the script not working if the
  python2-sqlparse package is installed but not python3-sqlparse and it will
  keep the python2-sqlparse package from depending on python3.

* Tue Nov 03 2015 Robert Kuska <rkuska@redhat.com> - 0.1.18-2
- Rebuilt for Python3.5 rebuild

* Sun Oct 25 2015 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 0.1.18-1
- Update to 0.1.18 (#1275044)

* Fri Sep 18 2015 Honza Horak <None> - 0.1.16-1
- New upstream release 0.1.16

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0.1.11-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon May 12 2014 Honza Horak <hhorak@redhat.com> - 0.1.11-2
- Add python3 package

* Mon May 12 2014 Honza Horak <hhorak@redhat.com> - 0.1.11-1
- Rebase to 0.1.11
- Change the upstream URL

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun  3 2011 David Malcolm <dmalcolm@redhat.com> - 0.1.2-1
- 0.1.2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 10 2009 David Malcolm <dmalcolm@redhat.com> - 0.1.1-4
- bump release to enable build

* Fri Jun  5 2009 David Malcolm <dmalcolm@redhat.com> - 0.1.1-3
- run the tests in the "check" section

* Fri Jun  5 2009 David Malcolm <dmalcolm@redhat.com> - 0.1.1-2
- run the selftests during the "build" phase

* Thu May 14 2009 David Malcolm <dmalcolm@redhat.com> - 0.1.1-1
- initial packaging

