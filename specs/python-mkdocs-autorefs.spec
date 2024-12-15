%bcond tests 1

Name:           python-mkdocs-autorefs
Version:        1.2.0
Release:        %autorelease
Summary:        Automatically link across pages in MkDocs.

License:        ISC
URL:            https://mkdocstrings.github.io/autorefs
Source:         %{pypi_source mkdocs_autorefs}
# Fix test_reference_implicit_with_code_inlinehilite_python
Patch:          https://github.com/mkdocstrings/autorefs/pull/60.patch

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3dist(pymdown-extensions)
BuildRequires:  python3dist(pytest)
%endif

%global _description %{expand:
This package provides a plugin to automatically link across pages in MkDocs.}

%description %_description

%package -n     python3-mkdocs-autorefs
Summary:        %{summary}

%description -n python3-mkdocs-autorefs %_description

%prep
%autosetup -p1 -n mkdocs_autorefs-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L mkdocs_autorefs

%check
%if %{with tests}
%pytest -v
%else
%pyproject_check_import
%endif

%files -n python3-mkdocs-autorefs -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md

%changelog
%autochangelog
