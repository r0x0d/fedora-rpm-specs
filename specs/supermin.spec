# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

# On platforms and architectures that support it, the default is
# ‘--with dietlibc’.
#
# To use glibc-static instead, do ‘--without dietlibc’.  This results
# in a much larger (about 40 times larger) init binary.
#
# On other platforms, there is no dietlibc, so the default for those
# is ‘--without dietlibc’.
#
# See also:
# https://github.com/libguestfs/supermin/commit/9bb57e1a8d0f3b57eb09f65dd574f702b67e1c2f

%if 0%{?rhel}
%bcond_with dietlibc
%else
%ifarch aarch64 %{arm} %{ix86} %{power} s390x x86_64
%bcond_without dietlibc
%else
%bcond_with dietlibc
%endif
%endif

%if 0%{?fedora} > 40 || 0%{?rhel} > 10
%bcond_without dnf5
%else
%bcond_with dnf5
%endif

# Whether we should verify tarball signature with GPGv2.
%global verify_tarball_signature 1

# The source directory.
%global source_directory 5.3-development

Summary:       Tool for creating supermin appliances
Name:          supermin
Version:       5.3.5
Release:       4%{?dist}
License:       GPL-2.0-or-later

ExclusiveArch: %{kernel_arches}
%if 0%{?rhel}
# No qemu-kvm on POWER (RHBZ#1946532).
ExcludeArch:   %{power64}
%endif

URL:           http://people.redhat.com/~rjones/supermin/
Source0:       http://download.libguestfs.org/supermin/%{source_directory}/%{name}-%{version}.tar.gz
Source1:       http://download.libguestfs.org/supermin/%{source_directory}/%{name}-%{version}.tar.gz.sig
# Keyring used to verify tarball signature.
Source2:       libguestfs.keyring

# Use stable owner, group and mtime in base.tar.gz
# Upstream in > 5.3.5
# https://bugzilla.redhat.com/show_bug.cgi?id=2320025
Patch1:        0001-prepare-Use-stable-owner-group-and-mtime-in-base.tar.patch

BuildRequires: gcc
BuildRequires: make
BuildRequires: autoconf, automake
BuildRequires: /usr/bin/pod2man
BuildRequires: /usr/bin/pod2html
BuildRequires: rpm
BuildRequires: rpm-devel
%if %{with dnf5}
BuildRequires: dnf5
%else
BuildRequires: dnf
BuildRequires: dnf-plugins-core
%endif
BuildRequires: /usr/sbin/mke2fs
BuildRequires: e2fsprogs-devel
BuildRequires: findutils
%if %{with dietlibc}
BuildRequires: dietlibc-devel
%else
BuildRequires: glibc-static
%endif
BuildRequires: ocaml, ocaml-findlib-devel
%if 0%{verify_tarball_signature}
BuildRequires: gnupg2
%endif

# These are required only to run the tests.  We could patch out the
# tests to not require these packages.
BuildRequires: augeas hivex kernel tar

%if 0%{?rhel}
%ifarch s390x
# On RHEL 9 s390x, kernel incorrectly pulls in kernel-zfcpdump-core
# https://bugzilla.redhat.com/show_bug.cgi?id=2027654
BuildRequires: kernel-core
%endif
%endif

# For complicated reasons, this is required so that
# /bin/kernel-install puts the kernel directly into /boot, instead of
# into a /boot/<machine-id> subdirectory (in Fedora >= 23).  Read the
# kernel-install script to understand why.
BuildRequires: grubby
# https://bugzilla.redhat.com/show_bug.cgi?id=1331012
BuildRequires: systemd-udev

# This only includes the dependencies needed at runtime, ie.  supermin
# --build.  For supermin --prepare, dependencies like dnf are placed
# in the -devel subpackage.
Requires:      rpm
Requires:      util-linux-ng
Requires:      cpio
Requires:      tar
Requires:      /usr/sbin/mke2fs
# RHBZ#771310
Requires:      e2fsprogs-libs >= 1.42

# For automatic RPM dependency generation.
# See: https://rpm-software-management.github.io/rpm/manual/dependency_generators.html
Source3:       supermin.attr
Source4:       supermin-find-requires


%description
Supermin is a tool for building supermin appliances.  These are tiny
appliances (similar to virtual machines), usually around 100KB in
size, which get fully instantiated on-the-fly in a fraction of a
second when you need to boot one of them.

