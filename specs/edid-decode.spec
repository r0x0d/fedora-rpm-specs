%global codate 20241118
%global commit 4bdd7790f41516e191332cc3680b0030e439c4f0
%global shortcommit %(c=%{commit}; echo ${c:0:8})

Name:           edid-decode
Version:        0
Release:        %autorelease -s %{codate}git%{shortcommit}
Summary:        Decode EDID data in human-readable format

License:        MIT
URL:            https://git.linuxtv.org/edid-decode.git/
Source0:        edid-decode-%{shortcommit}.tar.xz
Source1:        edid-decode-snapshot.sh

BuildRequires:  gcc-c++
BuildRequires:  meson

Conflicts:	xorg-x11-utils < 7.5-33

%description
Decodes raw monitor EDID data in human-readable format.


%prep
%setup -q -n %{name}


%build
%meson
%meson_build


%install
%meson_install


%files
%doc README
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*


%changelog
%autochangelog
