# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/opendns/vegadns2client
%global goipath         github.com/opendns/vegadns2client
%global commit          a3fa4a771d87bda2514a90a157e1fed1b6897d2e

%gometa

%global goaltipaths     github.com/OpenDNS/vegadns2client

%global common_description %{expand:
Vegadns2client is a Go client for VegaDNS-API. This is an incomplete client,
initially intended to support lego.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease
Summary:        Go Client for VegaDNS-API

# Upstream license specification: Apache-2.0
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
