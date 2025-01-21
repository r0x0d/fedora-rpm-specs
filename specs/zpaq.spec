# JIT is supported on x86 and x86_64 only, bug #1309772
%ifarch %{ix86} x86_64
%bcond_without jit
%else
%bcond_with jit
%endif

Name:           zpaq
Version:        7.15
Release:        23%{?dist}
Summary:        Incremental journaling back-up archiver
# COPYING:      Unlicense text AND MIT text
# Parts of libzpaq.cpp: LicenseRef-Fedora-Public-Domain
#               <https://gitlab.com/fedora/legal/fedora-license-data/-/issues/306>
## In zpaq-libs package
# libzpaq.cpp:  Unlicense AND MIT AND LicenseRef-Fedora-Public-Domain
License:        Unlicense AND LicenseRef-Fedora-Public-Domain
URL:            http://mattmahoney.net/dc/%{name}.html
Source0:        http://mattmahoney.net/dc/%{name}%(echo %{version}|tr -d .).zip
# Do not bundle zpaq library into zpaq tool, upstream does not want it
# <http://encode.ru/threads/456-zpaq-updates?s=8510051f0caeb4c019c6d0af1dd6f585&p=47379&viewfull=1#post47379>
Patch0:         zpaq-7.15-Build-a-shared-library.patch
BuildRequires:  coreutils
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-podlators
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
This is a journaling archiver optimized for user-level incremental backup of
directory trees. It supports AES-256 encryption, 5 multi-threaded compression
levels, and content-aware file fragment level deduplication. For backups it
adds only files whose date has changed, and keeps both old and new versions.
You can roll back the archive date to restore from old versions of the
archive. The default compression level is faster than zip usually with better
compression. zpaq uses a self-describing compressed format to allow for future
improvements without breaking compatibility with older versions of the
program.

%package        libs
Summary:        Library for ZPAQ compression and decompression
License:        Unlicense AND MIT AND LicenseRef-Fedora-Public-Domain
# libdivsufsort-lite-2.00 is bundled to libzpaq.cpp from
# <https://libdivsufsort.googlecode.com/files/libdivsufsort-lite.zip> that
# is simplified version of
# <http://libdivsufsort.googlecode.com/files/libdivsufsort-2.0.0.tar.bz2>.
# New libdivsufsort upstream is <https://github.com/y-256/libdivsufsort>.
Provides:       bundled(libdivsufsort-lite) = 2.00

%description    libs
This is a library for ZPAQ compression a decompression.

%package        devel
Summary:        Development files for ZPAQ library
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       gcc-c++%{?_isa}

%description    devel
These are header files for developing applications that support ZPAQ
compression.

%prep
%autosetup -p1 -c -n %{name}-%{version}
# Normalize EOLs
for F in readme.txt; do
    tr -d "\r" < "${F}" > "${F}.new"
    touch -r "$F" "${F}.new"
    mv "${F}.new" "$F"
done

%build
# -Wl,--as-needed to not require unused libm, bug #1310128
%{make_build} \
    CXXFLAGS='%{optflags}' \
    LDFLAGS='%{?__global_ldflags} -Wl,--as-needed' \
    CPPFLAGS="${CPPFLAGS} -Dunix %{!?with_jit: -DNOJIT}"

%check
make check %{?_smp_mflags}

%install
%{make_install} PREFIX=%{_prefix} LIBDIR=%{_libdir}

%ldconfig_scriptlets libs

%files
%doc readme.txt
%{_bindir}/zpaq
%{_mandir}/man1/zpaq.1*

%files libs
%license COPYING
%{_libdir}/libzpaq.so.0.1

%files devel
%{_includedir}/libzpaq.h
%{_libdir}/libzpaq.so

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 7.15-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.15-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 7.15-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 30 2023 Petr Pisar <ppisar@redhat.com> - 7.15-20
- zpaq to require an exact release of zpaq-libs

* Fri Aug 25 2023 Petr Pisar <ppisar@redhat.com> - 7.15-19
- Convert a license tag to SPDX

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.15-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.15-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.15-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.15-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.15-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.15-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.15-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.15-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.15-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.15-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.15-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 23 2018 Petr Pisar <ppisar@redhat.com> - 7.15-7
- Modernize a spec file

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 7.15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 21 2016 Petr Pisar <ppisar@redhat.com> - 7.15-1
- 7.15 bump

* Thu Apr 14 2016 Petr Pisar <ppisar@redhat.com> - 7.11-1
- 7.11 bump

* Tue Apr 12 2016 Petr Pisar <ppisar@redhat.com> - 7.10-1
- 7.10 bump
- License changed from (MIT and Public Domain) to (Unlicense and MIT and
  Public Domain)

* Fri Feb 19 2016 Petr Pisar <ppisar@redhat.com> - 7.05-1
- 7.05 version packaged
