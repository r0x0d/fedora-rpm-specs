Name:    haruna
Version: 1.3.1
Release: %autorelease
Summary: Open source video player built with Qt/QML and libmpv

License: BSD-3-Clause AND CC-BY-4.0 AND CC-BY-SA-4.0 AND GPL-2.0-or-later AND GPL-3.0-or-later AND MIT
URL:     https://invent.kde.org/multimedia/%{name}/
Source0: https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz.sig
Source2: gpgkey-4E421C6554B89766DF9B7A37E12AB207C8755905.gpg

## upstream patches

BuildRequires: cmake
BuildRequires: gnupg2
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(MpvQt)

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Core5Compat)

BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6FileMetaData)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Kirigami)

BuildRequires: cmake(Breeze)

BuildRequires: pkgconfig(mpv)
BuildRequires: pkgconfig(libavcodec)
BuildRequires: pkgconfig(libavdevice)
BuildRequires: pkgconfig(libavfilter)
BuildRequires: pkgconfig(libavformat)
BuildRequires: pkgconfig(libavutil)
BuildRequires: pkgconfig(libpostproc)
BuildRequires: pkgconfig(libswresample)
BuildRequires: pkgconfig(libswscale)

Requires:      kde-filesystem
Requires:      hicolor-icon-theme
Requires:      kf6-kirigami%{?_isa}
Requires:      kf6-qqc2-desktop-style%{?_isa}
Recommends:    yt-dlp

%description
%{summary}.

Features:
 + play online videos, through youtube-dl;
 + supports youtube playlists;
 + toggle playlist with mouse-over, playlist overlays the video;
 + auto skip chapter containing certain words;
 + configurable shortcuts and mouse buttons;
 + quick jump to next chapter by middle click on progress bar.


%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
# Cleaning icons with non-standard resolution
for i in 44 150 310; do
  rm -rf %{buildroot}%{_kf6_datadir}/icons/hicolor/"${i}x${i}"
done
%find_lang %{name} --with-html


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml


%files -f %{name}.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_bindir}/haruna
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/haruna.{svg,png}
%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml


%changelog
%autochangelog
