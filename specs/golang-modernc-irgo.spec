# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://gitlab.com/cznic/irgo
%global goipath         modernc.org/irgo
%global forgeurl        https://gitlab.com/cznic/irgo
Version:                1.0.0
%global tag             v%{version}

%gometa -f

%global common_description %{expand:
Translates intermediate representations to Go.}

%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Translates intermediate representations to Go

License:        BSD-3-Clause
URL:            %{gourl}
Source:         %{gosource}
Patch0001:      irgo-v1.0.0-include-internal-buffer.patch

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
# .: uses internal package modernc.org/internal/buffer
%gocheck -d .
%endif

%gopkgfiles

%changelog
%autochangelog