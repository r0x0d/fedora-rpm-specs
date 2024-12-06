Name:           python-sdkmanager
Version:        0.6.10
Release:        %autorelease
Summary:        Android SDK manager written in Python

License:        AGPL-3.0-or-later
URL:            https://gitlab.com/fdroid/sdkmanager
Source:         %{pypi_source sdkmanager}

BuildArch:      noarch
BuildRequires:  python3-devel


%global _description %{expand:
A drop-in replacement for sdkmanager from the Android SDK
written in Python. It implements the exact API of the
sdkmanager command line.  It only deviates from that API
if it can be done while being 100 percent compatible.

The project also attempts to maintain the same terminal
output so it can be compatible with things that scrape
sdkmanager output.}

%description %_description

%package -n     python3-sdkmanager
Summary:        Android SDK manager written in Python

%description -n python3-sdkmanager %_description


%prep
%autosetup -n sdkmanager-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
sed -i '/env python3/d' sdkmanager.py
chmod -x sdkmanager.py
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files sdkmanager


%check
%pyproject_check_import
# Tests require internet access

%files -n python3-sdkmanager -f %{pyproject_files}
%{_bindir}/sdkmanager

%changelog
%autochangelog
