Name:           python-webcolors
Version:        24.11.1
Release:        %autorelease
Summary:        A library for working with the color formats defined by HTML and CSS
License:        BSD-3-Clause
URL:            https://github.com/ubernostrum/webcolors
Source:         %{pypi_source webcolors}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
webcolors is a module for working with and converting between the various
HTML/CSS color formats.}


%description %_description


%package -n python3-webcolors
Summary:        %{summary}


%description -n python3-webcolors %_description


%prep
%autosetup -n webcolors-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -L webcolors


%check
%{py3_test_envvars} %{python3} -m unittest discover


%files -n python3-webcolors -f %{pyproject_files}
%license %{python3_sitelib}/webcolors-%{version}.dist-info/licenses/LICENSE
%doc README.rst


%changelog
%autochangelog