Note that if you want to run 'supermin --prepare' you will need the
extra dependencies provided by %{name}-devel.


%package devel
Summary:       Development tools for %{name}
Requires:      %{name} = %{version}-%{release}
Requires:      rpm-build

# Dependencies needed for supermin --prepare
%if %{with dnf5}
Requires:      dnf5
%else
Requires:      dnf
Requires:      dnf-plugins-core
%endif
Requires:      findutils


%description devel
%{name}-devel contains development tools for %{name}.

It contains extra dependencies needed for 'supermin --prepare' to
work, as well as tools for automatic RPM dependency generation from
supermin appliances.


%prep
%if 0%{verify_tarball_signature}
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif
%setup -q
%autopatch -p1


%build
autoreconf -fi
# Setting DNF is temporarily required for Rawhide.  We should be able
# to remove this later.  See:
# https://bugzilla.redhat.com/show_bug.cgi?id=2209412
# https://fedoraproject.org/wiki/Changes/ReplaceDnfWithDnf5
%configure %{?with_dnf5:DNF=%{_bindir}/dnf5} --disable-network-tests

%if %{with dietlibc}
make -C init CC="diet gcc"
%endif
make %{?_smp_mflags}


%install
make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT%{_rpmconfigdir}/fileattrs/
install -m 0644 %{SOURCE3} $RPM_BUILD_ROOT%{_rpmconfigdir}/fileattrs/
install -m 0755 %{SOURCE4} $RPM_BUILD_ROOT%{_rpmconfigdir}/


%check

# Skip execstack test where it is known to fail.
%if 0%{?fedora} <= 20
%ifarch aarch64 %{arm}
export SKIP_TEST_EXECSTACK=1
%endif
%endif

make check || {
    cat tests/test-suite.log
    exit 1
}


%files
%doc COPYING README examples/build-basic-vm.sh
%{_bindir}/supermin
%{_mandir}/man1/supermin.1*


%files devel
%{_rpmconfigdir}/fileattrs/supermin.attr
%{_rpmconfigdir}/supermin-find-requires


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jan  9 2025 Jerry James <loganjerry@gmail.com> - 5.3.5-3
- OCaml 5.3.0 rebuild for Fedora 42

