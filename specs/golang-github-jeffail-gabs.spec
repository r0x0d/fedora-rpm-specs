# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/Jeffail/gabs
%global goipath         github.com/Jeffail/gabs
Version:                1.4.0

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-Jeffail-gabs-devel < 1.2.0-2
}

%global common_description %{expand:
Gabs is a small utility for dealing with dynamic or unknown JSON structures in
golang. It's pretty much just a helpful wrapper around the golang
json.Marshal/json.Unmarshal behaviour and map[string]interface{} objects. It
does nothing spectacular except for being fabulous.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        For parsing, creating and editing unknown or dynamic JSON in Go

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