%global debug_package %{nil}

# rhbz #1923589
%define _legacy_common_support 1
%global _lto_cflags %nil

# prefer new (rpm >= 4.11) macrosdir if present
%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] ||
d=%{_sysconfdir}/rpm; echo $d)

Name:           gnustep-make
Version:        2.9.2
Release:        5%{?dist}
Summary:        GNUstep makefile package
License:        GPL-3.0-or-later
URL:            http://www.gnustep.org/
Source0:        ftp://ftp.gnustep.org/pub/gnustep/core/%{name}-%{version}.tar.gz

# Taken from git://fedorahosted.org/git/gnustep-rpm-macros.git
Source1:        %{name}-macros.gnustep

BuildRequires:  gcc-objc
BuildRequires:  texinfo-tex tetex-latex tetex-dvips latex2html texi2html
BuildRequires:  make
Requires:       gnustep-filesystem%{?_isa} = %{version}-%{release}


%description
The makefile package is a simple, powerful and extensible way to write
makefiles for a GNUstep-based project.  It allows the user to write a
project without having to deal with the complex issues associated with
configuration, building, installation, and packaging.  It also allows
the user to easily create cross-compiled binaries.


%package -n     gnustep-filesystem
Summary:        The basic directory layout for GNUstep packages
License:        LicenseRef-Not-Copyrightable

%description -n gnustep-filesystem
The gnustep-filesystem package contains the basic directory layout for
GNUstep packages.


%package        doc
Summary:        Documentation for %{name}
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
BuildArch:      noarch
Requires:       gnustep-filesystem = %{version}-%{release}

%description    doc
The makefile package is a simple, powerful and extensible way to write
makefiles for a GNUstep-based project.  It allows the user to write a
project without having to deal with the complex issues associated with
configuration, building, installation, and packaging.  It also allows
the user to easily create cross-compiled binaries.
This package contains documentation for %{name}.

%prep
%autosetup

cp %{SOURCE1} macros.gnustep

sed -i "s|/@libdir@|/%{_lib}|g" FilesystemLayouts/fhs-system
sed -i "s|/@libdir@|/%{_lib}|g" FilesystemLayouts/fhs

# /usr/share/GNUstep/Makefiles/config-noarch.make and
# /usr/share/GNUstep/Makefiles/ix86/linux-gnu/gnu-gnu-gnu/config.make
# are spoiling a pure /usr/share install
sed -i "s|=/share/GNUstep/Makefiles|=/%{_lib}/GNUstep/Makefiles|" \
    FilesystemLayouts/fhs-system

# Fix files location except GNUSTEP_LOCAL_*
sed -i "67,77!s|=/local|=|" FilesystemLayouts/fhs-system 

%build
%if 0%{?rhel} >= 8
export CC=gobjc
%endif

%configure --with-layout=fhs-system --enable-flattened
%make_build V=1

%install
%make_install GNUSTEP_INSTALLATION_DOMAIN=SYSTEM
%make_install -C Documentation GNUSTEP_INSTALLATION_DOMAIN=SYSTEM GNUSTEP_MAKEFILES=%{buildroot}%{_libdir}/GNUstep/Makefiles
%make_install -C Documentation GNUSTEP_INSTALLATION_DOMAIN=SYSTEM GNUSTEP_MAKEFILES=%{buildroot}%{_libdir}/GNUstep/Makefiles

# create remaining GNUstep directories
for i in Applications WebApplications; do
    mkdir -p %{buildroot}%{_prefix}{,/local}/lib{,64}/GNUstep/$i
done
mkdir -p %{buildroot}%{_prefix}{,/local}/share/GNUstep/Documentation/Developer

# INstall rpm macros
install -d %{buildroot}%{macrosdir}
install -p -m 644 macros.gnustep %{buildroot}%{macrosdir}

