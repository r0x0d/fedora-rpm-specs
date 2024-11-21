%global pypi_name trie
%global common_description %{expand:
Self-describing content-addressed identifiers for distributed systems
implementation in Python.}

Name:          python-%{pypi_name}
Version:       3.0.1
Release:       %autorelease
BuildArch:     noarch
Summary:       Library which implements the Ethereum Trie structure
License:       MIT
URL:           https://github.com/ethereum/py-trie
VCS:           git:%{url}.git
Source0:       %{pypi_source %pypi_name}
# PyuPi archive lacks tests-suite
Patch1:        python-trie-0001-Readd-tools.patch
Patch2:        python-trie-0002-Re-add-Trie-fixtures.patch
BuildRequires: python3-devel
BuildRequires: python3-hypothesis
BuildRequires: python3-pytest

%description %{common_description}

%package -n python3-%{pypi_name}
Summary: %{summary}

%description -n python3-%{pypi_name} %{common_description}

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

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
