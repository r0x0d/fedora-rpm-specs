# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/yvasiyarov/gorelic
%global goipath         github.com/yvasiyarov/gorelic
Version:                0.0.7

%gometa

%global common_description %{expand:
New Relic agent for Go runtime. It collect a lot of metrics about scheduler,
garbage collector and memory allocator and send them to NewRelic.}

%global golicenses      LICENSE
%global godocs          examples README.md

Name:           %{goname}
Release:        %autorelease
Summary:        New relic agent for Go

# Upstream license specification: BSD-2-Clause
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/yvasiyarov/go-metrics)
BuildRequires:  golang(github.com/yvasiyarov/newrelic_platform_go)

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