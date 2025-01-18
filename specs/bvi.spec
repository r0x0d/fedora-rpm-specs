Name:           bvi
Version:        1.4.2
Release:        6%{?dist}
Summary:        Display-oriented editor for binary files
Summary(fr):    Afficheur orienté editeur pour fichiers binaires

License:        GPL-3.0-or-later
URL:            http://bvi.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.src.tar.gz

BuildRequires:  gcc
BuildRequires:  ncurses-devel
BuildRequires: make


%description
The bvi is a display-oriented editor for binary files, based
on the vi text-editor. If you are familiar with vi, just start
the editor and begin to edit! A bmore program is also
included in the package.

%description -l fr
Le bvi est un afficheur orienté éditeur pour fichiers binaires, basé sur
l'éditeur de texte vi. Si vi vous est familié, démarrez juste l'éditeur
et commencez à éditer! Un logiciel bmore est également inclu dans le
paquet.


%prep
%setup -q
# Fix the path of the bmore.help file specified in the man page :
sed -i "s@/usr/local/share/bmore.help@/usr/share/bvi/bmore.help@" ./bmore.1


%build
%configure
%make_build


%install
%make_install


%files
%doc README COPYING CREDITS CHANGES
%{_bindir}/%{name}
%{_bindir}/bmore
%{_bindir}/bvedit
%{_bindir}/bview
%{_datadir}/%{name}/
%{_mandir}/man1/*.1.*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 07 2023 Steven A. Falco <stevenfalco@gmail.com> - 1.4.2-1
- Update to 1.4.2

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 08 2022 Steven A. Falco <stevenfalco@gmail.com> - 1.4.1-9
- Convert license to SPDX format

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Tom Stellard <tstellar@redhat.com> - 1.4.1-3
- Use make macros
- https://fedoraproject.org/wiki/Changes/UseMakeBuildInstallMacro

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 12 2019 Steven A. Falco <stevenfalco@gmail.com> - 1.4.1-1
- Update to 1.4.1

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Nov 24 2014 Matthieu Saulnier <fantom@fedoraproject.org> - 1.4.0-1
- Update to 1.4.0 stable release

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0beta-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.0beta-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec 26 2013 Matthieu Saulnier <fantom@fedoraproject.org> - 1.4.0beta-0.1
- Update to 1.4.0beta
- Remove patch to move help file (upstream issue)
- Remove patch to fix empty debuginfo package (upstream issue)
- Fix FTBFS if "-Werror=format-security" flag is used (RHBZ#1037006) (upstream issue)
- Fix bogus date in %%changelog section

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 16 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 1.3.2-8
- Add French translation in spec file

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 07 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 1.3.2-6
- fix license in spec file

* Sat Dec 24 2011 Matthieu Saulnier <fantom@fedoraproject.org> - 1.3.2-5
- remove version macro in patches names
- cleanup sed statement

* Wed Dec 21 2011 Matthieu Saulnier <fantom@fedoraproject.org> - 1.3.2-4
- add comments for patches
- fix path of bmore.help specified in man page by sed

* Sun Dec 11 2011 Matthieu Saulnier <fantom@fedoraproject.org> - 1.3.2-3
- add patch to fix empty debuginfo package
- add patch to move help file

* Fri Dec 09 2011 Matthieu Saulnier <fantom@fedoraproject.org> - 1.3.2-2
- fix broken help function

* Thu Dec 08 2011 Matthieu Saulnier <fantom@fedoraproject.org> - 1.3.2-1
- Initial Release