* Mon Oct 21 2024 Richard W.M. Jones <rjones@redhat.com> - 5.3.5-2
- Use stable owner, group and mtime in base.tar.gz (RHBZ#2320025)

* Sat Aug 31 2024 Richard W.M. Jones <rjones@redhat.com> - 5.3.5-1
- New upstream version 5.3.5

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 5.3.4-4
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 5.3.4-3
- OCaml 5.2.0 for Fedora 41

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Richard W.M. Jones <rjones@redhat.com> - 5.3.4-1
- New upstream version 5.3.4
- Remove patches which are now all upstream.

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 5.3.3-19
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 5.3.3-18
- OCaml 5.1.1 rebuild for Fedora 40

* Fri Nov 10 2023 Richard W.M. Jones <rjones@redhat.com> - 5.3.3-17
- Fix RISC-V gzip compressed kernels

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 5.3.3-16
- OCaml 5.1 rebuild for Fedora 40

* Wed Aug 02 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 5.3.3-15
- Defer dnf5 until Fedora 41

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 12 2023 Richard W.M. Jones <rjones@redhat.com> - 5.3.3-13
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 5.3.3-10
- OCaml 5.0.0 rebuild

* Mon Jun 12 2023 Richard W.M. Jones <rjones@redhat.com> - 5.3.3-9
- Fix --if-newer

* Mon Jun 05 2023 Richard W.M. Jones <rjones@redhat.com> - 5.3.3-8
- Migrated to SPDX license

* Wed May 31 2023 Richard W.M. Jones <rjones@redhat.com> - 5.3.3-7
- Further fix for dnf5 (RHBZ#2211386)

* Tue May 30 2023 Richard W.M. Jones <rjones@redhat.com> - 5.3.3-6
- Add support for dnf5 (RHBZ#2209412)

* Fri May 19 2023 Richard W.M. Jones <rjones@redhat.com> - 5.3.3-5
- Rebuild against librpm 10

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 5.3.3-4
- Rebuild OCaml packages for F38

* Sat Jan 21 2023 Richard W.M. Jones <rjones@redhat.com> - 5.3.3-3
- Deal with new RPM database location
- https://fedoraproject.org/wiki/Changes/RelocateRPMToUsr

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 18 2022 Richard W.M. Jones <rjones@redhat.com> - 5.3.3-1
- New upstream development version 5.3.3

* Wed Sep 07 2022 Richard W.M. Jones <rjones@redhat.com> - 5.3.2-5
- Include all upstream patches since 5.3.2
- Add debugging and accurate exception backtraces (RHBZ#2124571).

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 5.3.2-3
- OCaml 4.14.0 rebuild

* Sun May 15 2022 Richard W.M. Jones <rjones@redhat.com> - 5.3.2-2
- Move dependency on dnf to -devel subpackage (RHBZ#2086302)

* Fri Mar 04 2022 Richard W.M. Jones <rjones@redhat.com> - 5.3.2-1
- New upstream development version 5.3.2

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 5.3.1-5
- OCaml 4.13.1 rebuild to remove package notes

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 01 2021 Richard W.M. Jones <rjones@redhat.com> - 5.3.1-3
- Further fix to ignore zfcpdump kernel on s390x

* Tue Nov 30 2021 Richard W.M. Jones <rjones@redhat.com> - 5.3.1-2
- Ignore zfcpdump kernel on s390x

* Thu Aug 26 2021 Richard W.M. Jones <rjones@redhat.com> - 5.3.1-1
- New upstream development version 5.3.1.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun  2 2021 Richard W.M. Jones <rjones@redhat.com> - 5.2.1-3
- Add gating tests (for RHEL 9)

* Fri May 07 2021 Richard W.M. Jones <rjones@redhat.com> - 5.2.1-2
- Do not include the package on POWER on RHEL 9
  resolves: rhbz#1956934

* Mon Feb 01 2021 Richard W.M. Jones <rjones@redhat.com> - 5.2.1-1
- New upstream version 5.2.1.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan 14 2021 Richard W.M. Jones <rjones@redhat.com> - 5.2.0-6
- Remove inactive strip override (see RHBZ#1915570).

* Mon Nov 23 2020 Richard W.M. Jones <rjones@redhat.com> - 5.2.0-5
- Disable dietlibc on RHEL 9.

* Fri Aug 07 2020 Troy Dawson <tdawson@redhat.com> - 5.2.0-4
- Use ExclusiveArch: %{kernel_arches}

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 03 2020 Richard W.M. Jones <rjones@redhat.com> - 5.2.0-2
- ppc64le: ibmvscsi driver missing from supermin appliance (RHBZ#1819019).

* Tue Mar 10 2020 Richard W.M. Jones <rjones@redhat.com> - 5.2.0-1
- New upstream stable version 5.2.0.

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.20-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Richard W.M. Jones <rjones@redhat.com> - 5.1.20-11
- Add further patch to fix symlinks (RHBZ#1770304).
- Add all patches since 5.1.20 was released.

* Thu Nov 28 2019 Richard W.M. Jones <rjones@redhat.com> - 5.1.20-10
- Add upstream patch to fix symlinks on recent kernels (RHBZ#1770304).

* Wed Nov 27 2019 Richard W.M. Jones <rjones@redhat.com> - 5.1.20-9
- Use gpgverify macro instead of explicit gpgv2 command.

* Wed Jul 31 2019 Richard W.M. Jones <rjones@redhat.com> - 5.1.20-8
- OCaml 4.08.1 (rc2) rebuild.

* Sat Jul 27 2019 Richard W.M. Jones <rjones@redhat.com> - 5.1.20-7
- Disable package on i686 because no kernel.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.20-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jun 10 22:13:23 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.1.20-5
- Rebuild for RPM 4.15

* Mon Jun 10 15:42:06 CET 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 5.1.20-4
- Rebuild for RPM 4.15

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.20-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Richard W.M. Jones <rjones@redhat.com> - 5.1.20-2
- Add upstream patches to diagnose possible F29 issue.

* Thu Jan 17 2019 Richard W.M. Jones <rjones@redhat.com> - 5.1.20-1
- New upstream version 5.1.20.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.19-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Feb 24 2018 Florian Weimer <fweimer@redhat.com> - 5.1.19-4
- Reenable hardened build

* Tue Feb 13 2018 Richard W.M. Jones <rjones@redhat.com> - 5.1.19-3
- Fix bytes/string problems.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Sep 19 2017 Richard W.M. Jones <rjones@redhat.com> - 5.1.19-1
- New upstream version 5.1.19.
- Remove all patches, now upstream.

* Thu Aug 10 2017 Igor Gnatenko <ignatenko@redhat.com> - 5.1.18-5
- Rebuilt for RPM soname bump

* Thu Aug 03 2017 Richard W.M. Jones <rjones@redhat.com> - 5.1.18-4
- Fix supermin crash with truncated vmlinuz file (RHBZ#1477758).
- Include all upstream patches since 5.1.18.

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Richard W.M. Jones <rjones@redhat.com> - 5.1.18-1
- New upstream release 5.1.18.
- Fixes problem with creating incorrect symlinks (RHBZ#1470157).

* Sat Mar 18 2017 Richard W.M. Jones <rjones@redhat.com> - 5.1.17-5
- Enable dietlibc on aarch64 and POWER.

* Fri Mar 17 2017 Richard W.M. Jones <rjones@redhat.com> - 5.1.17-4
- Drop dependency on hawkey and versioned dependencies on dnf.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Nov 05 2016 Richard W.M. Jones <rjones@redhat.com> - 5.1.17-2
- Rebuild for OCaml 4.04.0.

* Tue Nov 01 2016 Richard W.M. Jones <rjones@redhat.com> - 5.1.17-1
- New upstream release 5.1.17.
- Check signature on the tarball before unpacking it.
- Remove patches, all upstream.

* Thu Sep 15 2016 Dan Horák <dan[at]danny.cz> - 5.1.16-6
- Switch to dietlibc on s390x

* Thu Sep 15 2016 Dan Horák <dan[at]danny.cz> - 5.1.16-5
- Do not break the binary on interpreted builds (#1375213)

* Wed Jul 06 2016 Richard W.M. Jones <rjones@redhat.com> - 5.1.16-4
- Add all upstream patches since 5.1.16 was released.

* Tue May 17 2016 Richard W.M. Jones <rjones@redhat.com> - 5.1.16-3
- Add upstream patch for DAX / vNVDIMM support.

* Wed Apr 27 2016 Richard W.M. Jones <rjones@redhat.com> - 5.1.16-2
- New upstream version 5.1.16.
- Drop all patches since they are upstream.
- Depend on systemd-udev to work around RHBZ#1331012.

* Fri Mar 18 2016 Richard W.M. Jones <rjones@redhat.com> - 5.1.15-2
- Add all upstream patches since 5.1.15 was released.
- These should improve boot performance and initrd size.

* Wed Feb 17 2016 Richard W.M. Jones <rjones@redhat.com> - 5.1.15-1
- New upstream version 5.1.15.
- Remove all patches, since they are now included in this version.
- Enable dietlibc, remove glibc-static, xz-static, zlib-static.

* Wed Feb 17 2016 Richard W.M. Jones <rjones@redhat.com> - 5.1.14-4
- Add more patches since 5.1.14.

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.14-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 12 2016 Richard W.M. Jones <rjones@redhat.com> - 5.1.14-2
- Add all patches since 5.1.14.

* Mon Jan 11 2016 Richard W.M. Jones <rjones@redhat.com> - 5.1.14-1
- New upstream version 5.1.14.
- Remove all patches - now upstream.

* Tue Oct 13 2015 Richard W.M. Jones <rjones@redhat.com> - 5.1.13-4
- Pull in all upstream patches since 5.1.13.
- Choose providers better (RHBZ#1266918).
- Use autopatch.
- Explicitly depend on pod2html.

* Mon Jul 27 2015 Richard W.M. Jones <rjones@redhat.com> - 5.1.13-3
- Bump version to rebuild against new RPM in Rawhide.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 26 2015 Richard W.M. Jones <rjones@redhat.com> - 5.1.13-1
- New upstream version 5.1.13.
- Remove patch, now upstream.

* Thu May 21 2015 Richard W.M. Jones <rjones@redhat.com> - 5.1.12-11
- Prefer 'dnf download' over 'yumdownloader' (again).
- BR grubby for the tests to work.

* Fri Apr 10 2015 Richard W.M. Jones <rjones@redhat.com> - 5.1.12-9
- Revert back to yumdownloader (RHBZ#1186948).

* Fri Apr  3 2015 Richard W.M. Jones <rjones@redhat.com> - 5.1.12-8
- Prefer 'dnf download' over 'yumdownloader'.

* Fri Mar 20 2015 Richard W.M. Jones <rjones@redhat.com> - 5.1.12-7
- Disable hardened build again.  See RHBZ#1202091 RHBZ#1204162.

* Mon Mar 16 2015 Richard W.M. Jones <rjones@redhat.com> - 5.1.12-6
- Enable hardening flags by building the static 'init' specially
  before the main build.
- Use _smp_mflags.

* Thu Mar 12 2015 Richard W.M. Jones <rjones@redhat.com> - 5.1.12-4
- Add a -devel subpackage containing automated RPM dependency generator
  for supermin appliances.

* Mon Mar  9 2015 Richard W.M. Jones <rjones@redhat.com> - 5.1.12-2
- Disable hardened build as it breaks building the static 'init' binary.

* Sat Mar  7 2015 Richard W.M. Jones <rjones@redhat.com> - 5.1.12-1
- New upstream version 5.1.12.
- Includes ARM fix: lpae kernels can now be booted (RHBZ#1199733).

* Thu Jan  8 2015 Pino Toscano <ptoscano@redhat.com> - 5.1.11-2
- Rebuild for xz-5.2.0 in Rawhide (RHBZ#1179252).

* Sat Oct 25 2014 Richard W.M. Jones <rjones@redhat.com> - 5.1.11-1
- New upstream version 5.1.11.

* Tue Oct  7 2014 Pino Toscano <ptoscano@redhat.com> - 5.1.10-2
- Update to upstream commit d78c898c7e2bc5f12cbebef98b95a7908d9120f1.
- BR rpm-devel, since it is now used instead of invoking rpm.
- BR automake and autoconf, and run autoreconf (configure.ac is modified by
  the patches).

* Thu Sep  4 2014 Richard W.M. Jones <rjones@redhat.com> - 5.1.10-1
- New upstream version 5.1.10.
- Remove patch which is now included upstream.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Aug  3 2014 Richard W.M. Jones <rjones@redhat.com> - 5.1.9-2
- Add upstream patch to avoid endless loop in Rawhide.

* Mon Jul 21 2014 Richard W.M. Jones <rjones@redhat.com> - 5.1.9-1
- New upstream version 5.1.9.
- Remove patches which are now upstream.

* Wed Jun 25 2014 Richard W.M. Jones <rjones@redhat.com> - 5.1.8-9
- Add Requires findutils (RHBZ#1113029).

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 21 2014 Richard W.M. Jones <rjones@redhat.com> - 5.1.8-7
- Add patch to fix RPM handler when filenames may contain spaces.

* Mon May 19 2014 Richard W.M. Jones <rjones@redhat.com> - 5.1.8-4
- Skip execstack test on Fedora 20 (ARM only).

* Fri May 16 2014 Richard W.M. Jones <rjones@redhat.com> - 5.1.8-3
- BR xz-static & xz-devel packages, to support xz-compressed kernel modules.

* Fri May  9 2014 Richard W.M. Jones <rjones@redhat.com> - 5.1.8-1
- New upstream version 5.1.8.
- Remove patches which are now upstream.

* Thu May  1 2014 Richard W.M. Jones <rjones@redhat.com> - 5.1.7-3
- Add upstream patch which removes need to run execstack (RHBZ#1093261).

* Mon Apr  7 2014 Richard W.M. Jones <rjones@redhat.com> - 5.1.7-2
- Add patch to fix quoting around mke2fs parameter (RHBZ#1084960).

* Sun Apr  6 2014 Richard W.M. Jones <rjones@redhat.com> - 5.1.7-1
- New upstream version 5.1.7.
- Remove ppc64p7 patch which is now upstream.

* Thu Apr  3 2014 Richard W.M. Jones <rjones@redhat.com> - 5.1.6-5
- Requires tar, which is not installed in an @Core installation.

* Fri Mar 28 2014 Richard W.M. Jones <rjones@redhat.com> - 5.1.6-4
- Add upstream patch to fix supermin on ppc64p7.

* Thu Mar 27 2014 Richard W.M. Jones <rjones@redhat.com> - 5.1.6-3
- New upstream version 5.1.6.
- Fix tests.

* Mon Mar 24 2014 Richard W.M. Jones <rjones@redhat.com> - 5.1.5-2
- Disable execstack on aarch64.
  It comes from prelink which does not exist on aarch64.

* Thu Mar 13 2014 Richard W.M. Jones <rjones@redhat.com> - 5.1.5-1
- New upstream version 5.1.5.

* Thu Mar  6 2014 Richard W.M. Jones <rjones@redhat.com> - 5.1.3-1
- New upstream version 5.1.3.

* Sun Mar  2 2014 Richard W.M. Jones <rjones@redhat.com> - 5.1.2-1
- New upstream version 5.1.2.
- Fixes a serious bug in --build mode.

* Sat Mar  1 2014 Richard W.M. Jones <rjones@redhat.com> - 5.1.1-1
- New upstream version 5.1.1.
- Remove patch which is now upstream.

* Wed Feb 26 2014 Richard W.M. Jones <rjones@redhat.com> - 5.1.0-3
- Add BR yum-utils (for yumdownloader).
- Add upstream patch which stops duplicate packages appearing.

* Wed Feb 26 2014 Richard W.M. Jones <rjones@redhat.com> - 5.1.0-2
- New upstream version 5.1.0.
- Note this is effectively a rewrite, and is not completely compatible.
- There is no separate 'supermin-helper' subpackage any more.
- Requires rpm instead of yum.

* Mon Dec 23 2013 Richard W.M. Jones <rjones@redhat.com> - 4.1.6-2
- New upstream version 4.1.6.
- Should fix all autotools brokenness.
- Man pages are now all in section 1.
- Remove patch which is now upstream.
- +BR /usr/bin/execstack (from prelink).

* Mon Dec 23 2013 Richard W.M. Jones <rjones@redhat.com> - 4.1.5-5
- Rerun autoreconf to fix autotools brokenness.

* Sun Dec 22 2013 Richard W.M. Jones <rjones@redhat.com> - 4.1.5-4
- Why was prelink required?  Remove it.

* Fri Sep 13 2013 Michael Schwendt <mschwendt@fedoraproject.org> - 4.1.5-3
- correct Obsoletes version for febootstrap and febootstrap-supermin-helper

* Sun Sep  8 2013 Richard W.M. Jones <rjones@redhat.com> - 4.1.5-2
- (For ARM) Don't crash if SUPERMIN_DTB is set and --dtb not specified.

* Fri Sep  6 2013 Richard W.M. Jones <rjones@redhat.com> - 4.1.5-1
- New upstream version 4.1.5.
- Has (optionally) a new command line syntax.
- Supports device trees for ARM.

* Wed Aug 28 2013 Richard W.M. Jones <rjones@redhat.com> - 4.1.4-1
- New upstream version 4.1.4.
- Supports compressed cpio image files, experimentally.

* Fri Aug  9 2013 Richard W.M. Jones <rjones@redhat.com> - 4.1.3-1
- New upstream version 4.1.3.
- Remove patch which is now upstream.
- Add examples directory to documentation.

* Tue Aug  6 2013 Richard W.M. Jones <rjones@redhat.com> - 4.1.2-2
- Include upstream patch to get correct directory setgid/sticky bits in
  the appliance.

* Sat Aug  3 2013 Richard W.M. Jones <rjones@redhat.com> - 4.1.2-1
- New upstream version 4.1.2.
- Remove patch which is now upstream.

* Wed Jun 26 2013 Richard W.M. Jones <rjones@redhat.com> - 4.1.1-2
- Add upstream patch to ignore ghost non-regular files.
- This fixes builds on Fedora 20 because the filesystem package has
  been changed so /var/lock and /var/run are marked as ghost.

* Tue Feb  5 2013 Richard W.M. Jones <rjones@redhat.com> - 4.1.1-1
- New upstream version 4.1.1.
- The program has been renamed 'supermin' from 'febootstrap'.
- Obsolete, but don't Provide because supermin is not a compatible replacement.
- Use '_isa' to specify architecture of supermin-helper subpackage.

* Tue Jan 22 2013 Richard W.M. Jones <rjones@redhat.com> - 1:3.21-2
- Add upstream patch to drop supplemental groups (RHBZ#902476).
- Remove 'Group:' RPM headers which are no longer necessary.
- Remove some commented-out requirements.

* Sat Dec 22 2012 Richard W.M. Jones <rjones@redhat.com> - 1:3.21-1
- New upstream version 3.21.

* Fri Aug 31 2012 Richard W.M. Jones <rjones@redhat.com> - 1:3.20-1
- New upstream version 3.20.

* Wed Aug 22 2012 Richard W.M. Jones <rjones@redhat.com> - 1:3.19-2
- Work around brokenness in yum (RHBZ#850913).
- Remove defattr, no longer required.

* Tue Jul 31 2012 Richard W.M. Jones <rjones@redhat.com> - 1:3.19-1
- New upstream version 3.19.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.18-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 18 2012 Richard Jones <rjones@redhat.com> - 3.18-1
- New upstream version 3.18.
- This adds support for EPEL 5.

* Thu Jun 14 2012 Richard Jones <rjones@redhat.com> - 3.17-1
- New upstream version 3.17.

* Wed Jun 13 2012 Richard Jones <rjones@redhat.com> - 3.16-1
- New upstream version 3.16.

* Tue Jun 12 2012 Richard Jones <rjones@redhat.com> - 3.15-1
- New upstream version 3.15.
- This version includes root=<device> support, needed for libguestfs
  with virtio-scsi.
- Remove upstream patch.

* Thu May 17 2012 Richard Jones <rjones@redhat.com> - 3.14-6
- For RHEL 7 only, add ExclusiveArch x86-64.

* Tue May 15 2012 Richard Jones <rjones@redhat.com> - 3.14-5
- Bundled gnulib (RHBZ#821752).

* Fri Apr 13 2012 Richard Jones <rjones@redhat.com> - 3.14-4
- Add back explicit dependencies for external programs.

* Fri Apr 13 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 3.14-3
- Drop ExclusiveArch as it's supported on all primary & secondary arches
- Cleanup spec and deps

* Fri Mar 30 2012 Richard Jones <rjones@redhat.com> - 3.14-2
- New upstream version 3.14.
- Add upstream patch to fix RHBZ#808421.

* Thu Mar 29 2012 Richard Jones <rjones@redhat.com> - 3.13-4
- e2fsprogs moved /sbin/mke2fs to /usr/sbin (thanks Eric Sandeen).

* Thu Mar  1 2012 Richard Jones <rjones@redhat.com> - 3.13-2
- Missing BR zlib-static.

* Thu Feb  9 2012 Richard Jones <rjones@redhat.com> - 3.13-1
- New upstream version 3.13.
- Remove upstream patch which is included in this version.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jan  3 2012 Richard Jones <rjones@redhat.com> - 3.12-4
- Depend on latest e2fsprogs (RHBZ#771310).

* Wed Nov  9 2011 Richard Jones <rjones@redhat.com> - 3.12-2
- Include upstream patch to work around Python stupidity.

* Tue Oct 18 2011 Richard Jones <rjones@redhat.com> - 3.12-1
- New upstream version 3.12.
- Remove upstream patch which is included in this version.

* Fri Oct 14 2011 Richard Jones <rjones@redhat.com> - 3.11-2
- Add upstream patch to fix febootstrap on non-Debian.

* Fri Oct 14 2011 Richard Jones <rjones@redhat.com> - 3.11-1
- New upstream version 3.11.

* Thu Sep  1 2011 Richard Jones <rjones@redhat.com> - 3.10-1
- New upstream version 3.10.

* Fri Aug 26 2011 Richard Jones <rjones@redhat.com> - 3.9-1
- New upstream version 3.9.

* Tue Jul 26 2011 Richard Jones <rjones@redhat.com> - 3.8-1
- New upstream version 3.8.

* Fri Jul 15 2011 Richard Jones <rjones@redhat.com> - 3.7-1
- New upstream version 3.7.

* Wed Jun  1 2011 Richard Jones <rjones@redhat.com> - 3.6-1
- New upstream version 3.6.
- This version no longer needs external insmod.static.

* Fri May 27 2011 Richard Jones <rjones@redhat.com> - 3.5-1
- New upstream version 3.5.
- Remove patch which is now upstream.

* Fri Mar 18 2011 Richard Jones <rjones@redhat.com> - 3.4-2
- Don't fail if objects are created in a symlinked dir (RHBZ#698089).

* Fri Mar 18 2011 Richard Jones <rjones@redhat.com> - 3.4-1
- New upstream version 3.4.
- febootstrap-supermin-helper Obsoletes older versions of febootstrap.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 14 2011 Richard Jones <rjones@redhat.com> - 3.3-4
- Split package into febootstrap (for building) and febootstrap-supermin-helper
  (for running).  Note that febootstrap depends on febootstrap-supermin-helper,
  but you can install febootstrap-supermin-helper on its own.

* Fri Jan 14 2011 Richard Jones <rjones@redhat.com> - 3.3-3
- Clear executable stack flag on febootstrap-supermin-helper.

* Thu Jan 13 2011 Dan Horák <dan[at]danny.cz> - 3.3-2
- add the ocaml's ExclusiveArch

* Sat Dec 11 2010 Richard Jones <rjones@redhat.com> - 3.3-1
- New upstream version 3.3.

* Tue Dec  7 2010 Richard Jones <rjones@redhat.com> - 3.2-1
- New upstream version 3.2.
- Remove upstream patches.

* Tue Dec  7 2010 Richard Jones <rjones@redhat.com> - 3.1-5
- Previous fix for RHBZ#654638 didn't work, fix it correctly.

* Mon Dec  6 2010 Richard Jones <rjones@redhat.com> - 3.1-4
- Properly ignore .*.hmac files (accidental reopening of RHBZ#654638).

* Mon Dec  6 2010 Richard Jones <rjones@redhat.com> - 3.1-3
- Uses yumdownloader at runtime, so require yum-utils.

* Mon Dec  6 2010 Richard Jones <rjones@redhat.com> - 3.1-2
- New upstream version 3.1.
- BR insmod.static.

* Sun Dec  5 2010 Richard Jones <rjones@redhat.com> - 3.0-2
- New upstream version 3.0 (note this is incompatible with 2.x).
- Fix upstream URLs.
- fakeroot, fakechroot no longer required.
- insmod.static is required at runtime (missing dependency from earlier).
- The only programs are 'febootstrap' and 'febootstrap-supermin-helper'.
- BR ocaml, ocaml-findlib-devel.
- No examples are provided with this version of febootstrap.

* Thu Nov 25 2010 Richard Jones <rjones@redhat.com> - 2.11-1
- New upstream version 2.11.
- Fixes "ext2fs_mkdir .. No free space in directory" bug which affects
  libguestfs on rawhide.

* Thu Oct 28 2010 Richard Jones <rjones@redhat.com> - 2.10-1
- New upstream version 2.10.
- Adds -u and -g options to febootstrap-supermin-helper which are
  required by virt-v2v.

* Fri Aug 27 2010 Richard Jones <rjones@redhat.com> - 2.9-1
- New upstream version 2.9.
- Fixes directory ordering problem in febootstrap-supermin-helper.

* Tue Aug 24 2010 Richard Jones <rjones@redhat.com> - 2.8-1
- New upstream version 2.8.

* Sat Aug 21 2010 Richard Jones <rjones@redhat.com> - 2.8-0.2
- New pre-release version of 2.8.
  + Note this is based on 2.7 + mailing list patches.
- New BRs on mke2fs, libext2fs, glibc-static.

* Fri May 14 2010 Richard Jones <rjones@redhat.com> - 2.7-2
- New upstream version 2.7.
- febootstrap-supermin-helper shell script rewritten in C for speed.
- This package contains C code so it is no longer 'noarch'.
- MAKEDEV isn't required.

* Fri Jan 22 2010 Richard Jones <rjones@redhat.com> - 2.6-1
- New upstream release 2.6.
- Recheck package in rpmlint.

* Thu Oct 22 2009 Richard Jones <rjones@redhat.com> - 2.5-2
- New upstream release 2.5.
- Remove BR upx (not needed by upstream).
- Two more scripts / manpages.

* Thu Jul 30 2009 Richard Jones <rjones@redhat.com> - 2.4-1
- New upstream release 2.4.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 15 2009 Richard Jones <rjones@redhat.com> - 2.3-1
- New upstream release 2.3.

* Mon Jun 15 2009 Richard Jones <rjones@redhat.com> - 2.2-1
- New upstream release 2.2.

* Mon May 11 2009 Richard Jones <rjones@redhat.com> - 2.0-1
- New upstream release 2.0.

* Thu May  7 2009 Richard Jones <rjones@redhat.com> - 1.9-1
- New upstream release 1.9.

* Fri May  1 2009 Richard Jones <rjones@redhat.com> - 1.8-1
- New upstream release 1.8.

* Mon Apr 20 2009 Richard Jones <rjones@redhat.com> - 1.7-1
- New upstream release 1.7.

* Tue Apr 14 2009 Richard Jones <rjones@redhat.com> - 1.5-3
- Configure script has (unnecessary) BuildRequires on fakeroot,
  fakechroot, yum.

* Tue Apr 14 2009 Richard Jones <rjones@redhat.com> - 1.5-2
- Initial build for Fedora.
