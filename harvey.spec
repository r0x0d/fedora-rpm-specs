%global appname io.github.danirabbit.harvey

Name:           harvey
Summary:        The hero that Gotham needs right now
Version:        2.0.0
Release:        %autorelease
# The entire source is GPL-3.0-or-later:
#
#   The COPYING file is GPLv3, and while the phrase “or any later version” does
#   not appear, data/harvey.metainfo.xml.in, debian/copyright, and the SPDX
#   headers of the Vala sources, src/*.vala, indicate GPLv3+ is intended. For
#   example, from the AppData file:
#
#     <project_license>GPL-3.0-or-later</project_license>
#
# …except:
#   - data/Application.css is GPL-2.0-or-later
#   - data/harvey.metainfo.xml.in is CC0-1.0, which is only allowed for content
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND CC0-1.0

URL:            https://github.com/danrabbit/harvey
Source:         %{url}/archive/%{version}/harvey-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  desktop-file-utils
BuildRequires:  gettext

# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
BuildRequires:  libappstream-glib
# Matches what gnome-software and others use:
BuildRequires:  appstream

BuildRequires:  hardlink

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  gcc

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk4) >= 4.10.0
BuildRequires:  pkgconfig(granite-7) >= 7.0.0

Requires:       hicolor-icon-theme

Summary(fr):    Le héro dont Gotham a besoin dès à présent
Summary(es):    El héroe que Gotham estaba necesitando
Summary(en_AU): The hero that Gotham needs right now
Summary(en_CA): The hero that Gotham needs right now
Summary(en_GB): The hero that Gotham needs right now

%description
Calculate and visualize color contrast. Harvey checks a given set of colors for
WCAG contrast compliance.

%description -l fr
Calculez et visualisez les contrastes de couleur. Harvey vérifie qu’un jeu de
couleur est conforme aux recommandation de contraste WCAG.

%description -l es
Calcule y visualice el contraste de color, Harvey comprueba un conjunto
determinado de colores para el cumplimiento del contraste WCAG.

%description -l en_AU
Calculate and visualise colour contrast. Harvey checks a given set of colours
for WCAG contrast compliance.

%description -l en_CA
Calculate and visualize colour contrast. Harvey checks a given set of colours
for WCAG contrast compliance.

%description -l en_GB
Calculate and visualise colour contrast. Harvey checks a given set of colours
for WCAG contrast compliance.


%prep
%autosetup -p1

rename_lang() {
  set -ue
  sed -r -i "s/(Language:[[:blank:]]+)${1}\\b/\\1${2}/" \
      "po/${1}.po" "po/extra/${1}.po"
  mv "po/${1}.po" "po/${2}.po"
  mv "po/extra/${1}.po" "po/extra/${2}.po"
  sed -r -i "s/^${1}(\\r?)\$/${2}\\1/" po/LINGUAS po/extra/LINGUAS
}

# https://salsa.debian.org/iso-codes-team/iso-codes/-/blob/v4.16.0/CHANGELOG.md
# See https://bugzilla.redhat.com/show_bug.cgi?id=2279336 for discussion of the
# issue and possible upstreamability.
rename_lang mo ro_MD


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{appname}

# Upstream installs the same SVG icon in many size-specific directories like
# /usr/share/icons/hicolor/64x64@2/; we can save space by hardlinking these
# together.
hardlink -c -v '%{buildroot}%{_datadir}/icons/hicolor'


%check
desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/%{appname}.desktop

# Still required by guidelines for now
# (https://pagure.io/packaging-committee/issue/1053):
appstream-util validate-relax --nonet \
    %{buildroot}/%{_metainfodir}/%{appname}.metainfo.xml
# Matches what gnome-software and others use:
# The appstream validator has some complaints about the metainfo XML
# https://github.com/danirabbit/harvey/issues/71
appstreamcli validate --no-net --explain \
    %{buildroot}/%{_metainfodir}/%{appname}.metainfo.xml || :


%files -f %{appname}.lang
%doc README.md
%license LICENSE

%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/glib-2.0/schemas/%{appname}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_metainfodir}/%{appname}.metainfo.xml


%changelog
%autochangelog
