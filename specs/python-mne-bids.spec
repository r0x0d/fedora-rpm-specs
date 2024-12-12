%bcond tests 1

# Until python3-edfio is packaged, omit it from the [full] extra
%bcond edfio 0
# Until python3-eeglabio is packaged, omit it from the [full] extra
%bcond eeglabio 0

%global desc %{expand: \
MNE-BIDS: Organizing MEG, EEG, and iEEG data according to the BIDS
specification and facilitating their analysis with MNE-Python}

Name:           python-mne-bids
Version:        0.16.0
Release:        %autorelease
Summary:        Experimental code for BIDS using MNE
License:        BSD-3-Clause
URL:            https://github.com/mne-tools/mne-bids
Source:         %{url}/archive/v%{version}/mne-bids-%{version}.tar.gz
BuildArch:      noarch
ExcludeArch:    %{ix86}

BuildRequires:  python3-devel
%if %{without edfio} || %{without eeglabio}
BuildRequires:  tomcli
%endif

%if %{with tests}
# See the [test] extra in pyproject.toml, and
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters.
# - mne_bids[full]: self-dependency; try to generate the right BR’s
# - pytest >= 8 – but pytest 7 *does* work, and we have it in Fedora 40
BuildRequires:  %{py3_dist pytest}
# - pytest-cov: coverage analysis; unwanted
# - pytest-sugar: just makes the output fancy; unnecessary
# - ruff: linter/formatter; unwanted
%endif

%description
%{desc}

%package -n python3-mne-bids
Summary:        %{summary}

%description -n python3-mne-bids
%{desc}

%pyproject_extras_subpkg -n python3-mne-bids full

%prep
%autosetup -n mne-bids-%{version}
%if %{without edfio}
tomcli set pyproject.toml lists delitem --type regex \
    project.optional-dependencies.full 'edfio($|\b.*)'
%endif
%if %{without eeglabio}
tomcli set pyproject.toml lists delitem --type regex \
    project.optional-dependencies.full 'eeglabio($|\b.*)'
%endif

%generate_buildrequires
%pyproject_buildrequires -x full

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l mne_bids

%check
%pyproject_check_import
%if %{with tests}
# Most tests that require the test dataset are automatically skipped when it is
# unavailable. The following tests do also require unpackaged mne test data:
# - mne/io/bti/tests/data/test_config_linux
k="${k-}${k+ and }not test_infer_eeg_placement_scheme"
k="${k-}${k+ and }not test_print_dir_tree"
# - mne/io/brainvision/tests/data/test.vhdr
k="${k-}${k+ and }not test_copyfile_brainvision"
k="${k-}${k+ and }not test_get_brainvision_paths"
# - mne/io/edf/tests/data/test.bdf
k="${k-}${k+ and }not test_bdf"
# - mne/io/edf/tests/data/test.edf
k="${k-}${k+ and }not test_copyfile_edf"
k="${k-}${k+ and }not test_copyfile_edfbdf_uppercase"
# - mne/io/kit/tests/data/test.sqd
k="${k-}${k+ and }not test_copyfile_kit"

# Require (NodeJS-based) bids-validator command-line tool, not packaged
k="${k-}${k+ and }not test_create_fif"
k="${k-}${k+ and }not test_line_freq"
k="${k-}${k+ and }not test_preload"

%pytest mne_bids -W ignore::DeprecationWarning --doctest-modules -k "${k-}" -v
%endif

%files -n python3-mne-bids -f %{pyproject_files}
%doc README.md
%{_bindir}/mne_bids

%changelog
%autochangelog
