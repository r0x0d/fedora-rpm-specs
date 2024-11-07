%global         srcname         pyrdfa3
%global         forgeurl        https://github.com/prrvchr/pyrdfa3
Version:        3.6.4
%global         tag             v%{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        RDFa 1.1 distiller/parser library

License:        W3C
URL:            %{forgeurl}
Source:         %{forgeurl}/archive/%{tag}/%{srcname}-%{version}.tar.gz

BuildRequires:  python3-devel

BuildArch: noarch

%global _description %{expand:
pyRdfa distiller/parser library.
}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%autosetup -n %{srcname}-%{version}
# Remove pre-generated files
rm -r doc
rm -r src/pyRdfa3.egg-info

# Relax version requirement on setuptools and requests
sed -i 's/setuptools>=71.1.0/setuptools/g' pyproject.toml
sed -i 's/requests>=2.32.3/requests>=2.31.0/g' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyRdfa -l


%check
# No tests associated with distribution
%pyproject_check_import

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
