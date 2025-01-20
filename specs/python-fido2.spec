%global srcname fido2

Name:           python-%{srcname}
Version:        1.2.0
Release:        2%{?dist}
Summary:        Functionality for FIDO 2.0, including USB device communication

# Main code is BSD
# pyu2f is APLv2
# public_suffix_list.dat is MPLv2
# Automatically converted from old format: BSD and ASL 2.0 and MPLv2.0 - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND Apache-2.0 AND MPL-2.0
URL:            https://github.com/Yubico/python-fido2
Source0:        https://github.com/Yubico/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%global _description\
Provides library functionality for communicating with a FIDO device over USB\
as well as verifying attestation and assertion signatures.\
\
WARNING: This project is in beta. Expect things to change or break at any time!\
\
This library aims to support the FIDO U2F and FIDO 2.0 protocols for\
communicating with a USB authenticator via the Client-to-Authenticator\
Protocol (CTAP 1 and 2). In addition to this low-level device access, classes\
defined in the fido2.client and fido2.server modules implement higher level\
operations which are useful when interfacing with an Authenticator, or when\
implementing a Relying Party.\
\
For usage, see the examples/ directory.

%description %_description


%package -n python%{python3_pkgversion}-%{srcname}
Summary: %summary
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest

%description -n python%{python3_pkgversion}-%{srcname} %_description


%prep
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
# EL8 has old python-cryptography that makes a few tests fail
# https://github.com/Yubico/python-fido2/issues/111
%{__python3} -m unittest discover -v %{?el8:|| :}


%files -n python%{python3_pkgversion}-%{srcname} -f %pyproject_files
%license COPYING*
%doc NEWS README.adoc examples


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Nov 30 2024 Orion Poplawski <orion@nwra.com> - 1.2.0-1
- Update to 1.2.0

* Fri Oct 18 2024 Orion Poplawski <orion@nwra.com> - 1.1.3-1
- Update to 1.1.3
- Add patch to properly skip SHA1 test (FTBFS rhbz#2301146)

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 1.1.2-7
- convert license to SPDX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.1.2-5
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 16 2023 Orion Poplawski <orion@nwra.com> - 1.1.2-1
- Update to 1.1.2

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 1.1.1-2
- Rebuilt for Python 3.12

* Wed Apr 05 2023 Orion Poplawski <orion@nwra.com> - 1.1.1-1
- Update to 1.1.1

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Oct 23 2022 Orion Poplawski <orion@nwra.com> - 1.1.0-1
- Update to 1.1.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.0.0-2
- Rebuilt for Python 3.11

* Thu Jun 09 2022 Orion Poplawski <orion@nwra.com> - 1.0.0-1
- Update to 1.0.0

* Fri May 20 2022 Orion Poplawski <orion@nwra.com> - 0.9.3-1
- Update to 0.9.3 (bz#2087023)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 15 2021 Orion Poplawski <orion@nwra.com> - 0.9.2-1
- Update to 0.9.2

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.9.1-3
- Rebuilt for Python 3.10

* Wed Feb 10 2021 Orion Poplawski <orion@nwra.com> - 0.9.1-2
- Drop python2 / python3_other support
- Skip failing tests on EL8

* Thu Feb 04 2021 Orion Poplawski <orion@nwra.com> - 0.9.1-1
- Update to 0.9.1

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 25 2021 Orion Poplawski <orion@nwra.com> - 0.9.0-1
- Update to 0.9.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Orion Poplawski <orion@nwra.com> - 0.8.1-4
- Add BR on python-setuptools

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.8.1-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Orion Poplawski <orion@nwra.com> - 0.8.1-1
- Update to 0.8.1

* Thu Oct 24 2019 Orion Poplawski <orion@nwra.com> - 0.7.2-1
- Update to 0.7.2

* Thu Sep 26 2019 Orion Poplawski <orion@nwra.com> - 0.7.1-1
- Update to 0.7.1

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.7.0-2
- Rebuilt for Python 3.8

* Sun Aug 11 2019 Orion Poplawski <orion@nwra.com> - 0.7.0-1
- Update to 0.7.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat May 11 2019 Orion Poplawski <orion@nwra.com> - 0.6.0-1
- Update to 0.6.0

* Thu Mar 14 2019 Orion Poplawski <orion@nwra.com> - 0.5.0-4
- Fix for python3 on EPEL

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 01 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.5.0-2
- Enable python dependency generator

* Mon Dec 31 2018 Orion Poplawski <orion@nwra.com> - 0.5.0-1
- Update to 0.5.0

* Mon Dec 3 2018 Orion Poplawski <orion@nwra.com> - 0.4.0-2
- Fix License
- Remove tab and fix permissions

* Fri Nov 30 2018 Orion Poplawski <orion@nwra.com> - 0.4.0-1
- Initial Fedora package
