# Generated by go2rpm 1.5.0
%bcond_without check

%global debug_package %{nil}

# https://github.com/peterhellberg/link
%global goipath         github.com/peterhellberg/link
Version:                1.1.0

%gometa

%global common_description %{expand:
Parses Link headers used for pagination, as defined in RFC 5988.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Parses Link headers used for pagination, as defined in RFC 5988

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