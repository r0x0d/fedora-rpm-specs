# Generated by go2rpm
# Dead upstream
%ifnarch aarch64 ppc64le s390x
%bcond_without check
%endif

%global debug_package %{nil}

# https://github.com/BurntSushi/graphics-go
%global goipath         github.com/BurntSushi/graphics-go
%global commit          b43f31a4a96688fba0b612e25e22648b9267e498

%gometa

# Remove in F33:
%global godevelheader %{expand:
Obsoletes:      golang-github-BurntSushi-graphics-go-devel < 0-0.7
}

%global common_description %{expand:
This is a Graphics library for the Go programming language.}

%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README

Name:           %{goname}
Version:        0
Release:        %autorelease
Summary:        Graphics library for the Go programming language

# Upstream license specification: BSD-3-Clause
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{gosource}

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