%global __remake_config 0

# FTBFS on i686 with GCC 14 -Werror=incompatible-pointer-types
# https://github.com/ofiwg/libfabric/issues/9763
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10
%ifarch %{ix86}
%global build_type_safety_c 2
%endif
%endif

Name:           libfabric
Version:        1.22.0
Release:        2%{?dist}
Summary:        Open Fabric Interfaces

License:        BSD-2-Clause OR GPL-2.0-only
URL:            https://github.com/ofiwg/libfabric
Source0:        https://github.com/ofiwg/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.bz2

%if %{__remake_config}
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
%endif
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libnl3-devel
# RDMA not available on 32-bit ARM: #1484155
%ifnarch %{arm}
BuildRequires:  libibverbs-devel
BuildRequires:  librdmacm-devel
%endif
%ifarch x86_64
%if 0%{?fedora} || 0%{?rhel} == 7
BuildRequires:  infinipath-psm-devel
%endif
%if 0%{?fedora} || (0%{?rhel} >= 7 && 0%{?rhel} < 10)
BuildRequires:  libpsm2-devel
%endif
BuildRequires:  numactl-devel
%endif

%description
OpenFabrics Interfaces (OFI) is a framework focused on exporting fabric
communication services to applications.  OFI is best described as a collection
of libraries and applications used to export fabric services.  The key
components of OFI are: application interfaces, provider libraries, kernel
services, daemons, and test applications.

Libfabric is a core component of OFI.  It is the library that defines and
exports the user-space API of OFI, and is typically the only software that
applications deal with directly.  It works in conjunction with provider
libraries, which are often integrated directly into libfabric.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-%{version}

%build
%if %{__remake_config}
./autogen.sh
%endif
%configure --disable-static --disable-silent-rules
%make_build


%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%ldconfig_scriptlets


