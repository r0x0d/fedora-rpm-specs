Name:           python-tox-uv
Version:        1.11.4
Release:        %autorelease
Summary:        Integration of uv with tox

License:        MIT
URL:            https://github.com/tox-dev/tox-uv
Source:         %{pypi_source tox_uv}

# Make a test fixture work without /usr/bin/python
Patch:          https://github.com/tox-dev/tox-uv/pull/103.patch

# as with python-tox, those tests run ont he CI only, as they need internet access
%bcond ci_tests 0

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
tox-uv is a tox plugin, which replaces virtualenv and pip with uv in your tox
environments. Note that you will get both the benefits (performance)
or downsides (bugs) of uv.

Installing this package changes the behavior of tox.
It also makes it impossible to use tox with a Python version
not supported by uv.}

%description %_description

%package -n     python3-tox-uv
Summary:        %{summary}

%description -n python3-tox-uv %_description


%prep
%autosetup -p1 -n tox_uv-%{version}
# Remove unpackaged (devpi-process) and coverage test dependencies
sed -Ei '/"(devpi-process|covdefaults|pytest-cov)/d' pyproject.toml
# Relax some build/test dependencies
sed -Ei 's/"(hatchling|pytest(-mock)?|diff-cover)>=[^"]+"/"\1"/' pyproject.toml
# And a runtime dependency, where we must be more careful
sed -i 's/"packaging>=24.1"/"packaging>=23.1"/' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -x testing


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l tox_uv


%check
# only works with the package actually installed
k="${k-}${k+ and }not test_tox_version"

%if %{without ci_tests}
# requires internet
k="${k-}${k+ and }not test_uv_install"
k="${k-}${k+ and }not test_uv_package_editable_legacy"
k="${k-}${k+ and }not test_uv_package_requirements"
k="${k-}${k+ and }not test_uv_python_set"
%endif

%pytest -v "${k:+-k $k}"


%files -n python3-tox-uv -f %{pyproject_files}


%changelog
%autochangelog