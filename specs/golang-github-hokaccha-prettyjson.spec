# Generated by go2rpm 1.8.1
%bcond_without check
%global debug_package %{nil}

# https://github.com/hokaccha/go-prettyjson
%global goipath         github.com/hokaccha/go-prettyjson
%global commit          0474bc63780f190edc23bb56214893dab107909c

%gometa -f

%global common_description %{expand:
JSON pretty print for Golang.}

%global golicenses      LICENSE
%global godocs          _example README.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        JSON pretty print for Golang

License:        MIT
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