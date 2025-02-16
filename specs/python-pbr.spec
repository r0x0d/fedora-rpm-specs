%global pypi_name pbr
# Disable bootstrap
%bcond bootstrap 0

# EPEL does not have the necessary testing dependencies
# During the bootstrap the test dependencies are not ready yet
%bcond tests %[%{defined fedora} && %{without bootstrap}]

Name:           python-%{pypi_name}
Version:        6.1.1
Release:        1%{?dist}
Summary:        Python Build Reasonableness

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://pypi.python.org/pypi/pbr
Source0:        https://pypi.io/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  git-core
%if %{with tests}
BuildRequires:  gcc
BuildRequires:  gnupg2
%endif


%description
PBR is a library that injects some useful and sensible default behaviors into
your setuptools run. It started off life as the chunks of code that were copied
between all of the OpenStack projects. Around the time that OpenStack hit 18
different projects each with at least 3 active branches, it seems like a good
time to make that code into a proper re-usable library.

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        Python Build Reasonableness
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

Requires:       python%{python3_pkgversion}-setuptools
Requires:       git-core

%description -n python%{python3_pkgversion}-%{pypi_name}
Manage dynamic plugins for Python applications


%generate_buildrequires
%pyproject_buildrequires %{?with_tests:-e %{default_toxenv}} %{!?with_bootstrap:-e docs}


%prep
%autosetup -n %{pypi_name}-%{version} -p1

sed -i '/^six.*/d' test-requirements.txt
sed -i 's/hacking.*/hacking/' test-requirements.txt
sed -i '/^six.*/d' doc/requirements.txt
sed -i '/^reno.*/d' doc/requirements.txt
sed -i 's/^sphinx!=.*/sphinx/' doc/requirements.txt
sed -i 's/^sphinxcontrib-apidoc.*/sphinxcontrib-apidoc/' doc/requirements.txt
sed -i 's/^openstackdocstheme.*/openstackdocstheme/' doc/requirements.txt


%build
%pyproject_wheel

%if %{without bootstrap}
# generate html docs
PYTHONPATH=%{pyproject_build_lib} sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif


%install
%pyproject_install
%pyproject_save_files %{pypi_name}
mv %{buildroot}%{_bindir}/pbr %{buildroot}%{_bindir}/pbr-3
ln -s ./pbr-3 %{buildroot}%{_bindir}/pbr


%if %{with tests}
%check
export PYTHONDONTWRITEBYTECODE=1
# Exclude tests that require networking
%tox -e %{default_toxenv} -- -- -E 'test_requirement_parsing|test_pep_517_support'
%endif

%files -n python%{python3_pkgversion}-pbr -f %{pyproject_files}
%license LICENSE
%doc README.rst %{?without_bootstrap:html}
%{_bindir}/pbr
%{_bindir}/pbr-3

%changelog
* Fri Feb 14 2025 Joel Capitao <jcapitao@redhat.com> - 6.1.1-1
- Update to 6.1.1

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 30 2024 Joel Capitao <jcapitao@redhat.com> - 6.0.0-1
- Update to 6.0.0

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 5.11.1-10
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 5.11.1-8
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Oct 20 2023 Karolina Surma <ksurma@redhat.com> - 5.11.1-5
- When boostrapping the package switch off the tests

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 14 2023 Python Maint <python-maint@redhat.com> - 5.11.1-3
- Rebuilt for Python 3.12

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 5.11.1-2
- Bootstrap for Python 3.12

