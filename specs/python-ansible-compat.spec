%global srcname ansible-compat
%global pkgname python-ansible-compat

%bcond_without tests

Name:    %{pkgname}
Version: 25.1.2
Release: %autorelease
Summary: Ansible python helper functions

URL:       https://github.com/ansible/ansible-compat
Source0:   %{url}/archive/refs/tags/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

License:   MIT
BuildArch: noarch

BuildRequires: pyproject-rpm-macros
BuildRequires: ansible-core

%if %{with tests}
BuildRequires: python3dist(flaky)
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pytest-mock)
%endif

%global common_description %{expand:
A python package containing functions that help interacting with
various versions of Ansible}

%description %{common_description}

%package -n python-%{srcname}-doc
Summary: %summary

%description -n python-%{srcname}-doc
Documentation for python-ansible-compat

%package -n python3-%{srcname}
Summary: %summary


%description -n python3-%{srcname} %{common_description}

%prep
%autosetup -p1 -n %{srcname}-%{version}
sed -i 's/--instafail//g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%if %{with doc}
PYTHONPATH=src sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%pyproject_save_files ansible_compat

%if %{with tests}
%check
%pytest -vv test -k \
    %{shrink:
        '
        not test_prepare_environment_with_collections
        and not test_prerun_reqs_v1
        and not test_prerun_reqs_v2
        and not test_install_collection_from_disk
        and not test_load_plugins
        and not test_require_collection
        and not test_install_collection
        and not test_install_collection_git
        and not test_runtime_example
        and not test_runtime_has_playbook
        and not test_runtime_plugins
        and not test_runtime_scan_path
        and not test_upgrade_collection
        '
    }
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE

%if %{with doc}
%files -n python-%{srcname}-doc
%license LICENSE
%doc *.rst
%doc html/
%endif

%changelog
%autochangelog
