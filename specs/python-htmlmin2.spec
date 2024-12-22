Name:           python-htmlmin2
Version:        0.1.13
Release:        %autorelease
Summary:        Configurable HTML Minifier with safety features

License:        BSD-3-Clause AND Python-2.0.1
URL:            https://github.com/wilhelmer/htmlmin
Source:         %{url}/archive/v%{version}/htmlmin-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

# Vendored and modified copy of Lib/html/parser.py from cpython under
# htmlmin/python3html
# License: Python-2.0.1
Provides:       bundled(cpython) = 3.6

%global _description %{expand:
This package provides a configurable HTML Minifier with safety features. This
is a fork of htmlmin.}

%description %_description

%package -n     python3-htmlmin2
Summary:        %{summary}

%description -n python3-htmlmin2 %_description

%prep
%autosetup -p1 -n htmlmin-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l htmlmin

%check
%pytest -v

%files -n python3-htmlmin2 -f %{pyproject_files}
%doc README.rst CHANGELOG
%{_bindir}/htmlmin

%changelog
%autochangelog
