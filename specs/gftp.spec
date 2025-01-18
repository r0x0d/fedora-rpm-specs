Summary: A multi-threaded FTP client for the X Window System
Name: gftp
Version: 2.9.1b
Release: 10%{?dist}
Epoch: 2
License: GPL-2.0-or-later
Url: https://github.com/masneyb/gftp/tags
Source0: https://github.com/masneyb/gftp/archive/%{version}/%{name}-%{version}.tar.gz

Patch0:  pointer-types.patch

BuildRequires: gcc
BuildRequires: gtk2-devel >= 2.2.0
BuildRequires: readline-devel
BuildRequires: openssl-devel
BuildRequires: desktop-file-utils
BuildRequires: make
BuildRequires: autoconf automake gettext-devel

%description
gFTP is a multi-threaded FTP client for the X Window System. gFTP
supports simultaneous downloads, resumption of interrupted file
transfers, file transfer queues to allow downloading of multiple
files, support for downloading entire directories/subdirectories,
a bookmarks menu to allow quick connection to FTP sites, caching of
remote directory listings, local and remote chmod, drag and drop, 
a connection manager and much more.

Install gftp if you need a graphical FTP client.

%prep
%setup -q

%patch -P 0 -p0

%build
./autogen.sh
%configure

make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT 

# desktop-file-install is picky about this
#sed -i -e "s#Icon=gftp.png#Icon=/usr/share/pixmaps/gftp.png#" \
#  $RPM_BUILD_ROOT%{_datadir}/applications/gftp.desktop
   
desktop-file-install --vendor net --delete-original         \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications             \
  --remove-category Application                             \
  $RPM_BUILD_ROOT%{_datadir}/applications/gftp.desktop

%find_lang %name

%files -f %{name}.lang
%license LICENSE
%doc ChangeLog README.md TODO AUTHORS LICENSE USERS-GUIDE
%{_bindir}/gftp
%{_bindir}/gftp-gtk
%{_bindir}/gftp-text
%{_datadir}/gftp
%{_datadir}/icons/hicolor/*/apps/gftp.*
%{_datadir}/applications/net-gftp.desktop
%{_mandir}/man1/gftp.1.gz

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.9.1b-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.9.1b-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Feb 05 2024 Gwyn Ciesla <gwync@protonmail.com> - 2:2.9.1b-8
- Patch for stricter flags.

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.9.1b-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.9.1b-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.9.1b-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Mar 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 2:2.9.1b-4
- migrated to SPDX license

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.9.1b-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.9.1b-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr 07 2022 Gwyn Ciesla <gwync@protonmail.com> - 2:2.9.1b-1
- 2.9.1b

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.19-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.19-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.19-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.19-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.19-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.19-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2:2.0.19-22
- Rebuild for readline 8.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.19-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 30 2018 Gwyn Ciesla <limburgher@gmail.com> - 2:2.0.19-20
- Re-enable gftp-text. Disks are larger than 14 years ago.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.19-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.19-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.19-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.19-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.19-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.0.19-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:2.0.19-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:2.0.19-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:2.0.19-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:2.0.19-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:2.0.19-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:2.0.19-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:2.0.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2:2.0.19-6
- Rebuild for new libpng

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:2.0.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Mar 17 2010 Tom "spot" Callaway <tcallawa@redhat.com> - 2:2.0.19-4
- fix broken bookmarks (bz 463006)

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 2:2.0.19-3
- rebuilt with new openssl

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:2.0.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 01 2009 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2:2.0.19-1
- upgrade to 2.0.19
- spec cleanup

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:2.0.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 16 2009 Tomas Mraz <tmraz@redhat.com> - 2:2.0.18-5
- rebuild with new openssl

* Mon Oct 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2:2.0.18-4
- fix bookmarks (bz 463006)

* Wed Apr  2 2008 Christopher Aillon <caillon@redhat.com> - 2:2.0.18-3
- stropts.h was removed from glibc; don't #include it anymore

* Sat Feb 16 2008 Christopher Aillon <caillon@redhat.com> - 2:2.0.18-2
- Fix merge review comments

* Wed Dec  5 2007 Matthias Clasen <mclasen@redhat.com> - 2:2.0.18-1
- Rebuild against new openssl
- Fix license field
- Fix desktop file issues

* Fri Aug 24 2007 Adam Jackson <ajax@redhat.com> - 1:2.0.18-7
- Rebuild for build ID

* Sat Jul  7 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.0.18-6
- Fix directory ownership issues

* Thu Mar 15 2007 Alexander Larsson <alexl@redhat.com> - 1:2.0.18-5
- Default to download directory if started from $HOME

* Sun Feb 25 2007 Matthias Clasen <mclasen@redhat.com> - 1:2.0.18-4
- Take the GDK lock early enough (#229943)
- Don't add invalid/obsolete categories to the desktop file

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:2.0.18-3.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1:2.0.18-3.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1:2.0.18-3.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Nov  9 2005 Tomas Mraz <tmraz@redhat.com> 2.0.18-3
- rebuilt with new openssl

* Fri Mar  4 2005 David Zeuthen <davidz@redhat.com> 2.0.18-2
- Rebuild

* Thu Feb 10 2005 Warren Togami <wtogami@redhat.com> 2.0.18-1
- 2.0.18

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Apr 15 2004 Warren Togami <wtogami@redhat.com> 2.0.17-2
- disable gftp-text

* Wed Apr 14 2004 Warren Togami <wtogami@redhat.com> 2.0.17-1
- update to 2.0.17, should fix #114935 x86-64 segfault

* Sat Mar 13 2004 Warren Togami <wtogami@redhat.com> 2.0.16-3
- default to sshv2_use_sftp_subsys=1 so SFTP works out-of-the-box 

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Mon Dec  1 2003 Jonathan Blandford <jrb@redhat.com> 1:2.0.16-1
- updated version

* Fri Oct 24 2003 Jonathan Blandford <jrb@redhat.com> 1:2.0.14-4
- rebuilt for exec shield

* Sun Oct 19 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- changed %%prefix -> %%_prefix and disabled that part of the specfile,
  seems to be unused

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Mon Dec  9 2002 Havoc Pennington <hp@redhat.com>
- 2.0.14
- build req gtk2

* Wed Aug 21 2002 Owen Taylor <otaylor@redhat.com>
- Fix problem where partial translations would lead to completely 
  borked menus (#69782)

* Sun Aug  4 2002 Havoc Pennington <hp@redhat.com>
- s/Internet/Network/ in Categories

* Tue Jul 30 2002 Havoc Pennington <hp@redhat.com>
- move desktop file to /usr/share/applications #69396

* Thu Jul 25 2002 Owen Taylor <otaylor@redhat.com>
- Fix broken .mo files by forcing regeneration (#67217)
- Fix zh_TW.po, again.

* Tue Jul 23 2002 Havoc Pennington <hp@redhat.com>
- 2.0.13

* Mon Jul 15 2002 Owen Taylor <otaylor@redhat.com>
- Upgrade to 2.0.12
- Fix bugs in pofile encoding specification

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Feb 27 2002 Havoc Pennington <hp@redhat.com>
- move to Hampton

* Mon Feb 11 2002 Havoc Pennington <hp@redhat.com>
- 2.0.11

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Thu Apr 19 2001 Havoc Pennington <hp@redhat.com>
- Upgrade to 2.0.8, fixes a security exploit and a bunch of other
  things, adds a console frontend 

* Tue Feb 27 2001 Trond Eivind Glomsrød <teg@redhat.com>
- langify
- don't try to include two non-existing files in %%doc
- move changelog to end of file

* Thu Aug 10 2000 Havoc Pennington <hp@redhat.com>
- Set Epoch, since upstream versions are not ascending

* Mon Aug 07 2000 Havoc Pennington <hp@redhat.com>
- 2.0.7b, should fix outstanding bugs

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon Jun 19 2000 Preston Brown <pbrown@redhat.com>
- FHS paths

* Fri May 19 2000 Havoc Pennington <hp@redhat.com>
- Update to 2.0.7pre3, and build for Winston

* Fri Feb 11 2000 Elliot Lee <sopwith@redhat.com>
- Add -mieee on alpha to solve bug #9317

* Thu Feb 03 2000 Preston Brown <pbrown@redhat.com>
- gzip man page

* Tue Jan 04 2000 Elliot Lee <sopwith@redhat.com>
- Update to 2.0.6a

* Fri Sep 3 1999 Elliot Lee <sopwith@redhat.com>
- Upgrade to the full 2.0.4 release. (Yes, pre1 fixed that bug.)

* Wed Sep 1 1999 Elliot Lee <sopwith@redhat.com>
- Try 2.0.4pre1 to see if it fixes bug #4700.

* Thu Jul  8 1999 Michael Fulbright <drmike@redhat.com>
- version 2.0.3

* Wed Jul  7 1999 Michael Fulbright <drmike@redhat.com>
- bumped to version 2.0.2

* Wed Mar 31 1999 Michael Fulbright <drmike@redhat.com>
- version 1.13

* Tue Mar 30 1999 Michael Fulbright <drmike@redhat.com>
- patch to fix a segfault reported by Chris Evans <chris@ferret.lmh.ox.ac.uk>

* Tue Feb 16 1999 Michael Fulbright <drmike@redhat.com>
- version 1.12

* Wed Feb 10 1999 Michael Fulbright <drmike@redhat.com>
- first attempt at spec file
