Name:           python-python-multipart
Version:        0.0.12
Release:        %autorelease
Summary:        A streaming multipart parser for Python

License:        Apache-2.0
URL:            https://github.com/Kludex/python-multipart
Source:         %{pypi_source python_multipart}

BuildArch:      noarch

BuildRequires:  python3-devel

# See testenv.deps from
# https://github.com/Kludex/python-multipart/blob/%%{version}/tox.ini.  Because
# of unwanted coverage dependencies and arguments, it’s not worth packaging
# from the GitHub source archive and generating test dependencies with tox;
# it’s much easier to just enumerate them manually.
BuildRequires:  %{py3_dist pytest}
BuildRequires:  %{py3_dist PyYAML}

%global common_description %{expand:
Python-Multipart is a streaming multipart parser for Python.}

%description %{common_description}


%package -n python3-python-multipart
Summary:        %{summary}

# Prior to Fedora 41, the python-multipart package provided this library,
# https://pypi.org/project/python-multipart/. In Fedora 41, the
# python-python-multipart package was introduced and python-multipart was
# repurposed for https://pypi.org/project/multipart/. See
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_library_naming.
#
# This package uses the same import namespace (“import multipart”); this means
# there are file conflicts. This is not generally allowable, but there is no
# way to avoid it in this case. See:
#
#   Namespace conflict with multipart package
#   https://github.com/Kludex/python-multipart/issues/149
Conflicts:      python3-multipart
# Ensure proper upgrade path from the old package
Obsoletes:      python3-multipart < 0.1

%description -n python3-python-multipart %{common_description}


%prep
%autosetup -n python_multipart-%{version} -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l multipart


%check
%pytest


%files -n python3-python-multipart -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog