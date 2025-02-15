%global pypi_name cmarkgfm

Name:           python-%{pypi_name}
Version:        2024.1.14
Release:        %autorelease
Summary:        Minimal bindings to GitHub's fork of cmark

License:        MIT
URL:            https://github.com/jonparrott/cmarkgfm
Source0:        %{pypi_source}

BuildRequires:  gcc

%description
Bindings to GitHub's cmark Minimalist bindings to GitHub's fork of cmark.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-cffi
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Bindings to GitHub's cmark Minimalist bindings to GitHub's fork of cmark.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info
chmod -x README.rst LICENSE.txt

%build
%py3_build

%install
%py3_install

%check
%pytest -v tests

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitearch}/%{pypi_name}/
%{python3_sitearch}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
%autochangelog

