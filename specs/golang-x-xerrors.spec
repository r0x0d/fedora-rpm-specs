# Generated by go2rpm 1
%bcond_without check

%global debug_package %{nil}

# https://github.com/golang/xerrors
%global goipath         golang.org/x/xerrors
%global forgeurl        https://github.com/golang/xerrors
%global commit          5ec99f83aff198f5fbd629d6c8d8eb38a04218ca

%gometa

%global common_description %{expand:
This package holds the transition packages for the new Go 1.13 error values.
See golang.org/design/29934-error-values.}

%global golicenses      LICENSE PATENTS
%global godocs          README

Name:           %{goname}
Version:        0
Release:        %autorelease
Summary:        Transition packages for the new Go 1.13 error values

# Upstream license specification: BSD-3-Clause
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
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
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog