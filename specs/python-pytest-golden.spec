Name:           python-pytest-golden
Version:        0.2.2
Release:        %autorelease
Summary:        Plugin for pytest that offloads expected outputs to data files

License:        MIT
URL:            https://github.com/oprypin/pytest-golden
# PyPI tarball doesn't include tests
Source:         %{url}/archive/v%{version}/pytest-golden-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  sed

%global _description %{expand:
This package provides a plugin for pytest that offloads expected outputs to
data files.}

%description %_description

%package -n     python3-pytest-golden
Summary:        %{summary}

%description -n python3-pytest-golden %_description

%prep
%autosetup -p1 -n pytest-golden-%{version}

# Relax version pin for testfixtures
sed -i 's:testfixtures = ".*:testfixtures = ">=6.15.0":' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L pytest_golden

%check
%pytest -v

%files -n python3-pytest-golden -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
%autochangelog
