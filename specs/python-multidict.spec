Name:           python-multidict
Version:        6.1.0
Release:        2%{?dist}
Summary:        MultiDict implementation

License:        Apache-2.0
URL:            https://github.com/aio-libs/multidict
Source:         %{pypi_source multidict}

BuildRequires:  gcc

%global _description %{expand:
Multidict is dict-like collection of key-value pairs where key might occur more
than once in the container.}

%description %_description

%package -n python3-multidict
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-Cython
BuildRequires:  python3dist(pytest)

%description -n python3-multidict %_description

%prep
%autosetup -n multidict-%{version}
sed -i -e "/--cov/d" pytest.ini
sed -i -e "/-p pytest_cov/d" pytest.ini

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files multidict

%check
%pytest -v tests --ignore tests/test_circular_imports.py

%files -n python3-multidict -f %{pyproject_files}
%doc README.rst

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 16 2024 Fabian Affolter <mail@fabian-affolter.ch> - 6.1.0-1
- Update to latest upstream release 6.1.0 (closes rhbz#2310967)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 6.0.5-2
- Rebuilt for Python 3.13

* Mon Apr 08 2024 Fabian Affolter <mail@fabian-affolter.ch> - 1.9.4-1
- Update to latest upstream release 6.0.5 (closes rhbz#2262328)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 6.0.4-2
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 6.0.4-1
- Update to 6.0.4, resolves rhbz#2150589
- Convert to pyproject macros

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 6.0.2-6
- Rebuilt for Python 3.11

* Tue Feb 22 2022 Fabian Affolter <mail@fabian-affolter.ch> - 6.0.2-1
- Update to new upstream version 6.0.2 (closes rhbz#2009584)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 03 2021 Python Maint <python-maint@redhat.com> - 5.1.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 04 2020 Fabian Affolter <mail@fabian-affolter.ch> - 5.1.0-1
- Update to latest upstream release 5.1.0 (#1897800)

* Mon Nov 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 5.0.2-1
- Update to latest upstream release 5.0.2 (#1897800)

* Wed Oct 14 2020 Fabian Affolter <mail@fabian-affolter.ch> - 5.0.0-1
- Update to latest upstream release 5.0.0 (#1887481)

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 4.7.6-2
- Rebuilt for Python 3.9

* Sat May 16 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.7.6-1
- Update to latest upstream release 4.7.6 (#1836076)

* Sat Feb 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.7.5-1
- Update to latest upstream release 4.7.5 (#1806083)

* Mon Feb 03 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.7.4-1
- UPdate to latest upstream release 4.7.4 (#1774256)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 26 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.5.2-1
- Update to 4.5.2

* Fri Aug 16 2019 Miro Hrončok <mhroncok@redhat.com> - 4.3.1-5
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 07 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.3.1-1
- Update to 4.3.1

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 4.1.0-3
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 29 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.1.0-1
- Update to 4.1.0

* Mon Jan 15 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.0.0-1
- Update to 4.0.0

* Fri Nov 03 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.3.2-1
- Update to 3.3.2

* Thu Nov 02 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.3.1-1
- Update to 3.3.1

* Fri Oct 20 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.3.0-1
- Update to 3.3.0

* Sun Oct 01 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.2.0-1
- Update to 3.2.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jul 16 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.1.3-1
- Update to 3.1.3

* Mon Jul 03 2017 Athmane Madjoudj <athmane@fedoraproject.org> - 3.1.0-1
- Update to 3.1.0
- Ignore tests until imports are fixed

* Thu Jun 08 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.6-1
- Update to 2.1.6

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.1.4-1.1
- Rebuild for Python 3.6

* Thu Dec 01 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.1.4-1
- Update to 2.1.4

* Thu Dec 01 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.1.3-1
- Update to 2.1.3

* Mon Nov 07 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 2.1.2-1
- Update to 2.1.2

* Fri Sep 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 2.1.1-1
- Update to 2.1.1

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-1.1
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Jul 07 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.1.0-1
- Update to 1.1.0
- Trivial fixes

* Thu Jun 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.1.0-0.1b4
- Initial package
