Name:           python-spnego
Version:        0.11.1
Release:        2%{?dist}
Summary:        Windows Negotiate Authentication Client and Server

# SPDX License
License:        MIT
URL:            https://github.com/jborean93/pyspnego
Source:         %{pypi_source pyspnego}
BuildArch:      noarch

%global _description %{expand:
Python SPNEGO Library to handle SPNEGO (Negotiate, NTLM, Kerberos)
authentication. Also includes a packet parser that can be used to
decode raw NTLM/SPNEGO/Kerberos tokens into a human readable format.}

%description %{_description}

%package -n     python3-spnego
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-mock)

%description -n python3-spnego %{_description}

%pyproject_extras_subpkg -n python3-spnego kerberos

%prep
%autosetup -n pyspnego-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files spnego

%check
%pytest -v tests

%files -n python3-spnego -f %{pyproject_files}
%doc README.md
%{_bindir}/pyspnego-parse

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 18 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.11.1-1
- Update to latest upstream release (closes rhbz#2291427)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.10.2-2
- Rebuilt for Python 3.13

* Sat Feb 03 2024 Fabian Affolter <mail@fabian-affolter.ch> - 0.10.2-1
- Update to latest upstream release 0.10.2 (closes rhbz#2240855)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 11 2023 Carl George <carlwgeorge@fedoraproject.org> - 0.9.2-1
- Update to version 0.9.2, resolves rhbz#2137695

* Mon Sep 11 2023 Orion Poplawski <orion@nwra.com> - 0.9.0-1
- Update to 0.9.0
- Verify SPDX license

* Mon Sep 11 2023 Carl George <carlwgeorge@fedoraproject.org> - 0.6.0-5
- Convert to pyproject macros

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jun 14 2023 Python Maint <python-maint@redhat.com> - 0.6.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Aug 19 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.6.0-1
- Update to latest upstream release 0.6.0 (closes rhbz#2105846, closes #2113657)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.5.0-2
- Rebuilt for Python 3.11

* Tue Feb 22 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.5.0-1
- Update to latest upstream release 0.5.0

* Wed Jan 26 2022 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.1-1
- Update to latest upstream release 0.3.1 (closes rhbz#2046177)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.1.5-2
- Rebuilt for Python 3.10

* Fri Mar 05 2021 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.5-1
- Update to latest upstream release 0.1.5

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Sep 12 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.1-2
- Add missing BR (rhbz#1876588)

* Mon Sep 07 2020 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.1-1
- Initial package for Fedora
