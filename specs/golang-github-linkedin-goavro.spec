# Generated by go2rpm
# https://github.com/linkedin/goavro/issues/214
%ifnarch %{arm} %{ix86}
%global debug_package %{nil}

%bcond_without check
%endif

# https://github.com/linkedin/goavro
%global goipath         github.com/linkedin/goavro
Version:                2.10.0

%gometa

%global goaltipaths     github.com/linkedin/goavro/v2

%global common_description %{expand:
Goavro is a library that encodes and decodes Avro data.}

%global golicenses      LICENSE
%global godocs          examples AUTHORS README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Library that encodes and decodes Avro data

# Upstream license specification: Apache-2.0
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/golang/snappy)

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
