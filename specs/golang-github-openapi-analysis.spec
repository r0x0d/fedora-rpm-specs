# Generated by go2rpm
%bcond_without check
%bcond_without bootstrap
%global debug_package %{nil}


# https://github.com/go-openapi/analysis
%global goipath         github.com/go-openapi/analysis
Version:                0.19.16

%gometa

%global common_description %{expand:
A foundational library to analyze an OAI specification document for easier
reasoning about the content.}

%global golicenses      LICENSE
%global godocs          CODE_OF_CONDUCT.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Openapi specification object model analyzer

# Upstream license specification: Apache-2.0
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/go-openapi/jsonpointer)
BuildRequires:  golang(github.com/go-openapi/spec)
BuildRequires:  golang(github.com/go-openapi/strfmt)
BuildRequires:  golang(github.com/go-openapi/swag)

%if %{without bootstrap}
%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{without bootstrap}
%if %{with check}
%check
%gocheck
%endif
%endif

%gopkgfiles

%changelog
%autochangelog