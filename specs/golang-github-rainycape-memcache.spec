# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/rainycape/memcache
%global goipath         github.com/rainycape/memcache
%global commit          1031fa0ce2f20c1c0e1e1b51951d8ea02c84fa05

%gometa

%global common_description %{expand:
This is a memcache client library for the Go programming language.}

%global golicenses      LICENSE
%global godocs          README.md orig.txt

Name:           %{goname}
Version:        0
Release:        %autorelease
Summary:        High performance memcache client in Go

# Upstream license specification: Apache-2.0
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}
# https://github.com/rainycape/memcache/pull/5
Patch0:         Use-Skipf-to-permit-formatting-directive.patch

%description
%{common_description}

%gopkg

%prep
%goprep
%patch -P0 -p1

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog