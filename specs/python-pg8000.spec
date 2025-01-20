%global srcname pg8000

Name:           python-%{srcname}
Version:        1.31.2
Release:        2%{?dist}
Summary:        Pure Python PostgreSQL Driver

License:        BSD-3-Clause
URL:            http://github.com/tlocke/pg8000/
Source0:        %{pypi_source}
BuildArch:      noarch

%description
pg8000 is a pure-Python PostgreSQL driver that complies with DB-API 2.0.
The driver communicates with the database using the PostgreSQL Backend and
Frontend Protocol.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        Pure Python3 PostgreSQL Driver
BuildRequires:  python%{python3_pkgversion}-devel

%{?fedora:Suggests:       python3-sqlalchemy}
%{?fedora:Suggests:       postgresql}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python%{python3_pkgversion}-%{srcname}
pg8000 is a pure Python3 PostgreSQL driver that complies with DB-API 2.0.
The driver communicates with the database using the PostgreSQL Backend /
Frontend Protocol.

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
# Test requires a running PostgreSQL instance

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.31.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Sep 28 2024 Fabian Affolter <mail@fabian-affolter.ch> - 1.31.2-1
- Update to latest upstream version (closes rhbz#2277630)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.31.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 29 2024 Python Maint <python-maint@redhat.com> - 1.31.1-2
- Rebuilt for Python 3.13

* Sun Apr 07 2024 Fabian Affolter <mail@fabian-affolter.ch> - 1.31.1-1
- Update to latest upstream version 1.31.1 (closes rhbz#2265564)

* Tue Feb 06 2024 Nils Philippen <nils@tiptoe.de> - 1.30.4-1
- Update to latest upstream release 1.30.4

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 1.26.1-5
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.26.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 1.26.1-2
- Rebuilt for Python 3.11

* Wed Apr 27 2022 Fabian Affolter <mail@fabian-affolter.ch> - 1.26.1-1
- Update to latest upstream release 1.26.1 (closes rhbz#2078092)

* Wed Apr 20 2022 Fabian Affolter <mail@fabian-affolter.ch> - 1.26.0-1
- Update to latest upstream release 1.26.0 (closes rhbz#2075781)

* Thu Mar 03 2022 Fabian Affolter <mail@fabian-affolter.ch> - 1.24.1-1
- Update to latest upstream release 1.24.1 (closes rhbz#2060155)

* Tue Feb 22 2022 Fabian Affolter <mail@fabian-affolter.ch> - 1.24.0-1
- Update to latest upstream release 1.24.0 (closes rhbz#2051238)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.23.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 13 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.23.0-1
- Update to latest upstream release 1.23.0 (closes rhbz#2022952)

* Fri Nov 12 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.22.1-1
- Update to latest upstream release 1.22.1 (closes rhbz#2022137)

* Wed Oct 20 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.22.0-1
- Update to latest upstream release 1.22.0 (closes rhbz#2013794)

* Wed Oct 13 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.21.3-1
- Update to latest upstream release 1.21.3 (closes rhbz#2012584)

* Mon Sep 20 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.21.2-1
- Update to latest upstream release 1.21.2 (closes rhbz#2004267)

* Wed Aug 25 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.21.1-1
- Update to latest upstream release 1.21.1 (rhbz#1922640)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.17.0-2
- Rebuilt for Python 3.10

* Wed Feb 24 2021 Fabian Affolter <mail@fabian-affolter.ch> - 1.17.0-1
- Update to latest upstream release 1.17.0 (#1846920)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 10 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.16.6-1
- Update to 1.16.6 (#1887083)
- Enable python dependency generator

* Sun Aug 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.16.5-1
- Update to new upstream release 1.16.5 (rhbz#1855968)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.16.0-1
- Update to latest upstream release 1.16.0 (rhbz#1855968)

* Mon Jun 15 2020 Fabian Affolter <mail@fabian-affolter.ch> - 1.15.3-1
- Update to latest upstream release 1.15.3 (rhbz#1846920)

* Sat Jun 13 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.15.2-3
- adjust requires to scramp 1.2.0

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.15.2-2
- Rebuilt for Python 3.9

* Mon Apr 20 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 1.15.2-1
- Update to v1.15.2
- include fixes from BZ#1825716

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 24 2019 William Moreno Reyes <williamjmorenor@gmail.com> - 1.13.1-1
- Update to v1.13.1
  BZ#1671827

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 24 2018 William Moreno Reyes <williamjmorenor@gmail.com> - 1.12.3-1
- Update to v1.12.3

* Thu Oct 11 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.12.2-3
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Jul 01 2018 William Moreno Reyes <williamjmorenor@gmail.com> - 1.12.2-1
- Update to v.1.12.2
- BZ#1596431

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.12.1-2
- Rebuilt for Python 3.7

* Sun Jun 17 2018 William Moreno Reyes <williamjmorenor@gmail.com> - 1.12.1-1
- Update to v1.12.1
- BZ#1590323

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.11.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 30 2017 williamjmorenor@gmail.com - 1.11.0-1
- Update to v1.11.0 release
  Note that this version is not backward compatible with previous versions.
  https://github.com/mfenniak/pg8000#version-1-11-0-2017-08-16
- Drop docs subpackage removed from upstream

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.10.6-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.5-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Mar 11 2016 William Moreno <williamjmorenor@gmail.com> - 1.10.5-1
- Update to 1.10.5
- Remove patch included in upstream release
- Build docs in Fedora builds
- Update Source0 link

* Wed Mar 02 2016 William Moreno <williamjmorenor@gmail.com> - 1.10.4-1
- Epel7 packaging of version 1.10.4

* Tue Mar 01 2016 William Moreno <williamjmorenor@gmail.com> - 1.10.4-1
- Update to 1.10.4
- Remove patch1 included in upstream release
- Change source name
- Remove doc subpackage, upstream remove source in this release
- Patch licence text not include in the release

* Mon Feb 08 2016 William Moreno <williamjmorenor at gmail.com> - 1.10.3-2
- Remove bundled six library.

* Wed Feb 03 2016 William Moreno <williamjmorenor at gmail.com> - 1.10.3-1
- Initial Packaging


