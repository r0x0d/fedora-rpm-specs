# Generated by go2rpm
# Tests are FUBAR and I don't speak Chinese
%bcond_with check
%global debug_package %{nil}


# https://github.com/aliyun/aliyun-oss-go-sdk
%global goipath         github.com/aliyun/aliyun-oss-go-sdk
Version:                2.2.0

%gometa

%global common_description %{expand:
Alibaba Cloud OSS SDK for Go.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README-CN.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Alibaba Cloud OSS SDK for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/aliyun/alibaba-cloud-sdk-go/services/kms)
BuildRequires:  golang(golang.org/x/time/rate)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/baiyubin/aliyun-sts-go-sdk/sts)
BuildRequires:  golang(gopkg.in/check.v1)
%endif

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