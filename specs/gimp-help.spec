# NOTE: en/English is in the main package
# LANGUAGES: bg,Bulgarian ca,Catalan cs,Czech da,Danish de,German el,Greek en_GB,British_English es,Spanish fa,Farsi fi,Finnish fr,French hr,Croatian hu,Hungarian it,Italian ja,Japanese ko,Korean lt,Lithuanian nl,Dutch nn,Norwegian_Nynorsk pl,Polish pt,Portuguese pt_BR,Brazilian_Portuguese ro,Romanian ru,Russian sl,Slovenian sv,Swedish tr,Turkish uk,Ukrainian zh_CN,Simplified_Chinese

%constrain_build -m 6144

%global gimpsubver 3.0

Summary: Help files for GIMP
Name: gimp-help
Version: 2.99.0~20250212git2b4f24e36
Release: %autorelease
License: GFDL-1.2-invariants-only
URL: https://docs.gimp.org/
BuildArch: noarch
# https://bugzilla.redhat.com/show_bug.cgi?id=2318369
ExcludeArch: s390x

# Compute some version related macros.

# In the case of a snapshot version (e.g. "Version: 2.99.19^20240814git256e0ca5a0"), this computes
# the "plain" version (as defined in upstream sources), %%snapshot and %%git_rev macros. In the case
# of a normal release, %%plain_version will be the same as %%version.
%global plain_version %{lua:
    local plain_version = (string.gsub(macros.version, '^(.*)[%^~].*$', '%1'))
    print(plain_version)
    if plain_version ~= macros.version then
        macros.snapshot = (string.gsub(macros.version, '^.*[%^~](.*)$', '%1'))
        macros.git_rev = (string.gsub(macros.snapshot, '^.*git(.*)$', '%1'))
    end
}

%if ! %defined snapshot
Source0: https://download.gimp.org/pub/gimp/help/gimp-help-%{version}.tar.xz
%else
Source0: gimp-help-%{plain_version}-git%{git_rev}.tar.xz
%endif

BuildRequires: dblatex
# BuildRequires: docbook2odf [orphaned]
BuildRequires: docbook-style-xsl
BuildRequires: gnome-doc-utils
BuildRequires: libxml2-python3
BuildRequires: libxslt
BuildRequires: pkgconfig >= 0.9.0
BuildRequires: gimp-devel >= 2:3.0.0~RC1
BuildRequires: gettext
BuildRequires: graphviz
BuildRequires: pngnq
BuildRequires: pngcrush
BuildRequires: python3
BuildRequires: make
Requires: gimp >= 2:3.0.0~RC1
# BEGIN: OBSOLETE LANGUAGES
# END: OBSOLETE LANGUAGES
%description
This package contains a user manual written for the GNU Image Manipulation
Program.

# BEGIN: LANGUAGE SUB PACKAGES
%package bg
Summary: Bulgarian (bg) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-bg)

%description bg
Bulgarian language support for gimp-help.

%package ca
Summary: Catalan (ca) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-ca)

%description ca
Catalan language support for gimp-help.

%package cs
Summary: Czech (cs) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-cs)

%description cs
Czech language support for gimp-help.

%package da
Summary: Danish (da) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-da)

%description da
Danish language support for gimp-help.

%package de
Summary: German (de) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-de)

%description de
German language support for gimp-help.

%package el
Summary: Greek (el) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-el)

%description el
Greek language support for gimp-help.

%package en_GB
Summary: British English (en_GB) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-en_GB)

%description en_GB
British English language support for gimp-help.

%package es
Summary: Spanish (es) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-es)

%description es
Spanish language support for gimp-help.

%package fa
Summary: Farsi (fa) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-fa)

%description fa
Farsi language support for gimp-help.

%package fi
Summary: Finnish (fi) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-fi)

%description fi
Finnish language support for gimp-help.

%package fr
Summary: French (fr) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-fr)

%description fr
French language support for gimp-help.

%package hr
Summary: Croatian (hr) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-hr)

%description hr
Croatian language support for gimp-help.

%package hu
Summary: Hungarian (hu) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-hu)

%description hu
Hungarian language support for gimp-help.

%package it
Summary: Italian (it) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-it)

%description it
Italian language support for gimp-help.

