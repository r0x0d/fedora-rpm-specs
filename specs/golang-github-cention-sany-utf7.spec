# Generated by go2rpm 1.6.0
%bcond_without check

%global debug_package %{nil}

# https://github.com/cention-sany/utf7
%global goipath         github.com/cention-sany/utf7
%global commit          26cad61bd60aa9fe1819b49717dda49ab82cc929

%gometa

%global common_description %{expand:
UTF7 UTF8 transcoder. With transformer interface.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        UTF7 UTF8 transcoder. With transformer interface

# Upstream license specification: BSD-3-Clause
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/text/encoding)
BuildRequires:  golang(golang.org/x/text/transform)

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
