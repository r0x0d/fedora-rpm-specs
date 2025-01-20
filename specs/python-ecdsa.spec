%global srcname ecdsa

Name:           python-%{srcname}
Version:        0.19.0
Release:        4%{?dist}
Summary:        ECDSA cryptographic signature library

License:        MIT
URL:            https://pypi.python.org/pypi/ecdsa
Source0:        %{pypi_source ecdsa}

BuildArch:      noarch

BuildRequires:  python3-devel
# For tests
BuildRequires:  openssl
BuildRequires:  python3-pytest
BuildRequires:  python3-hypothesis
%if 0%{!?rhel}
# for better performance
BuildRequires:  python3-gmpy2
%endif

%description
This is an easy-to-use implementation of ECDSA cryptography (Elliptic Curve
Digital Signature Algorithm), implemented purely in Python, released under
the MIT license. With this library, you can quickly create keypairs (signing
key and verifying key), sign messages, and verify the signatures. The keys
and signatures are very short, making them easy to handle and incorporate
into other protocols.

%package -n python3-%{srcname}
Summary:        ECDSA cryptographic signature library

%description -n python3-%{srcname}
This is an easy-to-use implementation of ECDSA cryptography (Elliptic Curve
Digital Signature Algorithm), implemented purely in Python, released under
the MIT license. With this library, you can quickly create keypairs (signing
key and verifying key), sign messages, and verify the signatures. The keys
and signatures are very short, making them easy to handle and incorporate
into other protocols.


%prep
%autosetup -p1 -n %{srcname}-%{version}
# Remove extraneous #!
find src/ecdsa -name \*.py | xargs sed -ie '/\/usr\/bin\/env/d'

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}


%check
export OPENSSL_ENABLE_SHA1_SIGNATURES=yes
%pytest


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc NEWS README.md


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.19.0-2
- Rebuilt for Python 3.13

* Tue Apr 09 2024 Orion Poplawski <orion@nwra.com> - 0.19.0-1
- Update to 0.19.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.18.0-4
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.18.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 25 2022 Miro Hrončok <mhroncok@redhat.com> - 0.18.0-2
- In the tests, tighter the bounds for hypothesis parameters
- Fixes: rhbz#2137441

* Fri Aug 26 2022 Jonathan Wright <jonathan@almalinux.org> - 0.18.0-1
- update to 0.18.0
- rhbz#1873173

* Fri Aug 26 2022 Jonathan Wright <jonathan@almalinux.org> - 0.17.0-9
- improve performance with gmpy2

* Fri Aug 26 2022 Jonathan Wright <jonathan@almalinux.org> - 0.17.0-8
- modernize spec file

* Fri Aug 26 2022 Jonathan Wright <jonathan@almalinux.org> - 0.17.0-7
- remove python2-related code from spec

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.17.0-5
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.17.0-2
- Rebuilt for Python 3.10

* Sun May 30 2021 Orion Poplawski <orion@nwra.com> - 0.17.0-1
- Update to 0.17.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov 16 2020 Orion Poplawski <orion@nwra.com> - 0.16.1-1
- Update to 0.16.1

* Thu Aug 27 2020 Orion Poplawski <orion@nwra.com> - 0.16.0-1
- Update to 0.16.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.15-2
- Rebuilt for Python 3.9

* Thu Feb 27 2020 Orion Poplawski <orion@nwra.com> - 0.15-1
- Update to 0.15

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov  9 2019 Orion Poplawski <orion@nwra.com> - 0.14.1-1
- Update to 0.14.1

* Mon Oct  7 2019 Orion Poplawski <orion@nwra.com> - 0.13.3-1
- Update to 0.13.3 - CVE-2019-14853 (bugz #1758704)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.2-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.13.2-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 18 2019 Orion Poplawski <orion@nwra.com> - 0.13.2-1
- Update to 0.13.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 07 2018 Orion Poplawski <orion@cora.nwra.com> - 0.13-14
- Drop Python 2 package for Fedora 30+ (bugz #1631326)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.13-12
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.13-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 09 2017 Orion Poplawski <orion@nwra.com> - 0.13-9
- Modernize spec

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.13-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.13-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Apr 5 2016 Orion Poplawski <orion@cora.nwra.com> - 0.13-4
- Enable python3 builds for EPEL7

* Sat Feb 13 2016 Orion Poplawski <orion@cora.nwra.com> - 0.13-3
- Fix provide typo

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 14 2015 Orion Poplawski <orion@cora.nwra.com> - 0.13-1
- Update to 0.13
- Modernize spec

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 10 2014 Orion Poplawski <orion@cora.nwra.com> - 0.11-2
- Rebuild for Python 3.4

* Sat May 10 2014 Orion Poplawski <orion@cora.nwra.com> - 0.11-1
- Update to 0.11

* Mon Feb 24 2014 Orion Poplawski <orion@cora.nwra.com> - 0.10-3
- Add python3 package

* Mon Feb 24 2014 Orion Poplawski <orion@cora.nwra.com> - 0.10-2
- Use system python-six
- Remove extraneous #!s

* Fri Feb 21 2014 Orion Poplawski <orion@cora.nwra.com> - 0.10-1
- Initial package
