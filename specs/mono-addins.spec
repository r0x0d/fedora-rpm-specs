%if 0%{?rhel}%{?el6}%{?el7}
# see https://lists.fedoraproject.org/pipermail/packaging/2011-May/007762.html
%global _missing_build_ids_terminate_build 0
%global debug_package %{nil}
# see https://fedorahosted.org/fpc/ticket/395
%define _monodir %{_prefix}/lib/mono
%define _monogacdir %{_prefix}/lib/mono/gac
%endif

%define debug_package %{nil}

Name:		mono-addins
Version:	1.3.3
Release:	8%{?dist}
Summary:	Addins for mono
License:	MIT
URL:		http://www.mono-project.com/Main_Page
Source0:	https://github.com/mono/mono-addins/archive/refs/tags/mono-addins-%{version}.tar.gz
Patch0:		mono-addins-1.0-libdir.patch

BuildRequires: make
BuildRequires:	mono-devel >= 2.4
BuildRequires:	gtk-sharp2-devel
BuildRequires:  autoconf, automake, libtool
BuildRequires:	pkgconfig

# Mono only available on these:
ExclusiveArch: %mono_arches

Provides: mono(Mono.Addins) = 0.2.0.0
Provides: mono(Mono.Addins) = 0.3.0.0
Provides: mono(Mono.Addins) = 0.4.0.0
Provides: mono(Mono.Addins) = 0.5.0.0
Provides: mono(Mono.Addins) = 0.6.0.0
Provides: mono(Mono.Addins.Gui) = 0.2.0.0
Provides: mono(Mono.Addins.Gui) = 0.3.0.0
Provides: mono(Mono.Addins.Gui) = 0.4.0.0
Provides: mono(Mono.Addins.Gui) = 0.5.0.0
Provides: mono(Mono.Addins.Gui) = 0.6.0.0
Provides: mono(Mono.Addins.Setup) = 0.2.0.0
Provides: mono(Mono.Addins.Setup) = 0.3.0.0
Provides: mono(Mono.Addins.Setup) = 0.4.0.0
Provides: mono(Mono.Addins.Setup) = 0.5.0.0
Provides: mono(Mono.Addins.Setup) = 0.6.0.0
Provides: mono(Mono.Addins.CecilReflector) = 0.2.0.0
Provides: mono(Mono.Addins.CecilReflector) = 0.3.0.0
Provides: mono(Mono.Addins.CecilReflector) = 0.4.0.0
Provides: mono(Mono.Addins.CecilReflector) = 0.5.0.0
Provides: mono(Mono.Addins.CecilReflector) = 0.6.0.0

%description
Mono.Addins is a generic framework for creating extensible applications,
and for creating libraries which extend those applications.

%package devel
Summary: Development files for mono-addins
Requires: %{name} = %{version}-%{release} pkgconfig
Provides: mono(Mono.Addins.MSBuild) = 0.2.0.0
Provides: mono(Mono.Addins.MSBuild) = 0.3.0.0
Provides: mono(Mono.Addins.MSBuild) = 0.4.0.0
Provides: mono(Mono.Addins.MSBuild) = 0.5.0.0
Provides: mono(Mono.Addins.MSBuild) = 0.6.0.0

%description devel
Mono.Addins is a generic framework for creating extensible applications,
and for creating libraries which extend those applications.
This package contains MSBuild tasks file and target, which allows
using add-in references directly in a build file (still experimental).

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch -P0 -p1 -b .libdir

%build
sed -i "s#AC_PATH_PROG(MCS, gmcs, no)#AC_PATH_PROG(MCS, mcs, no)#g" configure.ac
autoreconf -vif
%configure --enable-gui
#find . -name "Makefile*" -print -exec sed -i 's#ASSEMBLY_COMPILER_COMMAND = gmcs#ASSEMBLY_COMPILER_COMMAND = mcs#g; s#-r:Microsoft.Build.Utilities #-r:Microsoft.Build.Utilities.v4.0 #g' {} \;
find . -name "*.sln" -print -exec sed -i 's/Format Version 10.00/Format Version 11.00/g' {} \;
find . -name "*.csproj" -print -exec sed -i 's#ToolsVersion="3.5"#ToolsVersion="4.0"#g; s#<TargetFrameworkVersion>.*</TargetFrameworkVersion>##g; s#<PropertyGroup>#<PropertyGroup><TargetFrameworkVersion>v4.5</TargetFrameworkVersion>#g' {} \;
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files 
%doc README NEWS AUTHORS ChangeLog
%{_bindir}/mautil
%dir %{_monodir}/mono-addins
%{_monodir}/mono-addins/Mono.Addins.CecilReflector.dll
%{_monodir}/mono-addins/Mono.Addins.Gui*.dll
%{_monodir}/mono-addins/Mono.Addins.Setup.dll
%{_monodir}/mono-addins/Mono.Addins.dll
%{_monodir}/mono-addins/mautil.exe
%{_monogacdir}/Mono.Addins.Gui*
%{_monogacdir}/Mono.Addins.Setup
%{_monogacdir}/Mono.Addins
%{_monogacdir}/Mono.Addins.CecilReflector
%{_monogacdir}/policy.*.Mono.Addins
%{_monogacdir}/policy.*.Mono.Addins.Gui*
%{_monogacdir}/policy.*.Mono.Addins.Setup
%{_monogacdir}/policy.*.Mono.Addins.CecilReflector

