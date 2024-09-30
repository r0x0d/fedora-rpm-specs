Name:           python-importlib-resources
Version:        6.4.4
Release:        %autorelease
Summary:        Backport of the importlib.resources module

License:        Apache-2.0
URL:            https://github.com/python/importlib_resources
Source:         %{pypi_source importlib_resources}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
importlib_resources is a backport of Python standard library importlib.resources
module for older Pythons.

The key goal of this module is to replace parts of pkg_resources with a solution in
Python's stdlib that relies on well-defined APIs. This makes reading resources
included in packages easier, with more stable and consistent semantics.}

%description %_description

%package -n python3-importlib-resources
Summary:        %{summary}
%description -n python3-importlib-resources %_description


%prep
%autosetup -n importlib_resources-%{version}


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files importlib_resources


%check
%pytest


%files -n python3-importlib-resources -f %{pyproject_files}
%license LICENSE
%doc README.rst


%changelog
%autochangelog
