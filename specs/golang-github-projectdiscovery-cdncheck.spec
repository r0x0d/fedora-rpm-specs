# Generated by go2rpm 1.9.0
%bcond_without check
%bcond_with network
%global debug_package %{nil}

# https://github.com/projectdiscovery/cdncheck
%global goipath         github.com/projectdiscovery/cdncheck
Version:                1.0.9

%gometa -f


%global common_description %{expand:
A utility to detect various technology for a given IP address.}

%global golicenses      LICENSE.md
%global godocs          examples README.md

%global gosupfiles      sources_data.json

Name:           %{goname}
Release:        %autorelease
Summary:        A utility to detect various technology for a given IP address

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

%if %{with network}
%if %{with check}
%check
%gocheck
%endif
%endif

%gopkgfiles

%changelog
%autochangelog