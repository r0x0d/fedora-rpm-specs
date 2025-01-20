Name: pnm2ppa
Summary: Drivers for printing to HP PPA printers
Epoch: 1
Version: 1.13
Release: 6%{?dist}
URL: http://sourceforge.net/projects/pnm2ppa 
Source: http://download.sourceforge.net/pnm2ppa/pnm2ppa-%{version}.tar.gz
# Following sourcelink is dead currently.
Source1: http://www.httptech.com/ppa/files/ppa-0.8.6.tar.gz
# Upstream sync.
Patch1: pbm2ppa-20000205.diff
# Use RPM_OPT_FLAGS.
Patch2: pnm2ppa-redhat.patch
# Don't return a local variable out of scope (bug #704568).
Patch3: pnm2ppa-coverity-return-local.patch
# FTBFS with GCC10
Patch4: pnm2ppa-gcc10.patch
# add ldflags to Makefile
Patch5: pnm2ppa-ldflags.patch
# match NOPRINTER enum with its position in global printer table
# fixes crash on aarch64
Patch6: pnm2ppa-aarch-help-crash.patch
# pbm2ppa, pnm2ppa - GPL-2.0-or-later
# pdq/* - GPL-2.0, but not shipped, thus not mentioned in license tag
License: GPL-2.0-or-later

# for autoreconf
BuildRequires: autoconf
# for autoreconf
BuildRequires: automake
# gcc is no longer in buildroot by default
BuildRequires: gcc
# uses make
BuildRequires: make

# foomatic is needed for using the filters in CUPS
Requires: foomatic

%description
Pnm2ppa is a color driver for HP PPA host-based printers such as the
HP710C, 712C, 720C, 722C, 820Cse, 820Cxi, 1000Cse, and 1000Cxi.
Pnm2ppa accepts Ghostscript output in PPM format and sends it to the
printer in PPA format.

Install pnm2ppa if you need to print to a PPA printer.

%prep
%setup -q

#pbm2ppa source
%setup -q -T -D -a 1 
%patch -P 1 -p0 -b .20000205
%patch -P 2 -p1 -b .rh
%patch -P 3 -p1 -b .coverity-return-local
%patch -P 4 -p1 -b .gcc10
%patch -P 5 -p1 -b .ldflags
%patch -P 6 -p1 -b .help-aarch-crash

for file in docs/en/LICENSE pbm2ppa-0.8.6/LICENSE; do
 sed "s|\r||g" $file > $file.new && \
 touch -r $file $file.new && \
 mv $file.new $file
done

autoreconf -vfi

%build
# set redhat build flags
%set_build_flags
%configure
%make_build
pushd pbm2ppa-0.8.6
%make_build
popd


%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_sysconfdir}
install -d %{buildroot}%{_mandir}/man1
make INSTALLDIR=%{buildroot}%{_bindir} CONFDIR=%{buildroot}%{_sysconfdir} DESTDIR=%{buildroot} \
    MANDIR=%{buildroot}%{_mandir}/man1 install
install -p -m 0755 utils/Linux/detect_ppa %{buildroot}%{_bindir}
install -p -m 0755 utils/Linux/test_ppa %{buildroot}%{_bindir}
install -p -m 0755 pbm2ppa-0.8.6/pbm2ppa  %{buildroot}%{_bindir}
install -p -m 0755 pbm2ppa-0.8.6/pbmtpg   %{buildroot}%{_bindir}
install -p -m 0644 pbm2ppa-0.8.6/pbm2ppa.conf %{buildroot}%{_sysconfdir}
install -p -m 0644 pbm2ppa-0.8.6/pbm2ppa.1   %{buildroot}%{_mandir}/man1

chmod 644 docs/en/LICENSE
mkdir -p pbm2ppa
for file in CALIBRATION CREDITS INSTALL INSTALL-MORE LICENSE README ; do
  install -p -m 0644 pbm2ppa-0.8.6/$file pbm2ppa/$file
done


%files 
%license docs/en/LICENSE
%doc docs/en/CREDITS docs/en/INSTALL docs/en/README
%doc docs/en/RELEASE-NOTES docs/en/TODO
%doc docs/en/INSTALL.REDHAT.txt docs/en/COLOR.txt docs/en/CALIBRATION.txt
%doc docs/en/INSTALL.REDHAT.html docs/en/COLOR.html docs/en/CALIBRATION.html
%doc test.ps
%doc pbm2ppa
%{_bindir}/pnm2ppa
%{_bindir}/pbm2ppa
%{_bindir}/pbmtpg
%{_bindir}/calibrate_ppa
%{_bindir}/test_ppa
%{_bindir}/detect_ppa
%{_mandir}/man1/pnm2ppa.1*
%{_mandir}/man1/pbm2ppa.1*
%config(noreplace) %{_sysconfdir}/pnm2ppa.conf
%config(noreplace) %{_sysconfdir}/pbm2ppa.conf

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.13-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 03 2024 Zdenek Dohnal <zdohnal@redhat.com> - 1:1.13-5
- fix out of bound array access

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Oct 20 2023 Zdenek Dohnal <zdohnal@redhat.com> - 1:1.13-1
- rebase to 1.13
- license rescan and SPDX conversion

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.04-55
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.04-54
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.04-53
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.04-52
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.04-51
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.04-50
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 05 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1:1.04-49
- make is no longer in buildroot by default

