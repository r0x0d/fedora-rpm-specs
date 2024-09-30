%global realname xmlrpc


Name:		erlang-%{realname}
Version:	1.14
Release:	%autorelease
BuildArch:	noarch
Summary:	HTTP 1.1 compliant XML-RPC library for Erlang
License:	BSD
URL:		https://github.com/etnt/%{realname}
VCS:		scm:git:%{url}.git
Source0:	%{url}/archive/f3f696c3c0988282fea182b61cdafdaa6a56d169/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar3
BuildRequires:	erlang-xmerl


%description
%{summary}.


%prep
%setup -q -n %{realname}-f3f696c3c0988282fea182b61cdafdaa6a56d169
rm -f ./rebar ./rebar.config


%build
%{erlang3_compile}


%install
%{erlang3_install}


%check
%{erlang3_test}


%files
%license LICENSE
%doc README examples/ doc/erlang.png doc/*.html doc/rfc2068.txt doc/stylesheet.css doc/xmlrpc_spec.txt
%{erlang_appdir}/


%changelog
%autochangelog
