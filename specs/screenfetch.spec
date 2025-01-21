Name:           screenfetch
Version:        3.9.1
Release:        13%{?dist}
Summary:        A "Bash Screenshot Information Tool"

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/KittyKatt/screenFetch
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
Recommends:     scrot
Requires:       pciutils

%description
This handy Bash script can be used to generate one of
those nifty terminal theme information + ASCII distribution
logos you see in everyone's screen-shots nowadays. It will
auto-detect your distribution and display an ASCII version
of that distribution's logo and some valuable information
to the right. There are options to specify no ASCII art,
colors, taking a screen-shot upon displaying info, and even
customizing the screen-shot command! This script is very easy
to add to and can easily be extended.

%prep
%setup -qn screenFetch-%{version}
sed -i -e '1s|.*|#!/bin/bash|' screenfetch-dev

%build
#Nothing to build

%install
install -m 755 -p -D screenfetch-dev %{buildroot}%{_bindir}/screenfetch
install -m 644 -p -D screenfetch.1 %{buildroot}%{_mandir}/man1/screenfetch.1

%files
%license COPYING
%doc CHANGELOG README.mkdn TODO
%{_bindir}/screenfetch
%{_mandir}/man1/screenfetch.1*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 3.9.1-12
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 3.9.1-2
- requires pciutils

* Sun Apr 26 2020 Eduard Lucena <x3mboy@fedoraproject.org> - 3.9.1-1
- Updating to version 3.9.1

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Mar 11 2017 Igor Gnatenko <ignatenko@redhat.com> - 3.8.0-1
- Update to 3.8.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 06 2015 Martín Buenahora <zironid@fedoraproject.org> - 3.7.0-2
- Added 'scrot' as a dependencie
- Fixed source URL

* Wed Jul 29 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.7.0-1
- Update to 3.7.0
- minor packaging fixes

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.6.5-2.20140929git0fb57330
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 18  2015 Martín Buenahora <zironid@fedoraproject.org> - 3.6.5-1.20140929git0fb57330
- Updated program to version 3.6.5

* Wed Sep 24 2014 Martín Buenahora <zironid@fedoraproject.org> - 3.6.2-7.20140914gitdec1cd6c
- Deleted dot tag from manpage location (not nedded)

* Wed Sep 24 2014 Martín Buenahora <zironid@fedoraproject.org> - 3.6.2-6.20140914gitdec1cd6c
- Changed manpage on files, to prevent crashes in the future if uncompressed manpages are used

* Mon Sep 15 2014 Martín Buenahora <zironid@fedoraproject.org> - 3.6.2-5.20140914gitdec1cd6c
- Removed mkdir from install
- Added -p -D flags to install command
- Recovered old changelog entries
- Changed Release tag to <release>.<date>git<git short commit>

* Sat Sep 13 2014 Martín Buenahora <zironid@fedoraproject.org> - 3.6.2-4.20140914gitdec1cd6c
- Changed summary to: A "Bash Screenshot Information Tool".
- Added doc tag in front of man page location
- Changed from capital to minuscule the f on the name

* Tue Sep 09 2014 Martin Buenahora <zironid@fedoraproject.org> - 3.6.2-3.20140914gitdec1cd6c
- Deleted the line rm -rf {buildroot} from install section (not needed)

* Tue May 20 2014 Martin Buenahora <zironid@fedoraproject.org> - 3.6.2-2.20140914gitdec1cd6c
- Installed the screenfetch-dev file as screenfetch
- Deleted clean section
- Deleted bash as depedency

* Mon May 19 2014 Martin Buenahora <zironid@fedoraproject.org> - 3.6.2-1.20140914gitdec1cd6c
- Initial version of the package
