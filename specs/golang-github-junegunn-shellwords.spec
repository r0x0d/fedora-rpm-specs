# Generated by go2rpm 1.14.0
%bcond check 1
%bcond bootstrap 0

%global debug_package %{nil}
%if %{with bootstrap}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^golang\\(.*\\)$
%endif

# https://github.com/junegunn/go-shellwords
%global goipath         github.com/junegunn/go-shellwords
%global commit          a62c48c52e972b3ab9f6874bb5313e55e9673638

%gometa -L -f

%global common_description %{expand:
Parse line as shell words.}

%global golicenses      LICENSE
%global godocs          _example README.md

Name:           golang-github-junegunn-shellwords
Version:        0
Release:        %autorelease -p
Summary:        Parse line as shell words

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