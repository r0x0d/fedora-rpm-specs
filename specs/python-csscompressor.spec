Name:           python-csscompressor
Version:        0.9.5
Release:        %autorelease
Summary:        Python port of YUI CSS Compressor

License:        BSD-3-Clause
URL:            https://github.com/sprymix/csscompressor
Source:         %{pypi_source csscompressor}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
This package is an almost exact port of YUI CSS Compressor to Python that
passes all the original unittests.}

%description %_description

%package -n     python3-csscompressor
Summary:        %{summary}

%description -n python3-csscompressor %_description

%prep
%autosetup -p1 -n csscompressor-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l csscompressor

%check
%pytest -v

%files -n python3-csscompressor -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