%files
%license COPYING
%{_bindir}/fi_info
%{_bindir}/fi_pingpong
%{_bindir}/fi_strerror
%{_libdir}/*.so.1*
%{_mandir}/man1/*.1*

%files devel
%license COPYING
%doc AUTHORS README
# We knowingly share this with kernel-headers and librdmacm-devel
# https://github.com/ofiwg/libfabric/issues/1277
%{_includedir}/rdma/
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man3/*.3*
%{_mandir}/man7/*.7*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 31 2024 Orion Poplawski <orion@nwra.com> - 1.22.0-1
- Update to 1.22.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Mar 30 2024 Orion Poplawski <orion@nwra.com> - 1.21.0-1
- Update to 1.21.0

* Fri Feb 09 2024 Orion Poplawski <orion@nwra.com> - 1.20.1-1
- Update to 1.20.1

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Sep 04 2023 Orion Poplawski <orion@nwra.com> - 1.19.0-1
- Update to 1.19.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.18.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 17 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 1.18.1-2
- Disable PSM2 in RHEL 10 builds

* Sat Jul 15 2023 Orion Poplawski <orion@nwra.com> - 1.18.1-1
- Update to 1.18.1

* Sun Apr 09 2023 Orion Poplawski <orion@nwra.com> - 1.18.0-1
- Update to 1.18.0
- Use SPDX License tag

* Sun Mar 05 2023 Orion Poplawski <orion@nwra.com> - 1.17.1-1
- Update to 1.17.1

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec 29 2022 Orion Poplawski <orion@nwra.com> - 1.17.0-2
- Re-enable LTO on x86_64

* Wed Dec 21 2022 Orion Poplawski <orion@nwra.com> - 1.17.0-1
- Update to 1.17.0

* Thu Dec 15 2022 Orion Poplawski <orion@nwra.com> - 1.17.0-0.1.rc2
- Update to 1.17.0rc2

* Fri Nov 11 2022 Orion Poplawski <orion@nwra.com> - 1.16.1-3
- Actually apply patch

* Fri Nov 11 2022 Orion Poplawski <orion@nwra.com> - 1.16.1-2
- Add upstream patch to fix openmpi hang on koji builders (bz#2141137)

* Tue Oct 11 2022 Orion Poplawski <orion@nwra.com> - 1.16.1-1
- Update to 1.16.1

* Wed Aug 24 2022 Orion Poplawski <orion@nwra.com> - 1.15.2-1
- Update to 1.15.2

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon May 16 2022 Orion Poplawski <orion@nwra.com> - 1.15.1-1
- Update to 1.15.1
- Disable LTO on x86_64 due to memory issues

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 23 2021 Honggang Li <honli@redhat.com> - 1.14.0-1
- Update to upstream release v1.14.0
- Resolves: bz2023044

* Fri Nov 05 2021 Honggang Li <honli@redhat.com> - 1.14.0-0.2
- Update to upstream release v1.14.0rc2
- Resolves: bz2019559

* Tue Nov 02 2021 Honggang Li <honli@redhat.com> - 1.14.0-0.1
- Update to upstream release v1.14.0rc1
- Resolves: bz2019559

* Sat Oct 16 2021 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.13.2-1
- Update to 1.13.2 (#2011975)

* Mon Sep 06 2021 Honggang Li <honli@redhat.com> - 1.13.1-1
- Update to upstream release v1.13.1
- Resolves: bz1993636

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.13.0-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Honggang Li <honli@redhat.com> - 1.13.0-0.1
- Update to upstream release v1.13.0rc1
- Resolves: bz1945627

* Thu Apr 01 2021 Honggang Li <honli@redhat.com> - 1.12.1-1
- Update to upstream release v1.12.1
- Enable psm3 support
- Resolves: bz1945627

* Sun Jan 31 2021 Honggang Li <honli@redhat.com> - 1.12.0-0.1
- Update to upstream release v1.12.0rc1

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 16 2020 Honggang Li <honli@redhat.com> - 1.11.2-1
- Update to upstream release v1.11.2

* Tue Dec 08 2020 Honggang Li <honli@redhat.com> - 1.11.2-0.1
- Update to upstream release v1.11.2rc1
- Resolves: bz1905751

* Sun Oct 11 2020 Honggang Li <honli@redhat.com> - 1.11.1
- Update to upstream release v1.11.1
- Resolves: bz1887069

* Thu Oct 08 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.11.1rc1-1
- Update to 1.11.1rc1 (#1886494)

* Sat Aug 15 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.11.0-1
- Update to 1.11.0 (#1869025)

* Tue Aug 04 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.11.0rc2-1
- Update to 1.11.0rc2 (#1866049)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0rc1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.11.0rc1-1
- Update to 1.11.0rc1 (#1859427)

* Sat May 09 2020 Honggang Li <honli@redhat.com> - 1.10.1-1
- Update to upstream release v1.10.1
- Resolves: bz1833620

* Fri Apr 24 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 1.10.0-1
- Update to 1.10.0 (#1827815)

* Sun Apr 12 2020 Honggang Li <honli@redhat.com> - 1.10.0rc2-1
- Update to 1.10.0rc2

* Fri Apr 03 2020 Honggang Li <honli@redhat.com> - 1.10.0rc1-1
- Update to 1.10.0rc1
- Resolves: bz1820096

* Mon Mar 09 2020 Honggang Li <honli@redhat.com> - 1.9.1-1
- Update to 1.9.1
- Resolves: bz1811269

* Sun Feb 16 2020 Honggang Li <honli@redhat.com> - 1.9.1rc1-1
- Update to 1.9.1rc
- Resolves: bz1803485

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 28 2019 Honggang Li <honli@redhat.com> - 1.9.0
- Update to 1.9.0
- Resolves: bz1775865

* Thu Oct 24 2019 Honggang Li <honli@redhat.com> - 1.9.0rc1-1
- Update to 1.9.0rc1
- Resolves: bz1751860

* Fri Sep 06 2019 Honggang Li <honli@redhat.com> - 1.8.0-3
- Fix two segment fault issues
- Resolves: bz1749608

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jun 29 2019 Honggang Li <honli@redhat.com> - 1.8.0
- Update to 1.8.0

* Mon Jun 17 2019 Honggang Li <honli@redhat.com> - 1.8.0rc1
- Update to 1.8.0rc1
- Resolves: 1720773

* Mon Jun 10 2019 Honggang Li <honli@redhat.com> - 1.7.2rc2
- Update to 1.7.2rc2
- Resolves: bz1689783

* Mon Apr  8 2019 Orion Poplawski <orion@nwra.com> - 1.7.1-1
- Update to 1.7.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 31 2019 Honggang Li <honli@redhat.com> - 1.7.0-1
- Rebase libfabric to latest upstream release v1.7.0
- Resolves: bz1671189

* Mon Oct  8 2018 Honggang Li <honli@redhat.com> - 1.6.2-1
- Rebase libfabric to latest upstream release v1.6.2
- Resolves: bz1637334

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Honggang Li <honli@redhat.com> - 1.6.1-1
- Rebase to latest upstream release 1.6.1
- Resolves: bz1550404

* Thu Mar 15 2018 Orion Poplawski <orion@nwra.com> - 1.6.0-1
- Update to 1.6.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 23 2017 Adam Williamson <awilliam@redhat.com> - 1.4.2-5
- Disable RDMA support on 32-bit ARM (#1484155)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 1.4.2-3
- Rebuild with binutils fix for ppc64le (#1475636)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 11 2017 Orion Poplawski <orion@cora.nwra.com> - 1.4.2-1
- Update to 1.4.2

* Mon Apr 10 2017 Orion Poplawski <orion@cora.nwra.com> - 1.4.1-1
- Update to 1.4.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 3 2016 Orion Poplawski <orion@cora.nwra.com> - 1.4.0-1
- Update to 1.4.0

* Thu Jul 21 2016 Orion Poplawski <orion@cora.nwra.com> - 1.3.0-3
- Rebuild for aarch64 glibc update

* Tue May 31 2016 Orion Poplawski <orion@cora.nwra.com> - 1.3.0-2
- Use psm/psm2 if possible on Fedora (bug #1340988)

* Tue Apr 12 2016 Orion Poplawski <orion@cora.nwra.com> - 1.3.0-1
- Update to 1.3.0

* Wed Mar 9 2016 Orion Poplawski <orion@cora.nwra.com> - 1.2.0-1
- Update to 1.2.0
- Use psm/psm2 if possible on EL
- Add upstream patch to fix non-x86 builds

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Aug 26 2015 Orion Poplawski <orion@cora.nwra.com> - 1.1.0-1
- Update to 1.1.0

* Mon Jul 20 2015 Orion Poplawski <orion@cora.nwra.com> - 1.0.0-1
- Initial package