%package ja
Summary: Japanese (ja) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-ja)

%description ja
Japanese language support for gimp-help.

%package ko
Summary: Korean (ko) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-ko)

%description ko
Korean language support for gimp-help.

%package lt
Summary: Lithuanian (lt) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-lt)

%description lt
Lithuanian language support for gimp-help.

%package nl
Summary: Dutch (nl) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-nl)

%description nl
Dutch language support for gimp-help.

%package nn
Summary: Norwegian Nynorsk (nn) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-nn)

%description nn
Norwegian Nynorsk language support for gimp-help.

%package pl
Summary: Polish (pl) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-pl)

%description pl
Polish language support for gimp-help.

%package pt
Summary: Portuguese (pt) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-pt)

%description pt
Portuguese language support for gimp-help.

%package pt_BR
Summary: Brazilian Portuguese (pt_BR) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-pt_BR)

%description pt_BR
Brazilian Portuguese language support for gimp-help.

%package ro
Summary: Romanian (ro) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-ro)

%description ro
Romanian language support for gimp-help.

%package ru
Summary: Russian (ru) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-ru)

%description ru
Russian language support for gimp-help.

%package sl
Summary: Slovenian (sl) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-sl)

%description sl
Slovenian language support for gimp-help.

%package sv
Summary: Swedish (sv) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-sv)

%description sv
Swedish language support for gimp-help.

%package tr
Summary: Turkish (tr) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-tr)

%description tr
Turkish language support for gimp-help.

%package uk
Summary: Ukrainian (uk) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-uk)

%description uk
Ukrainian language support for gimp-help.

%package zh_CN
Summary: Simplified Chinese (zh_CN) language support for gimp-help
Requires: %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Supplements: (%{name} = %{?epoch:%{epoch}:}%{version}-%{release} and langpacks-zh_CN)

%description zh_CN
Simplified Chinese language support for gimp-help.

# END: LANGUAGE SUB PACKAGES

%prep
%setup -q -n gimp-help-%{plain_version}

%build
%configure
# Building gimp-help in parallel is flaky 😬. Do as much as possible in parallel, then attempt to
# fix.
make -k %{?_smp_mflags} || make

%install
make DESTDIR=%{buildroot} install

rm -f files.list.*
f="$PWD/files.list"

pushd %{buildroot}%{_datadir}/gimp/%{gimpsubver}/help
for lang in *; do
    [ "$lang" = "pdf" ] && continue
    echo "%%lang($lang) %%{_datadir}/gimp/%%{gimpsubver}/help/$lang" > "$f.$lang"
done
cd pdf
for pdf in *.pdf; do
    l="${pdf%.pdf}"
    l="${l#gimp-keys-}"
    if [ ! -d "../$l" ]; then
        rm -f "$pdf"
    else
        echo "%%lang($lang) %%{_datadir}/gimp/%%{gimpsubver}/help/pdf/$pdf" >> "$f.$lang"
    fi
done
popd

%files
%dir %{_datadir}/gimp/%{gimpsubver}/help
%{_datadir}/gimp/%{gimpsubver}/help/en
%doc AUTHORS ChangeLog NEWS README.md TERMINOLOGY
%license COPYING

# BEGIN: LANGUAGE FILE LISTS
%files bg -f files.list.bg
%files ca -f files.list.ca
%files cs -f files.list.cs
%files da -f files.list.da
%files de -f files.list.de
%files el -f files.list.el
%files en_GB -f files.list.en_GB
%files es -f files.list.es
%files fa -f files.list.fa
%files fi -f files.list.fi
%files fr -f files.list.fr
%files hr -f files.list.hr
%files hu -f files.list.hu
%files it -f files.list.it
%files ja -f files.list.ja
%files ko -f files.list.ko
%files lt -f files.list.lt
%files nl -f files.list.nl
%files nn -f files.list.nn
%files pl -f files.list.pl
%files pt -f files.list.pt
%files pt_BR -f files.list.pt_BR
%files ro -f files.list.ro
%files ru -f files.list.ru
%files sl -f files.list.sl
%files sv -f files.list.sv
%files tr -f files.list.tr
%files uk -f files.list.uk
%files zh_CN -f files.list.zh_CN
# END: LANGUAGE FILE LISTS

%changelog
%autochangelog
