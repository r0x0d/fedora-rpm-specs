# Generated by go2rpm 1
%bcond_without check

%global debug_package %{nil}

# https://github.com/spacemonkeygo/monkit
%global goipath         github.com/spacemonkeygo/monkit
Version:                3.0.7

%gometa

%global goaltipaths     github.com/spacemonkeygo/monkit/v3

%global common_description %{expand:
A flexible process data collection, metrics, monitoring, instrumentation, and
tracing client library for Go.}

%global golicenses      LICENSE
%global godocs          AUTHORS README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Flexible process data collection, instrumentation, and tracing client library

# Upstream license specification: Apache-2.0
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
sed -i "s|github.com/spacemonkeygo/monkit/v3|github.com/spacemonkeygo/monkit|" $(find . -type f -iname "*.go")
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog