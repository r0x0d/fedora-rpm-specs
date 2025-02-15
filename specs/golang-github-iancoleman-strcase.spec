# Generated by go2rpm 1
%bcond_without check

%global debug_package %{nil}

# https://github.com/iancoleman/strcase
%global goipath         github.com/iancoleman/strcase
Version:                0.1.3

%gometa

%global common_description %{expand:
A Golang package for converting to snake_case or CamelCase.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        A Golang package for converting to snake_case or CamelCase

License:        MIT
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
