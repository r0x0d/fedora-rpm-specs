#global commit  f44636f00666b8eb869417960926d01690ff4f42
#global shortcommit #(c=#{commit}; echo ${c:0:7})
#global checkout_date 2023094
%global upstream_version  1.9.0

# setup.py does not list all requirements, and we also unbundle quite a few
# from the externals folder, so we can't only rely on the automatic generator
# here.
# Additionally, requirements.txt seems to be dev requirements, and is not used
# in setup.py for install_requires.

Name:           python-mne

%if "0%{?commit}" != "0"
Version:        %{upstream_version}^%{checkout_date}git%{shortcommit}
%global python_version  %{upstream_version}.dev%{checkout_date}
%else
Version:        %{upstream_version}
%global python_version  %{version}
%endif

Release:        %autorelease
Summary:        Magnetoencephalography (MEG) and Electroencephalography (EEG) data analysis

# Bundled FieldTrip
# https://github.com/fieldtrip/fieldtrip/blob/master/realtime/src/buffer/python/FieldTrip.py
# Not possible to package because it is matlab package with some plugins

# SPDX
License:        BSD-3-Clause
URL:            http://mne.tools/


%if "0%{?commit}" != "0"
Source0:        https://github.com/mne-tools/mne-python/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0:        https://github.com/mne-tools/mne-python/archive/v%{version}/%{name}-%{version}.tar.gz
%endif

#Source1:        https://s3.amazonaws.com/mne-python/datasets/MNE-sample-data-processed.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# The base package is arched to make it easier for us to detect arch-dependent
# test failures, since the tests will always be run on every platform, and
# easier for us to skip failing tests if necessary, since we can be sure that
# %%ifarch macros work as expected.
#
# Since the package still contains no compiled machine code, we still have no
# debuginfo.
%global debug_package %{nil}

BuildRequires:  python3-devel

%global _description %{expand:
This package is designed for sensor- and source-space analysis of M-EEG data,
including frequency-domain and time-frequency analyses and non-parametric
statistics.}

%description %_description

%package -n python3-mne
Summary:        %{summary}

# This package is now arched because some dependencies are not available on
# every architecture.

Provides:       bundled(bootstrap)
Provides:       bundled(js-jquery)
Provides:       bundled(js-jquery-ui)
Provides:       bundled(js-d3)
Provides:       bundled(js-mpld3)
Provides:       bundled(python3-FieldTrip)
BuildRequires:  python3-setuptools
BuildRequires:  python3-numpy
BuildRequires:  python3-scipy

# Test deps
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-qt
BuildRequires:  python3-pytest-timeout
# We could run the tests in parallel by uncommenting this and adding "-n auto"
# to the pytest arguments. However, the algorithms are highly parallelized, so
# they already use many-core systems well. Running multiple tests in parallel
# actually greatly increases the time required – from about five to 32 minutes
# in a test on a 16-core system – presumably due to increased contention.
# BuildRequires:  python3-pytest-xdist
BuildRequires:  python3-matplotlib
BuildRequires:  python3-pandas
BuildRequires:  python3-h5py
BuildRequires:  python3-decorator
%ifnarch s390x
# https://bugzilla.redhat.com/show_bug.cgi?id=2116690
BuildRequires:  python3-pymatreader
%endif
BuildRequires:  python3-h5io
BuildRequires:  python3-jinja2
BuildRequires:  python3-scikit-learn
BuildRequires:  python3-Traits
BuildRequires:  python3-tqdm
BuildRequires:  python3-nibabel
%ifnarch s390x
BuildRequires:  python3-pyedflib
%endif
BuildRequires:  python3-nilearn
BuildRequires:  python3-qt5
BuildRequires:  python3-dipy
BuildRequires:  python3-xlrd
BuildRequires:  python3-nitime
BuildRequires:  python3-pooch
BuildRequires:  python3-nbformat
BuildRequires:  python3-vtk
# Makes pytest segfault
# BuildRequires:  python3-mayavi
# Currently in procps-ng, but let’s not assume:
BuildRequires:  /usr/bin/free

