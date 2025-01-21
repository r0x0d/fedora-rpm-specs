%bcond_without check
%define _warning_options -Wall -Werror=format-security -Wno-deprecated-declarations -Wno-maybe-uninitialized

Name:          sbsigntools
Version:       0.9.5
Release:       8%{?dist}
Summary:       Signing utility for UEFI secure boot
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:       GPL-3.0-or-later
URL:           https://build.opensuse.org/package/show/home:jejb1:UEFI/sbsigntools
# upstream tarballs don't include bundled ccan
# run sbsigntools-mktarball.sh
Source0:       %{name}-%{version}.tar.xz
Source1:       %{name}-mktarball.sh
# don't fetch ccan or run git from autogen.sh, already done by mktarball.sh
Patch0:        %{name}-no-git.patch
# add Fedora gnu-efi path and link statically against libefi.a/libgnuefi.a
Patch1:        %{name}-gnuefi.patch
# fix wchar_t (a.k.a. CHAR16) abuse
Patch2:        %{name}-no-wchar_t.patch
# same as gnu-efi
ExclusiveArch: x86_64 aarch64 %{arm} %{ix86}
BuildRequires: make
BuildRequires: automake
BuildRequires: binutils-devel
BuildRequires: gcc
BuildRequires: gnu-efi-devel >= 1:3.0.18-1
BuildRequires: help2man
BuildRequires: libuuid-devel
%if %{with check}
BuildRequires: openssl
%endif
BuildRequires: openssl-devel
%if 0%{?fedora} >= 41
# https://fedoraproject.org/wiki/Changes/OpensslDeprecateEngine
BuildRequires: openssl-devel-engine
%endif
Provides: bundled(ccan-array_size)
Provides: bundled(ccan-build_assert)
Provides: bundled(ccan-check_type)
Provides: bundled(ccan-compiler)
Provides: bundled(ccan-container_of)
Provides: bundled(ccan-endian)
Provides: bundled(ccan-failtest)
Provides: bundled(ccan-hash)
Provides: bundled(ccan-htable)
Provides: bundled(ccan-list)
Provides: bundled(ccan-read_write_all)
Provides: bundled(ccan-str)
Provides: bundled(ccan-talloc)
Provides: bundled(ccan-tcon)
Provides: bundled(ccan-time)
Provides: bundled(ccan-tlist)
Provides: bundled(ccan-typesafe_cb)

%description
Tools to add signatures to EFI binaries and Drivers.

%prep
%autosetup -p1

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%if %{with check}
%check
make check
%endif

%files
%license COPYING LICENSE.GPLv3 lib/ccan/licenses/*
%doc AUTHORS ChangeLog
%{_bindir}/sbattach
%{_bindir}/sbkeysync
%{_bindir}/sbsiglist
%{_bindir}/sbsign
%{_bindir}/sbvarsign
%{_bindir}/sbverify
%{_mandir}/man1/sbattach.1.*
%{_mandir}/man1/sbkeysync.1.*
%{_mandir}/man1/sbsiglist.1.*
%{_mandir}/man1/sbsign.1.*
%{_mandir}/man1/sbvarsign.1.*
%{_mandir}/man1/sbverify.1.*

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 18 2024 Dominik Mierzejewski <dominik@greysector.net> - 0.9.5-7
- fix wchar_t usage in sbvarsign (fixes rhbz#2310759)

* Wed Aug 21 2024 Michel Lind <salimma@fedoraproject.org> - 0.9.5-6
- Fix building with gnu-efi 3.0.18
- Fix building on Fedora 41+ due to OpenSSL engine deprecation
- Fix building on aarch64, need to use non-TEST_BINARY_FORMAT codepath like x86_64
- FIxes: RHBZ#2301267

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 0.9.5-5
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri May 05 2023 Dominik Mierzejewski <dominik@greysector.net> - 0.9.5-1
- update to 0.9.5 (#2179697)
- drop obsolete patches

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jan 17 2023 Dominik Mierzejewski <dominik@greysector.net> - 0.9.4-10
- fix build with GCC 13

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 19 2021 Dominik Mierzejewski <dominik@greysector.net> - 0.9.4-7
- fix build with OpenSSL 3.0.0 (fixes rhbz#2021909)

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 0.9.4-6
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Dominik Mierzejewski <dominik@greysector.net> - 0.9.4-4
- don't ignore errors from sbkeysync (fixes rhbz#1955828)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 03 2020 Dominik Mierzejewski <dominik@greysector.net> - 0.9.4-1
- update to 0.9.4 (#1846578)

* Mon Feb 03 2020 Dominik Mierzejewski <dominik@greysector.net> - 0.9.3-1
- update to 0.9.3
- update bundled CCAN components list
- support building with gnu-efi 3.0.11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 28 2019 Dominik Mierzejewski <dominik@greysector.net> - 0.9.2-1
- update to 0.9.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Jul 25 2018 Dominik Mierzejewski <dominik@greysector.net> - 0.9.1-3
- fix paths to gnu-efi (work around #1608293)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 22 2018 Dominik Mierzejewski <dominik@greysector.net> - 0.9.1-1
- update to 0.9.1
- add Fedora gnu-efi libs location to search path
- link tests statically against gnu-efi libs, there are no shared versions

* Mon Sep  4 2017 Dominik Mierzejewski <dominik@greysector.net> - 0.8-1
- initial build
