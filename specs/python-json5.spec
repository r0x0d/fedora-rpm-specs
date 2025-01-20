%global pypi_name json5

Name:           python-%{pypi_name}
Version:        0.10.0
Release:        2%{?dist}
Summary:        Python implementation of the JSON5 data format

License:        Apache-2.0
URL:            https://github.com/dpranke/pyjson5
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
JSON5 extends the JSON data interchange format to make it slightly more usable
as a configuration language:

- JavaScript-style comments (both single and multi-line) are legal.
- Object keys may be unquoted if they are legal ECMAScript identifiers
- Objects and arrays may end with trailing commas.
- Strings can be single-quoted, and multi-line string literals are allowed.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(hypothesis)

%description -n python3-%{pypi_name}
JSON5 extends the JSON data interchange format to make it slightly more usable
as a configuration language:

- JavaScript-style comments (both single and multi-line) are legal.
- Object keys may be unquoted if they are legal ECMAScript identifiers
- Objects and arrays may end with trailing commas.
- Strings can be single-quoted, and multi-line string literals are allowed.

%package -n pyjson5
Summary:        Tool for working with the JSON5 data format

Requires:       python3-%{pypi_name} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n pyjson5
Command-line tool for working with the JSON5 data format.

%prep
%autosetup -n py%{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%files -n pyjson5
%doc README.md
%license LICENSE
%{_bindir}/pyjson5

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 29 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.10.0-1
- Update to latest upstream release (closes rhbz#2327388)

* Wed Nov 13 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.28-1
- Update to latest upstream release (closes rhbz#2325109)

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.25-4
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.9.25-2
- Rebuilt for Python 3.13

* Sun Apr 07 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.25-1
- Update to latest upstream release (closes rhbz#2274807)

* Sun Apr 07 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.24-1
- Update to latest upstream release (closes rhbz#2203645)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.9.12-2
- Rebuilt for Python 3.12

* Wed Jan 25 2023 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.12-1
- Update to latest upstream release 0.9.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Jan 09 2023 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.11-1
- Update to latest upstream release 0.9.11 (closes rhbz#2157808)

* Fri Aug 19 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.9-1
- Update to latest upstream release 0.9.9 (closes rhbz#2082728)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.9.6-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Aug 26 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.6-1
- Update to latest upstream release 0.9.6 (closes rhbz#1974533)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.5-4
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 30 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.5-1
- Update to latest upstream release 0.9.5 (rhbz#1840447)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.9.4-2
- Rebuilt for Python 3.9

* Fri Mar 27 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.4-1
- Update to latest upstream release 0.9.4 (rhbz#1817785)

* Thu Mar 19 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.3-1
- Update to latest upstream release 0.9.3 (rhbz#1815084)

* Sun Feb 09 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.1-1
- Update to latest upstream release 0.9.1

* Thu Feb 06 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.0-1
- Update to latest upstream release 0.9.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Sep 10 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.5-2
- Update summary
- Add version (rhbz#1750541)

* Mon Sep 09 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.8.5-1
- Initial package for Fedora
