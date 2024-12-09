Name:           rpi-imager
Version:        1.9.0
Release:        %autorelease
Summary:        Graphical user-interface to write disk images and format SD cards
License:        Apache-2.0
URL:            https://github.com/raspberrypi/rpi-imager
Source0:        %{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/raspberrypi/rpi-imager/blob/v1.9.0/src/CMakeLists.txt#L235
ExcludeArch:    s390x

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6DBus)

BuildRequires:  gnutls-devel

BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

Provides:       bundled(xz) = 5.6.2
Provides:       bundled(zstd) = 1.5.6
Provides:       bundled(zlib) = 1.3.1
Provides:       bundled(libarchive) = 3.7.4
Provides:       bundled(curl) = 8.8.0

Requires:       hicolor-icon-theme
Requires:       dosfstools
Requires:       util-linux

# Needed if you want to be able to run rpi-imager as a regular user
Recommends:     udisks2

%description
Graphical user-interface to download and write Raspberry Pi disk images, or
write custom disk images and format SD cards.

%prep
%autosetup -p1

%build
pushd src
%cmake -GNinja \
    -DBUILD_SHARED_LIBS=OFF \
    -DENABLE_CHECK_VERSION=OFF \
    -DENABLE_TELEMETRY=OFF
%cmake_build

%install
install -pDm755 src/%{_vpath_builddir}/%{name} %{buildroot}%{_bindir}/%{name}
install -pDm644 src/linux/org.raspberrypi.rpi-imager.desktop \
    %{buildroot}%{_datadir}/applications/org.raspberrypi.%{name}.desktop
install -pDm644 debian/rpi-imager.png \
    %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -pDm644 debian/rpi-imager.metainfo.xml \
    %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files
%license license.txt
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/org.raspberrypi.%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_metainfodir}/%{name}.metainfo.xml

%changelog
%autochangelog
