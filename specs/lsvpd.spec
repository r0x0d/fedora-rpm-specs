Name:		lsvpd
Version:	1.7.15
Release:	6%{?dist}
Summary:	VPD/hardware inventory utilities for Linux

License:	GPL-2.0-or-later
URL:    https://github.com/power-ras/%{name}/releases
Source: https://github.com/power-ras/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: gcc-c++
BuildRequires: libvpd-devel >= 2.2.9
BuildRequires: sg3_utils-devel
BuildRequires: zlib-devel
BuildRequires: automake
BuildRequires: libtool
BuildRequires:	librtas-devel
BuildRequires: make

Requires(post): %{_sbindir}/vpdupdate

ExclusiveArch:	%{power64}

%description
The lsvpd package contains all of the lsvpd, lscfg and lsmcode
commands. These commands, along with a scanning program
called vpdupdate, constitute a hardware inventory
system. The lsvpd command provides Vital Product Data (VPD) about
hardware components to higher-level serviceability tools. The lscfg
command provides a more human-readable format of the VPD, as well as
some system-specific information.  lsmcode lists microcode and
firmware levels.  lsvio lists virtual devices, usually only found
on POWER PC based systems.

%prep
%autosetup -p1

%build
./bootstrap.sh
%configure
%make_build


%install
%make_install

%post
%{_sbindir}/vpdupdate &
# Ignore the vpdupdate failures and enforce a success
exit 0

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README
%{_sbindir}/lsvpd
%{_sbindir}/lscfg
%{_sbindir}/lsmcode
%{_sbindir}/lsvio
%{_sbindir}/vpdupdate
%{_mandir}/man8/vpdupdate.8.gz
%{_mandir}/man8/lsvpd.8.gz
%{_mandir}/man8/lscfg.8.gz
%{_mandir}/man8/lsvio.8.gz
%{_mandir}/man8/lsmcode.8.gz
%config %{_sysconfdir}/lsvpd/scsi_templates.conf
%config %{_sysconfdir}/lsvpd/cpu_mod_conv.conf
%config %{_sysconfdir}/lsvpd/nvme_templates.conf
%dir %{_sysconfdir}/lsvpd

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Feb 09 2024 Dan Horák <dan@danny.cz> - 1.7.15-4
- rebuilt for sg3_utils 1.48

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 02 2023 Than Ngo <than@redhat.com> - 1.7.15-1
- update to 1.7.15
- drop -std=c++14 build flag

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.14-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 23 2023 Than Ngo <than@redhat.com> - 1.7.14-6
- lsvpd is not reporting the correct I/O microcode
  for HBA, PCIe, SAS adapters, HDD, etc

* Thu Feb 16 2023 Than Ngo <than@redhat.com> - 1.7.14-5
- migrated to SPDX license

* Sun Feb 05 2023 Than Ngo <than@redhat.com> - 1.7.14-4
- added updatream patches to fix nvme vpd data

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr 07 2022 Dan Horák <dan[at]danny.cz> - 1.7.14-1
- rebase to 1.7.14

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Sep 15 2021 Than Ngo <than@redhat.com> - 1.7.13-1
- rebase to 1.7.13

* Fri Sep 03 2021 Than Ngo <than@redhat.com> - 1.7.12-1
- rebase to 1.7.12
- add support for SCSI loc-code
- Fix catching polymorphic type by value

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr 28 2021 Stephen Gallagher <sgallagh@redhat.com> - 1.7.11-7
- Rebuild to pick up sg3_utils in ELN

* Tue Apr 06 2021 Tomas Bzatek <tbzatek@redhat.com> - 1.7.11-6
- rebuilt for sg3_utils 1.46

* Tue Feb 09 2021 Than Ngo <than@redhat.com> - 1.7.11-5
- Fix, Vendor and Device information mismatch for usb-xhci

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Oct 27 2020 Jeff Law <law@redhat.com> - 1.7.11-3
- Force C++14 as this code is not C++17 ready

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 08 2020 Than Ngo <than@redhat.com> - 1.7.11-1
- update to 1.7.11

* Mon Apr 20 2020 Dan Horák <dan@danny.cz> - 1.7.10-3
- rebuilt for sg3_utils 1.45 (#1809392)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 02 2019 Than Ngo <than@redhat.com> - -1
- rebase to 1.7.10
- update Url

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Sinny Kumari <sinnykumari@fedoraproject.org> - 1.7.9-3
- Add gcc-c++ as BuildRequires

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Sinny Kumari<sinnykumari@fedoraproject.org> - 1.7.9-1
- Rebase to 1.7.9

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 20 2017 Sinny Kumari <sinnykumari@fedoraproject.org> - 1.7.8-4
- Add patches from upstream master branch to include fixes

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 05 2017 Sinny Kumari <sinnykumari@fedoraproject.org> - 1.7.8-1
- Rebase to 1.7.8

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr 14 2016 Sinny Kumari <sinnykumari@fedoraproject.org> - 1.7.7-1
- Update to 1.7.7

* Sat Apr  9 2016 Peter Robinson <pbrobinson@fedoraproject.org> 1.7.6-3
- Spec cleanup, use %%license
- Rebuild for litrtas soname bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Nov 16 2015 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.7.6
- Update to latest upstream 1.7.6

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.7.5-2
- Rebuilt for GCC 5 C++11 ABI change

* Mon Sep 22 2014 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.7.5
- Update to latest upstream 1.7.5

* Fri Aug 01 2014 Brent Baude <bbaude@redhat.com> - 1.7.4-4
- NVR bump for Fedora 21 build on merged koji

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 14 2014 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.7.4-2
- Grant permission to link with librtas library

* Mon Mar 17 2014 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.7.4
- Update to latest upstream 1.7.4

* Mon Mar 10 2014 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.7.3
- Update to latest upstream 1.7.3

* Thu Oct 10 2013 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.7.2-3
- Add ppc64le architecture

* Sun Sep 15 2013 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.7.2-2
- Fix build issue

* Thu Aug 22 2013 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.7.2
- Update to latest upstream 1.7.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Vasant Hegde <hegdevasant@linux.vnet.ibm.com> - 1.7.1
- Update to latest upstream 1.7.1
- Exclude invscout command from lsvpd package

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 04 2012 Karsten Hopp <karsten@redhat.com> 1.6.12-1
- update to 1.6.12

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.11-5
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 23 2011 Jiri Skala <jskala@redhat.com> - 1.6.11-3
- added ExclusiveArch for ppc[64]

* Wed Nov 09 2011 Jiri Skala <jskala@redhat.com> - 1.6.11-2
- fixes #752244 - similar output for different options in lsmcode

* Wed Aug 10 2011 Jiri Skala <jskala@redhat.com> - 1.6.11-1
- rebase to latest upstream 1.6.11

* Tue Feb 15 2011 Jiri Skala <jskala@redhat.com> - 1.6.10-1
- rebase to latest upstream 1.6.10

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Apr 13 2010 Dan Horák <dan@danny.cz> - 1.6.8-2
- rebuilt for sg3_utils 1.29

* Tue Apr 06 2010 Roman Rakus <rrakus@redhat.com> - 1.6.8-1
- Version 1.6.8 (need ugly bootstrap)

* Wed Dec 02 2009 Eric Munson <ebmunson@us.ibm.com> - 1.6.7-1
- Update to latest lsvpd release
- Add librtas support to build on POWERPC
- Add patch to lookup *.ids file location at runtime

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 28 2009 - Dan Horak <dan[at]danny.cz> - 1.6.5-2
- rebuild for sg3_utils 1.27

* Mon Mar 16 2009 Eric Munson <ebmunson@us.ibm.com> - 1.6.5-1
- Update source to use new glibc C header includes

* Mon Mar 16 2009 Eric Munson <ebmunson@us.ibm.com> - 1.6.4-6
- Bump for rebuild against latest build of libvpd

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 14 2008 - Eric Munson <ebmunson@us.ibm.com> - 1.6.4-4
- Bump for rebuild with new libvpd.

* Mon Jun 30 2008 - Dan Horak <dan[at]danny.cz> - 1.6.4-3
- add patch for sg3_utils 1.26 and rebuild

* Fri Jun 06 2008 - Caolán McNamara <caolanm@redhat.com> - 1.6.4-2
- rebuild for dependancies

* Fri Apr 25 2008 - Brad Peters <bpeters@us.ibm.com> - 1.6.4-1
- Adding ability to limit SCSI direct inquiry size, fixing Windows SCSI
  device inquiry problem

* Fri Mar 21 2008 - Eric Munson <ebmunson@us.ibm.com> - 1.6.3-1
- Adding proper conf file handling
- Removing executable bit on config and documentation files
- Removing second listing for config files

* Fri Mar 14 2008 - Eric Munson <ebmunson@us.ibm.com> - 1.6.2-3
- Becuase librtas is not yet in Fedora, the extra ppc dependency should
  be ignored

* Thu Mar 13 2008 - Eric Munson <ebmunson@us.ibm.com> - 1.6.2-2
- Adding arch check for ppc[64] dependency.

* Tue Mar 4 2008 - Eric Munson <ebmunson@us.ibm.com> - 1.6.2-1
- Updating for lsvpd-1.6.2

* Mon Mar 3 2008 - Eric Munson <ebmunson@us.ibm.com> - 1.6.1-1
- Updating for lsvpd-1.6.1

* Sat Feb 2 2008 - Eric Munson <ebmunson@us.ibm.com> - 1.6.0-1
- Updating lsvpd to use the new libvpd-2.0.0
- Removing %%{_mandir}/man8/* from %%files and replacing it with each
  individual file installed in the man8 directory

* Fri Dec 7 2007 - Brad Peters <bpeters@us.ibm.com> - 1.5.0
- Major changes in device detection code, basing detection on /sys/devices
  rather than /sys/bus as before
- Enhanced aggressiveness of AIX naming, ensuring that every detected device
  has at least one AIX name, and thus appears in lscfg output
- Changed method for discovering /sys/class entries
- Added some new VPD fields, one example of which is the device driver
  associated with the device
- Some minor changes to output formating
- Some changes to vpd collection
- Removing unnecessary Requires field

* Fri Nov 16 2007 - Eric Munson <ebmunson@us.ibm.com> - 1.4.0-1
- Removing udev rules from install as they are causing problems.  Hotplug 
  will be disabled until we find a smarter way of handling it.
- Updating License
- Adjusting the way vpdupdater is inserted into run control
- Removing #! from the beginning of the file.
- Fixes requested by Fedora Community

* Tue Oct 30 2007 - Eric Munson <ebmunson@us.ibm.com> - 1.3.5-1
- Remove calls to ldconfig
