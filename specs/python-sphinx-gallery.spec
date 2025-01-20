%global srcname sphinx-gallery

Name:           python-%{srcname}
Version:        0.18.0
Release:        3%{?dist}
Summary:        Sphinx extension to automatically generate an examples gallery

License:        BSD-3-Clause
URL:            https://sphinx-gallery.github.io/stable/index.html
Source0:        https://github.com/sphinx-gallery/sphinx-gallery/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
A Sphinx extension that builds an HTML version of any Python script and puts
it into an examples gallery.


%package -n     python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
BuildRequires:  python%{python3_pkgversion}-devel
# For tests
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-absl-py
BuildRequires:  python%{python3_pkgversion}-lxml
BuildRequires:  python%{python3_pkgversion}-matplotlib

%description -n python%{python3_pkgversion}-%{srcname}
A Sphinx extension that builds an HTML version of any Python script and puts
it into an examples gallery.


%pyproject_extras_subpkg -n python%{python3_pkgversion}-%{srcname} recommender
%pyproject_extras_subpkg -n python%{python3_pkgversion}-%{srcname} show_api_usage


%prep
%autosetup -n %{srcname}-%{version}

# No coverage report
sed -i -e 's/"--cov[^ ]*//g' pyproject.toml


%generate_buildrequires
# extras with missing deps:
#  "show_memory": ["memory_profiler"],
#  "jupyterlite": ["jupyterlite_sphinx"],
%pyproject_buildrequires -x recommender -x show_api_usage


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files sphinx_gallery


%check
# test_dummy_image requires jupyterlite_sphinx optional dep
# test_embed_code_links_get_data requires network
%pytest -v -k 'not test_dummy_image and not test_embed_code_links_get_data'


%files -n python%{python3_pkgversion}-%{srcname} -f %pyproject_files
%doc README.rst CHANGES.rst
%{_bindir}/sphinx_gallery_py2jupyter


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 31 2024 Sandro <devel@penguinpee.nl> - 0.18.0-2
- Add missing test dependency

* Mon Oct 21 2024 Orion Poplawski <orion@nwra.com> - 0.18.0-1
- Update to 0.18.0

* Wed Jul 31 2024 Orion Poplawski <orion@nwra.com> - 0.17.0-1
- Update to 0.17.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 0.15.0-6
- Rebuilt for Python 3.13

* Mon Jan 29 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 09 2024 Jerry James <loganjerry@gmail.com> - 0.15.0-2
- Convert License tag to SPDX
- Ship sphx_glr_python_to_jupyter.py

* Tue Jan 09 2024 Orion Poplawski <orion@nwra.com> - 0.15.0-1
- Update to 0.15.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 27 2023 Python Maint <python-maint@redhat.com> - 0.11.1-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Oct 02 2022 Orion Poplawski <orion@nwra.com> - 0.11.1-1
- Update to 0.11.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun 15 2022 Python Maint <python-maint@redhat.com> - 0.10.1-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 14 2021 Orion Poplawski <orion@nwra.com> - 0.10.1-1
- Update to 0.10.1

* Mon Sep 27 2021 Orion Poplawski <orion@nwra.com> - 0.10.0-1
- Update to 0.10.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.2-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 24 2021 Orion Poplawski <orion@nwra.com> - 0.8.2-1
- Update to 0.8.2

* Thu Sep 10 2020 Orion Poplawski <orion@nwra.com> - 0.8.1-1
- Update to 0.8.1

* Thu Aug 06 2020 Orion Poplawski <orion@nwra.com> - 0.7.0-4
- Completely drop python2 support

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-2
- Rebuilt for Python 3.9

* Fri May 22 2020 Orion Poplawski <orion@nwra.com> - 0.7.0-1
- Update to 0.7.0

* Fri May 08 2020 Orion Poplawski <orion@nwra.com> - 0.6.2-1
- Update to 0.6.2

* Thu Apr 09 2020 Orion Poplawski <orion@nwra.com> - 0.6.1-1
- Update to 0.6.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 18 2019 Orion Poplawski <orion@nwra.com> - 0.5.0-1
- Update to 0.5.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 9 2019 Orion Poplawski <orion@nwra.com> - 0.3.1-1
- Update to 0.3.1

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 7 2018 Orion Poplawski <orion@nwra.com> - 0.2.0-1
- Update to 0.2.0
- Drop Python 2 package for Fedora 30+ (bugz #1628982)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.1.13-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 27 2017 Orion Poplawski <orion@nwra.com> - 0.1.13-1
- Update to 0.1.13

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.1.5-4
- Rebuild for Python 3.6

* Mon Nov 21 2016 Orion Poplawski <orion@cora.nwra.com> - 0.1.5-3
- Add upstream patch to fix UnicodeDecodeError

* Sat Nov 19 2016 Orion Poplawski <orion@cora.nwra.com> - 0.1.5-2
- Use github source, ship LICENSE
- Update URL
- Add needed requires

* Tue Nov 15 2016 Orion Poplawski <orion@cora.nwra.com> - 0.1.5-1
- Initial Fedora package
