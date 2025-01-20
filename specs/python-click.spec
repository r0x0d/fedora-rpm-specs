%bcond tests 1

Name:           python-click
Version:        8.1.7
Release:        7%{?dist}
Summary:        Simple wrapper around optparse for powerful command line utilities

License:        BSD-3-Clause
URL:            https://github.com/pallets/click
Source0:        %{url}/archive/%{version}/click-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel

%global _description \
click is a Python package for creating beautiful command line\
interfaces in a composable way with as little amount of code as necessary.\
It's the "Command Line Interface Creation Kit".  It's highly configurable but\
comes with good defaults out of the box.

%description %{_description}


%package -n     python%{python3_pkgversion}-click
Summary:        %{summary}

%description -n python%{python3_pkgversion}-click %{_description}


%prep
%autosetup -n click-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:requirements/tests.in}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files click


%check
%pyproject_check_import
%if %{with tests}
%pytest
%endif


%files -n python%{python3_pkgversion}-click -f %pyproject_files
%license LICENSE.rst
%doc README.rst CHANGES.rst


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 8.1.7-5
- Rebuilt for Python 3.13

* Wed Jan 31 2023 Maxwell G <maxwell@gtmx.me> - 8.1.7-4
- Add test bcond to make click easier to bootstrap
- Use pytest directly instead of pulling in tox

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 23 2023 Charalampos Stratakis <cstratak@redhat.com> - 8.1.7-1
- Update to 8.1.7
Resolves: rhbz#2220975

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 8.1.3-4
- Rebuilt for Python 3.12

* Wed Apr 12 2023 Miro Hrončok <mhroncok@redhat.com> - 8.1.3-3
- Fix test failures with pytest 7.3.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Aug 06 2022 Charalampos Stratakis <cstratak@redhat.com> - 8.1.3-1
- Update to 8.1.3
Resolves: rhbz#2080026

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 8.1.2-2
- Rebuilt for Python 3.11

* Tue Apr 05 2022 Charalampos Stratakis <cstratak@redhat.com> - 8.1.2-1
- Update to 8.1.2
Resolves: rhbz#2069360

* Wed Mar 02 2022 Charalampos Stratakis <cstratak@redhat.com> - 8.0.4-2
- Unpin pytest version

* Thu Feb 24 2022 Charalampos Stratakis <cstratak@redhat.com> - 8.0.4-1
- Update to 8.0.4
Resolves: rhbz#2056119

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 05 2021 Karolina Surma <ksurma@redhat.com> - 8.0.3-1
- Update to 8.0.3
Resolves: rhbz#2012353

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jul 08 2021 Lumír Balhar <lbalhar@redhat.com> - 8.0.1-2
- Use test dependencies without version locks

* Tue Jun 22 2021 Lumír Balhar <lbalhar@redhat.com> - 8.0.1-1
- Update to 8.0.1
Resolves: rhbz#1901659

* Wed Jun 02 2021 Python Maint <python-maint@redhat.com> - 7.1.2-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Sep 11 2020 Charalampos Stratakis <cstratak@redhat.com> - 7.1.2-4
- Modernize the SPEC and convert it to pyproject macros

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 7.1.2-2
- Rebuilt for Python 3.9

* Tue Apr 28 2020 Fabian Affolter <mail@fabian-affolter.ch> - 7.1.2-1
- Update to latest upstream release 7.1.2 (rhbz#1828589)

* Sat Apr 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 7.1.1-1
- Update to latest upstream release 7.1.1 (rhbz#1811727)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 18 2019 Miro Hrončok <mhroncok@redhat.com> - 7.0-6
- Subpackage python2-click has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 7.0-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov 18 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 7.0-2
- Drop explicit locale setting
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Tue Oct 02 2018 Charalampos Stratakis <cstratak@redhat.com> - 7.0-1
- Update to 7.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Miro Hrončok <mhroncok@redhat.com> - 6.7-8
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 12 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.7-6
- Fixup EPEL packaging

* Thu Oct 12 2017 Carl George <carl@george.computer> - 6.7-6
- Add EPEL compatibility

* Thu Oct 12 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 6.7-5
- Fix FTBFS

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 09 2017 Miro Hrončok <mhroncok@redhat.com> - 6.7-2
- Fixed a copy-paste bug in %%python_provide (rhbz#1411169)

* Sat Jan 07 2017 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 6.7-1
- Update to 6.7
- Adopt to packaging guidelines

* Tue Dec 13 2016 Charalampos Stratakis <cstratak@redhat.com> - 6.6-4
- Enable tests

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 6.6-3
- Rebuild for Python 3.6
- Disable python3 tests for now

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Apr 18 2016 Charalampos Stratakis <cstratak@redhat.com> - 6.6-1
- Update to 6.6
- Removed non-applied patch file.

* Tue Mar 08 2016 Robert Kuska <rkuska@redhat.com> - 6.3-1
- Update to 6.3

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Robert Kuska <rkuska@redhat.com> - 6.2-1
- Update to 6.2

* Wed Oct 14 2015 Robert Kuska <rkuska@redhat.com> - 5.1-2
- Rebuilt for Python3.5 rebuild

* Mon Aug 24 2015 Robert Kuska <rkuska@redhat.com> - 5.1-1
- Update to 5.1

* Mon Aug 03 2015 Robert Kuska <rkuska@redhat.com> - 4.1-1
- Update to 4.1

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun May 31 2015 Robert Kuska <rkuska@redhat.com> - 4.0-2
- Rebuilt

* Wed Apr 01 2015 Robert Kuska <rkuska@redhat.com> - 4.0-1
- Update to 4.0

* Fri Oct 03 2014 Robert Kuska <rkuska@redhat.com> - 3.3-1
- Update to 3.3

* Sun Aug 24 2014 Robert Kuska <rkuska@redhat.com> - 3.2-2
- Add patch for exception check of TypeError

* Sun Aug 24 2014 Robert Kuska <rkuska@redhat.com> - 3.2-1
- Update to 3.2

* Mon Aug 18 2014 Robert Kuska <rkuska@redhat.com> - 3.1-1
- Update to 3.1

* Wed Jul 16 2014 Robert Kuska <rkuska@redhat.com> - 2.4-1
- Update to 2.4

* Mon Jun 30 2014 Robert Kuska <rkuska@redhat.com> - 2.2-1
- Update to 2.2

* Thu Jun 12 2014 Robert Kuska <rkuska@redhat.com> - 2.0-1
- Update to 2.0

* Fri Jun 06 2014 Robert Kuska <rkuska@redhat.com> - 1.1-3
- Make click own its folder
- Use pythonX_version macros from devel package

* Thu May 29 2014 Robert Kuska <rkuska@redhat.com> - 1.1-2
- Remove __pycache__ folder from tests

* Mon May 12 2014 Robert Kuska <rkuska@redhat.com> - 1.1-1
- Update source

* Wed May 07 2014 Robert Kuska <rkuska@redhat.com> - 0.6-1
- Initial package.
