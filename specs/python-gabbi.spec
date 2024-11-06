%global pypi_name gabbi
%global pypi gabbi-run

%global with_docs 1

Name:           python-%{pypi_name}
Version:        3.0.0
Release:        %autorelease
Summary:        Declarative HTTP testing library

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/cdent/gabbi
Source0:        %pypi_source
BuildArch:      noarch

%description
Gabbi is a tool for running HTTP tests where requests and responses
are represented in a declarative YAML-based form.

%package -n python3-%{pypi_name}
Summary:        Declarative HTTP testing library

%description -n python3-%{pypi_name}
Gabbi is a tool for running HTTP tests where requests and responses
are represented in a declarative YAML-based form.

%if 0%{?with_doc}
%package -n python-%{pypi_name}-doc
Summary:        Documentation for the gabbi module

%description -n python-%{pypi_name}-doc
Documentation for the gabbi module
%endif

%prep
%autosetup -n %{pypi_name}-%{version}

sed -i 's/urllib3.*/urllib3/' requirements.txt

%generate_buildrequires
%if 0%{?with_doc}
  %pyproject_buildrequires -t -e %{default_toxenv},docs
%else
  %pyproject_buildrequires -t -e %{default_toxenv}
%endif

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%if 0%{?with_docs}
# generate html docs
%tox -e docs
sphinx-build -b man docs/source man
install -p -D -m 644 man/gabbi.1 %{buildroot}%{_mandir}/man1/gabbi.1
# remove the sphinx-build leftovers
rm -rf docs/build/html/.{doctrees,buildinfo}
%endif

%check
export GABBI_SKIP_NETWORK=true
%tox

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/%{pypi}
%{_mandir}/man1/gabbi.1*
%exclude %{python3_sitelib}/gabbi/tests/gabbits_intercept/horse

%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%doc docs/build/html
%license LICENSE
%endif

%changelog
%autochangelog
