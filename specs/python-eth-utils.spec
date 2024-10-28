%global pypi_name eth_utils

Name:          python-eth-utils
Version:       5.0.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Utility functions for working with Ethereum related codebases
License:       MIT
URL:           https://github.com/ethereum/eth-utils
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
Patch1:        python-eth-utils-0001-Disable-this-test-we-don-t-have-internet-access-anyw.patch
BuildRequires: python3-devel
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest

%description
%{summary}.

%package -n python3-eth-utils
Summary: %{summary}

%description -n python3-eth-utils
%{summary}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# We don't have mypy fixtures anyway
rm -rf ./tests/core/functional-utils/test_type_inference.py
# Remove egg-info
rm -rf %{pypi_name}.egg-info/

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
%pytest

%files -n python3-eth-utils -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
