# Generated by go2rpm 1.10.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/google/go-cmp
%global goipath         github.com/google/go-cmp
Version:                0.6.0

%gometa -L


%global common_description %{expand:
This package is intended to be a more powerful and safer alternative
to reflect.DeepEqual for comparing whether two values are semantically
equal.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md

Name:           golang-github-google-cmp
Release:        %autorelease
Summary:        Package for comparing Go values in tests

License:        BSD-3-Clause
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