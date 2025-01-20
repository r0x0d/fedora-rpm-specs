%global common_description %{expand:
Create beautiful and testable command-line interfaces.

Cleo is mostly a higher level wrapper for CliKit, so a lot of the
components and utilities comes from it. Refer to its documentation for
more information.}

#global prerel ...
%global base_version 2.1.0

Name:           python-cleo
Summary:        Create beautiful and testable command-line interfaces
Version:        %{base_version}%{?prerel:~%{prerel}}
Release:        5%{?dist}
License:        MIT

URL:            https://github.com/sdispater/cleo
Source0:        %{pypi_source cleo}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock

%description %{common_description}


%package -n     python3-cleo
Summary:        %{summary}

%description -n python3-cleo %{common_description}


%prep
%autosetup -n cleo-%{base_version}%{?prerel} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files cleo


%check
%pytest


%files -n python3-cleo -f %{pyproject_files}
%license LICENSE
%doc README.md


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 2.1.0-3
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 23 2024 Tomáš Hrnčiar <thrnciar@redhat.com> - 2.1.0-1
- Update to 2.1.0
- Fixes: rhbz#2247125

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 2.0.1-2
- Rebuilt for Python 3.12

* Tue Feb 21 2023 Tomáš Hrnčiar <thrnciar@redhat.com> - 2.0.1-1
- Update to 2.0.1

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~a5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 04 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 1.0.0~a5-1
- Update to 1.0.0a5
- Fixes: rhbz#2093481

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.1-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.8.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Oct 03 2020 Fabio Valentini <decathorpe@gmail.com> - 0.8.1-1
- Update to version 0.8.1.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.7.6-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Dec 08 2019 Fabio Valentini <decathorpe@gmail.com> - 0.7.6-1
- Update to version 0.7.6.

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.8-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.6.8-2
- Rebuilt for Python 3.8

* Wed Dec 19 2018 Fabio Valentini <decathorpe@gmail.com> - 0.6.8-1
- Initial package.

