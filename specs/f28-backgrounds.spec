%global relnum 28
%global Bg_Name F%{relnum}
%global bgname %(t="%{Bg_Name}";echo ${t,,})

# Enable Animation
%global with_animated 0

# Enable Extras
%global with_extras 1

Name:		%{bgname}-backgrounds
Version:	%{relnum}.1.5
Release:	16%{?dist}
Summary:	Fedora %{relnum} default desktop background

License:	CC-BY-SA-4.0
URL:		https://fedoraproject.org/wiki/F%{relnum}_Artwork
Source0:	https://github.com/fedoradesign/backgrounds/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Plasma desktoptheme
Source1:	metadata.desktop

BuildArch:	noarch

BuildRequires: make

Requires:	%{name}-gnome = %{version}-%{release}
Requires:	%{name}-kde = %{version}-%{release}
Requires:	%{name}-xfce = %{version}-%{release}
Requires:	%{name}-mate = %{version}-%{release}


%description
This package contains desktop backgrounds for the Fedora %{relnum} default
theme.  Pulls in themes for GNOME, KDE, Mate and Xfce desktops.

%package	base
Summary:	Base images for Fedora %{relnum} default background
License:	CC-BY-SA-4.0

%description	base
This package contains base images for Fedora %{relnum} default background.

%if %{with_animated}
%package	animated
Summary:	Time of day images for Fedora %{relnum} backgrounds

Requires:	%{name}-base = %{version}-%{release}

%description	animated
This package contains the time of day images for Fedora %{relnum} 
Backgrounds.
%endif

%package	kde
Summary:	Fedora %{relnum} default wallpaper for KDE

Requires:	%{name}-base = %{version}-%{release}
Requires:	kde-filesystem
Supplements:	%{name}-animated = %{version}-%{release}

%description    kde
This package contains KDE desktop wallpaper for the Fedora %{relnum}
default them

%package	gnome
Summary:	Fedora %{relnum} default wallpaper for Gnome and Cinnamon

Requires:	%{name}-base = %{version}-%{release}
Supplements:	%{name}-animated = %{version}-%{release}

%description	gnome
This package contains Gnome/Cinnamon desktop wallpaper for the
Fedora %{relnum} default theme.

%package	mate
Summary:	Fedora %{relnum} default wallpaper for Mate

Requires:	%{name}-base = %{version}-%{release}
Supplements:	%{name}-animated = %{version}-%{release}

%description	mate
This package contains Mate desktop wallpaper for the Fedora %{relnum}
default theme.

%package	xfce
Summary:	Fedora %{relnum} default background for XFCE4

Requires:	%{name}-base = %{version}-%{release}
Requires:	xfdesktop

%description	xfce
This package contains XFCE4 desktop background for the Fedora %{relnum}
default theme.

%if %{with_extras}
%package	extras-base
Summary:	Base images for F%{relnum} Extras Backrounds
# Automatically converted from old format: CC-BY and CC-BY-SA - review is highly recommended.
License:	LicenseRef-Callaway-CC-BY AND LicenseRef-Callaway-CC-BY-SA

%description	extras-base
This package contains base images for F%{relnum} supplemental
wallpapers.

%package	extras-gnome
Summary:	Extra F%{relnum} Wallpapers for Gnome and Cinnamon
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:	%{name}-extras-base = %{version}-%{release}

%description	extras-gnome
This package contains F%{relnum} supplemental wallpapers for Gnome
and Cinnamon

%package	extras-mate
Summary:	Extra F%{relnum} Wallpapers for Mate
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:	%{name}-extras-base = %{version}-%{release}

%description    extras-mate
This package contains F%{relnum} supplemental wallpapers for Mate

%package	extras-kde
Summary:	Extra F%{relnum} Wallpapers for KDE
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:	%{name}-extras-base = %{version}-%{release}

%description	extras-kde
This package contains F%{relnum} supplemental wallpapers for Gnome

