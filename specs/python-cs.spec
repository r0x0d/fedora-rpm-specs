%global forgeurl https://github.com/ngine-io/cs
Version:        3.3.0
%forgemeta

Name:           python-cs
Release:        %autorelease
Summary:        A simple, yet powerful CloudStack API client for python and the command-line

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildArch:      noarch

%global _description %{expand:
A simple, yet powerful CloudStack API client for python and the command-line.

* Async support.
* All present and future CloudStack API calls and parameters are supported.
* Syntax highlight in the command-line client if Pygments is installed.}

%description %_description

%package -n python3-cs
Summary:        %{summary}

BuildRequires:  python3-devel
# Test dependencies:
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(pytest)
# clearsilver also wants to install the cs executable, the upstream is dead,
# Fedora package is probably used by someone, python3-cs is modern, and conflicts are unlikely.
Conflicts: clearsilver

%description -n python3-cs %_description

%pyproject_extras_subpkg -n python3-cs async highlight

%prep
%forgeautosetup

# Remove unnecessary shebang
sed -i '/#! \/usr\/bin\/env python/d' cs/client.py


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install

%pyproject_save_files cs


%check
%pytest -c /dev/null tests.py


%files -n python3-cs -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/cs


%changelog
%autochangelog
