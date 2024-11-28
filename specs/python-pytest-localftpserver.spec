%global pypi_name pytest-localftpserver

Name:           python-%{pypi_name}
Version:        1.3.2
Release:        %{autorelease}
Summary:        A PyTest plugin which provides an FTP fixture for your tests

%global forgeurl https://github.com/oz123/pytest-localftpserver
%forgemeta

# SPDX
License:        MIT
URL:            https://pytest-localftpserver.readthedocs.io/
Source:         %forgesource

# Avoid the multiprocessing forkserver method
# https://github.com/oz123/pytest-localftpserver/pull/351
#
# Fixes:
#
# python-pytest-localftpserver fails to build with Python 3.14: multiprocessing
# has changed the start method to 'forkserver'
# https://bugzilla.redhat.com/show_bug.cgi?id=2328701
Patch:          %{forgeurl}/pull/351.patch

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3dist(cryptography)

%global _description %{expand:
A PyTest plugin which provides an FTP fixture for your tests.

Documentation: https://pytest-localftpserver.readthedocs.io/}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%forgeautosetup -p1

# Remove shebang
sed -i '/env python/ d' pytest_localftpserver/plugin.py


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=v%{version}
%pyproject_buildrequires


%build
export SETUPTOOLS_SCM_PRETEND_VERSION=v%{version}
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l pytest_localftpserver


%check
%pytest -v \
  tests/test_pytest_localftpserver.py \
  tests/test_helper_functions.py


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst AUTHORS.rst HISTORY.rst


%changelog
%autochangelog
