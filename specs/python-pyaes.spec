%global pypi_name pyaes
%global common_description %{expand:
A pure-Python implementation of the AES block cipher algorithm and the common
modes of operation (CBC, CFB, CTR, ECB and OFB).}

Name:       python-%{pypi_name}
Version:    1.6.1
Release:    %autorelease
Summary:    Pure-Python implementation of AES block-cipher and common modes of operation
License:    MIT
URL:        https://github.com/ricmoo/%{pypi_name}
VCS:        git:%{url}.git
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:     python-pyaes-0001-Use-relative-imports-during-tests.patch
Patch2:     51.patch
BuildArch:  noarch
BuildRequires: python3-devel
BuildRequires: python3dist(pycrypto)

%description %{common_description}

%package -n python3-%{pypi_name}
Summary:  %{summary}

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
%{__python3} tests/test-aes.py
%{__python3} tests/test-blockfeeder.py
%{__python3} tests/test-util.py

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog