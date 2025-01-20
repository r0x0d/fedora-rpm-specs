%bcond_without check
%global srcname seaborn

Name: python-%{srcname}
Version: 0.13.2
Release: 7%{?dist}
Summary: Statistical data visualization in Python
License: BSD-3-Clause

URL: http://seaborn.pydata.org/
Source0: %{pypi_source}
# Use system python-husl
Patch0: seaborn-husl.patch
Patch1: seaborn-docscrape.patch
BuildArch: noarch

BuildRequires: python3-devel

%global _description %{expand:
Seaborn is a library for making attractive and informative statistical
graphics in Python. It is built on top of matplotlib and tightly integrated
with the PyData stack, including support for numpy and pandas data structures
and statistical routines from scipy and statsmodels.}

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}

BuildRequires: %{py3_dist flit_core}

%if %{with check}
BuildRequires: %{py3_dist husl}
BuildRequires: %{py3_dist numpydoc}
BuildRequires: %{py3_dist pytest}
%endif

Requires: %{py3_dist husl}
Requires: %{py3_dist numpydoc}
Recommends: %{py3_dist statsmodels}
## Not in fedora
##Recommends: _{py3_dist fastcluster}

%description -n python3-%{srcname} %_description

%prep
rm -rf seaborn/external/husl.py
rm -rf seaborn/external/docscrape.py
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires -x stats

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files seaborn


%if %{with check}
%check
%pytest
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Dec 08 2024 Sergio Pascual <sergiopr@fedoraproject.com> - 0.13.2-6
- Update SPDX indentifier

* Wed Nov 20 2024 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.13.2-5
- Enable full testing

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.13.2-4
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.13.2-2
- Rebuilt for Python 3.13

* Mon May 27 2024 Sergio Pascual <sergiopr@fedoraproject.com> - 0.13.2-1
- New upstream source 0.13.2

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Nov 01 2023 Sergio Pascual <sergiopr@fedoraproject.com> - 0.13.0-1
- New upstream source 0.13.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 28 2023 Python Maint <python-maint@redhat.com> - 0.12.2-2
- Rebuilt for Python 3.12

* Sun Apr 30 2023 Sergio Pascual <sergiopr@fedoraproject.org> - 0.12.2-1
- New upstream version 0.12.2

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.11.2-2
- Rebuilt for Python 3.11

* Mon Jun 13 2022 Sergio Pascual <sergiopr@fedoraproject.org> - 0.11.2-1
- New upstream version 0.11.2
- Update spec with new macros

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 0.11.1-4
- Add requirement on numpydoc (fixes bz #1973562)

* Wed Jun 09 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 0.11.1-3
- Fix wrong changelog entry

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.11.1-2
- Rebuilt for Python 3.10

* Fri Apr 09 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 0.11.1-1
- New upstream version 0.11.1
- Update spec

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 27 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.11.0-1
- New upstream version 0.11.0

* Tue Aug 18 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.10.1-5
- Fix problem with get_aspect in tests

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 06 2020 Sergio Pascual <sergiopr@fedoraproject.com> - 0.10.1-2
- New upstream version (0.10.1)
- Enable tests
- Use correct husl patch

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-3
- Rebuilt for Python 3.9

* Mon Mar 02 2020 Sergio Pascual <sergiopr@fedoraproject.com> - 0.10.0-2
- Disable tests for the moment

* Sun Mar 01 2020 Sergio Pascual <sergiopr@fedoraproject.com> - 0.10.0-1
- New upstream source 0.10.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-8
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.9.0-7
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 05 2018 Sergio Pascual <sergiopr@fedoraproject.com> - 0.9.0-4
- Do not create pytest pyc files
- Drop python2 subpackage
- Disable testing for the momment

* Tue Sep 11 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9.0-1
- Update to latest version

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-5
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-4
- Rebuilt for Python 3.7
- Exclude test_get_color_cycle because the test assumes old matplotlib API

* Fri Mar 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.1-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Mar 08 2018 Sergio Pascual <sergiopr@fedoraproject.com> - 0.8.1-2
- New upstream source 0.8.1
- And the sources

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.1-4
- Rebuild for Python 3.6

* Wed Sep 28 2016 Dominik Mierzejewski <rpm@greysector.net> - 0.7.1-3
- rebuilt for matplotlib-2.0.0
- fix testsuite failure

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 13 2016 Sergio Pascual <sergiopr@fedoraproject.com> - 0.7.1-1
- New upstream source 0.7.1
- Updated pypi url

* Mon Mar 28 2016 Sergio Pascual <sergiopr@fedoraproject.com> - 0.7.0-1
- New upstream source 0.7.0
- Add patch with fixes for Python 3.5

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Nov 15 2015 Thomas Spura <tomspur@fedoraproject.org> - 0.5.1-7
- Use newer python macros and add python2 subpackage

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Nov 27 2014 Sergio Pascual <sergiopr at fedoraproject.com> - 0.5.1-4
- Add source of LICENSE from upstream, distribution of LICENSE is required

* Thu Nov 27 2014 Sergio Pascual <sergiopr at fedoraproject.com> - 0.5.1-3
- More comments

* Wed Nov 26 2014 Sergio Pascual <sergiopr at fedoraproject.com> - 0.5.1-2
- Added BRs: six and husl

* Mon Nov 17 2014 Sergio Pascual <sergiopr at fedoraproject.com> - 0.5.1-1
- Initial spec

