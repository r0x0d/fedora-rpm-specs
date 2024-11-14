Name:           xbacklight
Version:        1.2.4
Release:        %autorelease
Summary:        Adjust backlight brightness using RandR

License:        MIT
URL:            https://xorg.freedesktop.org/releases/individual/app/
Source:         https://xorg.freedesktop.org/releases/individual/app/xbacklight-%{version}.tar.xz

BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-atom)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-randr)

%description
Xbacklight is used to adjust the backlight brightness where
supported. It finds all outputs on the X server supporting backlight
brightness control and changes them all in the same way.


%prep
%autosetup -p1


%build
%configure
%make_build


%install
%make_install


%files
%license COPYING
%doc ChangeLog README.md
%{_bindir}/xbacklight
%{_datadir}/man/man1/xbacklight.*


%changelog
%autochangelog
