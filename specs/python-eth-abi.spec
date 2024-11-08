%global pypi_name eth_abi

Name:          python-eth-abi
Version:       5.1.0
Release:       %autorelease
BuildArch:     noarch
Summary:       Python utilities for working with Ethereum ABI definitions
License:       MIT
URL:           https://github.com/ethereum/eth-abi
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
Patch1:        python-eth-abi-0001-Fix-four-tests.patch
BuildRequires: python3-devel
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest

%description
%{summary}.

%package -n python3-eth-abi
Summary: %{summary}

%description -n python3-eth-abi
%{summary}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
PYTHONPATH=$(pwd) %pytest

%files -n python3-eth-abi -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