* Thu Feb 09 2023 Joel Capitao <jcapitao@redhat.com> - 5.11.1-1
- Update to latest upstream (#2136463)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 17 2022 Joel Capitao <jcapitao@redhat.com> - 5.10.0-1
- Update to 5.10.0. Fixes rhbz#2117702

* Sat Jul 23 2022 Maxwell G <gotmax@e.email> - 5.9.0-1
- Update to 5.9.0. Fixes rhbz#2020182.
- Re-enable unit tests

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 5.6.0-5
- Rebuilt for Python 3.11

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 5.6.0-4
- Bootstrap for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jul 21 2021 Joel Capitao <jcapitao@redhat.com> - 5.6.0-1
- Update to latest release (#1953661)
- Use git-core as BR instead of git

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 5.5.1-4
- Rebuilt for Python 3.10

* Wed Jun 02 2021 Python Maint <python-maint@redhat.com> - 5.5.1-3
- Bootstrap for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 29 2020 Joel Capitao <jcapitao@redhat.com> - 5.5.1-1
- Update to 5.5.1 (rhbz#1684239)

* Mon Sep 14 2020 Joel Capitao <jcapitao@redhat.com> - 5.5.0-1
- Update to 5.5.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 5.4.3-5
- Rebuilt for Python 3.9

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 5.4.3-4
- Bootstrap for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Miro Hrončok <mhroncok@redhat.com> - 5.4.3-2
- Subpackage python2-pbr has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Tue Sep 10 2019 Yatin Karel <ykarel@redhat.com> - 5.4.3-1
- Update to 5.4.3

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 5.1.2-7
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 5.1.2-6
- Bootstrap for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 24 2019 Yatin Karel <ykarel@redhat.com> - 5.1.2-3
- Fix FTBFS: No more python2-openstackdocstheme

* Thu Feb 07 2019 Javier Peña <jpena@redhat.com> - 5.1.2-2
- Fix doc requirements

* Thu Feb 07 2019 Javier Peña <jpena@redhat.com> - 5.1.2-1
- Update to 5.1.2 (rhbz#1671081)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 04 2018 Matthias Runge <mrunge@redhat.com> - 4.2.0-1
- update to 4.2.0 (rhbz#1605192)

* Wed Aug  8 2018 Haïkel Guémar <hguemar@fedoraproject.org> - 4.1.1-2
- Add runtime requirement to git-core

* Fri Jul 20 2018 Matthias Runge <mrunge@redhat.com> - 4.1.1-1
- rebase to 4.1.1 (rhbz#1605192)

* Wed Jul 18 2018 Haïkel Guémar  <hguemar@fedoraproject.org> - 4.1.0-2
- Add dependency to setuptools (RHBZ#1601767)

* Tue Jul 17 2018 Matthias Runge <mrunge@redhat.com> - 4.1.0-1
- update to 4.1.0 (rhbz#1561252)
- modernize spec

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 13 2018 Miro Hrončok <mhroncok@redhat.com> - 3.1.1-8
- Rebuilt for Python 3.7

* Tue Feb 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.1.1-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 15 2018 Tomas Orsava <torsava@redhat.com> - 3.1.1-6
- Switch %%python macro to %%python2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 3.1.1-4
- Cleanup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 17 2017 Jan Beran <jberan@redhat.com> 3.1.1-2
- Fix of missing Python 3 version of executables in python3-pbr subpackage

* Wed Jun 28 2017 Alan Pevec <alan.pevec@redhat.com> 3.1.1-1
- Update to 3.1.1

* Fri Mar  3 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 2.0.0-1
- Upstream 2.0.0
- Drop upstreamed patch

* Sat Feb 18 2017 Alan Pevec <apevec AT redhat.com> - 1.10.0-4
- Fix newer Sphinx and Python 3.5 support LP#1379998

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 1.10.0-2
- Rebuild for Python 3.6

* Wed Oct 12 2016 Alan Pevec <apevec AT redhat.com> - 1.10.0-1
- Update to 1.10.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 4 2016 Paul Belanger <pabelanger@redhat.com> 1.8.1-3
- Provide python2-pbr (rhbz#1282126)
- minor spec cleanup

* Thu Nov 12 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Nov 12 2015 Alan Pevec <alan.pevec@redhat.com> 1.8.1-1
- Update to 1.8.1

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Sep 14 2015 Alan Pevec <alan.pevec@redhat.com> 1.8.0-1
- Update to upstream 1.8.0

* Tue Sep 08 2015 Alan Pevec <alan.pevec@redhat.com> 1.7.0-1
- Update to upstream 1.7.0

* Mon Aug 31 2015 Matthias Runge <mrunge@redhat.com> - 1.6.0-1
- update to upstream 1.6.0 (rhbz#1249840)

* Sat Aug 15 2015 Alan Pevec <alan.pevec@redhat.com> 1.5.0-1
- Update to upstream 1.5.0

* Wed Jul 15 2015 Alan Pevec <alan.pevec@redhat.com> 1.3.0-1
- Update to upstream 1.3.0

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Jun 02 2015 Alan Pevec <apevec@redhat.com> - 0.11.0-1
- update to 0.11.0

* Fri Mar 20 2015 Alan Pevec <apevec@redhat.com> - 0.10.8-1
- update to 0.10.8

* Mon Dec 29 2014 Alan Pevec <apevec@redhat.com> - 0.10.7-1
- update to 0.10.7

* Tue Nov 25 2014 Matthias Runge <mrunge@redhat.com> - 0.10.0-1
- update to 0.10.0 (rhbz#1191232)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Apr 30 2014 Matthias Runge <mrunge@redhat.com> - 0.8.0-1
- update to 0.8.0 (rhbz#1078761)

* Tue Apr 08 2014 Matthias Runge <mrunge@redhat.com> - 0.7.0-2
- Added python3 subpackage.
- slight modification of Ralph Beans proposal

* Mon Mar 24 2014 Matthias Runge <mrunge@redhat.com> - 0.7.0-1
- update to 0.7.0 (rhbz#1078761)

* Tue Feb 11 2014 Matthias Runge <mrunge@redhat.com> - 0.6.0-1
- update to 0.6.0 (rhbz#1061124)

* Fri Nov 01 2013 Matthias Runge <mrunge@redhat.com> - 0.5.23-1
- update to 0.5.23 (rhbz#1023926)

* Tue Aug 13 2013 Matthias Runge <mrunge@redhat.com> - 0.5.21-2
- add requirement python-pip (rhbz#996192)
- remove requirements.txt

* Thu Aug 08 2013 Matthias Runge <mrunge@redhat.com> - 0.5.21-1
- update to 0.5.21 (rhbz#990008)

* Fri Jul 26 2013 Matthias Runge <mrunge@redhat.com> - 0.5.19-2
- remove one buildrequires: python-sphinx

* Mon Jul 22 2013 Matthias Runge <mrunge@redhat.com> - 0.5.19-1
- update to python-pbr-0.5.19 (rhbz#983008)

* Mon Jun 24 2013 Matthias Runge <mrunge@redhat.com> - 0.5.17-1
- update to python-pbr-0.5.17 (rhbz#976026)

* Wed Jun 12 2013 Matthias Runge <mrunge@redhat.com> - 0.5.16-1
- update to 0.5.16 (rhbz#973553)

* Tue Jun 11 2013 Matthias Runge <mrunge@redhat.com> - 0.5.14-1
- update to 0.5.14 (rhbz#971736)

* Fri May 31 2013 Matthias Runge <mrunge@redhat.com> - 0.5.11-2
- remove requirement setuptools_git
- fix docs build under rhel

* Fri May 17 2013 Matthias Runge <mrunge@redhat.com> - 0.5.11-1
- update to 0.5.11 (rhbz#962132)
- disable tests, as requirements can not be fulfilled right now

* Thu Apr 25 2013 Matthias Runge <mrunge@redhat.com> - 0.5.8-1
- Initial package.
