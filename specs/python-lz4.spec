%global srcname lz4

Name:           python-%{srcname}
Version:        4.3.3
Release:        8%{?dist}
URL:            https://github.com/%{name}/%{name}
Summary:        LZ4 Bindings for Python
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
Source:         https://files.pythonhosted.org/packages/source/l/%{srcname}/%{srcname}-%{version}.tar.gz
# Reduce setuptools_scm dep to >= 6
Patch:          python-lz4-deps.patch

BuildRequires:  lz4-devel
BuildRequires:  python3-devel
BuildRequires:  gcc

# For tests
BuildRequires:  python3-psutil
# For docs
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-bootstrap-theme


%description
Python bindings for the lz4 compression library.


%package -n python3-lz4
Summary:        LZ4 Bindings for Python 3
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-lz4
Python 3 bindings for the lz4 compression library.


%prep
%autosetup -n %{srcname}-%{version} -p1
sed -i -e '/pytest-cov/d' setup.py
sed -i -e 's/--cov=lz4\/block --cov=lz4\/frame//' tox.ini

rm lz4libs/lz4*.[ch]

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files lz4
# Fix permissions on shared objects
find %{buildroot}%{python3_sitearch} -name 'lz4*.so' \
    -exec chmod 0755 {} \;

# Build HTML docs
pushd docs
PYTHONPATH=$RPM_BUILD_ROOT%{python3_sitearch} make html
popd
mv docs/_build/html ./html


%check
%tox


%files -n python3-lz4 -f %{pyproject_files}
%license LICENSE
%doc README.rst html


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 4.3.3-7
- convert license to SPDX

* Tue Sep 03 2024 Orion Poplawski <orion@nwra.com> - 4.3.3-6
- Do not run coverage tests

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 4.3.3-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 02 2024 Jonathan Wright <jonathan@almalinux.org> - 4.3.3-1
- Update to 4.3.3 rhbz#2256387

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 4.3.2-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 02 2023 Jonathan Wright <jonathan@almalinux.org> - 4.3.2-1
- update to 4.3.2 rhbz#2156909

* Wed Dec 07 2022 Jonathan Wright <jonathan@almalinux.org> - 4.0.2-2
- build against system lz4

* Wed Dec 07 2022 Jonathan Wright <jonathan@almalinux.org> - 4.0.2-1
- update to 4.0.2 rhbz#1716085
- use pyproject macros

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.0.2-9
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.0.2-6
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.2-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 29 2019 Jonathan Underwood <jonathan.underwood@gmail.com> - 3.0.2-1
- Update to version 3.0.2
- Disable tests on Arm due to insufficient RAM

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 27 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.2-3
- Subpackage python2-lz4 has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Nov  4 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 2.1.2-1
- Update to version 2.1.2

* Thu Aug  9 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 2.1.0-1
- Update to version 2.1.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul  7 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 2.0.2-1
- Update to version 2.0.2

* Sun Jun 24 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 2.0.1-2
- Bump release and rebuild for f29-python side tag

* Thu Jun 21 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 2.0.1-1
- Update to version 2.0.1

* Wed Jun 20 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 2.0.0-2
- Add BuildRequires for python{2,3}-psutil for tests

* Wed Jun 20 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 2.0.0-1
- Update to version 2.0.0

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.0-3
- Rebuilt for Python 3.7

* Sat Apr 28 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.1.0-2
- Add a Requires for python2-future to python2 package (BZ 1571130)

* Tue Apr  3 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.1.0-1
- Update to version 1.1.0 (fixes BZ#1553856)

* Tue Apr  3 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0.1-3
- Update to version 1.0.1
- Build and package html docs
- Run make doctest during %%check

* Sun Feb 18 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0.0-2
- Add a BuildRequires for gcc

* Sun Feb 18 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0.0-1
- Update to version 1.0.0

* Wed Feb 14 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.23.2-1
- Update to 0.23.2

* Sun Feb 11 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.23.1-4
- Rebuild for fixed spec

* Sun Feb 11 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.23.1-3
- Rebuild for fixed spec

* Sun Feb 11 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.23.1-2
- Add LICENSE file to packages

* Sun Feb 11 2018 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.23.1-1
- Update to 0.23.1
- Update BuildRequires
- Spec file cleanups

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 25 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.4-4
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun  2 2017 Haïkel Guémar <hguemar@fedoraproject.org> - 0.9.4-1
- Upstream 0.9.4
- Fix BR

* Mon Mar 13 2017 Alan Pevec <alan.pevec@redhat.com> 0.9.0-1
- Update to 0.9.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-2
- Rebuild for Python 3.6

* Tue Nov  8 2016 Orion Poplawski <orion@cora.nwra.com> - 0.8.2-1
- Update to 0.8.2
- Enable EPEL7 builds

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Apr 27 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.8.1-1
- Update to 0.8.1
- Use new upstream URL
- Drop upstreamed patch
- Use PyPi source url with hash, for now

* Sun Feb 28 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.7.0-6
- Spec file cleanup
- Add use of python_provide macro
- Remove python 3 conditional build - always build
- Use standard python packaging build and install macros

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 06 2015 Robert Kuska <rkuska@redhat.com> - 0.7.0-4
- Rebuilt for Python3.5 rebuild

* Mon Jun 29 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.7.0-3
- Update patch to build against system libs and add compress_fast method
- Add BR for python[3]-nose
- Run bundled test in %%check

* Sat Jun 27 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.7.0-2
- Drop unneeded Requires for lz4
- Remove commented out cruft from spec
- Regenerate setup.py patch to use libraries=["lz4"]
- Remove bundled lz4 code in %%prep

* Sat Jun 27 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.7.0-1
- Build against system lz4 libs
- Rudimentary check to see if we can import the module

* Sat Jun 27 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.7.0-0.2
- Include README.rst in python3 package as well

* Sat Jun 27 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.7.0-0.1
- Fix permissions of shared objects to be 0755

* Sat Jun 27 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 0.7.0-0
- Initial package for Fedora

