# Generated by go2rpm 1.8.2
%bcond_without check
%global debug_package %{nil}

# https://github.com/hashicorp/go-multierror
%global goipath         github.com/hashicorp/go-multierror
Version:                1.1.1

%gometa

%global common_description %{expand:
Go-multierror is a package for Go that provides a mechanism for representing a
list of error values as a single error.

This allows a function in Go to return an error that might actually be a list of
errors. If the caller knows this, they can unwrap the list and access the
errors. If the caller does not know, the error formats to a nice human-readable
format.

Go-multierror implements the errwrap interface so that it can be used with that
library, as well.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Go package for representing a list of errors as a single error

License:        MPL-2.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep

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