# Generated by go2rpm
%bcond_without check

%global debug_package %{nil}

# https://github.com/wellington/go-libsass
%global goipath         github.com/wellington/go-libsass
Version:                0.9.2
%global commit          f870eaa15594bb64b1908df39d0812704f0ceb8f

%gometa

%global godevelheader %{expand:
Requires:       libsass-devel >= 3.5.4}

%global common_description %{expand:
Go wrapper for libsass, the only Sass 3.5 compiler for Go.}

%global golicenses      LICENSE
%global godocs          examples README.md docs

Name:           %{goname}
Release:        %autorelease
Summary:        Go wrapper for libsass, the only Sass 3.5 compiler for Go

# Upstream license specification: Apache-2.0
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{gosource}
# https://github.com/wellington/go-libsass/pull/83
Patch:          0001-Fix-build-with-Go-1.20.patch

BuildRequires:  golang(golang.org/x/net/context)
BuildRequires:  gcc-c++
BuildRequires:  libsass-devel >= 3.5.4

%description
%{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

# Remove bundled libsass.
rm -rf libsass-build
rm libs/wrap_main.go
for f in $(find -iname '*_dev.go'); do
    sed -e '/ +build dev/, 1d' $f > $f.new &&
    touch -r $f $f.new &&
    mv $f.new $f
done

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog