%global pypi_name sport-activities-features

%bcond tests 1

# Run tests requiring network access, e.g. `mock --enable-network`.
# We cannot run these Koji builds.
%bcond network_tests 0

Name:           python-%{pypi_name}
Version:        0.5.0
Release:        %autorelease
Summary:        A minimalistic toolbox for extracting features from sports activity files

%global forgeurl https://github.com/firefly-cpp/sport-activities-features
%global tag %{version}
%forgemeta

# SPDX
License:        MIT
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist toml-adapt}
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
%endif

%global _description %{expand:
A minimalistic toolbox for extracting features from sport activity files
written in Python. Proposed software supports the extraction of following
topographic features from sport activity files: number of hills, average
altitude of identified hills, total distance of identified hills, climbing
ratio (total distance of identified hills vs. total distance), average ascent
of hills, total ascent, total descent and many others.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
%if !0%{?fc39} && !0%{?fc40}
Obsoletes:      python3-%{pypi_name}-tests < 0.4.2-1
%endif

%description -n python3-%{pypi_name} %_description

%if 0%{?fc39} || 0%{?fc40}
%package -n python3-%{pypi_name}-tests
Summary:        Tests for python3-%{pypi_name}

Requires:       python3-%{pypi_name} = %{version}-%{release}

%description -n python3-%{pypi_name}-tests
%{summary}.
%endif

%package doc
Summary:        Documentation and examples for %{name}
Requires:       python3-%{pypi_name} = %{version}-%{release}

%description doc
%{summary}.

%prep
%forgeautosetup -p1
rm -fv poetry.lock

#make dependencies consistent with Fedora versions
toml-adapt -path pyproject.toml -a change -dep ALL -ver X

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sport_activities_features

%check
%if %{with tests}
%if %{without network_tests}
# These tests require network access (e.g. to load topographical data).
k="${k-}${k+ and }not (TestMissingElevationIdentification and test_fetch_elevation_data_open_elevation_api)"
k="${k-}${k+ and }not (TestMissingElevationIdentification and test_fetch_elevation_data_open_topo_data_api)"
k="${k-}${k+ and }not (TestWeather and test_generated_object_altitudes)"
k="${k-}${k+ and }not (TestWeather and test_generated_object_properties)"
%endif
# This test *also* requires network access; however, even with network access,
# it fails with:
#
# E   ValueError: node array from the pickle has an incompatible dtype:
# E   - expected: {'names': ['left_child', 'right_child', 'feature',
#       'threshold', 'impurity', 'n_node_samples', 'weighted_n_node_samples',
#       'missing_go_to_left'], 'formats': ['<i8', '<i8', '<i8', '<f8', '<f8',
#       '<i8', '<f8', 'u1'], 'offsets': [0, 8, 16, 24, 32, 40, 48, 56],
#       'itemsize': 64}
# E   - got     : [('left_child', '<i8'), ('right_child', '<i8'), ('feature',
#       '<i8'), ('threshold', '<f8'), ('impurity', '<f8'), ('n_node_samples',
#       '<i8'), ('weighted_n_node_samples', '<f8')]
#
# sklearn/tree/_tree.pyx:1571: ValueError
#
# This seems to be an issue of not being able to load pipelines created with a
# significantly different version of scikit-learn.
k="${k-}${k+ and }not (TestDataAnalysis and test_load_pipeline)"
%pytest "${k:+-k $k}"
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md

%if 0%{?fc39} || 0%{?fc40}
%files -n python3-%{pypi_name}-tests
%doc tests/
%endif

%files doc
# Depends on base package, which provides the LICENSE file
%doc AUTHORS.rst
%doc CHANGELOG.md
%doc CITATION.cff
%doc CODE_OF_CONDUCT.md
%doc CONTRIBUTING.md
%doc docs/preprints/A_minimalistic_toolbox.pdf
%doc examples/

%changelog
%autochangelog
