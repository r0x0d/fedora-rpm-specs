# Generated by go2rpm 1.6.0
# Tests stall in Mock
%bcond_with check
%global debug_package %{nil}


# https://github.com/thoj/go-ircevent
%global goipath         github.com/thoj/go-ircevent
Version:                0.2
%global tag             0.2
%global commit          73e444401d645f686b4aa9adcab88fa78cf85a4f

%gometa

%global common_description %{expand:
Event based IRC client library in Go (golang).}

%global golicenses      LICENSE
%global godocs          examples README.markdown

Name:           %{goname}
Release:        %autorelease
Summary:        Event based IRC client library in Go (golang)

# Upstream license specification: BSD-3-Clause
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(golang.org/x/net/proxy)
BuildRequires:  golang(golang.org/x/text/encoding)

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