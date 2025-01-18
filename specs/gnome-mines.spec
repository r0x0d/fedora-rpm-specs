%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           gnome-mines
Version:        40.1
Release:        10%{?dist}
Summary:        GNOME Mines Sweeper game

License:        GPL-3.0-or-later AND CC-BY-SA-3.0
URL:            https://wiki.gnome.org/Apps/Mines
Source0:        https://download.gnome.org/sources/gnome-mines/40/gnome-mines-%{tarball_version}.tar.xz

Requires:       rsvg-pixbuf-loader

BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libgnome-games-support-1)
BuildRequires:  pkgconfig(librsvg-2.0)

BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  vala

%description
The popular logic puzzle minesweeper. Find mines on a grid 
using hints from squares you have already cleared.


%prep
%autosetup -p1 -n gnome-mines-%{tarball_version}


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name} --with-gnome


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Mines.desktop


%files -f %{name}.lang
%license COPYING
%{_bindir}/gnome-mines
%{_datadir}/applications/org.gnome.Mines.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Mines.gschema.xml
%{_datadir}/gnome-mines/
%{_datadir}/icons/hicolor/*/apps/org.gnome.Mines*svg
%{_datadir}/metainfo/org.gnome.Mines.appdata.xml
%{_mandir}/man6/gnome-mines.6*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 40.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 40.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb  2 2024 Yanko Kaneti <yaneti@declera.com> - 40.1-8
- SPDX migration. License update to reflect (not so recent) upstream change

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 40.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 40.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Oct 25 2023 Yanko Kaneti <yaneti@declera.com> - 40.1-5
- Require rsvg-pixbuf-loader for svg theme images support #2211205

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 40.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 40.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 40.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Feb 18 2022 David King <amigadave@amigadave.com> - 40.1-1
- Update to 40.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 40.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar 22 2021 Kalev Lember <klember@redhat.com> - 40.0-1
- Update to 40.0

* Mon Mar 15 2021 Kalev Lember <klember@redhat.com> - 40~rc-1
- Update to 40.rc

* Fri Feb 19 2021 Kalev Lember <klember@redhat.com> - 40~alpha-1
- Update to 40.alpha

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 17 2020 Kalev Lember <klember@redhat.com> - 3.36.1-1
- Update to 3.36.1

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.36.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 08 2020 Kalev Lember <klember@redhat.com> - 3.36.0-1
- Update to 3.36.0

* Sun Feb  2 2020 Yanko Kaneti <yaneti@declera.com> - 3.35.90-1
- Update to 3.35.90

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.34.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Kalev Lember <klember@redhat.com> - 3.34.0-1
- Update to 3.34.0

* Tue Sep 03 2019 Kalev Lember <klember@redhat.com> - 3.33.92-1
- Update to 3.33.92

* Mon Aug 19 2019 Kalev Lember <klember@redhat.com> - 3.33.91-1
- Update to 3.33.91

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.33.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Yanko Kaneti <yaneti@declera.com> - 3.33.3-1
- Update to 3.33.3

* Mon May 06 2019 Yanko Kaneti <yaneti@declera.com> - 3.32.2-1
- Update to 3.32.2

* Mon Mar 11 2019 Kalev Lember <klember@redhat.com> - 3.32.0-1
- Update to 3.32.0

* Tue Mar 05 2019 Kalev Lember <klember@redhat.com> - 3.31.92-1
- Update to 3.31.92

* Mon Feb 18 2019 Kalev Lember <klember@redhat.com> - 3.31.91-1
- Update to 3.31.91

* Mon Feb 04 2019 Yanko Kaneti <yaneti@declera.com> - 3.31.90-1
- Update to 3.31.90

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.31.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Yanko Kaneti <yaneti@declera.com> - 3.31.4.1-1
- Update to 3.31.4.1. Drop patch.

* Tue Jan 08 2019 Yanko Kaneti <yaneti@declera.com> - 3.31.4-2
- Fix crash on preferences

* Mon Jan 07 2019 Kalev Lember <klember@redhat.com> - 3.31.4-1
- Update to 3.31.4

* Tue Dec 11 2018 Yanko Kaneti <yaneti@declera.com> - 3.31.3-1
- Update to 3.31.3

* Tue Oct 09 2018 Kalev Lember <klember@redhat.com> - 3.31.1-1
- Update to 3.31.1

* Wed Sep 26 2018 Yanko Kaneti <yaneti@declera.com> - 3.30.1.1-1
- Update to 3.30.1.1. Drop upstreamed workaround

* Wed Sep 26 2018 Kalev Lember <klember@redhat.com> - 3.30.1-1
- Update to 3.30.1

* Tue Sep 11 2018 Yanko Kaneti <yaneti@declera.com> - 3.30.0-2
- Workaround recent glib changes by removing flag-symbolic.svg

* Tue Sep  4 2018 Yanko Kaneti <yaneti@declera.com> - 3.30.0-1
- Update to 3.30.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.29.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Yanko Kaneti <yaneti@declera.com> - 3.29.3-1
- Update to 3.29.3

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 3.28.0-1
- Update to 3.28.0

* Mon Mar 12 2018 Kalev Lember <klember@redhat.com> - 3.27.92.1-1
- Update to 3.27.92.1
- Switch to the meson build system

* Mon Mar  5 2018 Yanko Kaneti <yaneti@declera.com> - 3.27.92-1
- Update to 3.27.92
- Go back to autotools because upstream can't make their mind

* Mon Feb 19 2018 Yanko Kaneti <yaneti@declera.com> - 3.27.90-3
- Rebuild for libgnome-games-support soname bump

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.27.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Feb  5 2018 Yanko Kaneti <yaneti@declera.com> - 3.27.90-1
- Update to 3.27.90. Switch to meson

* Fri Jan 05 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3.27.2-2
- Remove obsolete scriptlets

* Tue Nov 14 2017 Yanko Kaneti <yaneti@declera.com> - 3.27.2-1
- Update to 3.27.2

* Mon Sep 11 2017 Yanko Kaneti <yaneti@declera.com> - 3.26.0-1
- Update to 3.26.0

* Tue Sep  5 2017 Yanko Kaneti <yaneti@declera.com> - 3.25.92-1
- Update to 3.25.92

* Tue Aug 22 2017 Yanko Kaneti <yaneti@declera.com> - 3.25.91-1
- Update to 3.25.91

* Sun Aug 13 2017 Yanko Kaneti <yaneti@declera.com> - 3.25.90-1
- Update to 3.25.90

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.25.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 23 2017 Yanko Kaneti <yaneti@declera.com> - 3.25.2-1
- Update to 3.25.2

* Tue Mar 21 2017 Yanko Kaneti <yaneti@declera.com> - 3.24.0-1
- Update to 3.24.0

* Tue Feb 28 2017 Yanko Kaneti <yaneti@declera.com> - 3.23.91-1
- Update to 3.23.91

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.23.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 22 2016 Yanko Kaneti <yaneti@declera.com> - 3.23.2-1
- Update to 3.23.2

* Tue Nov  8 2016 Yanko Kaneti <yaneti@declera.com> - 3.22.2-1
- Update to 3.22.2

* Mon Oct 10 2016 Yanko Kaneti <yaneti@declera.com> - 3.22.1-1
- Update to 3.22.1

* Mon Sep 19 2016 Kalev Lember <klember@redhat.com> - 3.22.0-1
- Update to 3.22.0

* Tue Sep 13 2016 Yanko Kaneti <yaneti@declera.com> - 3.21.92-1
- Update to 3.21.92

* Tue Aug 30 2016 Yanko Kaneti <yaneti@declera.com> - 3.21.91-1
- Update to 3.21.91

* Thu Aug 18 2016 Kalev Lember <klember@redhat.com> - 3.21.90.1-1
- Update to 3.21.90.1

* Thu Aug 18 2016 Kalev Lember <klember@redhat.com> - 3.21.90-1
- Update to 3.21.90
- Move desktop file validation to the check section

* Tue Jun 21 2016 Yanko Kaneti <yaneti@declera.com> - 3.21.3-1
- Update to 3.21.3. Drop old obsoletes. Use pkgconfig BR

* Tue Jun 14 2016 Yanko Kaneti <yaneti@declera.com> - 3.20.1-1
- Update to 3.20.1

* Tue Mar 22 2016 Yanko Kaneti <yaneti@declera.com> - 3.20.0-1
- Update to 3.20.0

* Mon Mar 14 2016 Yanko Kaneti <yaneti@declera.com> - 3.19.91-1
- Update to 3.19.91

* Tue Feb 16 2016 Yanko Kaneti <yaneti@declera.com> - 3.19.90-1
- Update to 3.19.90. Drop upstreamed fixes.

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.19.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Yanko Kaneti <yaneti@declera.com> - 3.19.4-1
- Update to 3.19.4
- Fixup some desktop translations

* Mon Dec 14 2015 Yanko Kaneti <yaneti@declera.com> - 3.19.3-1
- Update to 3.19.3

* Tue Nov 24 2015 Yanko Kaneti <yaneti@declera.com> - 3.19.2-1
- Update to 3.19.2

* Tue Oct 27 2015 Yanko Kaneti <yaneti@declera.com> - 3.19.1-1
- First release on the next development branch

* Mon Oct 12 2015 Kalev Lember <klember@redhat.com> - 3.18.1-1
- Update to 3.18.1

* Mon Sep 21 2015 Kalev Lember <klember@redhat.com> - 3.18.0-1
- Update to 3.18.0

* Mon Sep 14 2015 Kalev Lember <klember@redhat.com> - 3.17.92-1
- Update to 3.17.92

* Mon Aug 31 2015 Kalev Lember <klember@redhat.com> - 3.17.91-1
- Update to 3.17.91
- Use make_install macro

* Mon Aug 17 2015 Yanko Kaneti <yaneti@declera.com> - 3.17.90-1
- Update to 3.17.90

* Mon Jul 20 2015 Yanko Kaneti <yaneti@declera.com> - 3.17.4-1
- Update to 3.17.4

* Tue Jun 23 2015 Yanko Kaneti <yaneti@declera.com> - 3.17.3-1
- Update to 3.17.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Yanko Kaneti <yaneti@declera.com> - 3.17.2-1
- Update to 3.17.2

* Tue Apr 14 2015 Yanko Kaneti <yaneti@declera.com> - 3.16.1-1
- Update to 3.16.1
- No more separate HighContrast icons

* Mon Mar 23 2015 Yanko Kaneti <yaneti@declera.com> - 3.16.0-1
- Update to 3.16.0
- Use license macro

* Mon Mar 16 2015 Yanko Kaneti <yaneti@declera.com> - 3.15.92-1
- Update to 3.15.92

* Mon Mar  2 2015 Yanko Kaneti <yaneti@declera.com> - 3.15.91-1
- Update to 3.15.91

* Mon Feb 16 2015 Yanko Kaneti <yaneti@declera.com> - 3.15.90-1
- Update to 3.15.90

* Mon Jan 19 2015 Yanko Kaneti <yaneti@declera.com> - 3.15.4-1
- Update to 3.15.4

* Mon Dec 15 2014 Yanko Kaneti <yaneti@declera.com> - 3.15.3-1
- Update to 3.15.3

* Mon Oct 27 2014 Yanko Kaneti <yaneti@declera.com> - 3.15.1-1
- First devlopment release from the 3.16 cycle

* Mon Oct 13 2014 Yanko Kaneti <yaneti@declera.com> - 3.14.1-1
- Update to 3.14.1

* Mon Sep 22 2014 Yanko Kaneti <yaneti@declera.com> - 3.14.0-1
- Update to 3.14.0

* Tue Sep 16 2014 Yanko Kaneti <yaneti@declera.com> - 3.13.92-1
- Update to 3.13.92

* Mon Sep 01 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.91-1
- Update to 3.13.91

* Tue Aug 19 2014 Yanko Kaneti <yaneti@declera.com> - 3.13.90-1
- Update to 3.13.90
- Add HighContrast theme

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 21 2014 Kalev Lember <kalevlember@gmail.com> - 3.13.4-1
- Update to 3.13.4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 27 2014 Yanko Kaneti <yaneti@declera.com> - 3.13.2-1
- Update to 3.13.2

* Mon Apr 28 2014 Yanko Kaneti <yaneti@declera.com> - 3.13.1-1
- First release from the new development cycle.
- Drop upstreamd patch and vala from BR.

* Wed Apr 16 2014 Yanko Kaneti <yaneti@declera.com> - 3.12.1-2
- Upstream patch to fix game pausing.

* Tue Apr 15 2014 Yanko Kaneti <yaneti@declera.com> - 3.12.1-1
- Update to 3.12.1

* Mon Mar 24 2014 Richard Hughes <rhughes@redhat.com> - 3.12.0-1
- Update to 3.12.0

* Tue Mar 18 2014 Yanko Kaneti <yaneti@declera.com> - 3.11.92-1
- Update to 3.11.92

* Tue Feb 18 2014 Yanko Kaneti <yaneti@declera.com> - 3.11.90-1
- Update to 3.11.90. Desktop file renamed.

* Tue Dec 17 2013 Yanko Kaneti <yaneti@declera.com> - 3.11.3-1
- Update to 3.11.3. New url.

* Tue Oct 29 2013 Richard Hughes <rhughes@redhat.com> - 3.11.1-1
- Update to 3.11.1

* Sat Oct 12 2013 Yanko Kaneti <yaneti@declera.com> - 3.10.1-1
- Update to 3.10.1

* Mon Sep 23 2013 Yanko Kaneti <yaneti@declera.com> - 3.10.0-1
- Update to 3.10.0

* Tue Sep 17 2013 Yanko Kaneti <yaneti@declera.com> - 3.9.92-1
- Update to 3.9.92
- Add appdata

* Wed Aug 21 2013 Yanko Kaneti <yaneti@declera.com> - 3.9.90-1
- Update to 3.9.90

* Tue Aug 20 2013 Yanko Kaneti <yaneti@declera.com> - 3.8.2-1
- Update to 3.8.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-3
- Obsolete gnome-games-help as well

* Thu Jun 20 2013 Matthias Clasen <mclasen@redhat.com> - 3.8.1-2
- Obsolete gnome-games (for upgrades from f17)

* Mon Apr 15 2013 Kalev Lember <kalevlember@gmail.com> - 3.8.1-1
- Update to 3.8.1

* Wed Mar 27 2013 Yanko Kaneti <yaneti@declera.com> - 3.8.0-1
- Update to 3.8.0

* Tue Mar 19 2013 Yanko Kaneti <yaneti@declera.com> - 3.7.92-1
- Update to 3.7.92

* Fri Feb 15 2013 Yanko Kaneti <yaneti@declera.com> - 3.7.5-1
- Initial packaging of standalone gnome-mines
