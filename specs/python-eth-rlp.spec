%global pypi_name eth-rlp

Name:          python-%{pypi_name}
Version:       2.1.0
Release:       %autorelease
BuildArch:     noarch
Summary:       RLP definitions for common Ethereum objects in Python
License:       MIT
URL:           https://github.com/ethereum/eth-rlp
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
BuildRequires: python3-devel
BuildRequires: python3-pytest

%description
%{summary}.

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name}
%{summary}.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l eth_rlp

%check
%pyproject_check_import
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
