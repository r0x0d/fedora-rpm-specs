# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/tencentcloud/tencentcloud-sdk-go
%global goipath         github.com/tencentcloud/tencentcloud-sdk-go
Version:                1.0.704

%gometa -f

%global common_description %{expand:
Tencent Cloud API 3.0 SDK for Golang.}

%global golicenses      LICENSE
%global godocs          examples CHANGELOG.md README.md SERVICE_CHANGELOG.md\\\
                        products.md

Name:           %{goname}
Release:        %autorelease
Summary:        Tencent Cloud API 3.0 SDK for Golang

License:        Apache-2.0
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