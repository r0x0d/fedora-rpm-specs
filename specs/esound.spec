Summary:       Allows several audio streams to play on a single audio device
Name:          esound
Epoch:         1
Version:       0.2.41
Release:       37%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:       LicenseRef-Callaway-LGPLv2+
URL:           https://ftp.gnome.org/pub/GNOME/sources/esound
Source0:       https://ftp.gnome.org/pub/gnome/sources/esound/0.2/esound-%{version}.tar.bz2
Patch4:        esound-0.2.38-drain.patch
Patch6:        esound-0.2.38-fix-open-macro.patch
Patch7:        remove-confusing-spew.patch
# default to nospawn, so we can kill the esd.conf file
Patch8:        esound-nospawn.patch
Patch9:        esound-0.2.41-libm.patch
Patch10:       esound-c99.patch
# temporarily disable doc build due to xml catalog issues
#BuildRequires: docbook-utils
BuildRequires: audiofile-devel
BuildRequires: alsa-lib-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: make
Obsoletes:     esound <= 1:0.2.36-4

%description
EsounD, the Enlightened Sound Daemon, is a server process that mixes
several audio streams for playback by a single audio device. For
example, if you're listening to music on a CD and you receive a
sound-related event from ICQ, the two applications won't have to
queue for the use of your sound card.

Install esound if you'd like to let sound applications share your
audio device. You'll also need to install the audiofile package.

%package libs
Summary: Library to talk to the EsounD daemon

%description libs
The esound-libs package includes the libraries required
for applications to talk to the EsounD daemon.

%package tools
Summary: Commandline tools to talk to the EsounD daemon

%description tools
The esound-tools package includes commandline utilities
for controlling the EsounD daemon.

%package  devel
Summary:  Development files for EsounD applications
Requires: esound-libs = %{epoch}:%{version}-%{release}
Requires: audiofile-devel
Requires: alsa-lib-devel
# we install a pc file
Requires: pkgconfig
# we install an automake macro
Requires: automake

%description devel
The esound-devel package includes the libraries, include files and
other resources needed to develop EsounD applications.

%package daemon
Summary: EsounD daemon

%description daemon
EsounD, the Enlightened Sound Daemon, is a server process that mixes
several audio streams for playback by a single audio device. For
example, if you're listening to music on a CD and you receive a
sound-related event from IM client, the two applications won't have to
queue for the use of your sound card.
The daemon functionality was replaced with PulseAudio (PA) and the binary
was dropped from Fedora in October 2007. However, on PA-disabled systems
the daemon functionality was completely missing and therefore
reintroduced to Fedora in June 2013 in form of subpackage.
The daemon cannot run on PA-enabled systems.


%prep
%autosetup -p1

%build
autoreconf -v -i -f
%configure --disable-static

EGREP='grep -E' make

%install
%makeinstall
rm -f %{buildroot}%{_sysconfdir}/esd.conf
rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets libs

