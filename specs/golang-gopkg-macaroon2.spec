# Generated by go2rpm 1.11.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/go-macaroon/macaroon
%global goipath         gopkg.in/macaroon.v2
%global forgeurl        https://github.com/go-macaroon/macaroon
Version:                2.1.0

%gometa -L -f


%global common_description %{expand:
A native Go implementation of macaroons.}

%global golicenses      LICENSE
%global godocs          README.md TODO

Name:           golang-gopkg-macaroon2
Release:        %autorelease
Summary:        A native Go implementation of macaroons

License:        BSD-3-Clause
URL:            %{gourl}
Source:         %{gosource}
# https://github.com/go-macaroon/macaroon/pull/38
Patch1:         0001-Fix-TestAsciiHex.patch

%description %{common_description}

%gopkg

%prep
%goprep -A
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