# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/kr/pretty
%global goipath         github.com/kr/pretty
Version:                0.2.1

%gometa

%global common_description %{expand:
Package pretty provides pretty-printing for go values. This is useful during
debugging, to avoid wrapping long output lines in the terminal.}

%global golicenses      License
%global godocs          Readme

%global gosupfiles glide.lock glide.yaml

Name:           %{goname}
Release:        %autorelease
Summary:        Pretty printing for go values

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

BuildRequires:  golang(github.com/kr/text)

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