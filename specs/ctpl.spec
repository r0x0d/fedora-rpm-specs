%global ctpl_docdir %{_defaultdocdir}/ctpl-%{version}

Name:           ctpl
Version:        0.3.5
Release:        2%{?dist}
Summary:        Template library and engine written in C

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://ctpl.tuxfamily.org/
Source0:        http://download.tuxfamily.org/ctpl/releases/ctpl-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  glib2-devel >= 2.10
BuildRequires:  make
Requires:       ctpl-libs = %{version}-%{release}

%description
CTPL is a template library written in C. It allows fast and easy parsing of
templates from many sources (including in-memory data and local and remote
streaming, thanks to GIO) and fine control over template parsing environment.

CTPL has following features:
* It is a library, then it can be easily used from programs
* Separated lexer and parser
* It is written in portable C
* Simple syntax
* Fast and strict parsing
* Possible in-memory parsing, allowing non-file data parsing and avoiding
  I/O-latency, through GIO's GMemoryInputStream and GMemoryOutputStream


%package libs
Summary: Template library written in C

%description libs
This package contains the CTPL library.

%ldconfig_scriptlets libs


%package devel
Summary:   Development headers of the template library written in C
Requires:  ctpl-libs = %{version}-%{release}

%description devel
This package contains the development headers of the CTPL library.


%package doc
Summary:   Documentation for the CTPL library
Requires:  ctpl-libs = %{version}-%{release}

%if %{?fedora}%{!?fedora:0} >= 10 || %{?rhel}%{!?rhel:0} >= 6
BuildArch: noarch
%endif

%description doc
This package contains the HTML documentation reference for the CTPL library.


%prep
%setup -q

# remove waf since this isn't needed for the build, we're building the
# package with autotools
rm -f waf
rm -f wscript


# The CLI tool only needs to be disabled on RHEL because of GIO dependency issues,
# see RHBZ#749874 for more detailed information.
%if 0%{?rhel}
%patch -P0 -p1
%endif

#%patch1 -p1


%build
%if 0%{?rhel}
%configure --docdir %{ctpl_docdir} --disable-cli-tool
%else
%configure --docdir %{ctpl_docdir}
%endif

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Seems the --docdir flag is not working correctly, working around this here
# for now
install -d $RPM_BUILD_ROOT%{ctpl_docdir}
install -Dpm0644 AUTHORS COPYING NEWS HACKING TODO README THANKS $RPM_BUILD_ROOT%{ctpl_docdir}

rm -f $RPM_BUILD_ROOT%{_libdir}/libctpl.a
rm -f $RPM_BUILD_ROOT%{_libdir}/libctpl.la


%if ! 0%{?rhel}
%files
%doc %{_mandir}/man1/%{name}.1.*
%{_bindir}/%{name}
%endif


%files libs
%dir %{ctpl_docdir}
%doc %{ctpl_docdir}/AUTHORS
%doc %{ctpl_docdir}/COPYING
%doc %{ctpl_docdir}/NEWS
%{_libdir}/lib%{name}.so.*
%{_datadir}/locale/fr/LC_MESSAGES/%{name}.mo
%{_datadir}/locale/it/LC_MESSAGES/%{name}.mo


%files devel
%doc %{ctpl_docdir}/HACKING
%doc %{ctpl_docdir}/TODO
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc


%files doc
%doc %{ctpl_docdir}/README
%doc %{ctpl_docdir}/THANKS
%doc %{_datadir}/gtk-doc/html/%{name}


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Aug 03 2024 Dominic Hopf <dmaphy@fedoraproject.org> - 0.3.5-1
- New Upstream release (RHBZ#2302212)
- Fixes #2261049 and #2300615 

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.3.4-22
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Feb 04 2015 Dominic Hopf <dmaphy@fedoraproject.org> - 0.3.4-1
- Update to 0.3.4 upstream release

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Oct 18 2013 Dominic Hopf <dmaphy@fedoraproject.org> - 0.3.3-1
- Update to 0.3.3 upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 28 2013  Dominic Hopf <dmaphy@fedoraproject.org> - 0.3.2-8
- support build for aarch64 (RHBZ#925206)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec 18 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 0.3.2-4
- do not build the CLI tool when building for EPEL

* Wed May 25 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 0.3.2-3
- remove depedency on gtk-doc (fixes #707547)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 18 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 0.3.2-1
- new upstream release: CTPL 0.3.2

* Tue Oct 26 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.3-1
- new upstream release: CTPL 0.3

* Sat Jul 17 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.2.2-4
- fix rpmlint binary-or-shlib-defines-rpath error
- fix rpmlint library-without-ldconfig-* errors
- make the -doc package noarch
- remove the -bin subpackage, the binary files will now be installed with the
  main package, thus when typing 'yum install ctpl'
- require gtk-doc for the -doc package
- ctpl-libs now owns /usr/share/doc/ctpl-0.2.2
- fix redundant file listings
- require -libs package with fully qualified version for the binary package

* Fri Jul 16 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.2.2-3
- move the %%{_libdir}/lib%%{name}.so back to the -devel package where it
  belongs to

* Fri Jul 16 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.2.2-2
- rename subpackage lib to libs
- add Requires on the libs package to -bin, -devel and -doc package
- install %%{_libdir}/lib%%{name}.so with a -static package
- install manpage only with the binary
- install HACKING and TODO only with the -devel package
- install README and THANKS only with the -doc package
- fix the installation path for documentation files

* Thu Jul 15 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.2.2-1
- initial specfile
