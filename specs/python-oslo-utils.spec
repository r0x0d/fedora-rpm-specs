%{!?sources_gpg: %{!?dlrn:%global sources_gpg 1} }
%global sources_gpg_sign 0xf8675126e2411e7748dd46662fc2093e4682645f
%global pypi_name oslo.utils
%global pkg_name oslo-utils
%global with_doc 1

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
# we are excluding some BRs from automatic generator
%global excluded_brs doc8 bandit pre-commit hacking flake8-import-order
# Exclude sphinx from BRs if docs are disabled
%if ! 0%{?with_doc}
%global excluded_brs %{excluded_brs} sphinx openstackdocstheme
%endif
# Exclude some BRs for Fedora
%if 0%{?fedora}
%global excluded_brs %{excluded_brs} eventlet
%endif

%global common_desc \
The OpenStack Oslo Utility library. \
* Documentation: http://docs.openstack.org/developer/oslo.utils \
* Source: http://git.openstack.org/cgit/openstack/oslo.utils \
* Bugs: http://bugs.launchpad.net/oslo

%global common_desc_tests Tests for the Oslo Utility library.

Name:           python-oslo-utils
Version:        7.3.0
Release:        2%{?dist}
Summary:        OpenStack Oslo Utility library

License:        Apache-2.0
URL:            http://launchpad.net/oslo
Source0:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
Source101:        https://tarballs.openstack.org/%{pypi_name}/%{pypi_name}-%{upstream_version}.tar.gz.asc
Source102:        https://releases.openstack.org/_static/%{sources_gpg_sign}.txt
%endif
BuildArch:      noarch

# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
BuildRequires:  /usr/bin/gpgv2
%endif

BuildRequires:  git-core

%description
%{common_desc}

%package -n python3-%{pkg_name}
Summary:    OpenStack Oslo Utility library

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  qemu-img

Requires:       python-%{pkg_name}-lang = %{version}-%{release}

%description -n python3-%{pkg_name}
%{common_desc}

%if 0%{?with_doc}
%package -n python-%{pkg_name}-doc
Summary:    Documentation for the Oslo Utility library

%description -n python-%{pkg_name}-doc
Documentation for the Oslo Utility library.
%endif

%package -n python3-%{pkg_name}-tests
Summary:    Tests for the Oslo Utility library

Requires: python3-%{pkg_name} = %{version}-%{release}
%if ! 0%{?fedora}
Requires: python3-eventlet
%endif
Requires: python3-hacking
Requires: python3-fixtures
Requires: python3-oslotest
Requires: python3-testtools
Requires: python3-ddt
Requires: python3-testscenarios

%description -n python3-%{pkg_name}-tests
%{common_desc_tests}

%package  -n python-%{pkg_name}-lang
Summary:   Translation files for Oslo utils library

%description -n python-%{pkg_name}-lang
Translation files for Oslo utils library

%prep
# Required for tarball sources verification
%if 0%{?sources_gpg} == 1
%{gpgverify}  --keyring=%{SOURCE102} --signature=%{SOURCE101} --data=%{SOURCE0}
%endif
%autosetup -n %{pypi_name}-%{upstream_version} -S git