%{_mandir}/man1/mautil.1.gz

%files devel
%{_monodir}/gac/policy.*.Mono.Addins.MSBuild
%{_monodir}/mono-addins/Mono.Addins.MSBuild.dll
%{_monodir}/gac/Mono.Addins.MSBuild
%{_libdir}/pkgconfig/mono-addins*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.3-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 21 2021 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 1.3.3-0
- Update to latest release 1.3.3

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 02 2019 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 1.1-12
- Rebuilt to avoid bad provides in previous build with broken mono rpm scripts

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- mono rebuild for aarch64 support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 17 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> - 1.1-1
- Update to 1.1
- Add mono macros for epel

* Wed Apr 15 2015 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 0.6.2-12
- build for Mono 4

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Brent Baude <baude@us.ibm.com> - 0.6.2-9
- Changing ppc64 arch to power64 macro

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 30 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.6.2-5
- Add patch to fix issues with pkglibdir

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Oct 23 2011 Christian Krause <chkr@fedoraproject.org> - 0.6.2-3
- Change paths for mono assemblies according to updated packaging
  guidelines (http://fedoraproject.org/wiki/Packaging:Mono)

* Sun Sep 11 2011 Christian Krause <chkr@fedoraproject.org> - 0.6.2-2
- Fix paths for x86_64

* Sun Sep 04 2011 Christian Krause <chkr@fedoraproject.org> - 0.6.2-1
- Update to 0.6.2 release
- Manually add some Provides to reflect the compatible API versions
  as defined by the policy files

* Mon Mar 28 2011 Christian Krause <chkr@fedoraproject.org> - 0.5-5
- Use official 0.5 release linked from http://ftp.novell.com/pub/mono/archive/2.6.7/sources/
- Move MSBuild parts into -devel package so that the main package does not
  depend on mono-devel (BZ 671917)
- Minor spec file cleanup

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 07 2011 Dan Horák <dan[at]danny.cz> - 0.5-3
- updated the supported arch list

* Fri Oct 29 2010 Christian Krause <chkr@fedoraproject.org> - 0.5-2
- Rebuild again to create correct requires/provides capabilities

* Sat Oct 09 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.5-1.1
- Rebuild

* Mon May 31 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.5-1
- Update to 5.0 release
- Alter URL

* Fri Apr 10 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.4-5.20091702svn127062.1
- Exclude ppc

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-5.20091702svn127062
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 17 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.4-4.20091702svn127062
- update from svn

* Tue Feb 10 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.4-4.20091002svn126354
- large update from svn
- now uses a tarball
- add mautil manual

* Thu Jan 29 2009 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.4-4.20081215svn105642
- update to 2.4 svn build
- remove mautil manuals

* Thu Dec 11 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.4-3
- Rebuild
- Correct licence to MIT
- Replaced patch with sed

* Tue Nov 25 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.4-2
- Fix archs

* Fri Nov 07 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.4-1
- new release
- removed scan fix patch

* Mon Jul 14 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.3.1-2.2
- rebuild

* Thu May 01 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.3.1-2.1
- rebuild

* Tue Apr 29 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.3.1-2
- added BR pkgconfig

* Mon Apr 21 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.3.1-1
- bump (should fix the monodevelop problems)

* Tue Apr 15 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 0.3-5
- Add patch from Debian to make sure addins don't disappear in f-spot (#442343)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3-4
- Autorebuild for GCC 4.3

* Mon Jan 14 2008 <paul@all-the-johnsons.co.uk> 0.3-3
- removed debug package
- spec file fixes
- additional BRs for autoreconf
- excludearch ppc64 added

* Thu Jan 03 2008 <paul@all-the-johnsons.co.uk> 0.3-2
- enabled gui
- spec file fixes

* Wed Dec 19 2007 <paul@all-the-johnsons.co.uk> 0.3-1
- Initial import for FE
