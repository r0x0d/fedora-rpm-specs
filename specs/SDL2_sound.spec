Name:           SDL2_sound
Version:        2.0.2
Release:        5%{?dist}
Summary:        An abstract soundfile decoder library
# Automatically converted from old format: zlib and LGPLv2+ - review is highly recommended.
License:        Zlib AND LicenseRef-Callaway-LGPLv2+
URL:            http://www.icculus.org/SDL_sound
Source0:        https://github.com/icculus/SDL_sound/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  SDL2-devel
# SDL_sound includes dr_flac and dr_mp3 from https://github.com/mackron/dr_libs
Provides:       bundled(dr_flac) = 0.12.39
Provides:       bundled(dr_mp3) = 0.6.34
# https://github.com/icculus/SDL_sound/issues/42
Provides:       bundled(libmodplug) = 0.8.9.1
Provides:       bundled(stb_vorbis) = 1.22
# SDL_mixer fork, stripped further, see https://github.com/icculus/SDL_sound/tree/main/src/timidity/CHANGES
Provides:       bundled(timidity) = 0.2i

%description
SDL_sound is a library that handles the decoding of several popular sound
file formats, such as .WAV and .OGG. It is meant to make the programmer's
sound playback tasks simpler. The programmer gives SDL_sound a filename,
or feeds it data directly from one of many sources, and then reads the
decoded waveform data back at her leisure. If resource constraints are a
concern, SDL_sound can process sound data in programmer-specified blocks.
Alternately, SDL_sound can decode a whole sound file and hand back a
single pointer to the whole waveform. SDL_sound can also handle sample
rate, audio format, and channel conversion on-the-fly and
behind-the-scenes, if the programmer desires.

%package        devel
Summary:        %{summary}
Requires:       %{name}%{_isa} = %{version}-%{release}
Requires:       cmake-filesystem
Requires:       pkgconfig
Requires:       SDL2-devel
# manpages conflict
Conflicts:      SDL_sound-devel

%description    devel
%{description}

This package contains the headers and libraries for SDL_sound development.

%prep
%setup -q -n SDL_sound-%{version}

%build
%cmake \
    -DSDLSOUND_BUILD_STATIC:BOOL=OFF \
    -DSDLSOUND_DECODER_MIDI:BOOL=ON \

%cmake_build
doxygen docs/Doxyfile

%install
%cmake_install
# Add namespaces to man pages (livna bug #1181)
cp -a docs/man/man3 man3
pushd man3
mv actual.3 Sound_Sample::actual.3
mv author.3 Sound_DecoderInfo::author.3
mv buffer.3 Sound_Sample::buffer.3
mv buffer_size.3 Sound_Sameple::buffer_size.3
mv channels.3 Sound_AudioInfo::channels.3
mv decoder.3 Sound_Sample::decoder.3
mv description.3 Sound_DecoderInfo::description.3
mv desired.3 Sound_Sample::desired.3
mv extensions.3 Sound_DecoderInfo::extensions.3
mv flags.3 Sound_Sample::flags.3
mv format.3 Sound_AudioInfo::format.3
mv major.3 Sound_Version::major.3
mv minor.3 Sound_Version::minor.3
mv opaque.3 Sound_Sample::opaque.3
mv patch.3 Sound_Version::patch.3
mv rate.3 Sound_AudioInfo::rate.3
mv url.3 Sound_DecoderInfo::url.3
popd

mkdir -p %{buildroot}/%{_mandir}
mv man3 %{buildroot}/%{_mandir}


%files
%license LICENSE.txt
%doc docs/CREDITS.txt README.md
%{_bindir}/playsound
%{_libdir}/libSDL2_sound.so.2{,.*}

%files devel
%doc docs/html
%{_libdir}/libSDL2_sound.so
%{_includedir}/SDL2/SDL_sound.h
%{_mandir}/man3/*
%{_libdir}/cmake/SDL2_sound
%{_libdir}/pkgconfig/SDL2_sound.pc


%changelog
* Wed Sep 4 2024 Miroslav Suchý <msuchy@redhat.com> - 2.0.2-5
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 17 2023 Dominik Mierzejewski <dominik@greysector.net> - 2.0.2-1
- update to 2.0.2 (#2218920)
- update bundled dependencies versions
- include cmake and pkgconfig files in -devel

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 30 2022 Dominik Mierzejewski <dominik@greysector.net> - 2.0.1-2
- build the bundled timidity fork for MIDI support (#2100058)

* Mon Mar 28 2022 Dominik Mierzejewski <dominik@greysector.net> - 2.0.1-1
- initial package based on SDL_sound