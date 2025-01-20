Name:           portaudio
Version:        19
Release:        46%{?dist}
Summary:        Free, cross platform, open-source, audio I/O library
License:        MIT
URL:            http://www.portaudio.com/

Source0:        http://files.portaudio.com/archives/pa_stable_v190700_20210406.tgz
Patch1:         portaudio-doxynodate.patch
Patch2:         portaudio-pkgconfig-alsa.patch
# Add some extra API needed by audacity
# http://audacity.googlecode.com/svn/audacity-src/trunk/lib-src/portmixer/portaudio.patch
Patch3:         portaudio-audacity.patch

BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
%if 0%{?fedora} || 0%{?rhel} >= 9
BuildRequires:  pipewire-jack-audio-connection-kit-devel
%else
BuildRequires:  jack-audio-connection-kit-devel
%endif
BuildRequires:  libtool
BuildRequires:  make

%description
PortAudio is a portable audio I/O library designed for cross-platform
support of audio. It uses a callback mechanism to request audio processing.
Audio can be generated in various formats, including 32 bit floating point,
and will be converted to the native format internally.


%package devel
Summary:        Development files for the portaudio audio I/O library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
PortAudio is a portable audio I/O library designed for cross-platform
support of audio. It uses a callback mechanism to request audio processing.
Audio can be generated in various formats, including 32 bit floating point,
and will be converted to the native format internally.

This package contains files required to build applications that will use the
portaudio library.


%prep
%autosetup -p1 -n %{name}
# Needed for patch3
autoreconf -i -f
# With autoconf-2.71 we need to run this twice for things to work ?? (rhbz#1943118)
autoreconf -i -f


%build
%configure --disable-static --enable-cxx
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' bindings/cpp/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' bindings/cpp/libtool
# no -j# because building with -j# is broken
make
# Build html devel documentation
doxygen


%install
%make_install


%ldconfig_scriptlets


%files
%license LICENSE.txt
%doc README.md
%{_libdir}/libportaudio.so.2*
%{_libdir}/libportaudiocpp.so.0*

%files devel
%doc doc/html/*
%{_includedir}/portaudiocpp/
%{_includedir}/portaudio.h
%{_includedir}/pa_jack.h
%{_includedir}/pa_linux_alsa.h
%{_includedir}/pa_unix_oss.h
%{_libdir}/libportaudio.so
%{_libdir}/libportaudiocpp.so
%{_libdir}/pkgconfig/portaudio-2.0.pc
%{_libdir}/pkgconfig/portaudiocpp.pc


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 19-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 16 2024 Xavier Bachelot <xavier@bachelot.org> - 19-45
- Add conditional for {pipewire-,}jack-audio-connection-kit-devel
- Narrow scope of globs for .so/.pc

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 19-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 19-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 19-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 19-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 19-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 19-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 19-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 19-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 04 2021 Hans de Goede <hdegoede@redhat.com> - 19-36
- Fix FTBFS with upcoming autoconf-2.71 (rhbz#1943118)

* Tue Apr 06 2021 Uwe Klotz <uwe.klotz@gmail.com> - 19-35
- Upgrade to pa_stable_v190700_20210406

* Mon Mar 22 2021 Hans de Goede <hdegoede@redhat.com> - 19-34
- Deal with pipewire jack identifiers containing chars which have special meanings in regexes
  Resolves rhbz#1939749

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 19-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 19-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 19-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 19-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 19-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 19-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 19-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 19-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 19-21
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 19-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 22 2014 Hans de Goede <hdegoede@redhat.com> - 19-19
- Upgrade to the "stable" v19_20140130 snapshot (rhbz#1111780)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 19-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 19-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat May  4 2013 Hans de Goede <hdegoede@redhat.com> - 19-16
- Add a patch from audacity adding some extra API calls audacity needs
- Cleanup spec-file
- Update svn snapshot to bring in some alsa samplerate handling fixes
- Run autoreconf for aarch64 support (rhbz#926363)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 19-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 19-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 19-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu May 05 2011 Dan Horák <dan[at]danny.cz> - 19-12
- fix dependency on alsa-lib-devel

* Sun Mar 27 2011 Hans de Goede <hdegoede@redhat.com> - 19-11
- Upgrade to a more recent snapshot to bring in various bugfixes (rhbz#691148)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Matthias Saou <http://freshrpms.net/> 19-7
- Add Doxyfile patch to remove date in footer and fix multilib (#342931).

* Sun Dec  7 2008 Hans de Goede <hdegoede@redhat.com> 19-6
- Add a patch by Kevin Kofler to make non mmap alsa (and thus pulseaudio) work
  (bz 445644)

* Sun Feb  3 2008 Matthias Saou <http://freshrpms.net/> 19-5
- Update to "stable" v19_20071207.
- Rebuild against latest jack in rawhide (#430672).
- Backport update to F8 too (#431266).

* Mon Dec 10 2007 Matthias Saou <http://freshrpms.net/> 19-4
- Include portaudiocpp library and headers (#413681).

* Wed Aug 22 2007 Matthias Saou <http://freshrpms.net/> 19-3
- Rebuild for new BuildID feature.

* Sun Aug  5 2007 Matthias Saou <http://freshrpms.net/> 19-2
- Update License field.

* Tue Jun 19 2007 Matthias Saou <http://freshrpms.net/> 19-1
- Update to "stable" v19_061121.
- Switch virtual devel provide to a real sub-package.
- Update spec to match build changes from custom Makefile to autotools.
- Include new pkgconfig file and require pkgconfig from the devel package.
- Add ldconfig calls now that we have a versionned shared library.
- Rebuild against alsa-lib and jack-audio-connection-kit.
- Build doxygen documentation and include it in the devel package.

* Mon Aug 28 2006 Matthias Saou <http://freshrpms.net/> 18.1-8
- FC6 rebuild.

* Mon Mar  6 2006 Matthias Saou <http://freshrpms.net/> 18.1-7
- FC5 rebuild.

* Thu Feb  9 2006 Matthias Saou <http://freshrpms.net/> 18.1-6
- Rebuild for new gcc/glibc.

* Sun May 22 2005 Jeremy Katz <katzj@redhat.com> - 18.1-5
- rebuild on all arches

* Thu Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> 18.1-4
- rebuilt

* Tue Nov 16 2004 Matthias Saou <http://freshrpms.net/> 18.1-3
- Bump release to provide Extras upgrade path.

* Fri Nov  5 2004 Matthias Saou <http://freshrpms.net/> 18.1-2
- Add -devel provides.
- Fix .so 644 mode (overidden in defattr).

* Thu Jun 10 2004 Dag Wieers <dag@wieers.com> - 18.1-1
- Added -fPIC for x86_64.

* Sat Sep 13 2003 Dag Wieers <dag@wieers.com> - 18.1-0
- Initial package. (using DAR)

