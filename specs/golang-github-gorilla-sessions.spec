# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/gorilla/sessions
%global goipath         github.com/gorilla/sessions
Version:                1.2.1

%gometa

%global common_description %{expand:
Package gorilla/sessions provides cookie and filesystem sessions and
infrastructure for custom session backends.}

%global golicenses      LICENSE
%global godocs          AUTHORS README.md

%global gosupfiles      glide.lock glide.yaml

Name:           %{goname}
Release:        %autorelease
Summary:        Cookie and filesystem sessions and infrastructure for custom session backends

# Upstream license specification: BSD-3-Clause
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.lock

BuildRequires:  golang(github.com/gorilla/securecookie)

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