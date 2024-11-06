%global pypi_name wsgi_intercept

%global with_docs 1

%global common_desc \
It installs a WSGI application in place of a real URI for testing. \
Testing a WSGI application normally involves starting a server at \
a local host and port, then pointing your test code to that address. \
Instead,this library lets you intercept calls to any specific host/port \
combination and redirect them into a `WSGI application`_ importable by \
your test program.


Name:           python-%{pypi_name}
Version:        1.13.1
Release:        %autorelease
Summary:        wsgi_intercept installs a WSGI application in place of a real URI for testing

License:        MIT
URL:            https://github.com/cdent/wsgi-intercept
Source0:        %pypi_source
Patch0001:      0001-Update-urllib3.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
%{common_desc}

%package -n python3-%{pypi_name}
Summary:        wsgi_intercept installs a WSGI application in place of a real URI for testing

%description -n python3-%{pypi_name}
%{common_desc}

%package -n python-%{pypi_name}-doc
Summary:        Documentation for the wsgi-intercept module

%description -n python-%{pypi_name}-doc
Documentation for the wsgi-intercept module


%prep
%autosetup -n %{pypi_name}-%{version} -p1
sed -i 's/\.\[.*\]//' tox.ini

%generate_buildrequires
%if 0%{?with_docs}
%pyproject_buildrequires -t -x testing -x docs
%else
%pyproject_buildrequires -t -x testing
%endif

%build
%pyproject_wheel

# generate html docs
%if 0%{?with_docs}
%tox -e docs
# remove the sphinx-build leftovers
rm -rf build/sphinx/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%pyproject_save_files wsgi_intercept

%check
export WSGI_INTERCEPT_SKIP_NETWORK=true
%tox

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README
%license LICENSE
%exclude %{python3_sitelib}/%{pypi_name}/tests

%if 0%{?with_docs}
%files -n python-%{pypi_name}-doc
%license LICENSE
%doc build/sphinx
%endif

%changelog
%autochangelog
