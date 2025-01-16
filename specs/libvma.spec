%{!?configure_options: %global configure_options %{nil}}

Name: libvma
Version: 9.8.60
Release: 2%{?dist}
Summary: A library for boosting TCP and UDP traffic (over RDMA hardware)

# Automatically converted from old format: GPLv2 or BSD - review is highly recommended.
License: GPL-2.0-only OR LicenseRef-Callaway-BSD
Url: https://github.com/Mellanox/libvma
Source0: https://github.com/Mellanox/libvma/archive/%{version}/%{name}-%{version}.tar.gz
# https://github.com/Mellanox/libvma/pull/1076
Patch0: 0001-Fix-gcc14-compilation-issue.patch
Patch1: 0002-kernel-6-10-netlink-issue.patch
Patch2: 0003-fix-memory-leak-and-style.patch

# libvma currently supports only the following architectures
ExclusiveArch: x86_64 ppc64le ppc64 aarch64

BuildRequires: pkgconfig
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: gcc-c++
BuildRequires: rdma-core-devel
BuildRequires: systemd-rpm-macros
BuildRequires: pkgconfig(libnl-3.0)
BuildRequires: pkgconfig(libnl-route-3.0)
BuildRequires: make

%description
libvma is a LD_PRELOAD-able library that boosts performance of TCP and
UDP traffic. It allows application written over standard socket API to
handle fast path data traffic from user space over Ethernet and/or
Infiniband with full network stack bypass and get better throughput,
latency and packets/sec rate.

No application binary change is required for that.
libvma is supported by RDMA capable devices that support "verbs"
IBV_QPT_RAW_PACKET QP for Ethernet and/or IBV_QPT_UD QP for IPoIB.

%package devel
Summary: Header files required to develop with libvma
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package includes headers for building programs with libvma's
interfaces.

%package utils
Summary: Utilities used with libvma
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
This package contains the tool for collecting and analyzing libvma statistic.

%prep
%setup -q
%autosetup -p1

%build
export revision=1
if [ ! -e configure ] && [ -e autogen.sh ]; then
    PRJ_RELEASE=1 ./autogen.sh
fi

%configure %{?configure_options}
%{make_build}

%install
%{make_install}

find $RPM_BUILD_ROOT%{_libdir} -name '*.la' -delete
install -D -m 644 contrib/scripts/vma.service $RPM_BUILD_ROOT/%{_prefix}/lib/systemd/system/vma.service
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/init.d/vma

%post
%systemd_post vma.service

%preun
%systemd_preun vma.service

%postun
%systemd_postun_with_restart vma.service

%files
%{_libdir}/%{name}.so*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/README
%doc %{_pkgdocdir}/CHANGES
%config(noreplace) %{_sysconfdir}/libvma.conf
%{_sbindir}/vmad
%{_prefix}/lib/systemd/system/vma.service
%license LICENSE
%{_mandir}/man7/vma.*
%{_mandir}/man8/vmad.*

%files devel
%dir %{_includedir}/mellanox
%{_includedir}/mellanox/vma_extra.h

%files utils
%{_bindir}/vma_stats
%{_mandir}/man8/vma_stats.*

%changelog
* Tue Jan 14 2025 Igor Ivanov <igori@nvidia.com> 9.8.60-2
- Fix memory leak and style issues

* Sat Jan 11 2025 Honggang Li <honggangli@163.com> - 9.8.60-1
- Bump version to 9.8.60
- VMA support for kernel 6.10

* Mon Sep  2 2024 Miroslav Suchý <msuchy@redhat.com> - 9.8.40-5
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.8.40-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.8.40-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 9.8.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Oct 27 2023 Igor Ivanov <igori@nvidia.com> 9.8.40-1
- Bump version to 9.8.40

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Igor Ivanov <igori@nvidia.com> 9.8.1-2
- Fix gcc13 compilation issue

* Mon Feb 20 2023 Igor Ivanov <igori@nvidia.com> 9.8.1-1
- Bump version to 9.8.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 9.6.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Jul 26 2022 Igor Ivanov <igori@nvidia.com> 9.6.4-1
- Bump version to 9.6.4

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Apr 29 2022 Igor Ivanov <igori@nvidia.com> 9.5.3-1
- Bump version to 9.5.3

* Thu Apr  7 2022 Igor Ivanov <igori@nvidia.com> 9.5.2-1
- Bump version to 9.5.2

* Mon Jan 31 2022 Fedora Release Engineering <igori@nvidia.com> - 9.4.0-3
- Fix gcc12 compilation issue

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 9.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 09 2021 Honggang Li <honli@redhat.com> - 9.4.0-1
- Bump version to 9.4.0

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Igor Ivanov <igori@nvidia.com> 9.3.1-1
- Bump version to 9.3.1

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 9.2.2-3
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 9.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 16 2020 Igor Ivanov <igor.ivanov.va@gmail.com> 9.2.2-1
- Bump version to 9.2.2
- Fix issues for gcc-11

* Thu Dec 10 2020 Jeff Law <law@redhat.com> 9.1.1-2
- Don't use "register" in C++17.  Still FTBFS though.

* Sun Nov 15 2020 Igor Ivanov <igor.ivanov.va@gmail.com> 9.1.1-1
- Bump version to 9.1.1

* Fri Apr 17 2020 Igor Ivanov <igor.ivanov.va@gmail.com> 9.0.2-1
- Align with Fedora guidelines
- Bump version to 9.0.2

* Thu Feb 7 2019 Igor Ivanov <igor.ivanov.va@gmail.com> 8.8.2-1
- Improve package update processing

* Tue Dec 19 2017 Igor Ivanov <igor.ivanov.va@gmail.com> 8.5.1-1
- Add systemd support

* Tue May 9 2017 Ophir Munk <ophirmu@mellanox.com> 8.3.4-1
- Add libvma-debug.so installation

* Mon Nov 28 2016 Igor Ivanov <igor.ivanov.va@gmail.com> 8.2.2-1
- Add daemon

* Mon Jan  4 2016 Avner BenHanoch <avnerb@mellanox.com> 7.0.12-1
- Initial Packaging
