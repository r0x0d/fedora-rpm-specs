# Generated by go2rpm 1.10.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/FiloSottile/edwards25519
%global goipath         filippo.io/edwards25519
%global forgeurl        https://github.com/FiloSottile/edwards25519
Version:                1.1.0

%gometa -f

%global common_description %{expand:
This library implements the edwards25519 elliptic curve, exposing the necessary
APIs to build a wide array of higher-level primitives.

The code is originally derived from Adam Langley's internal implementation in
the Go standard library, and includes George Tankersley's performance
improvements. It was then further developed by Henry de Valence for use in
ristretto255, and was finally merged back into the Go standard library as of Go
1.17. It now tracks the upstream codebase and extends it with additional
functionality.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           golang-filippo-edwards25519
Release:        %autorelease
Summary:        Safer, faster, and more powerful low-level edwards25519 Go implementation

License:        BSD-3-Clause
URL:            %{gourl}
Source:         %{gosource}

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