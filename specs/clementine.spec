%global tag     1.4.1-30-ga05464b42 

Name:           clementine
Version:        1.4.1
Release:        %autorelease
Summary:        A music player and library organizer

# Apache-2.0:
#   - ext/libclementine-common/core/latch.cpp
#   - ext/libclementine-common/core/latch.h
#   - ext/libclementine-remote/remotecontrolmessages.proto
#   - ext/libclementine-common/core/logging.cpp
#   - ext/libclementine-common/core/logging.h
#   - ext/libclementine-common/core/messagehandler.cpp
#   - ext/libclementine-common/core/messagehandler.h
#   - ext/libclementine-common/core/override.h
#   - ext/libclementine-common/core/timeconstants.h
# BSL-1.0: 3rdparty/utf8-cpp
# GPL-2.0-or-later:
#   - src/engines/gstengine.cpp
#   - src/engines/gstengine.h
#   - src/widgets/sliderwidget.cpp
#   - src/widgets/sliderwidget.h
# LGPL-2.0-or-later:
#   - gst/moodbar/gstfastspectrum.cpp
#   - gst/moodbar/gstfastspectrum.h
# LGPL-2.1-only:
#   - 3rdparty/taglib
#   - src/widgets/stylehelper:
# LGPL-2.1-only WITH Qt-LGPL-exception-1.1 OR GPL-3.0-only:
#   - 3rdparty/qsqlite/clementinesqlcachedresult.cpp
#   - 3rdparty/qsqlite/clementinesqlcachedresult.h
#   - 3rdparty/qsqlite/qsql_sqlite.cpp
#   - 3rdparty/qsqlite/qsql_sqlite.h
# LGPL-2.1-only WITH Qt-LGPL-exception-1.1 OR LGPL-3.0-only WITH Qt-LGPL-exception-1.1:
#   - 3rdparty/qsqlite/smain.cpp
#   - 3rdparty/qsqlite/smain.h
# MIT: 3rdparty/qocoa
License:        GPL-3.0-or-later AND GPL-2.0-or-later AND BSL-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-only AND Apache-2.0 AND (LGPL-2.1-only WITH Qt-LGPL-exception-1.1 OR GPL-3.0-only) AND (LGPL-2.1-only WITH Qt-LGPL-exception-1.1 OR LGPL-3.0-only WITH Qt-LGPL-exception-1.1) AND MIT
URL:            https://www.clementine-player.org/
VCS:            https://github.com/clementine-player/Clementine
Source:         %vcs/archive/%{tag}/%{name}-%{tag}.tar.gz

# Use qt5 libraries (qtiocompressor)
Patch:          0001-Use-QtIoCompressor-from-Qt5.patch

BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  liblastfm-qt5-devel
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(QxtCore-qt5)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-tag-1.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libchromaprint)
BuildRequires:  (pkgconfig(libcryptopp) or pkgconfig(cryptopp))
BuildRequires:  pkgconfig(libmtp)
BuildRequires:  pkgconfig(libmygpo-qt5)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libplist-2.0)
BuildRequires:  pkgconfig(libprojectM) >= 2.0.1-7
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libsparsehash)
BuildRequires:  pkgconfig(libudf)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(sqlite3) >= 3.7
BuildRequires:  pkgconfig(taglib) >= 1.11
BuildRequires:  pkgconfig(udisks)
BuildRequires:  qt5-linguist
BuildRequires:  qtiocompressor-devel
BuildRequires:  qtsingleapplication-qt5-devel >= 2.6.1-2
BuildRequires:  qtsinglecoreapplication-qt5-devel >= 2.6.1-2
%ifnarch s390 s390x
BuildRequires:  pkgconfig(libgpod-1.0)
BuildRequires:  pkgconfig(libimobiledevice-1.0)
%endif

Requires:       gstreamer1-plugins-good
Requires:       hicolor-icon-theme
Requires:       qtiocompressor >= 2.3.1-17

Provides:       bundled(qocoa)
Provides:       bundled(qsqlite)
Provides:       bundled(utf8-cpp)

%description
Clementine is a modern music player and library organiser.
It is inspired by Amarok 1.4, focusing on a fast and easy-to-use interface for
searching and playing your music.

Features include:
  * Search and play your local music library
  * Listen to internet radio from Last.fm, SomaFM, IntergalacticFM, Magnatune,
    Jamendo and Icecast
  * Create smart playlists and dynamic playlists
  * Tabbed playlists, import and export M3U, XSPF, PLS and ASX
  * Visualisations from projectM
  * Lyrics and artist biographies and photos
  * Transcode music into MP3, Ogg Vorbis, Ogg Speex, FLAC or AAC
  * Edit tags on MP3 and OGG files, organise your music
  * Download missing album cover art from Last.fm
  * Cross-platform - works on Windows, Mac OS X and Linux
  * Native desktop notifications on Linux (libnotify) and Mac OS X (Growl)
  * Remote control using a Wii Remote, MPRIS or the command-line
  * Copy music to your iPod, iPhone, MTP or mass-storage USB player
  * Queue manager

%prep
%autosetup -p1 -n Clementine-%{tag}

# Remove most 3rdparty libraries
mv 3rdparty/{qocoa,qsqlite,utf8-cpp}/ .
rm -rfv 3rdparty/*
mv {qocoa,qsqlite,utf8-cpp}/ 3rdparty/

%build
%cmake \
  -DBUILD_WERROR:BOOL=OFF \
  -DCMAKE_BUILD_TYPE:STRING=Release \
  -DCMAKE_CXX_STANDARD:INT=17 \
  -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
  -DFORCE_GIT_REVISION:STRING=%{tag} \
  -DUSE_SYSTEM_PROJECTM:BOOL=ON \
  -DUSE_SYSTEM_QTSINGLEAPPLICATION:BOOL=ON \
  -DUSE_SYSTEM_QXT:BOOL=ON \
  -DUSE_SYSTEM_TAGLIB:BOOL=ON
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.clementine_player.Clementine.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.clementine_player.Clementine.appdata.xml

%files
%license COPYING
%doc Changelog README.md
%{_bindir}/clementine
%{_bindir}/clementine-tagreader
%{_datadir}/applications/org.clementine_player.Clementine.desktop
%{_datadir}/icons/hicolor/*/apps/org.clementine_player.Clementine.*
%{_datadir}/kservices5/clementine-*.protocol
%{_metainfodir}/org.clementine_player.Clementine.appdata.xml

%changelog
%autochangelog
