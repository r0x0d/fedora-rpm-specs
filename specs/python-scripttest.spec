Name:           python-scripttest
Version:        1.3.0
Release:        %autorelease
Summary:        Helper to test command-line scripts

License:        MIT
URL:            http://pypi.python.org/pypi/ScriptTest/
Source0:        https://github.com/pypa/scripttest/archive/1.3.0.tar.gz

BuildArch:      noarch

BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: python%{python3_pkgversion}-setuptools
BuildRequires: python%{python3_pkgversion}-sphinx
BuildRequires: python%{python3_pkgversion}-pytest

%description
ScriptTest is a library to help you test your interactive 
command-line applications.

With it you can easily run the command (in a subprocess) and see 
the output (stdout, stderr) and any file modifications.

%package -n     python%{python3_pkgversion}-scripttest
Summary:        Helper to test command-line scripts
%{?python_provide:%python_provide python%{python3_pkgversion}-scripttest}

%description -n python%{python3_pkgversion}-scripttest
ScriptTest is a library to help you test your interactive 
command-line applications.

With it you can easily run the command (in a subprocess) and see 
the output (stdout, stderr) and any file modifications.


%prep
%setup -q -n scripttest-%{version}


%build
%py3_build

sphinx-build -b html docs/ docs/html


%install
%py3_install

%check
%{__python3} setup.py test

%files -n python%{python3_pkgversion}-scripttest
%doc docs/html
%license docs/license.rst
%{python3_sitelib}/scripttest.py
%{python3_sitelib}/__pycache__/scripttest.cpython-%{python3_version_nodots}*
%{python3_sitelib}/scripttest*.egg-info/


%changelog
%autochangelog