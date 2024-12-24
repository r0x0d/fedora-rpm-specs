# This package has support for integrating with Pydantic, including tests that
# require Pydantic; but both python-pydantic-core and python-pydantic use
# python-inline-snapshot in their tests, creating a dependency cycle. We can
# break it by disabling the Pydantic integration tests during bootstrapping.
%bcond bootstrap 0
%bcond pydantic_tests %{without bootstrap}

Name:           python-inline-snapshot
Version:        0.18.1
Release:        %autorelease
Summary:        Golden master/snapshot/approval testing library

# SPDX
License:        MIT
URL:            https://github.com/15r10nk/inline-snapshot
Source:         %{pypi_source inline_snapshot}

# Use sys.executable rather than "python" to invoke pytest
# https://github.com/15r10nk/inline-snapshot/pull/167
Patch:          %{url}/pull/167.patch

BuildArch:      noarch

BuildRequires:  python3-devel

# For extracting test dependencies from pyproject.toml:
BuildRequires:  tomcli

# Extra test dependencies:
# For test_xdist, test_xdist_disabled, test_xdist_and_disable
BuildRequires:  %{py3_dist pytest-xdist}
# For test_black_formatting_error (mocker fixture)
BuildRequires:  %{py3_dist pytest-mock}
# A comment in pyproject.toml in [tool.hatch.envs.hatch-test] says:
#   Info for everyone who packages this library:
#   The following dependencies are installed with uv if you run `pytest --use-uv`
#   and used for specific tests in specific versions:
#    - pydantic v1 & v2
#    - attrs
#   But you dont have to use uv to test this library.
#   You can also just install the dependencies and use `pytest` normally
%if %{with pydantic_tests}
BuildRequires:  %{py3_dist pydantic}
%endif
BuildRequires:  %{py3_dist attrs}

%global common_description %{expand:
Golden master/snapshot/approval testing library which puts the values right
into your source code.}

%description %{common_description}


%package -n python3-inline-snapshot
Summary:        %{summary}

%description -n python3-inline-snapshot %{common_description}


%prep
%autosetup -n inline_snapshot-%{version} -p1
# Extract test dependencies from pyproject.toml; filter out those that are not
# needed (currently, typecheckers; see
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters).
tomcli get pyproject.toml -F newline-list \
    'tool.hatch.envs.hatch-test.extra-dependencies' |
    grep -vE '^(pyright|mypy)\b' |
    tee _test-requirements.txt


%generate_buildrequires
%pyproject_buildrequires _test-requirements.txt


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l inline_snapshot


%check
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
ignore="${ignore-} --ignore=tests/test_typing.py"
%if %{without pydantic_tests}
ignore="${ignore-} --ignore=tests/test_pydantic.py"
%endif

# Ignore all DeprecationWarning messages; they may pop up from anywhere in our
# dependency tree, and this can cause tests that expect precisely-matching
# pytest output to fail unnecessarily.
export PYTHONWARNINGS='ignore::DeprecationWarning'

%pytest ${ignore-} -vv


%files -n python3-inline-snapshot -f %{pyproject_files}


%changelog
%autochangelog
