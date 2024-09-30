%global realname poolboy


Name:		erlang-%{realname}
Version:	1.5.2
Release:	%autorelease
BuildArch:	noarch
Summary:	A hunky Erlang worker pool factory
License:	LicenseRef-Fedora-Public-Domain OR Apache-2.0
URL:		https://github.com/devinus/%{realname}
VCS:		scm:git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar3


%description
A hunky Erlang worker pool factory.


%prep
%setup -q -n %{realname}-%{version}
# FIXME plugins are currently broken
sed -i -e '/rebar3_eqc/d' rebar.config


%build
%{erlang3_compile}


%install
%{erlang3_install}


%check
%{erlang3_test}


%files
%license LICENSE UNLICENSE
%doc README.md
%{erlang_appdir}/


%changelog
%autochangelog
