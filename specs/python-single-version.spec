%global         srcname         single-version
%global         forgeurl        https://github.com/hongquan/single-version
Version:        1.6.0
%global         tag             v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Utility to define version string

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}


BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildArch: noarch

%global _description %{expand:
Utility to let you have a single source version in your code base.

This utility targets modern Python projects which have layout generated
by Poetry, with a pyproject.toml file in place of setup.py.  With this
layout, the project initially has two places to maintain the version
string: one in pyproject.toml and one in some *.py file (normally
 __init__.py).  This duplicity often leads to inconsistency when you the
author forget to update both.

single-version was born to solve that headache circumstance.  By convention,
it chooses the pyproject.toml file as original source of version string.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%forgeautosetup
# Add license file to metadata once get poetry 1.9
# https://github.com/hongquan/single-version/pull/5
#sed -i 's/license = "MIT"/License-Expression = MIT/g' pyproject.toml
#sed -i '/License-Expression = MIT/a License-File = LICENSE\\n/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files single_version -L

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
