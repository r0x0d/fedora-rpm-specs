%global pypi_name ci-info

Name:           python-%{pypi_name}
Version:        0.3.0
Release:        %{autorelease}
Summary:        Continuous Integration Information

%global forgeurl https://github.com/mgxd/ci-info
%global tag %{version}
%forgemeta

License:        MIT
URL:            %forgeurl
Source:         %forgesource
# Don't install tests
Patch:          %{forgeurl}/pull/10.patch
# Fix license classification
Patch:          %{forgeurl}/pull/11.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A Python implementation of watson/ci-info [1]. Get details about the
current Continuous Integration environment.

[1] https://github.com/watson/ci-info}

%description %_description


%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description


%prep
%forgeautosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l ci_info


%check
# Tests require one of the supported CI environments
# We won't bother, but rely on upstream's testing
#%%pytest -v
# Run import test in absence of useful unit tests
%pyproject_check_import


%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGES.md README.md


%changelog
%autochangelog