%files
%config(noreplace) %{_sysconfdir}/GNUstep/GNUstep.conf
%{_bindir}/gnustep-config
%{_bindir}/gnustep-tests
%{_bindir}/openapp
%{_bindir}/debugapp
%{_bindir}/opentool
%{_libdir}/GNUstep/Makefiles/*
%{_mandir}/man*/*
%{_infodir}/gnustep*.info*
%{macrosdir}/macros.gnustep

%files -n gnustep-filesystem
%doc ANNOUNCE FAQ NEWS README
%license COPYING
%dir %{_sysconfdir}/GNUstep
%dir %{_libdir}/GNUstep
%dir %{_libdir}/GNUstep/Makefiles
%dir %{_libdir}/GNUstep/Applications
%dir %{_libdir}/GNUstep/WebApplications
%dir %{_datadir}/GNUstep
%dir %{_datadir}/GNUstep/Documentation
%dir %{_datadir}/GNUstep/Documentation/Developer

%files doc
%doc %{_datadir}/GNUstep/Documentation/*

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 2.9.2-4
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Antonio Trande <sagitter@fedoraproject.org> - 2.9.2-2
- Fix rhbz#2283758

* Sat Jun 01 2024 Antonio Trande <sagitter@fedoraproject.org> - 2.9.2-1
- Update to 2.9.2

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Nov 19 2023 Antonio Trande <sagitter@fedoraproject.org> - 2.9.1-1
- Update to 2.9.1

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Sep 06 2022 Antonio Trande <sagitter@fedoraproject.org> - 2.9.0-8
- Remove injected package_note flag in Fedora < 37 only

* Tue Sep 06 2022 Antonio Trande <sagitter@fedoraproject.org> - 2.9.0-7
- Remove injected package_note flag in Fedora < 38 only

* Wed Aug  3 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.9.0-6
- Remove injected package_note flag from installed scripts

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Sep 18 2021 Robert Scheck <robert@fedoraproject.org> - 2.9.0-3
- Change %%gnustep_{configure,make} macros to use gobjc on EPEL 8

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 15 2021 Antonio Trande <sagitter@fedoraproject.org> - 2.9.0-1
- Update to 2.9.0

* Sat Apr 03 2021 Antonio Trande <sagitter@fedoraproject.org> - 2.8.0-5
- RHBZ #1923589

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 16 2020 Antonio Trande <sagitter@fedoraproject.org> - 2.8.0-1
- Update to 2.8.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar  7 2019 Tim Landscheidt <tim@tim-landscheidt.de> - 2.7.0-7
- Remove obsolete requirements for %%post/%%preun scriptlets

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Apr 15 2017 Antonio Trande <sagitter@fedoraproject.org> - 2.7.0-1
- Update to 2.7.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 21 2016 Antonio Trande <sagitter@fedoraproject.org> - 2.6.8-1
- Update to 2.6.8

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 15 2015 Jochen Schmitt <Jochen herr-schmitt de> - 2.6.7-1
- New upstream release

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb  7 2014 Michel Salim <salimma@fedoraproject.org> - 2.6.6-2
- Use correct macros directory on systems with RPM >= 4.11

* Sun Jan 12 2014 Jochen Schmitt <Jochen herr-schmitt de> - 2.6.6-1
- New upstream release

* Fri Sep  6 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.6.5-4
- Fix issue with using DESTDIr in Framework.make (#1005328)

* Wed Aug 21 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.6.5-3
- Change macros in macros.gnustep

* Tue Aug  6 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.6.5-2
- Remove empty versioned docdir (#993796(

* Tue Jul 30 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.6.5-1
- New upstream release

* Tue May  7 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.6.4-13
- Remove %%gnustep_movefiles and %%gnustep_bothfiles from macros.gnustep

* Tue May  7 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.6.4-12
- Move DTDs subdir back to %%{gnustep_libdir} in macros.gnustep

* Sun May  5 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.6.4-11
- Remove /usr/local dirs from gnustep-filesystem (#959770)

* Fri Apr  5 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.6.4-9
- Remove / at the end of the gnustep macro definitions

* Thu Apr  4 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.6.4-8
- Make gnustep-filesystem acht dependent

* Mon Apr  1 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.6.4-7
- Remove GNUSTEP_MAKFILES assignment from %%gnustep_make macro

* Sun Mar 31 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.6.4-6
- Fix issue with continuations in rpm macros

* Sun Mar 31 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.6.4-5
- Fix typo in rpm macro definitions

* Sun Mar 31 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.6.4-4
- Add rpm macros for gnustep packaging
- Package cleanup

* Fri Mar 29 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.6.4-2
- Try to fix aarm64 issue (#925465)

* Fri Mar 29 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.6.4-1
- New upstream release

* Sun Mar  3 2013 Jochen Schmitt <Jochen herr-schmitt de> - 2.6.3-2
- New upstream Release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb  8 2012 Jochen Schmitt <Jochen herr-schmitt de> 2.6.2-1
- New upstream release
- Switch back to gcc-objc

* Wed Jan 18 2012 Jochen Schmitt <Jochen herr-schmitt de> 2.6.1-3
- Migratiing to clang

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun  7 2011 Jochen Schmitt <Jochen herr-schmitt de> 2.6.1-1
- New upstream release

* Mon May 30 2011 Jochen Schmitt <Jochen herr-schmitt de> 2.6.0-2
- Add BR gcc-objc for exception handling (#708975)

* Thu Apr 14 2011 Jochen Schmitt <Jochen herr-schmitt de> 2.6.0-1
- New upstream release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul  5 2010 Jochen Schmitt <Jochen herr-schmitt de> - 2.4.0-1
- New upstream release

* Sun May  9 2010 Michel Salim <salimma@fedoraproject.org> - 2.2.0-4
- Add Documentation/Developer directories to -filesystem (bug #585721)

* Sun Sep 13 2009 Michel Salim <salimma@fedoraproject.org> - 2.2.0-3
- Package now BuildConflicts: itself (bz#473342)

* Sun Sep 13 2009 Michel Salim <salimma@fedoraproject.org> - 2.2.0-2
- Rename overly-generic info files
- Fix all references to lib -> %%{_lib}
- Add more directories to gnustep-filesystem

* Sat Sep 12 2009 Michel Salim <salimma@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0
- Replace perl scripts with sed equivalents; dropping BR

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Mar 12 2009 Michel Salim <salimma@fedoraproject.org> - 2.0.8-2
- Put documentation into separate subpackage

* Tue Mar  3 2009 Jochen Schmitt <Jochen herr-schmitt de> - 2.0.8-1
- New upstream release

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Dec 10 2008 Jochen Schmitt <Jochen herr-schmitt de> - 2.0.6-14
- Remove libcombo stuff
- Make sure the libraries are going to /usr/lib64 on x86_64 architecure

* Tue Aug 26 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.6-13
- fix license tag

* Wed Aug  6 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.0.6-12
- Fix %%{_datadir} to %%{_libdir} bug in documentation build.

* Fri Jul  4 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.0.6-11
- Update to 2.0.6.
- Move %%{_datadir} to %%{_libdir}, see inline comment.

* Tue Mar  4 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.0.4-9
- Really fix the make.info clash.

* Fri Feb 22 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.0.4-8
- Rename make.info to avoid clash with GNU make.

* Mon Feb 18 2008 Axel Thimm <Axel.Thimm@ATrpms.net> - 2.0.4-7
- Update to 2.0.4.

* Mon Feb 12 2007 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.13.0-6
- Update to 1.13.0.

* Fri Jul 28 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.12.0-5
- Try to make FHS compliant.

* Tue Jul 11 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.12.0-4
- Remove default -lobjc-fd2 switch.
- Disable flat hierarchy to allow for different library combos.

* Wed Jul  5 2006 Axel Thimm <Axel.Thimm@ATrpms.net> - 1.12.0-3
- Update to 1.12.0.
- Use %%{?dist} instead of %%atrelease.
- Use %%{_libdir}/GNUstep as system root.

* Sun Mar 12 2006 Axel Thimm <Axel.Thimm@ATrpms.net>
- Initial build.

