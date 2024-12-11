%global srcname tmuxp

Name:           python-%{srcname}
Version:        1.49.0
Release:        %autorelease
Summary:        Tmux session manager

# This is the proper SPDX license
License:        MIT
URL:            https://tmuxp.git-pull.com/
Source:         %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
Session manager for tmux, which allows users to save and load tmux sessions
through simple configuration files.}

%description %_description

%package -n python3-%{srcname}
Summary:	%{summary}
BuildRequires:  python3-devel

%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files tmuxp


%check
%pyproject_check_import


%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGES examples
%{_bindir}/tmuxp


%changelog
%autochangelog
