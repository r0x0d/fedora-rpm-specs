%global pypi_name pymdown-extensions

Name:           python-%{pypi_name}
Version:        10.12
Release:        %autorelease
Summary:        Extension pack for Python Markdown

# Most of the package is MIT except two files (highlight.py and superfences.py)
License:        MIT and BSD-2-Clause
URL:            https://facelessuser.github.io/pymdown-extensions
Source:         %{pypi_source pymdown_extensions}

BuildArch:      noarch
 
%description
PyMdown Extensions (pymdownx) is a collection of extensions for Python
Markdown.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
# Needed for the tests to pass
BuildRequires:  python3-pygments >= 2.18.0

%description -n python3-%{pypi_name}
PyMdown Extensions (pymdownx) is a collection of extensions for Python
Markdown.

%pyproject_extras_subpkg -n python3-pymdown-extensions extra

%prep
%autosetup -n pymdown_extensions-%{version} -p1

# Drop invalid entry that breaks the pyproject macros
sed -i '/\.\[extra\]/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -t -x extra

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pymdownx

%check
%tox

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
%autochangelog
