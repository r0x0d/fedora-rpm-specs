# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/pmezard/go-difflib
%global goipath         github.com/pmezard/go-difflib
Version:                1.0.0

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-pmezard-go-difflib-devel < 0-0.15
}

%global common_description %{expand:
Go-difflib is a partial port of python 3 difflib package. Its main goal is to
make unified and context diff available in pure Go, mostly for testing
purposes.}

%global golicenses      LICENSE
%global godocs          README.md

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
Release:        %autorelease
Summary:        Partial port of python difflib package to Go

# Upstream license specification: BSD-3-Clause
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

%description
%{common_description}

%gopkg

%prep
%goprep
cp %{S:1} %{S:2} .

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog