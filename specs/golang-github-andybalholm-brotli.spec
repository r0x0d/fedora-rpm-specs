# Generated by go2rpm 1.14.0
%bcond check 1
%bcond bootstrap 0

%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/andybalholm/brotli
%global goipath         github.com/andybalholm/brotli
Version:                1.1.0

%gometa -L -f

%global common_description %{expand:
This package is a brotli compressor and decompressor implemented in Go. It was
translated from the reference implementation (https://github.com/google/brotli)
with the c2go tool at https://github.com/andybalholm/c2go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           golang-github-andybalholm-brotli
Release:        %autorelease
Summary:        Pure Go Brotli encoder and decoder

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep -A
%autopatch -p1

%if %{without bootstrap}
%generate_buildrequires
%go_generate_buildrequires
%endif

%install
%gopkginstall

%if %{without bootstrap}
%if %{with check}
%check
%gocheck
%endif
%endif

%gopkgfiles

%changelog
%autochangelog