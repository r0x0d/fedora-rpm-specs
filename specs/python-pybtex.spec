Name:           python-pybtex
Version:        0.24.0
Release:        18%{?dist}
Summary:        BibTeX-compatible bibliography processor written in Python

License:        MIT
URL:            https://pybtex.org/
VCS:            git:https://bitbucket.org/pybtex-devs/pybtex.git
Source:         %pypi_source pybtex
# Fix a minor sphinx problem, leads to bad man page output
Patch:          %{name}-parsing.patch
# Fix an extlinks configuration error
# https://bitbucket.org/pybtex-devs/pybtex/pull-requests/45
Patch:          %{name}-extlinks.patch

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-docs
BuildRequires:  %{py3_dist sphinx}

%global common_desc %{expand:
Pybtex is a BibTeX-compatible bibliography processor written in Python.
Pybtex aims to be 100%% compatible with BibTeX.  It accepts the same
command line options, fully supports BibTeX’s .bst styles and produces
byte-identical output.

Additionally:
- Pybtex is Unicode-aware.
- Pybtex supports bibliography formats other than BibTeX.
- It is possible to write formatting styles in Python.
- As a bonus, Pythonic styles can produce HTML, Markdown and other
  markup besides the usual LaTeX.
Pybtex also includes a Python API for managing bibliographies from Python.}

%description %common_desc

%package -n python3-pybtex
Summary:        BibTeX-compatible bibliography processor written in Python
# Needed until this issue is resolved:
# https://bitbucket.org/pybtex-devs/pybtex/issues/169/replace-pkg_resources-with
# See https://src.fedoraproject.org/rpms/babel/pull-request/11
Requires:       %{py3_dist setuptools}
Provides:       bundled(js-jquery)
Provides:       bundled(js-underscore)

%description -n python3-pybtex %common_desc

%package doc
# The content is MIT.  Other licenses are due to files copied in by Sphinx.
# _static/_sphinx_javascript_frameworks_compat.js: BSD-2-Clause
# _static/basic.css: BSD-2-Clause
# _static/doctools.js: BSD-2-Clause
# _static/documentation_options.js: BSD-2-Clause
# _static/file.png: BSD-2-Clause
# _static/jquery*.js: MIT
# _static/language_data.js: BSD-2-Clause
# _static/minus.png: BSD-2-Clause
# _static/plus.png: BSD-2-Clause
# _static/searchtools.js: BSD-2-Clause
# _static/underscore*.js: MIT
# genindex.html: BSD-2-Clause
# search.html: BSD-2-Clause
# searchindex.js: BSD-2-Clause
License:        MIT AND BSD-2-Clause
Summary:        Documentation for python-pybtex

%description doc
Documentation for python-pybtex.

%prep
%autosetup -p0 -n pybtex-%{version}

%conf
# Remove useless shebang
sed -i '\@/usr/bin/env python@d' pybtex/cmdline.py

# Fix shebangs
for fil in docs/generate_manpages.py \
           pybtex/bibtex/runner.py \
           pybtex/charwidths/make_charwidths.py \
           pybtex/database/{convert,format}/__main__.py \
           pybtex/__main__.py \
           setup.py; do
  sed -i 's/env python/python3/' $fil
done

# Use local objects.inv for intersphinx
sed -e "s|\('https://docs\.python\.org/3/', \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" \
    -i docs/source/conf.py

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

# Build documentation
# Workaround for pygments 2.13.  See bz 2127371.
cat >> pybtex.egg-info/entry_points.txt << EOF

[pygments.styles]
pybtex = pybtex_doctools.pygments:PybtexStyle

[pygments.lexers]
bibtex-pybtex = pybtex_doctools.pygments:BibTeXLexer
bst-pybtex = pybtex_doctools.pygments:BSTLexer
EOF

PYTHONPATH=$PWD:$PWD/build/lib make -C docs html man
rm -f docs/build/html/.buildinfo

%install
%pyproject_install
%pyproject_save_files -l pybtex

