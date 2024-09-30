# For GIMP version 3 compatibility, we must package a snapshot from the
# gimp-2.99 branch:
#
# https://github.com/rpeyron/plugin-gimp-fourier/tree/gimp2.99
%global commit 3ee5462c17d83b6c91c0d5f78ce55b8fa13b4763
%global snapdate 20240812

Name:           gimp-fourier-plugin
Version:        0.4.5^%{snapdate}git%{sub %{commit} 1 7}
Release:        %autorelease
Summary:        Do direct and reverse Fourier Transforms on your image

License:        GPL-3.0-or-later
URL:            https://www.lprp.fr/gimp_plugin_en/
%global forgeurl https://github.com/rpeyron/plugin-gimp-fourier
Source:         %{forgeurl}/archive/%{commit}/plugin-gimp-fourier-%{commit}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  make

BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool

BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gimp-3.0)

BuildRequires:  dos2unix

Requires:       gimp

%description
GIMP Plugin to do forward and reverse Fourier Transform. The major advantage of
this plugin is to be able to work with the transformed image inside GIMP. You
can draw or apply filters in fourier space and get the modified image with an
inverse fourier transform. Useful in fixing moire patterns or fixing some
regular banding noise.


%prep
%autosetup -n plugin-gimp-fourier-%{commit} -p1


%build
autoreconf --force --install --verbose
%configure --enable-gimp3-fourier
%make_build


%install
%make_install
%find_lang gimp30-fourier


# Upstream provides no tests.


%files -f gimp30-fourier.lang
%doc README.md
%doc README.Moire

%{_libdir}/gimp/3.0/plug-ins/fourier


%changelog
%autochangelog
