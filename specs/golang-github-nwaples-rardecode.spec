# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/nwaples/rardecode
%global goipath         github.com/nwaples/rardecode
Version:                1.1.2

%gometa

%global common_description %{expand:
A Go package for reading RAR archives.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Go package for reading RAR archives

# Upstream license specification: BSD-2-Clause
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