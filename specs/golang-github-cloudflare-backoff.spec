# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/cloudflare/backoff
%global goipath         github.com/cloudflare/backoff
%global commit          647f3cdfc87a18586e279c97afd6526d01b0d063

%gometa

%global common_description %{expand:
This package implements the backoff strategy described in the AWS Architecture
Blog article "Exponential Backoff And Jitter". Essentially, the backoff has an
interval time.Duration; the nth call to backoff will return an a time.Duration
that is 2 n * interval. If jitter is enabled (which is the default behaviour),
the duration is a random value between 0 and 2 n * interval. The backoff is
configured with a maximum duration that will not be exceeded; e.g., by default,
the longest duration returned is backoff.DefaultMaxDuration.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        Backoff timer shared between several projects

License:        BSD-2-Clause
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%gopkg

%prep
%goprep

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
