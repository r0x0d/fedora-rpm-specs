Name:           python-klusta
Version:        3.0.16
Release:        %autorelease
Summary:        Spike detection and automatic clustering for spike sorting

# Do not include test data in the source RPM because it does not have a known
# license. See:
#
# Please assign a license to the data
# https://github.com/kwikteam/phy-data/issues/1
#
# We use a global rather than a bcond because this affects the contents of the
# source RPM, but we leave in all the boilerplate for testing with data from
# the phy-data repository because it can still be done manually in mock builds
# outside of Fedora infrastructure, and because it will make it easy to enable
# these tests in the future if upstream does assign a proper licenses.
%global phy_data 0

License:        BSD-3-Clause
URL:            https://github.com/kwikteam/klusta
Source0:        %{pypi_source klusta}
%if 0%{?phy_data}
%global phy_data_url https://github.com/kwikteam/phy-data
%global phy_data_commit 804635aa76987a8900f3468cb08acf53139743a1
Source1:        %{phy_data_url}/archive/%{phy_data_commit}/phy-data-%{phy_data_commit}.tar.gz
%endif

# Add missing runtime/install-time dependencies to setup.py
# https://github.com/kwikteam/klusta/pull/80
#
# Includes:
#
# Require setuptools, klusta/__init__.py imports pkg_resources
# https://github.com/kwikteam/klusta/pull/76
Patch:          %{url}/pull/80.patch
# Stop using numpy type aliases that were deprecated in 1.20 and later removed
# https://github.com/kwikteam/klusta/pull/81
Patch:          %{url}/pull/81.patch
# Do not pass a float as the num argument to np.linspace
# Fixes compatibility of test_apply_filter with recent versions of numpy.
# https://github.com/kwikteam/klusta/pull/82
Patch:          %{url}/pull/82.patch

# We build this as an arched package to run tests on all architectures since
# there are arch-specific test failures, but there is no compiled code, and all
# the binary RPMs are noarch.
%global debug_package %{nil}

BuildRequires:  python3-devel
# For tests:
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist responses}

BuildRequires:  help2man

%global common_description %{expand:
klusta is an open source package for automatic spike sorting of multielectrode
neurophysiological recordings made with probes containing up to a few dozens of
sites.

klusta implements the following features:

  • Kwik: An HDF5-based file format that stores the results of a spike sorting
    session.
  • Spike detection (also known as SpikeDetekt): an algorithm designed for
    probes containing tens of channels, based on a flood-fill algorithm in the
    adjacency graph formed by the recording sites in the probe.
  • Automatic clustering (also known as Masked KlustaKwik): an automatic
    clustering algorithm designed for high-dimensional structured datasets.}

%description %{common_description}


%package -n python3-klusta
Summary:        %{summary}

BuildArch:      noarch

%description -n python3-klusta %{common_description}


%prep
%autosetup -n klusta-%{version} -p1

%if 0%{?phy_data}
# Mock out a home directory with downloaded data for testing
%setup -q -n klusta-%{version} -T -D -b 1
mkdir -p _user_home/.klusta/test_data
ln -s '../../../../phy-data-%{phy_data_commit}/test/test-32ch-10s.dat' \
    _user_home/.klusta/test_data/
%endif


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l klusta

# Do this in %%install to use the generated entry point
install -d '%{buildroot}%{_mandir}/man1'
%{py3_test_envvars} help2man \
    --no-info \
    --name='Spikesort a dataset' \
    --version-string='%{version}' \
    --output='%{buildroot}%{_mandir}/man1/klusta.1' \
    '%{buildroot}%{_bindir}/klusta'


%check
%pyproject_check_import

# These tests require python3dist(klustakwik2), not packaged.
k="${k-}${k+ and }not test_klustakwik"
k="${k-}${k+ and }not test_launch_real"
k="${k-}${k+ and }not test_launch_shanks"
k="${k-}${k+ and }not test_sparsify_features_masks"

%ifarch s390x
# As far as we can tell, each of these fails on big-endian architectures
# because the synthetic data file created at test time is written in a
# host-endian format, but the expected checksum is based on a little-endian
# data file. We could report this upstream, but considering that upstream has
# been inactive for several years and we don’t have an obvious fix to propose
# (which might benefit other downstreams), this might not be a good use of time
# unless upstream development picks back up again.
k="${k-}${k+ and }not test_check_md5_of_url"
k="${k-}${k+ and }not test_download_already_exists_invalid"
k="${k-}${k+ and }not test_download_already_exists_valid"
k="${k-}${k+ and }not test_download_file[mock_urls0]"
%endif

%if !0%{?phy_data}
# These tests require data from https://github.com/kwikteam/phy-data, either as
# an additional source or downloaded from the network.
k="${k-}${k+ and }not test_spike_detect_methods[real]"
k="${k-}${k+ and }not test_spike_detect_real_data[real]"
%endif

mkdir -p _empty
cd _empty
%if 0%{?phy_data}
HOME="${PWD}/../_user_home" \
%endif
    %pytest -v -k "${k-}" %{buildroot}%{python3_sitelib}/klusta


%files -n python3-klusta -f %{pyproject_files}
%doc README.md
%{_bindir}/klusta
%{_mandir}/man1/klusta.1*


%changelog
%autochangelog