* Tue Aug 04 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1:1.04-48
- fix argument reading for non x86_64 archs - use int instead of char

* Mon Aug 03 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1:1.04-47
- add foomatic as a dependency, because pnm2ppa drivers are not available as a driver without it

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.04-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 03 2020 Zdenek Dohnal <zdohnal@redhat.com> - 1:1.04-45
- FTBFS with GCC 10

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.04-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.04-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.04-42
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 24 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1:1.04-41
- correcting license

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.04-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1:1.04-39
- ship license in %%license tag

* Thu Mar 01 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1:1.04-38
- 1548734 - pnm2ppa: Partial Fedora build flags injection

* Mon Feb 19 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1:1.04-37
- gcc is no longer in buildroot by default

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.04-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 08 2018 Zdenek Dohnal <zdohnal@redhat.com> - 1:1.04-35
- remove old stuff https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/MRWOMRZ6KPCV25EFHJ2O67BCCP3L4Y6N/

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.04-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.04-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.04-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.04-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.04-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.04-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.04-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.04-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.04-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 23 2012 Tim Waugh <twaugh@redhat.com> - 1:1.04-25
- Fixed license tag.  pnm2ppa is GPLv2+; pbm2ppa is GPLv2.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.04-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.04-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri May 20 2011 Tim Waugh <twaugh@redhat.com> - 1:1.04-22
- Don't return a local variable out of scope (bug #704568).

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.04-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Oct 05 2010 Parag Nemade <paragn AT fedoraproject.org> - 1:1.04-20
- Merge-review cleanup (#226303)

* Fri Mar  5 2010 Tim Waugh <twaugh@redhat.com> - 1:1.04-19
- Consistent use of macros.
- Removed ancient obsoletes tag.
- Clean buildroot in install section not prep section.
- Make setup quiet.
- Use noreplace for config files.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.04-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.04-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 24 2008 Tim Waugh <twaugh@redhat.com> 1:1.04-16
- Removed patch fuzz.

* Wed Feb 13 2008 Tim Waugh <twaugh@redhat.com> 1:1.04-15
- Rebuild for GCC 4.3.

* Wed Aug 29 2007 Tim Waugh <twaugh@redhat.com> 1:1.04-14
- Added dist tag.
- Fixed summary.
- Better buildroot tag.
- More specific license tag.

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:1.04-13.2.2
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1:1.04-13.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1:1.04-13.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Wed Mar 16 2005 Tim Waugh <twaugh@redhat.com> 1:1.04-13
- Rebuild for new GCC.

* Wed Feb  9 2005 Tim Waugh <twaugh@redhat.com> 1:1.04-12
- s/Copyright:/License:/.
- s/Serial:/Epoch:/.
- Rebuilt.

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Thu Feb 19 2004 Tim Waugh <twaugh@redhat.com>
- rebuilt

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Wed Nov 20 2002 Tim Powers <timp@redhat.com>
- rebuild in current collinst

* Fri Jun 21 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Thu May 23 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed Jan 09 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Mon Dec 11 2000 Crutcher Dunnavant <crutcher@redhat.com>
- Upgrade to 1.04, editied the pbm2ppa patch to add <string.h>
- to pbmtpg.c, which uses strmp, edited the redhat patch to
- apply cleanly.

* Thu Aug 17 2000 Bill Nottingham <notting@redhat.com>
- tweak summary

* Thu Aug  3 2000 Bill Nottingham <notting@redhat.com>
- build upstream package

* Tue Jul 11 2000 Duncan Haldane <duncan_haldane@users.sourceforge.net>
- updated for 1.0 release.

* Mon Jul 10 2000 Florian La Roche <Florian.LaRoche@redhat.com>
- remove execute bits from config file and man-page

* Sun Apr 09 2000 <duncan_haldane@users.sourceforge.net>
- added optional updated rhs-printfilter  files

* Thu Feb 10 2000 Bill Nottingham <notting@redhat.com>
- adopt upstream package

* Sun Feb 6 2000 <duncan_haldane@users.sourceforge.net>
- new pnm2ppa release,  and add pbm2ppa driver.

* Thu Jan 6 2000 <duncan_haldane@users.sourceforge.net>
- created rpm



