%global pypi_name crick

Name:           python-%{pypi_name}
Version:        0.0.6
Release:        %{autorelease}
Summary:        High performance approximate and streaming algorithms

%global forgeurl https://github.com/dask/crick
%global tag %{version}
%forgemeta

# Apache-2.0 applies to `crick/tdigest_stubs.c`
License:        BSD-3-Clause AND Apache-2.0
URL:            %forgeurl
Source:         %forgesource

ExcludeArch:    %{ix86}
BuildRequires:  gcc
BuildRequires:  python3-devel
# Test dependencies
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(scipy)

%global _description %{expand:
Crick is a fast library of approximate and streaming algorithms. It is
still a work in progress, use at your own risk.}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%forgeautosetup -p1

# Don't install devel (.c, .h) files
# Also exclude test dir
# Sent upstream: https://github.com/dask/crick/pull/52
sed -r \
    -e 's/(include-package-data = )true/\1false/' \
    -e '/namespaces/a exclude = ["crick.tests*"]' \
    -i pyproject.toml


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%check
%pytest -v --import-mode importlib


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%license EXTERNAL_LICENSES


%changelog
%autochangelog