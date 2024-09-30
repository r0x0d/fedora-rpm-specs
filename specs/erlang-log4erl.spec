%global realname log4erl


Name:		erlang-%{realname}
Version:	0.9.0
Release:	%autorelease
BuildArch:	noarch
Summary:	A logger for erlang in the spirit of Log4J
# Dual licensing (MPL or BSD) is explicitly stated at project's web-page
# log4erl_parser.erl is licensed under ERPL
# Automatically converted from old format: MPLv1.1 or BSD and ERPL - review is highly recommended.
License:	LicenseRef-Callaway-MPLv1.1 OR LicenseRef-Callaway-BSD AND ErlPL-1.1
URL:		https://github.com/ahmednawras/%{realname}
VCS:		scm:git:%{url}.git
#Source0:	%{url}/archive/%{version}/%{realname}-%{version}.tar.gz
Source0:	%{url}/archive/76ef24cb3928fbacd5777eadeedac0df0a0dc822/%{realname}-%{version}.tar.gz
Patch1:		erlang-log4erl-0001-Stop-using-deprecated-function-crypto-hmac-3.patch
Patch2:		erlang-log4erl-0002-Remove-deprecated-function-httpd_util-integer_to_hex.patch
BuildRequires:	erlang-mochiweb
BuildRequires:	erlang-rebar3


%description
A logger for erlang in the spirit of Log4J.


%prep
#%%autosetup -q -n %{realname}-%{version}
%autosetup -p1 -n %{realname}-76ef24cb3928fbacd5777eadeedac0df0a0dc822
# in mochiweb
rm -f src/mochinum.erl


%build
%{erlang3_compile}


%install
%{erlang3_install}
install -D -p -m 0644 priv/l4e.conf %{buildroot}%{erlang_appdir}/priv/l4e.conf
install -D -p -m 0644 priv/log4erl.conf %{buildroot}%{erlang_appdir}/priv/log4erl.conf


%check
%{erlang3_test}


%files
%license LICENSE.txt
%doc API.txt Appenders_API.txt CHANGELOG.txt CONFIGURATION.txt README.txt TODO.txt
%{erlang_appdir}/


%changelog
%autochangelog