%package	extras-xfce
Summary:	Extra F%{relnum} Wallpapers for XFCE
License:        CC-BY-4.0 and CC-BY-SA-4.0 and CC0-1.0 and copyleft-next-0.3.1
Requires:	%{name}-extras-base = %{version}-%{release}

%description	extras-xfce
This package contains F%{relnum} supplemental wallpapers for XFCE
%endif

%prep
%autosetup -n %{name}


%build
%make_build


%install
%make_install

install -D -p -m644 %{SOURCE1} \
%{buildroot}%{_datadir}/plasma/desktoptheme/%{Bg_Name}/metadata.desktop

%files
%doc

%files base
%license CC-BY-SA-4.0 Attribution
%dir %{_datadir}/backgrounds/%{bgname}
%dir %{_datadir}/backgrounds/%{bgname}/default
%{_datadir}/backgrounds/%{bgname}/default/normalish
%{_datadir}/backgrounds/%{bgname}/default/standard
%{_datadir}/backgrounds/%{bgname}/default/wide
%{_datadir}/backgrounds/%{bgname}/default/tv-wide
%{_datadir}/backgrounds/%{bgname}/default/%{bgname}.xml

%if %{with_animated}
%files animated
%dir %{_datadir}/backgrounds/%{bgname}/default-animated
%{_datadir}/backgrounds/%{bgname}/default-animated/normalish
%{_datadir}/backgrounds/%{bgname}/default-animated/standard
%{_datadir}/backgrounds/%{bgname}/default-animated/wide
%{_datadir}/backgrounds/%{bgname}/default-animated/tv-wide
%{_datadir}/backgrounds/%{bgname}/default-animated/%{bgname}.xml
%endif

%files kde
%{_datadir}/wallpapers/%{Bg_Name}/
%dir %{_datadir}/plasma/
%dir %{_datadir}/plasma/desktoptheme/
%{_datadir}/plasma/desktoptheme/%{Bg_Name}/

%files gnome
%{_datadir}/gnome-background-properties/%{bgname}.xml
%if %{with_animated}
%{_datadir}/gnome-background-properties/%{bgname}-animated.xml
%endif
%dir %{_datadir}/gnome-background-properties/

%files mate
%{_datadir}/mate-background-properties/%{bgname}.xml
%if %{with_animated}
%{_datadir}/mate-background-properties/%{bgname}-animated.xml
%endif
%dir %{_datadir}/mate-background-properties/

%files xfce
%{_datadir}/xfce4/backdrops/%{bgname}.png
%dir %{_datadir}/xfce4/
%dir %{_datadir}/xfce4/backdrops/

%if %{with_extras}
%files extras-base
%license CC-BY-SA-4.0 CC-BY-4.0 CC0-1.0 Attribution-Extras
%{_datadir}/backgrounds/%{bgname}/extras/

%files extras-gnome
%{_datadir}/gnome-background-properties/%{bgname}-extras.xml

%files extras-kde
%{_datadir}/wallpapers/%{Bg_Name}_*/

%files extras-mate
%{_datadir}/mate-background-properties/%{bgname}-extras.xml

%files extras-xfce
%{_datadir}/xfce4/backdrops/
%endif

%changelog
* Mon Dec 02 2024 David Auer <dreua@posteo.de> - 28.1.5-16
- Fix build on f40+

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 28.1.5-15
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 28.1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 28.1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 28.1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 28.1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 28.1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 28.1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 28.1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 28.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 28.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 28.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 28.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 28.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 28.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon May 21 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 28.1.5-1
- Update to 28.1.5

* Thu Apr 26 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 28.1.4-1
- Update to 28.1.4

* Tue Apr 17 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 28.1.3-1
- Update to 28.1.3

* Tue Apr 10 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 28.1.2-1
- Update to 28.1.2

* Mon Apr 09 2018 Luya Tshimbalanga <luya@fedoraproject.org> - 28.1.1-1
- Update to 28.1.1

* Sun Dec 17 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 28.1.0-1
- Update to 28.1.0
- Fixes ownership files

* Sun Dec 17 2017 Luya Tshimbalanga <luya@fedoraproject.org> - 28.0.0-1
- Initial release
