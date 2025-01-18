Name:           codespell
Version:        2.3.0
Release:        3%{?dist}
Summary:        Fix common misspellings in text files

# Automatically converted from old format: GPLv2 and CC-BY-SA - review is highly recommended.
License:        GPL-2.0-only AND LicenseRef-Callaway-CC-BY-SA
URL:            https://github.com/codespell-project/codespell/
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
# For checks
BuildRequires:  python3dist(chardet)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-dependency)
BuildRequires:  aspell-en

%description
codespell fixes common misspellings in text files. It's designed primarily for
checking misspelled words in source code, but it can be used with other files
as well.

%generate_buildrequires
%pyproject_buildrequires

%prep
%autosetup -n %{name}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files codespell_lib

%check
# Skip coverage tests
sed -i -e 's/--cov=codespell_lib//' pyproject.toml
sed -i -e 's/--cov-report=//' pyproject.toml
%pytest

%files -f %{pyproject_files}
%doc README.rst
%license COPYING
%{_bindir}/codespell

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 2.3.0-2
- convert license to SPDX

* Mon Aug 26 2024 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.3.0-1
- Update to 2.3.0 - Closes rhbz#2283093

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.2.6-4
- Rebuilt for Python 3.13

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 04 2023 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.2.6-1
- Update to 2.2.6 rhbz#2242071
- Remove unneeded BuildRequires
- Add License file
- Enable check section and skip coverage tests

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 2.2.5-2
- Rebuilt for Python 3.12

* Wed Jun 14 2023 Bastien Nocera <bnocera@redhat.com> - 2.2.5-1
- Update to 2.2.5

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.2.4-2
- Rebuilt for Python 3.12

* Wed Mar 08 2023 Bastien Nocera <bnocera@redhat.com> - 2.2.4-1
- Update to 2.2.4

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Oct 19 2022 Bastien Nocera <bnocera@redhat.com> - 2.2.2-2
- Re-add egg-info

* Mon Oct 17 2022 Bastien Nocera <bnocera@redhat.com> - 2.2.2-1
- Update to 2.2.2

* Thu Aug 18 2022 Bastien Nocera <bnocera@redhat.com> - 2.2.1-1
+ codespell-2.2.1-1
- Update to 2.2.1

* Thu Aug 18 2022 Bastien Nocera <bnocera@redhat.com> - 2.2.0-1
+ codespell-2.2.0-1
- Update to 2.2.0

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.1.0-5
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Bastien Nocera <bnocera@redhat.com> - 2.1.0-3
+ codespell-2.1.0-3
- Fix CC-BY-SA shortname (#2036037)

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 11 2021 Bastien Nocera <bnocera@redhat.com> - 2.1.0-1
+ codespell-2.1.0-1
- Update to 2.1.0

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.0.0-3
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Nov 24 2020 Bastien Nocera <bnocera@redhat.com> - 2.0.0-1
+ codespell-2.0.0-1
- Update to 2.0.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 01 2020 Bastien Nocera <bnocera@redhat.com> - 1.17.1-5
+ codespell-1.17.1-5
- Replace Python version globs with macros to support 3.10

* Fri Jun 19 2020 Bastien Nocera <bnocera@redhat.com> - 1.17.1-4
+ codespell-1.17.1-4
- Bump version to match f32 branch

* Fri Jun 19 2020 Bastien Nocera <bnocera@redhat.com> - 1.17.1-3
+ codespell-1.17.1-3
- Fix usage dictionary not being distributed

* Mon Jun 15 2020 Bastien Nocera <bnocera@redhat.com> - 1.17.1-2
+ codespell-1.17.1-2
- Add usage dictionary

* Wed Jun 10 2020 Bastien Nocera <bnocera@redhat.com> - 1.17.1-1
+ codespell-1.17.1-1
- Update to 1.17.1
- Fix Python 3.8 warning (#1840693)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.16.0-3
- Rebuilt for Python 3.9

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Wolfgang Stöggl <c72578@yahoo.de> - 1.16.0-1
- New upstream version 1.16.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.15.0-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.15.0-4
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Bastien Nocera <bnocera@redhat.com> - 1.15.0-2
+ codespell-1.15.0-2
- Fix some review comments

* Tue Jun 18 2019 hadess <bnocera@redhat.com> - 1.15.0-1
- Initial package.