sed -i /^[[:space:]]*-c{env:.*_CONSTRAINTS_FILE.*/d tox.ini
sed -i "s/^deps = -c{env:.*_CONSTRAINTS_FILE.*/deps =/" tox.ini
sed -i /^minversion.*/d tox.ini
sed -i /^requires.*virtualenv.*/d tox.ini
# we consume pytz from AppStream repo instead of tzdata
sed -i 's/tzdata.*/pytz/' requirements.txt

# Exclude some bad-known BRs
for pkg in %{excluded_brs};do
  for reqfile in doc/requirements.txt test-requirements.txt; do
    if [ -f $reqfile ]; then
      sed -i /^${pkg}.*/d $reqfile
    fi
  done
done

%generate_buildrequires
%if 0%{?with_doc}
  %pyproject_buildrequires -t -e %{default_toxenv},docs
%else
  %pyproject_buildrequires -t -e %{default_toxenv}
%endif

%build
%pyproject_wheel

%if 0%{?with_doc}
# generate html docs
%tox -e docs
# remove the sphinx-build-3 leftovers
rm -rf doc/build/html/.{doctrees,buildinfo} doc/build/html/objects.inv
%endif


%install
%pyproject_install

# Generate i18n files
python3 setup.py compile_catalog -d %{buildroot}%{python3_sitelib}/oslo_utils/locale --domain oslo_utils


# Install i18n .mo files (.po and .pot are not required)
install -d -m 755 %{buildroot}%{_datadir}
rm -f %{buildroot}%{python3_sitelib}/oslo_utils/locale/*/LC_*/oslo_utils*po
rm -f %{buildroot}%{python3_sitelib}/oslo_utils/locale/*pot
mv %{buildroot}%{python3_sitelib}/oslo_utils/locale %{buildroot}%{_datadir}/locale

# Find language files
%find_lang oslo_utils --all-name

%check
%if 0%{?fedora}
# eventlet is not yet supported on python 3.13 and it's not used in openstack clients
rm oslo_utils/tests/test_eventletutils.py
%endif
%tox -e %{default_toxenv} -- -- --exclude-regex '(oslo_utils.tests.test_netutils.NetworkUtilsTest.test_is_valid_ip)'

%files -n python3-%{pkg_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/oslo_utils
%{python3_sitelib}/*.dist-info
%exclude %{python3_sitelib}/oslo_utils/tests

%if 0%{?with_doc}
%files -n python-%{pkg_name}-doc
%doc doc/build/html
%license LICENSE
%endif

%files -n python3-%{pkg_name}-tests
%{python3_sitelib}/oslo_utils/tests

%files -n python-%{pkg_name}-lang -f oslo_utils.lang
%license LICENSE

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 08 2024 Joel Capitao <jcapitao@redhat.com> 7.3.0-1
- Update to upstream version 7.3.0

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 08 2024 Alfredo Moralejo <amoralej@redhat.com> 7.1.0-2
- Remove eventlet as BR

* Mon May 06 2024 Alfredo Moralejo <amoralej@redhat.com> 7.1.0-1
- Update to upstream version 7.1.0

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 26 2023 Alfredo Moralejo <amoralej@gmail.com> 6.2.1-1
- Update to upstream version 6.2.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 6.1.0-2
- Rebuilt for Python 3.12

* Fri Apr 14 2023 Karolina Kula <kkula@redhat.com> 6.1.0-1
- Update to upstream version 6.1.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 17 2022 Alfredo Moralejo <amoralej@redhat.com> 6.0.1-1
- Update to upstream version 6.0.1

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 4.12.2-3
- Rebuilt for pyparsing-3.0.9

* Thu Jun 16 2022 Python Maint <python-maint@redhat.com> - 4.12.2-2
- Rebuilt for Python 3.11

* Thu May 19 2022 Joel Capitao <jcapitao@redhat.com> 4.12.2-1
- Update to upstream version 4.12.2

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 4.8.0-2
- Rebuilt for Python 3.10

* Mon Mar 22 2021 Joel Capitao <jcapitao@redhat.com> 4.8.0-1
- Update to upstream version 4.8.0

* Wed Feb 10 2021 Charalampos Stratakis <cstratak@redhat.com> - 4.6.0-4
- Remove redundant python-funcsigs depdendency

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 21 2020 Joel Capitao <jcapitao@redhat.com> 4.6.0-2
- Enable sources tarball validation using GPG signature.

* Thu Sep 17 2020 RDO <dev@lists.rdoproject.org> 4.6.0-1
- Update to 4.6.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 10 2020 Joel Capitao <jcapitao@redhat.com> 4.1.1-1
- Update to upstream version 4.1.1

* Mon Jun 01 2020 Javier Peña <jpena@redhat.com> - 3.41.1-5
- Remove python-hacking from requirements, it is not actually needed for the build

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.41.1-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.41.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 07 2019 Alfredo Moralejo <amoralej@redhat.com> 3.41.1-2
- Update to upstream version 3.41.1

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.40.3-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 21 2019 Alfredo Moralejo <amoralej@redhat.com> 3.40.3-4
- Add digestmod when using hmac - Resolves rhbz#1743899
- Disabled failing unit test with python 3.8.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.40.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.40.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 08 2019 RDO <dev@lists.rdoproject.org> 3.40.3-1
- Update to 3.40.3

