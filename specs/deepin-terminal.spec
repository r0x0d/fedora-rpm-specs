Name:           deepin-terminal
Version:        6.0.15
Release:        %autorelease
Summary:        Default terminal emulation application for Deepin
License:        GPL-3.0-or-later
URL:            https://github.com/linuxdeepin/deepin-terminal
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  qt5-qtbase-private-devel

BuildRequires:  cmake(lxqt2-build-tools)
# required by lxqt2-build-tools
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6LinguistTools)

BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(xcb-ewmh)

BuildRequires:  fontconfig-devel

Requires:       hicolor-icon-theme
Recommends:     deepin-manual

%description
%{summary}.

%prep
%autosetup -p1

sed -i 's|lxqt-build-tools|lxqt2-build-tools|; s|SHARED|STATIC|' 3rdparty/terminalwidget/CMakeLists.txt
sed -i 's|DDE;||' src/deepin-terminal.desktop

%build
%cmake -GNinja
%cmake_build

%install
%cmake_install

rm -r %{buildroot}%{_includedir}/terminalwidget5/ \
    %{buildroot}%{_libdir}/libterminalwidget5.a \
    %{buildroot}%{_libdir}/cmake/terminalwidget5/ \
    %{buildroot}%{_libdir}/pkgconfig/terminalwidget5.pc \
    %{buildroot}%{_datadir}/terminalwidget5/ \
    %{buildroot}%{_datadir}/deepin-terminal/translations/deepin-terminal.qm

# debuginfo generation fails with debugedit >= 5.1
# https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/GG4LQYBEKGWAGFSJ5PKTKJAOHLAB3A27/#QYIK5E642MDB4NGBXLRLLTMU7HAJOVV5
chmod u+w %{buildroot}%{_bindir}/deepin-terminal

%find_lang deepin-terminal --with-qt

%check
%ctest

%files -f deepin-terminal.lang
%doc README.md
%license LICENSE
%{_bindir}/deepin-terminal
%{_datadir}/applications/deepin-terminal.desktop
%{_datadir}/deepin-manual/manual-assets/application/deepin-terminal/
%{_datadir}/icons/hicolor/scalable/apps/deepin-terminal.svg

%changelog
%autochangelog
