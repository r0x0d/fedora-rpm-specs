# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/sacloud/iaas-api-go
%global goipath         github.com/sacloud/iaas-api-go
Version:                1.11.1

%gometa -f

%global common_description %{expand:
SAKURA Cloud library for Go.}

%global golicenses      LICENSE
%global godocs          docs AUTHORS README.md

Name:           %{goname}
Release:        %autorelease
Summary:        SAKURA Cloud library for Go

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1
rm -rfv trace/otel/examples trace/otel/example_test.go

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