mkdir -p %{buildroot}%{_mandir}/man1
cp -p docs/build/man/*.1 %{buildroot}%{_mandir}/man1
echo ".so man1/pybtex.1" > %{buildroot}%{_mandir}/man1/pybtex-convert.1
echo ".so man1/pybtex.1" > %{buildroot}%{_mandir}/man1/pybtex-format.1

pushd %{buildroot}%{python3_sitelib}
rm -fr custom_fixers tests
chmod a+x pybtex/bibtex/runner.py pybtex/charwidths/make_charwidths.py \
      pybtex/database/{convert,format}/__main__.py pybtex/__main__.py
popd

%check
%pytest -v

%files -n python3-pybtex -f %{pyproject_files}
%doc README
%{_bindir}/pybtex*
%{_mandir}/man1/pybtex*

%files doc
%doc CHANGES docs/build/html

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.24.0-16
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.24.0-12
- Rebuilt for Python 3.12

* Tue Mar 21 2023 Jerry James <loganjerry@gmail.com> - 0.24.0-11
- Fix an extlinks configuration error (rhbz#2180478)

* Tue Feb 28 2023 Jerry James <loganjerry@gmail.com> - 0.24.0-10
- Depend on setuptools at runtime

* Thu Feb 23 2023 Jerry James <loganjerry@gmail.com> - 0.24.0-9
- Dynamically generate BuildRequires
- Update pygments workaround

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 13 2022 Jerry James <loganjerry@gmail.com> - 0.24.0-8
- Convert License tags to SPDX

* Tue Sep 20 2022 Jerry James <loganjerry@gmail.com> - 0.24.0-8
- Add workaround for pygments 2.13 (rhbz#2127371)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.24.0-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.24.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan 17 2021 Jerry James <loganjerry@gmail.com> - 0.24.0-1
- Version 0.24.0

* Mon Oct 12 2020 Jerry James <loganjerry@gmail.com> - 0.23.0-1
- Version 0.23.0
- Drop upstreamed -elementtree patch

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.2-11.20200126.e1336fb33c92
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 0.22.2-10.20200126.e1336fb33c92
- Rebuilt for Python 3.9

* Fri Mar 27 2020 Jerry James <loganjerry@gmail.com> - 0.22.2-9.20200126.e1336fb33c92
- Update to git head to fix duplicate person issue
- Drop upstreamed -escape patch
- Add -elementtree patch to fix python 3.9 build (bz 1817962)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.2-8.20191015.6d9d812c82ce
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 24 2020 Jerry James <loganjerry@gmail.com> - 0.22.2-7.20191015.6d9d812c82ce
- Add -escape patch
- Invoke pytest directly

* Wed Nov 27 2019 Jerry James <loganjerry@gmail.com> - 0.22.2-6.20191015.6d9d812c82ce
- Update to git head to fix a variety of python 3 issues

* Fri Sep 20 2019 Jerry James <loganjerry@gmail.com> - 0.22.2-5.20190905.9cf6c600ea5d
- Update to git head to fix python-sphinxcontrib-bibtex sorting issues

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 0.22.2-4
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 26 2019 Jerry James <loganjerry@gmail.com> - 0.22.2-1
- New upstream version

* Mon Nov 26 2018 Jerry James <loganjerry@gmail.com> - 0.22.0-1
- New upstream version

* Tue Nov  6 2018 Jerry James <loganjerry@gmail.com> - 0.21-9
- Drop -python36 patch, replaced by 2to3 invocation
- Add -python3 patch to fix stuff that 2to3 didn't catch

* Thu Nov 01 2018 Miro Hrončok <mhroncok@redhat.com> - 0.21-8
- Subpackage python2-pybtex has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.21-6
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.21-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Jerry James <loganjerry@gmail.com> - 0.21-1
- New upstream version

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.20.1-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20.1-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Mar 18 2016 Jerry James <loganjerry@gmail.com> - 0.20.1-1
- New upstream version

* Thu Mar 10 2016 Jerry James <loganjerry@gmail.com> - 0.20-1
- New upstream version

* Wed Mar  2 2016 Jerry James <loganjerry@gmail.com> - 0.19-2
- Don't preserve timestamps of modified files
- Fix nosetests invocation
- Simplify files section

* Thu Feb 25 2016 Jerry James <loganjerry@gmail.com> - 0.19-1
- Initial RPM
