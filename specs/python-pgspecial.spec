Name:           python-pgspecial
Version:        2.1.3
Release:        %autorelease
Summary:        Python implementation of postgres meta (backslash) commands

License:        BSD-3-Clause
URL:            https://www.dbcli.com
Source:         %{pypi_source pgspecial}
BuildArch:      noarch

BuildRequires:  python3-devel

%global common_description %{expand:
This package provides an API to execute meta-commands (AKA “special”, or
“backslash commands”) on PostgreSQL.}

%description %{common_description}


%package -n     python3-pgspecial
Summary:        %{summary}

# Workaround for missing dependency for pure-Python implementation and missing
# python_c module in python-psycopg3,
# https://bugzilla.redhat.com/show_bug.cgi?id=2266555.
# This can be removed after Fedora 41 reaches end-of-life.
Requires:       python-psycopg3 >= 3.1.19-1

%description -n python3-pgspecial %{common_description}


%prep
%autosetup -p1 -n pgspecial-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pgspecial


%check
# Note that most tests will be skipped since there is not a postgres database
# we can connect to.
%pytest


%files -n python3-pgspecial -f %{pyproject_files}
%license License.txt
%doc README.rst
%doc changelog.rst
%doc DEVELOP.rst


%changelog
%autochangelog
