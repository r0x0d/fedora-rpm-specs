# Generated by go2rpm 1
%bcond_without check

%global debug_package %{nil}

# https://github.com/josharian/intern
%global goipath         github.com/josharian/intern
Version:                1.0.0

%gometa

%global common_description %{expand:
Intern Go strings.}

%global golicenses      license.md
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Intern Go strings

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