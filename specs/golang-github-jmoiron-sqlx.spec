# Generated by go2rpm 1.6.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/jmoiron/sqlx
%global goipath         github.com/jmoiron/sqlx
Version:                1.3.5

%gometa

%global common_description %{expand:
Sqlx is a library which provides a set of extensions on Go's standard
database/sql library. The sqlx versions of sql.DB, sql.TX, sql.Stmt, et al. all
leave the underlying interfaces untouched, so that their interfaces are a
superset on the standard ones. This makes it relatively painless to integrate
existing codebases using database/sql with sqlx.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        General purpose extensions to golang's database/sql

License:        MIT
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