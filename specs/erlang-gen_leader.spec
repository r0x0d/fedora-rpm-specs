%global realname gen_leader


Name:		erlang-%{realname}
Version:	1.0
Release:	%autorelease
BuildArch:	noarch
Summary:	A leader election behavior modeled after gen_server
License:	ErlPL-1.1
URL:		https://github.com/garret-smith/%{realname}_revival
VCS:		scm:git:%{url}.git
#Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Source0:	%{url}/archive/d9689e6/%{realname}-%{version}.tar.gz
BuildRequires:	erlang-rebar3


%description
This application implements a leader election behavior modeled after gen_server.
This behavior intends to make it reasonably straightforward to implement a fully
distributed server with master-slave semantics.


%prep
#%%setup -q -n %{realname}_revival-%{version}
%setup -q -n %{realname}_revival-d9689e6e80cd8a437bc207d37cb53290ecd64b35


%build
%{erlang3_compile}


%install
%{erlang3_install}


%check
%{erlang3_test}


%files
%doc README.markdown examples/
%{erlang_appdir}/


%changelog
%autochangelog