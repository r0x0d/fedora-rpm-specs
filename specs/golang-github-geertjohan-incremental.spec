# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/GeertJohan/go.incremental
%global goipath         github.com/GeertJohan/go.incremental
Version:                1.0.0

%gometa

%global common_description %{expand:
Go package Incremental provides typed incremental counters that are
concurrency-safe.}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Concurency-safe incremental numbers

# Upstream license specification: BSD-2-Clause
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
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