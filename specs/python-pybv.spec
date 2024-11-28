Name:           python-pybv
Version:        0.7.6
Release:        %autorelease
Summary:        A lightweight I/O utility for the BrainVision data format

License:        BSD-3-Clause
URL:            https://pybv.readthedocs.io/en/stable/
# A filtered source archive, obtained by (see Source1):
#
#   ./get_source %%{version}
#
# is required because specification/ contains a PDF file,
# BrainVisionCoreDataFormat_1-0.pdf, with unclear license terms.
#
# The unfiltered base source URL would be:
#
# https://github.com/bids-standard/pybv/archive/v%%{version}/pybv-%%{version}.tar.gz
#
# We have asked upstream to stop distributing the specification/ directory in
# PyPI sdists: https://github.com/bids-standard/pybv/pull/106
#
# However, we still must package from GitHub if we want to run the tests, since
# the sdist does not contain tests.
Source0:        pybv-%{version}-filtered.tar.zst
Source1:        get_source

BuildSystem:            pyproject
BuildOption(install):   -l pybv

BuildArch:      noarch
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel

# For tests; see the test extra, but it has linters, coverage tools, and other
# unwanted dev dependencies mixed in, so we list these manually.
BuildRequires:  %{py3_dist matplotlib}
BuildRequires:  %{py3_dist mne}
BuildRequires:  %{py3_dist pytest}

%global common_description %{expand:
pybv is a lightweight I/O utility for the BrainVision data format.

The BrainVision data format is a recommended data format for use in the Brain
Imaging Data Structure.}

%description %{common_description}


%package -n python3-pybv
Summary:        %{summary}

# The export extra was removed in 0.7.6 for Fedora 42; we can remove the
# following line after Fedora 44 reaches end-of-life.
Obsoletes:      python3-pybv+export < 0.7.6-1
# We stopped building PDF documentation for Fedora 42; we can remove the
# following line after Fedora 44 reaches end-of-life.
Obsoletes:      python-pybv-doc < 0.7.6-2

%description -n python3-pybv %{common_description}


%prep -a
# Patch out options for pytest-cov:
sed -r -i 's/--cov[^[:blank:]]+//g' pyproject.toml


%generate_buildrequires -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'


%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'


%check -a
PYTHONPATH="${PWD}" %pytest --ignore=docs


%files -n python3-pybv -f %{pyproject_files}
%doc CITATION.cff
%doc README.rst
%doc docs/changelog.rst


%changelog
%autochangelog
