# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/fatih/camelcase
%global goipath         github.com/fatih/camelcase
Version:                1.0.0

%gometa

%global common_description %{expand:
CamelCase is a Go package to split the words of a camelcase type string into a
slice of words. It can be used to convert a camelcase word (lower or upper case)
into any type of word.}

%global golicenses      LICENSE.md
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Split a camelcase word into a slice of words in Go

License:        MIT
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