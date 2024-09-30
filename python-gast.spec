Name:           python-gast
%global commit  bf62db902e3d6eb54af2467ad9f594256fbb826b
%global scommit %(c=%{commit}; echo ${c:0:8})
%global date    20240601
Version:        0.5.4^%{date}.%{scommit}
Release:        %autorelease
Summary:        Python AST that abstracts the underlying Python version
License:        BSD-3-Clause
URL:            https://github.com/serge-sans-paille/gast/
Source:         %{url}/archive/%{commit}/gast-%{scommit}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest


%global _description %{expand:
A generic AST to represent Python2 and Python3's Abstract Syntax Tree (AST).
GAST provides a compatibility layer between the AST of various Python versions,
as produced by ast.parse from the standard ast module.}
%description %_description


%package -n     python3-gast
Summary:        %{summary}

%description -n python3-gast %_description


%prep
%autosetup -p1 -n gast-%{commit}


%generate_buildrequires
# Don't use tox options to avoid an unwanted dependency in RHEL
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files gast


%check
%pytest -v


%files -n python3-gast -f %{pyproject_files}
%doc README.rst


%changelog
%autochangelog
