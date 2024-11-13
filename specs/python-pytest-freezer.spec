Name:           python-pytest-freezer
Version:        0.4.8
Release:        %autorelease
Summary:        Pytest plugin providing a fixture interface for freezegun

# SPDX
License:        MIT
URL:            https://github.com/pytest-dev/pytest-freezer
Source:         %{pypi_source pytest_freezer}

BuildArch:      noarch
 
BuildRequires:  python3-devel

BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n     python3-pytest-freezer
Summary:        %{summary}

%description -n python3-pytest-freezer %{common_description}


%prep
%autosetup -p1 -n pytest_freezer-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L pytest_freezer


%check
%pytest -v


%files -n python3-pytest-freezer -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
%autochangelog
