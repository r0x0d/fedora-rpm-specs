%global pypi_name pyqt-feedback-flow

%bcond tests 1

Name:           python-%{pypi_name}
Version:        0.3.5
Release:        %autorelease
Summary:        Show feedback in toast-like notifications

%global forgeurl https://github.com/firefly-cpp/pyqt-feedback-flow
%global tag %{version}
%forgemeta

License:        MIT
URL:            %forgeurl
Source0:        %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist toml-adapt}
%if %{with tests}
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-qt}
%endif
# The python3dist(pyqt6) dependency generated from PyQt6 in
# pyproject.toml is satisfied by python3-pyqt6-base, but this project
# uses PyQt6.QtSvg, which is packaged along with other “non-core” modules
# in python3-pyqt6. Since this is not represented (and currently cannot
# be represented) in the Python metadata, we need explicit BuildRequires
# *and* Requires on the full python3-pyqt6.
BuildRequires:  python3-pyqt6

%global _description %{expand:
This software allows us to show flowing notifications in the realm
of a text or a picture. Both text and pictures (raster and vector)
can be customized according to users' wishes, which offers a wide
variety of possibilities for providing flowing feedback.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
# See the comment on the corresponding BuildRequires.
Requires:       python3-pyqt6

%description -n python3-%{pypi_name} %_description

%prep
%forgeautosetup -p1
rm -rf %{pypi_name}.egg-info

toml-adapt -path pyproject.toml -a change -dep python -ver X
toml-adapt -path pyproject.toml -a change -dep emoji -ver X
toml-adapt -path pyproject.toml -a change -dep PyQt6 -ver X

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files pyqt_feedback_flow

%check
%if %{with tests}
%pytest -v
%else
%pyproject_check_import
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md
%doc CITATION.cff

%changelog
%autochangelog
