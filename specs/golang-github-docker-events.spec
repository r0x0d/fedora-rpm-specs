# Generated by go2rpm 1.8.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/docker/go-events
%global goipath         github.com/docker/go-events
%global commit          e31b211e4f1cd09aa76fe4ac244571fab96ae47f

%gometa

%global common_description %{expand:
The Docker Events package implements a composable event distribution package for
Go.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        Composable event distribution for Go

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep

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