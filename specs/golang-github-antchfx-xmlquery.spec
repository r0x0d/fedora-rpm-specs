# Generated by go2rpm 1.10.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/antchfx/xmlquery
%global goipath         github.com/antchfx/xmlquery
Version:                1.4.1

%gometa -L

%global common_description %{expand:
Xmlquery is Golang XPath package for XML query.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           golang-github-antchfx-xmlquery
Release:        %autorelease
Summary:        Xmlquery is Golang XPath package for XML query

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A
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