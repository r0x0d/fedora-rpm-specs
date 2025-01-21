Name: uClibc
Version: 0.9.33.2
Release: 32%{?dist}
Summary: C library for embedded Linux

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2
URL: http://www.uclibc.org/
Source0: http://www.uclibc.org/downloads/%{name}-%{version}.tar.xz
Source1: uClibc.config
Patch1: uClibc-0.9.33.2_kernel_long.patch
Patch2: CVE-2016-6264.patch

BuildRequires: make
BuildRequires: gcc

# This package only contains a static library
%global debug_package %{nil}

# uclibc only supports those
ExclusiveArch: %{arm} %{ix86} x86_64 %{mips}

%description
uClibc is a C library for developing embedded Linux systems.
It is much smaller than the GNU C Library, but nearly all applications
supported by glibc also work perfectly with uClibc.

%package devel
Summary: Header files and libraries for uClibc library
Provides: uClibc-static = %{version}-%{release}

%description devel
uClibc is a C library for developing embedded Linux systems.
It is much smaller than the GNU C Library, but nearly all applications
supported by glibc also work perfectly with uClibc.
This package contains the header files and libraries
needed for uClibc package.

%prep
%setup -q -n %{name}-%{version}
%patch -P1 -b .kernel_long -p1
%patch -P2 -b .CVE-2016-6264 -p1

cat %{SOURCE1} >.config1
iconv -f windows-1252 -t utf-8 README >README.pom
mv README.pom README

%build
mkdir kernel-include
cp -a /usr/include/asm kernel-include
cp -a /usr/include/asm-generic kernel-include
cp -a /usr/include/linux kernel-include

arch=`uname -m | sed -e 's/i.86/i386/' -e 's/ppc/powerpc/' -e 's/armv7l/arm/' -e 's/armv5tel/arm/'`
echo "TARGET_$arch=y" >.config
echo "TARGET_ARCH=\"$arch\"" >>.config
%ifarch %{arm}
echo "CONFIG_ARM_EABI=y" >>.config
echo "ARCH_ANY_ENDIAN=n" >>.config
echo "ARCH_LITTLE_ENDIAN=y" >>.config
echo "ARCH_WANTS_LITTLE_ENDIAN=y" >>.config
%endif
%ifarch mips mipsel
echo "CONFIG_MIPS_ISA_MIPS32R2=y" >>.config
%ifarch mipsel
echo "ARCH_WANTS_LITTLE_ENDIAN=y" >>.config
%endif
%endif
%ifarch mips64 mips64el
echo "CONFIG_MIPS_ISA_MIPS64=y" >>.config
echo "CONFIG_MIPS_N64_ABI=y" >>.config
%ifarch mips64el
echo "ARCH_WANTS_LITTLE_ENDIAN=y" >>.config
%endif
%endif
cat .config1 >>.config

yes "" | make oldconfig %{?_smp_mflags}
make V=1 %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT/lib
make install PREFIX="$RPM_BUILD_ROOT/"
make install_headers PREFIX="$RPM_BUILD_ROOT/" DEVEL_PREFIX=""
cp -a kernel-include/* $RPM_BUILD_ROOT/include/

# move libraries to proper subdirectory
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/uClibc
mv  $RPM_BUILD_ROOT/lib/*  $RPM_BUILD_ROOT/%{_libdir}/uClibc/
rm -rf  $RPM_BUILD_ROOT/lib/

# move the header files to /usr subdirectory
mkdir -p $RPM_BUILD_ROOT/%{_includedir}/uClibc
mv  $RPM_BUILD_ROOT/include/*  $RPM_BUILD_ROOT/%{_includedir}/uClibc
rm -rf  $RPM_BUILD_ROOT/include/

%files devel
%doc README docs/Glibc_vs_uClibc_Differences.txt docs/threads.txt docs/uClibc_vs_SuSv3.txt
%doc TODO DEDICATION.mjn3 MAINTAINERS
%doc docs/PORTING COPYING.LIB
%{_includedir}/uClibc
%{_libdir}/uClibc

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.33.2-31
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Nikola Forró <nforro@redhat.com> - 0.9.33.2-17
- add missing gcc build dependency

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 20 2016 Dan Horák <dan[at]danny.cz> - 0.9.33.2-12
- switch to ExclusiveArch

* Mon Aug 15 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.9.33.2-11
- Update Power64 macro

* Mon Jul 11 2016 Nikola Forró <nforro@redhat.com> - 0.9.33.2-10
- fix CVE-2016-6264
  resolves #1352460

* Thu Feb 18 2016 Nikola Forró <nforro@redhat.com> - 0.9.33.2-9
- add support for MIPS
  resolves #1305957

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.33.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.33.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.33.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.33.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon May 19 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.9.33.2-5
- No aarch64 support

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.33.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May  6 2013 Denys Vlasenko <dvlasenko@redhat.com> - 0.9.32-3
- Enable UCLIBC_HAS_RESOLVER_SUPPORT, UCLIBC_LINUX_MODULE_26,
  UCLIBC_HAS_SHA256/512_CRYPT_IMPL, UCLIBC_HAS_FOPEN_CLOSEEXEC_MODE
  config options.
- fix __kernel_long_t problem.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.33.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Peter Schiffer <pschiffe@redhat.com> - 0.9.33.2-1
- resolves: #771041
  update to 0.9.33.2

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.32-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 18 2011 Peter Schiffer <pschiffe@redhat.com> - 0.9.32-2
- fixed compile error on i686

* Tue Aug 16 2011 Peter Schiffer <pschiffe@redhat.com> - 0.9.32-1
- resolves: #712040
  resolves: #716134
  update to 0.9.32 final

* Mon Jun 13 2011 Peter Robinson <pbrobinson@gmail.com> - 0.9.32-0.5.rc2
- And set the ARM build to little endian

* Sat Jun 11 2011 Peter Robinson <pbrobinson@gmail.com> - 0.9.32-0.4.rc2
- It seems we need to set the ARM ABI to EABI too

* Sat Jun 11 2011 Peter Robinson <pbrobinson@gmail.com> - 0.9.32-0.3.rc2
- Add support for ARM

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.32-0.2.rc2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb  7 2011 Tom Callaway <spot@fedoraproject.org> - 0.9.32-0.1.rc2
- update config for 0.9.32-rc2, busybox
- patch getutent

* Tue Nov  9 2010 Ivana Hutarova Varekova <varekova@redhat.com> - 0.9.31-2
- update to 0.9.31

* Fri Jun  5 2009 Ivana Varekova <varekova@redhat.com> - 0.9.30.1-2
- initial build for Red Hat
