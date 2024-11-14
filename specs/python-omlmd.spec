%{?!python3_pkgversion:%global python3_pkgversion 3}

%global modname omlmd
%global srcname %{modname}
%global pypi_name %{modname}
%global forgeurl https://github.com/containers/%{pypi_name}
%global version0 0.1.6
%forgemeta

%global desc    Library to help leverage OCI Artifacts

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

This project is a collection of blueprints, patterns and tool-chain
(in the form of python SDK and CLI) to leverage OCI Artifact and
containers for ML model and metadata.


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
%{_bindir}/%{pypi_name}
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}.dist-info/

%changelog
%autochangelog
