# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/softlayer/xmlrpc
%global goipath         github.com/softlayer/xmlrpc
Version:                1.0
%global commit          5f089df7cb7e37ba0cba4e7790910af66f0f7b1a

%gometa -f

%global common_description %{expand:
Implementation of XMLRPC protocol in Go language with some changes to interact
with the SoftLayer api.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Implementation of XMLRPC protocol in Go language for the SoftLayer api

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog