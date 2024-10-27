%global         srcname         kiss-headers
%global         forgeurl        https://github.com/jawah/kiss-headers
Version:        2.4.3
%global         tag             %{version}
%forgemeta

Name:           python-%{srcname}
Release:        %autorelease
Summary:        Object-oriented HTTP and IMAP headers

License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}


BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(requests)
BuildArch: noarch

%global _description %{expand:
Python package for HTTP/1.1 style headers. Parse
headers to objects. Most advanced available structure
for http headers.}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %_description


%prep
%forgeautosetup
# Do not measure test coverage
sed -i '/"--cov=kiss_headers --doctest-modules --cov-report=term-missing -rxXs"/d' \
    pyproject.toml

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files kiss_headers

%check
# Do not run tests that access external network
%pytest -k 'not encode_decode and not httpbin and not parse_response'

%files -n python3-%{srcname} -f %{pyproject_files}
 
%changelog
%autochangelog
