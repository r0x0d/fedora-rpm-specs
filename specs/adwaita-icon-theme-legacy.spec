%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           adwaita-icon-theme-legacy
Version:        46.2
Release:        3%{?dist}
Summary:        Full-color icons for the Adwaita icon theme

License:        LGPL-3.0-only OR CC-BY-SA-3.0
URL:            https://gitlab.gnome.org/GNOME/adwaita-icon-theme-legacy
Source0:        https://download.gnome.org/sources/%{name}/46/%{name}-%{tarball_version}.tar.xz

BuildArch:      noarch

BuildRequires:  meson
BuildRequires:  /usr/bin/gtk4-update-icon-cache

# Offer alternative name
Provides:       adwaita-legacy-icon-theme = %{version}-%{release}

%description
This package contains the full color Adwaita icons for the Adwaita icon theme
used by the GNOME desktop.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

# Offer alternative name
Provides:       adwaita-legacy-icon-theme-devel = %{version}-%{release}

%description    devel
The %{name}-devel package contains the pkgconfig file for
developing applications that use %{name}.

%prep
%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install

# Delete license files being installed in the adwaita-icon-theme dir
rm -rf %{buildroot}%{_licensedir}/adwaita-icon-theme

# Delete useless hidden files
find %{buildroot} -name ".placeholder" -delete
find %{buildroot} -name ".empty" -delete

touch %{buildroot}%{_datadir}/icons/AdwaitaLegacy/.icon-theme.cache

%transfiletriggerin -- %{_datadir}/icons/AdwaitaLegacy
gtk-update-icon-cache --force %{_datadir}/icons/AdwaitaLegacy &>/dev/null || :

%transfiletriggerpostun -- %{_datadir}/icons/AdwaitaLegacy
gtk-update-icon-cache --force %{_datadir}/icons/AdwaitaLegacy &>/dev/null || :

%files
%license COPYING*
%dir %{_datadir}/icons/AdwaitaLegacy/
%{_datadir}/icons/AdwaitaLegacy/8x8/
%{_datadir}/icons/AdwaitaLegacy/16x16/
%{_datadir}/icons/AdwaitaLegacy/22x22/
%{_datadir}/icons/AdwaitaLegacy/24x24/
%{_datadir}/icons/AdwaitaLegacy/32x32/
%{_datadir}/icons/AdwaitaLegacy/48x48/
%{_datadir}/icons/AdwaitaLegacy/index.theme
%ghost %{_datadir}/icons/AdwaitaLegacy/.icon-theme.cache

%files devel
%{_datadir}/pkgconfig/%{name}.pc

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 46.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 46.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 29 2024 Neal Gompa <ngompa@fedoraproject.org> - 46.2-1
- Initial Fedora packaging
