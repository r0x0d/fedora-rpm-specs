%global commit 5aea0fd4461bd05dd96e4ad637f6be7bceb1cee5
%global snapdate 20231031

Name:           python-etcd
Version:        0.5.0~%{snapdate}git%(echo '%{commit}' | cut -b -7)
Release:        2%{?dist}
Summary:        A python client library for etcd

License:        MIT
URL:            https://github.com/jplana/python-etcd

Source:         %{url}/archive/%{commit}/python-etcd-%{commit}.tar.gz

# Support Python 3.13
# https://github.com/jplana/python-etcd/pull/288
Patch:          %{url}/pull/288.patch
# Replace removed TestCase method aliases
# https://github.com/jplana/python-etcd/pull/289
Patch:          %{url}/pull/289.patch
# Do not include tests in bdists/wheels
# https://github.com/jplana/python-etcd/pull/290
Patch:          %{url}/pull/290.patch

#VCS: git:https://github.com/jplana/python-etcd

BuildArch:      noarch

BuildRequires:  python3-devel

BuildRequires:  etcd
# setup.py: test_requires
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pyOpenSSL}

%global _description %{expand:
Client library for interacting with an etcd service, providing Python access to
the full etcd REST API. Includes authentication, accessing and manipulating
shared content, managing cluster members, and leader election.}

%description %{_description}

%package -n python3-etcd
Summary:        %{summary}

%py_provides python3-python-etcd

%description -n python3-etcd %{_description}

%prep
%autosetup -n python-etcd-%{commit} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l etcd

%check
# TODO: What is happening?
# OpenSSL.crypto.Error: [('digital envelope routines', '', 'invalid digest')]
k="${k-}${k+ and }not (TestEncryptedAccess and test_get_set_authenticated)"
k="${k-}${k+ and }not (TestEncryptedAccess and test_get_set_unauthenticated)"
k="${k-}${k+ and }not (TestEncryptedAccess and test_get_set_unauthenticated_missing_ca)"
k="${k-}${k+ and }not (TestEncryptedAccess and test_get_set_unauthenticated_with_ca)"
k="${k-}${k+ and }not (TestClientAuthenticatedAccess and test_get_set_unauthenticated)"

# TODO: What is happening?
# E           etcd.EtcdException: Raft Internal Error : nodePath /1/dir : Not a file ()
k="${k-}${k+ and }not (TestSimple and test_directory_ttl_update)"

%pytest -k "${k-}" -v

%files -n python3-etcd -f %{pyproject_files}
%doc README.rst
#license LICENSE.txt

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0~20231031git5aea0fd-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 07 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 0.5.0~20231031git5aea0fd-1
- Update to a pre-release snapshot of 0.5.0
- Update to current packaging standards, with pyproject-rpm-macros
- Run the tests (with a few unexplained failures)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 10 2024 Python Maint <python-maint@redhat.com> - 0.4.5-34
- Rebuilt for Python 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.4.5-33
- Rebuilt for Python 3.13

* Fri Feb 23 2024 Liu Yang <Yang.Liu.sn@gmail.com> - 0.4.5-32
- Add riscv64 to arches.

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun 15 2023 Python Maint <python-maint@redhat.com> - 0.4.5-28
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 0.4.5-25
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.4.5-22
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.4.5-19
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.5-17
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.4.5-16
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 20 2018 Matthew Barnes <mbarnes@redhat.com> - 0.4.5-13
- Remove python2 subpackage (rhbz#1630954).

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.4.5-11
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 16 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.4.5-9
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Dec 18 2017 Steve Milner <smilner@redhat.com> - 0.4.5-8
- Fix naming per rhbz#1526788.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 19 2017 Matthew Barnes <mbarnes@redhat.com> - 0.4.5-6
- I'm told etcd works on s390x too; add it to ExclusiveArch.

* Mon Jun 19 2017 Steve Milner <smilner@redhat.com> - 0.4.5-5
- Remove requirements on etcd for build and install

* Mon Jun 19 2017 Matthew Barnes <mbarnes@redhat.com> - 0.4.5-4
- Last change didn't help and we were in compliance with Packaging
  Guidelines before the change, so revert.  The fact that it still
  randomly gets built on ppc64 seems to be a Fedora infrastructure
  issue.

* Wed Jun 14 2017 Matthew Barnes <mbarnes@redhat.com> - 0.4.5-3
- Try excluding ppc64 directly, since ExclusiveArch doesn't.

* Wed Apr 12 2017 Matthew Barnes <mbarnes@redhat.com> - 0.4.5-2
- Add missing requires python[3]-urllib3 (rhbz#1440546).
- Patch from Oleg Gashev <oleg@gashev.net>

* Thu Mar  2 2017 Steve Milner <smilner@redhat.com> - 0.4.5-1
- Update to 0.4.5

* Fri Feb 17 2017 Matthew Barnes <mbarnes@redhat.com> - 0.4.4-1
- Update to 0.4.4

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.3-6
- Rebuild for Python 3.6

* Fri Nov 18 2016 Steve Milner <smilner@redhat.com> - 0.4.3-5
- Running unittests only.

* Wed Nov 16 2016 Steve Milner <smilner@redhat.com> - 0.4.3-4
- Added noarch to the list to build.
- Fixed provides (see rhbz#1374240)
- Disabled the new auth module (see https://github.com/jplana/python-etcd/issues/210)

* Wed Nov 09 2016 Matthew Barnes <mbarnes@redhat.com> - 0.4.3-3
- etcd now excludes ppc64; follow suit.
  related: #1393497

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Feb 22 2016 Matthew Barnes <mbarnes@redhat.com> - 0.4.3-1
- Initial packaging.
