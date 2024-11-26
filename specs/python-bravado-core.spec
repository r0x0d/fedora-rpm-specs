Name:           python-bravado-core
Version:        6.1.0
Release:        %autorelease
Summary:        Library for adding Swagger support to clients and servers

License:        BSD-3-Clause
URL:            https://github.com/Yelp/bravado-core
# PyPI tarball is missing tests
Source:         %{url}/archive/v%{version}/bravado-core-%{version}.tar.gz
# https://github.com/Yelp/bravado-core/pull/393
Patch:          0001-Use-standard-library-mock-when-possible.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
bravado-core is a Python library that adds client-side and server-side support
for the OpenAPI Specification v2.0.}


%description %_description


%package -n     python3-bravado-core
Summary:        %{summary}


%description -n python3-bravado-core %_description


%prep
%autosetup -n bravado-core-%{version} -p 1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l bravado_core


%check
# Recursive tests seem to hang forever, skip for now
# Profiling tests require pytest-benchmark[histogram], skip for now
%pytest -v \
    -k 'not recursive' \
    --ignore tests/profiling


%files -n python3-bravado-core -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
