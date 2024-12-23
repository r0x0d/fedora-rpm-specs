# Tests depend on specific versions of the underlying dependencies
%bcond tests 0

Name:           python-mkdocs-minify-plugin
Version:        0.8.0
Release:        %autorelease
Summary:        MkDocs plugin to minify HTML, JS or CSS files

License:        MIT
URL:            https://github.com/byrnereese/mkdocs-minify-plugin
# PyPI tarball doesn't include tests
Source:         %{url}/archive/%{version}/mkdocs-minify-plugin-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{with tests}
BuildRequires:  python3-pytest
%endif

%global _description %{expand:
This package provides an MkDocs plugin to minify HTML, JS or CSS files prior to
being written to disk. HTML minification is done using htmlmin2. JS
minification is done using jsmin. CSS minification is done using
csscompressor.}

%description %_description

%package -n     python3-mkdocs-minify-plugin
Summary:        %{summary}

%description -n python3-mkdocs-minify-plugin %_description

%prep
%autosetup -p1 -n mkdocs-minify-plugin-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mkdocs_minify_plugin

%check
%if %{with tests}
%pytest -v
%else
%pyproject_check_import
%endif

%files -n python3-mkdocs-minify-plugin -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