Requires:       python3-matplotlib
Requires:       python3-decorator
Requires:       python3-h5io
Requires:       python3-six
Requires:       python3-tempita
Requires:       python3-tqdm
%ifnarch s390x
Requires:       python3-pymatreader
%endif
Recommends:     python3-scikit-learn
Recommends:     python3-pandas
Recommends:     python3-patsy
Recommends:     python3-pillow
Recommends:     python3-h5py
Recommends:     python3-statsmodels
Recommends:     python3-Traits

# Should be included by the dep generator as they're mentioned in setup.py
# Requires:       python3-numpy
# Requires:       python3-scipy

%description -n python3-mne %_description

%prep
%if "0%{?commit}" != "0"
%autosetup -n mne-python-%{commit} -p1
%else
%autosetup -n mne-python-%{version} -p1
%endif

# fix non-executable scripts
sed -i -e '1{\@^#!/usr/bin/env python@d}' mne/commands/*.py
sed -i -e '1{\@^#!/usr/bin/env python@d}' mne/datasets/hf_sef/hf_sef.py
sed -i -e '1{\@^#!/usr/bin/env python@d}' mne/stats/cluster_level.py

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r -i 's/--cov[^[:blank:]]+//g' pyproject.toml


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION='%{python_version}'
%pyproject_buildrequires

#cp -p %{SOURCE1} .
#python -c "import mne; mne.datasets.sample.data_path(verbose=True, download=False)"

%build
export SETUPTOOLS_SCM_PRETEND_VERSION='%{python_version}'
%pyproject_wheel

%install
export SETUPTOOLS_SCM_PRETEND_VERSION='%{python_version}'
%pyproject_install
%pyproject_save_files -l mne

%check
export SETUPTOOLS_SCM_PRETEND_VERSION='%{python_version}'
export MNE_SKIP_TESTING_DATASET_TESTS=true
export MNE_SKIP_NETWORK_TESTS=1
export MNE_DONTWRITE_HOME=true
export MNE_FORCE_SERIAL=true

# required for some tests
mkdir subjects

# Docstrings differ from expected in Python 3.13 due to “Automatically dedent
# docstring constants by default”
# https://github.com/python/cpython/issues/81283.
# https://github.com/mne-tools/mne-python/issues/13013
k="${k-}${k+ and }not copy_doc"
k="${k-}${k+ and }not docs.copy_function_doc_to_method_doc"
k="${k-}${k+ and }not test_copy_function_doc_to_method_doc"

# Fails on F40 (didn't investigate)
# Failed: DID NOT WARN. No warnings of type (<class 'RuntimeWarning'>,) were emitted.
# The list of emitted warnings is: [].
%if %{defined fc40}
k="${k-}${k+ and }not test_brainvision_data_software_filters_latin1_global_units"
k="${k-}${k+ and }not test_brainvision_vectorized_data"
k="${k-}${k+ and }not test_ica_simple[fastica]"
k="${k-}${k+ and }not test_fit_sphere_to_headshape"
k="${k-}${k+ and }not test_compute_whitener_rank"
%endif

# Test segfaults intermittently
k="${k-}${k+ and }not test_plotting_scalebars[matplotlib]"
# Flaky (DID NOT RAISE <class 'numpy.linalg.LinAlgError'>)
k="${k-}${k+ and }not test_regularized_csp[None-full-eeg]"
%ifarch aarch64
# Flaky (Aborted)
k="${k-}${k+ and }not test_save_complex_data[single-2e-06-True-True]"
%endif
# Flaky (AssertionError: Shielding factor not 2.300 <= 2.847 < 2.800)
k="${k-}${k+ and }not test_fine_cal_systems[kit]"

# https://github.com/mne-tools/mne-python/blob/v1.0.3/tools/github_actions_test.sh#L7
# skip tests that require network
m='not (slowtest or pgtest)'

# Erroring on DeprecationWarnings, RuntimeWarings, UserWarnings, FutureWarnings,
# etc. makes sense upstream, but is probably too strict for distribution
# packaging.
w="${w-} -W ignore::Warning"
%pytest -v -m "${m}" ${ignore-} -k "${k-}" ${w-}


%files -n python3-mne -f %{pyproject_files}
%doc README.rst examples
%{_bindir}/mne

%changelog
%autochangelog
