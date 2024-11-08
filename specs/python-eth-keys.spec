%global pypi_name eth_keys

Name:          python-eth-keys
Version:       0.6.0
Release:       %autorelease
BuildArch:     noarch
Summary:       A common API for Ethereum key operations
License:       MIT
URL:           https://github.com/ethereum/eth-keys
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
BuildRequires: python3-asn1tools
BuildRequires: python3-coincurve
BuildRequires: python3-devel
BuildRequires: python3-factory-boy
BuildRequires: python3-hypothesis
BuildRequires: python3-pyasn1
BuildRequires: python3-pytest

%description
%{summary}.

%package -n python3-eth-keys
Summary: %{summary}

%description -n python3-eth-keys
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
%pytest

%files -n python3-eth-keys -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
