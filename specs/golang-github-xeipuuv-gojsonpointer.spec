# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/xeipuuv/gojsonpointer
%global goipath         github.com/xeipuuv/gojsonpointer
%global commit          02993c407bfbf5f6dae44c4f4b1cf6a39b5fc5bb

%gometa

%global common_description %{expand:
An implementation of JSON Pointer.}

%global golicenses      LICENSE-APACHE-2.0.txt
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease
Summary:        JSON Pointer implementation in Go

# Upstream license specification: Apache-2.0
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
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