%bcond tests 1

Name:           mkdocs-bootstrap
Version:        1.1.1
Release:        %autorelease
Summary:        Bootstrap theme for MkDocs

License:        BSD-2-Clause
URL:            http://mkdocs.github.io/mkdocs-bootstrap/
Source:         %{pypi_source mkdocs-bootstrap}

BuildArch:      noarch
BuildRequires:  python3-devel

%description
%{summary}.

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mkdocs_bootstrap

%check
%pyproject_check_import

%if %{with tests}
export PYTHONPATH=%{buildroot}/%{python3_sitelib}
mkdocs new testing
pushd testing
mkdocs build --theme bootstrap
popd
%endif

%files -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
