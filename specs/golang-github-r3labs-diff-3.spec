# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/r3labs/diff
%global goipath         github.com/r3labs/diff/v3
%global forgeurl        https://github.com/r3labs/diff
Version:                3.0.1

%gometa

%global common_description %{expand:
A library for diffing Golang structures.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Library for diffing Golang structures

License:        MPL-2.0
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