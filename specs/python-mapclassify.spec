%global srcname mapclassify

Name:           python-%{srcname}
Version:        2.8.1
Release:        %autorelease
Summary:        Classification Schemes for Choropleth Maps

License:        BSD-3-Clause
URL:            https://github.com/pysal/mapclassify
Source:         %pypi_source %{srcname}
# Don't use the network.
Patch:          0001-Use-system-copy-of-Natural-Earth-data.patch

BuildArch:      noarch

BuildRequires:  python3-devel

# Tests
BuildRequires:  natural-earth-map-data-110m

%description
mapclassify is an open-source python library for Choropleth map classification.
It is part of PySAL the Python Spatial Analysis Library.


%package -n     python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname}
mapclassify is an open-source python library for Choropleth map classification.
It is part of PySAL the Python Spatial Analysis Library.


%prep
%autosetup -n %{srcname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires -x tests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{pytest} --mpl

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
