# Generated by go2rpm 1
%bcond_without check

%global debug_package %{nil}

# https://github.com/cucumber/gherkin-go
%global goipath         github.com/cucumber/gherkin-go
Version:                21.0.0

%gometa

%global goaltipaths     github.com/cucumber/gherkin-go/v21

%global common_description %{expand:
Gherkin parser/compiler for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Gherkin parser/compiler for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/cucumber/messages-go/v17)

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep
sed -i 's|"github.com/cucumber/common/gherkin/go/v21|"github.com/cucumber/gherkin-go|' $(find . -iname "*.go" -type f)
sed -i 's|"github.com/cucumber/common/messages/go/v17|"github.com/cucumber/messages-go/v17|' $(find . -iname "*.go" -type f)

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog