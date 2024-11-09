%{?!python3_pkgversion:%global python3_pkgversion 3}

%global modname oras
%global srcname %{modname}
%global pypi_name oras-py
%global forgeurl https://github.com/oras-project/%{pypi_name}
%global version0 0.2.22
%forgemeta

%global desc OCI Registery as Storage

Name:           python-%{srcname}
Version:        %{version0}
Release:        %{autorelease}
Summary:        %{desc}
License:        Apache-2.0
URL:            %{forgeurl}
Source0:        %{pypi_source}
# Patches go here

BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%{?python_enable_dependency_generator}

%description
%{desc}
OCI Registry as Storage enables libraries to push OCI Artifacts to OCI
Conformant registries. This is a Python SDK for Python developers to
empower them to do this in their applications.


%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}

%if %{undefined python_enable_dependency_generator} && %{undefined python_disable_dependency_generator}
# Put manual requires here:

%endif

%description -n python%{python3_pkgversion}-%{srcname}
%{desc}


%prep
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%pyproject_check_import -t


%files -n  python%{python3_pkgversion}-%{srcname}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}.dist-info/

%changelog
%autochangelog
