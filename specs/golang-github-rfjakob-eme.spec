# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/rfjakob/eme
%global goipath         github.com/rfjakob/eme
Version:                1.1.2

%gometa

%global common_description %{expand:
EME (ECB-Mix-ECB or, clearer, Encrypt-Mix-Encrypt) is a wide-block encryption
mode developed by Halevi and Rogaway in 2003.

EME uses multiple invocations of a block cipher to construct a new cipher of
bigger block size (in multiples of 16 bytes, up to 2048 bytes).}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        EME (Encrypt-Mix-Encrypt) wide-block encryption for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

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