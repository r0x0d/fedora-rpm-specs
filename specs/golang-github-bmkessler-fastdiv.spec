# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/bmkessler/fastdiv
%global goipath         github.com/bmkessler/fastdiv
%global commit          41d5178f204490636154dfa541de575f0abb27bd

%gometa -f


%global common_description %{expand:
Fast division, modulus and divisibility checks in Go for divisors known only at
runtime.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        Fast division, modulus and divisibility checks in Go

License:        MIT
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