%global realname riak_pb_msgcodegen

Name:		erlang-rebar3-%{realname}
Version:	1.0.0
Release:	%autorelease
Summary:	A riak_pb message compiler for Rebar3
License:	BSD-3-Clause
URL:		https://github.com/basho/%{realname}
VCS:		git:%{url}.git
Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	erlang-rebar3

%description
%{summary}.

%prep
%autosetup -p1 -n %{realname}-%{version}

%build
%{erlang3_compile}

%check
%{erlang3_test}

%install
%{erlang3_install}

%files
%license LICENSE
%doc README.md
%{erlang_appdir}

%changelog
%autochangelog
