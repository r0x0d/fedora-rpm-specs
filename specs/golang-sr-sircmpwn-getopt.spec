# Generated by go2rpm 1.3
%bcond_without check

%global debug_package %{nil}

# https://git.sr.ht/~sircmpwn/getopt
%global goipath         git.sr.ht/~sircmpwn/getopt
Version:                1.0.0
%global tag             v%{version}

%gometa

%global common_description %{expand:
A POSIX-compatible getopt implementation for Go, because POSIX getopt is The
Correct Way to interpret arguments to command line utilities.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        POSIX-compatible getopt implementation for Go
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
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