%files libs
%license COPYING.LIB
%doc AUTHORS ChangeLog docs/esound.sgml
%doc NEWS README TIPS TODO
%{_libdir}/*.so.*

%files tools
%{_bindir}/esdcat
%{_bindir}/esdctl
%{_bindir}/esddsp
%{_bindir}/esdfilt
%{_bindir}/esdloop
%{_bindir}/esdmon
%{_bindir}/esdplay
%{_bindir}/esdrec
%{_bindir}/esdsample
%{_mandir}/man1/esdcat.1*
%{_mandir}/man1/esdctl.1*
%{_mandir}/man1/esddsp.1*
%{_mandir}/man1/esdfilt.1*
%{_mandir}/man1/esdloop.1*
%{_mandir}/man1/esdmon.1*
%{_mandir}/man1/esdplay.1*
%{_mandir}/man1/esdrec.1*
%{_mandir}/man1/esdsample.1*
# temporarily disable doc build due to xml catalog issues
%exclude %doc %{_datadir}/doc/esound

%files devel
%{_bindir}/esd-config
%{_includedir}/*
%{_datadir}/aclocal/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_mandir}/man1/esd-config.1*

%files daemon
%{_bindir}/esd
%{_mandir}/man1/esd.1*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.41-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 1:0.2.41-36
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.41-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jul 01 2024 Terje Rosten <terjeros@gmail.com> - 1:0.2.41-34
- Use autosetup macro

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.41-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.41-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.41-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Mar 17 2023 Florian Weimer <fweimer@redhat.com> - 1:0.2.41-30
- Port to C99 (#2179290)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.41-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.41-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.41-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.41-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.41-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.41-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.41-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.41-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.41-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.41-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.41-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.41-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.41-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.41-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.41-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 22 2015 Jaromir Capik <jcapik@redhat.com> - 1:0.2.41-14
- Just bumping the release to resurrect retired esound in f23 (#1251697)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.41-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.41-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.41-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.41-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 05 2013 Jaromir Capik <jcapik@redhat.com> - 1:0.2.41-9
- Reintroducing the daemon (#879700)
- Cleaning the spec
- Fixing bogus dates in the changelog

* Thu Feb 07 2013 Jon Ciesla <limburgher@gmail.com> 1:0.2.41-8
- Merge review fixes, BZ 225734.

* Wed Nov 07 2012 Adam Jackson <ajax@redhat.com> 1:0.2.41-7
- Rebuild for new audiofile
- esound-0.2.41-libm.patch: Fix linking against libm

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.41-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.41-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.41-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.41-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Mar 31 2009 Matthias Clasen <mclasen@redhat.com> - 1:0.2.41-2
- Remove /etc/esd.conf (#491481)

* Sun Mar 15 2009 Matthias Clasen <mclasen@redhat.com> - 1:0.2.41-1
- Update to 0.2.41

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Sep  4 2008 Matthias Clasen <mclasen@redhat.com> - 1:0.2.40-1
- Update to 0.2.40

* Thu Jul 17 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1:0.2.39-2
- fix license tag

* Tue Jul 15 2008 Matthias Clasen <mclasen@redhat.com> - 1:0.2.39-1
- Update to 0.2.39
- Drop upstreamed patches
- Temporarily disable doc build due to xml catalog issues

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:0.2.38-7
- Autorebuild for GCC 4.3

* Fri Oct 26 2007 - Bastien Nocera <bnocera@redhat.com> - 1:0.2.38-6
- Kill the main esound package, so people don't try to use it instead of
  pulseaudio itself (#353051)

* Wed Sep 19 2007 Matthias Clasen <mclasen@redhat.com> - 1:0.2.38-5
- Don't spew confusing warnings to stdout 

* Fri Aug 24 2007 Adam Jackson <ajax@redhat.com> - 1:0.2.38-4
- Rebuild for build ID

* Thu Aug 9 2007 - Lennart Poettering <lpoetter@redhat.com> - 1:0.2.38-3
- Move ESD socket from /tmp/.esd/socket to /tmp/.esd-`id -u`/socket to allow
  multiple concurrent esd instances, one per user (#251505)
- Fix build with newer libc

* Mon Jun 11 2007 - Bastien Nocera <bnocera@redhat.com> - 1:0.2.38-2
- Patch from Martin Stransky <stransky@redhat.com> to work around
  a race condition in snd_pcm_drain (#238680)

* Tue May 08 2007 - Bastien Nocera <bnocera@redhat.com> - 1:0.2.38-1
- New upstream release (#237487)
- Fix not obsoleting older non-split versions of esound (#230631)

* Tue Feb 27 2007 Matthias Clasen <mclasen@redhat.com> - 1:0.2.37-1
- Update to 0.2.37

* Mon Feb  5 2007 Matthias Clasen <mclasen@redhat.com> - 1:0.2.36-5
- Also split off a -tools package, and sort the man pages 
  to the right packages

* Sat Jan 20 2007 Matthias Clasen <mclasen@redhat.com> - 1:0.2.36-4
- Split a -libs package off the core esound package
  in preparation for pulseaudio  (#223503) 
- Correct the License tag

* Thu Jul 27 2006 Matthias Clasen <mclasen@redhat.com> - 1:0.2.36-3
- fix multilib conflicts

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:0.2.36-2.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1:0.2.36-2.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1:0.2.36-2.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Sat Oct 15 2005 Florian La Roche <laroche@redhat.com>
- link shared libs against all dependent libs

* Mon Jul 18 2005 John (J5) Palmieri <johnp@redhat.com> - 1:0.2.36-1
- Updated to 0.2.36
- removed esound-0.2.35-manpage.patch

* Wed Jun  1 2005 Bill Nottingham <notting@redhat.com> - 1.0.2.35-5
- readdd patch to prevent multilib conflicts

* Wed Mar 02 2005 John (J5) Palmieri <johnp@redhat.com> - 1:0.2.35-4
- Rebuild with gcc 4.0

* Sat Nov 20 2004 Miloslav Trmac <mitr@redhat.com> - 1:0.2.35-3
- Fix manual word wrapping in esd-config.1

* Wed Aug 18 2004 John (J5) Palmieri <johnp@redhat.com>
- update to 0.2.35

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Apr 13 2004 Warren Togami <wtogami@redhat.com> 1:0.2.34-2
- remove INSTALL and 536k of useless .ps and html
- move man pages from -devel to main pkg
- #117037 BR alsa-lib-devel
- #107781 remove old (2002) stripping disabling stuff (TEST ME!)
- other cleanups

* Tue Mar 23 2004 Alex Larsson <alexl@redhat.com> 1:0.2.34-1
- update to 0.2.34

* Wed Mar  3 2004 Alexander Larsson <alexl@redhat.com> 1:0.2.33-1
- update to 0.2.33, hopefully fixes alsa issues

* Tue Mar 02 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Jan 19 2004 Alexander Larsson <alexl@redhat.com> 1:0.2.32-2
- libtool workaround

* Mon Jan 19 2004 Alexander Larsson <alexl@redhat.com> 1:0.2.32-1
- 0.2.32

* Fri Aug 15 2003 Alexander Larsson <alexl@redhat.com> 1:0.2.31-1
- 0.2.31

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Tue Jun  3 2003 Jeff Johnson <jbj@redhat.com>
- add explicit epoch's where needed.

* Mon Feb 10 2003 Bill Nottingham <notting@redhat.com> 0.2.28-4
- fix URL (#74924)

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Dec 02 2002 Elliot Lee <sopwith@redhat.com> 0.2.28-2
- Remove unpackaged files

* Wed Aug 21 2002 Elliot Lee <sopwith@redhat.com> 0.2.28-1
- Update 0.2.28
- Fix some stupid bugs

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Jun 16 2002 Havoc Pennington <hp@redhat.com>
- 0.2.27
- clean up file list

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Mon May 20 2002 Havoc Pennington <hp@redhat.com>
- rebuild in different environment

* Fri May  3 2002 Havoc Pennington <hp@redhat.com>
- 0.2.25

* Fri Mar  1 2002 Havoc Pennington <hp@redhat.com>
- upgrade to new upstream version I just released with fix from #55877
- add URL field #54604

* Fri Jan 11 2002 Havoc Pennington <hp@redhat.com>
- hrm, put .pc file in file list

* Fri Jan 11 2002 Havoc Pennington <hp@redhat.com>
- upgrade to CVS snap that has .pc file
- remove nohang patch now moved upstream

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Aug 26 2001 Elliot Lee <sopwith@redhat.com> 0.2.22-5
- Remove useless URL: (#48441)

* Fri Jul 13 2001 Alexander Larsson <alexl@redhat.com>
- Add nohang patch that fixes "starting esd hangs for 10 seconds".

* Fri Jul  6 2001 Trond Eivind Glomsrød <teg@redhat.com>
- Use %%{_tmppath}
- Add BuildRequires
- Don't strip explicitly
- Make the esound-devel depend on esound with version
- s/Copyright/License/
- it isn't relocatable, don't pretend it is
- make /etc/esd.conf noreplace

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Thu Nov 30 2000  Elliot Lee <sopwith@redhat.com> 0.2.22-1
- Update to 0.2.22

* Tue Oct 3 2000  Elliot Lee <sopwith@redhat.com> 0.2.20-1
- Update to 0.2.20

* Fri Aug 11 2000 Jonathan Blandford <jrb@redhat.com>
- Up Epoch and release

* Wed Jul 19 2000 Havoc Pennington <hp@redhat.com> 
- Remove error spew when /dev/dsp is absent.

* Tue Jul 18 2000 Elliot Lee <sopwith@redhat.com> 0.2.19-1
- New version

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jul 10 2000 Elliot Lee <sopwith@redhat.com> 0.2.18-4
- Pass a prefix of /usr to configure, NOT %%prefix

* Thu Jun 29 2000 Dave Mason <dcm@redhat.com> 0.2.18-3
- fixed Doc Dir

* Sat Jun  3 2000 BIll Nottingham <notting@redhat.com> 0.2.18-2
- rebuild. Apparently the compiler ate this last time.

* Tue Apr 4 2000 Elliot Lee <sopwith@redhat.com> 0.2.18-1
- Update to 0.2.18

* Mon Aug 30 1999 Elliot Lee <sopwith@redhat.com> 0.2.13-1
- Update to 0.2.13
- Merge in changes from RHL 6.0 spec file.

* Sat Nov 21 1998 Pablo Saratxaga <srtxg@chanae.alphanet.ch>

- added /usr/share/aclocal/* to %%files devel
- added spanish and french translations for rpm

* Thu Oct 1 1998 Ricdude <ericmit@ix.netcom.com>

- make autoconf do the version updating for us.

* Wed May 13 1998 Michael Fulbright <msf@redhat.com>

- First try at an RPM
