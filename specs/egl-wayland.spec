%global commit0 26ba0e3ee448ff83644bc2ffbe5d06d21c60ce44
%global date 20250114
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
#global tag %{version}

Name:           egl-wayland
Version:        1.1.18%{!?tag:~%{date}git%{shortcommit0}}
Release:        2%{?dist}
Summary:        EGLStream-based Wayland external platform
License:        MIT
URL:            https://github.com/NVIDIA/%{name}

%if 0%{?tag:1}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
%else
Source0:        %{url}/archive/%{commit0}/%{name}-%{shortcommit0}.tar.gz
%endif

BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  libtool
BuildRequires:  pkgconfig(egl) >= 1.5
BuildRequires:  pkgconfig(eglexternalplatform) >= 1.1
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl-backend) >= 3
# Explicit synchronization since 1.34:
BuildRequires:  pkgconfig(wayland-protocols) >= 1.34
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)

# Required for directory ownership
Requires:       libglvnd-egl%{?_isa}

%description
EGL External Platform library to add client-side Wayland support to EGL on top
of EGLDevice and EGLStream families of extensions.

This library implements an EGL External Platform interface to work along with
EGL drivers that support the external platform mechanism.

%package devel
Summary:        EGLStream-based Wayland external platform development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
EGL External Platform library to add client-side Wayland support to EGL on top
of EGLDevice and EGLStream families of extensions.

This library implements an EGL External Platform interface to work along with
EGL drivers that support the external platform mechanism.

This package contains development files.

%prep
%if 0%{?tag:1}
%autosetup -p1
%else
%autosetup -p1 -n %{name}-%{commit0}
%endif

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot} -name '*.la' -delete

%files
%doc README.md
%license COPYING
%{_libdir}/libnvidia-egl-wayland.so.1
%{_libdir}/libnvidia-egl-wayland.so.1.1.18
%{_datadir}/egl/egl_external_platform.d/10_nvidia_wayland.json

%files devel
%{_datadir}/pkgconfig/wayland-eglstream-protocols.pc
%{_datadir}/wayland-eglstream/
%{_libdir}/libnvidia-egl-wayland.so
%{_libdir}/pkgconfig/wayland-eglstream.pc

%changelog
* Wed Jan 15 2025 Simone Caronni <negativo17@gmail.com> - 1.1.18~20250114git26ba0e3-2
- Update to latest snapshot.

* Mon Dec 16 2024 Simone Caronni <negativo17@gmail.com> - 1.1.18~20241210git0c6f823-1
- Update to 1.1.18 pre-release snapshot.

* Mon Dec 09 2024 Simone Caronni <negativo17@gmail.com> - 1.1.17-6
- Update to final 1.1.17 (no change to the codebase).

* Mon Nov 18 2024 Simone Caronni <negativo17@gmail.com> - 1.1.17^20241118giteeb29e1-5
- Update to latest snapshot.

* Sun Nov 03 2024 Simone Caronni <negativo17@gmail.com> - 1.1.17^20241101git218f678-4
- Update to latest snapshot.

* Wed Oct 16 2024 Simone Caronni <negativo17@gmail.com> - 1.1.17^20241016git0cd471d-3
- Update to latest snapshot.

* Mon Oct 07 2024 Simone Caronni <negativo17@gmail.com> - 1.1.17^20240924gitc10c530-2
- Update to latest snapshot.

* Fri Sep 20 2024 Simone Caronni <negativo17@gmail.com> - 1.1.17^20240919gitf5d9c69-1
- Update to latest snapshot.
- ICD is installed directly from sources.

* Thu Sep 19 2024 Simone Caronni <negativo17@gmail.com> - 1.1.17^20240918git845568c-1
- Update to latest snapshot.
- Switch to more recent packaging guidelines for snapshot versions.
- Move egl-gbm ICD to egl-gbm package.

* Tue Sep 03 2024 Simone Caronni <negativo17@gmail.com> - 1.1.17-2.20240828git2d5ecff
- Update to latest snapshot.

* Fri Aug 23 2024 Simone Caronni <negativo17@gmail.com> - 1.1.16-1
- Switch to 1.1.16 final.

* Wed Aug 21 2024 Simone Caronni <negativo17@gmail.com> - 1.1.15-2.20240819git8188db9
- Update to latest snapshot (#2305705).

* Fri Aug 09 2024 Simone Caronni <negativo17@gmail.com> - 1.1.15-1
- Update to 1.1.15 final.

* Thu Aug 08 2024 Simone Caronni <negativo17@gmail.com> - 1.1.14-3.20240808git4480345
- Update to latest snapshot.

* Wed Aug 07 2024 Simone Caronni <scaronni@nvidia.com> - 1.1.14-2.20240805gitc439cd5
- Update to latest snapshot with commits required for NVIDIA driver 560+ with
  explicit sync support.

* Thu Jul 18 2024 Leigh Scott <leigh123linux@gmail.com> - 1.1.14-1
- Update to 1.1.14

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue May 21 2024 Leigh Scott <leigh123linux@gmail.com> - 1.1.13-4
- Add Wayland explicit sync support

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Oct 20 2023 Leigh Scott <leigh123linux@gmail.com> - 1.1.13-1
- Update to 1.1.13

* Thu Sep 07 2023 José Expósito <jexposit@redhat.com> - 1.1.12-4
- SPDX migration: license is already SPDX compatible

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul 19 2023 Leigh Scott <leigh123linux@gmail.com> - 1.1.12-2
- Add patch to fix rhbz#2223856

* Fri Jun 09 2023 Leigh Scott <leigh123linux@gmail.com> - 1.1.12-1
- Update to 1.1.12

* Mon Apr 10 2023 Jonathan Schleifer <js@nil.im> - 1.1.11-3
- Fix Firefox and Thunderbird crashing on start

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Sep 10 2022 Leigh Scott <leigh123linux@gmail.com> - 1.1.11-1
- Update to 1.1.11

* Tue Aug 09 2022 Leigh Scott <leigh123linux@gmail.com> - 1.1.10-7.20220806git885f0a5
- Update snapshot

* Mon Aug 01 2022 Leigh Scott <leigh123linux@gmail.com> - 1.1.10-6.20220726gitaaf8608
- Update snapshot

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.10-5.20220621git53b6a87
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 30 2022 Leigh Scott <leigh123linux@gmail.com> - 1.1.10-4.20220621git53b6a87
- Fix GTK4 resizing

* Wed Jun 29 2022 Leigh Scott <leigh123linux@gmail.com> - 1.1.10-3.20220626gitd0febee
- Update to latest snapshot

* Sun Jun 12 2022 Leigh Scott <leigh123linux@gmail.com> - 1.1.10-2
- Update to 1.1.10

* Thu Jun 09 2022 Simone Caronni <negativo17@gmail.com> - 1.1.10-1.20220601git247335d
- Update to latest 1.10 snapshot

* Sat Feb 05 2022 Simone Caronni <negativo17@gmail.com> - 1.1.9-5
- Small cleanup.

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 23 2021 Leigh Scott <leigh123linux@gmail.com> - 1.1.9-3
- Add upstream commits

* Sat Oct 16 2021 Leigh Scott <leigh123linux@gmail.com> - 1.1.9-2
- Add 15_nvidia_gbm.json

* Fri Oct 15 2021 Leigh Scott <leigh123linux@gmail.com> - 1.1.9-1
- Update to 1.1.9

* Fri Sep 17 2021 Leigh Scott <leigh123linux@gmail.com> - 1.1.8-1
- Update to 1.1.8

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Leigh Scott <leigh123linux@gmail.com> - 1.1.7-1
- Update to 1.1.7

* Fri May   7 2021 Olivier Fourdan <ofourdan@redhat.com> - 1.1.6-3
- Fix EGL stream closing causing a crash in Xwayland with EGLstream
  (#1943936, #1949415)

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Jan  7 2021 Leigh Scott <leigh123linux@gmail.com> - 1.1.6-1
- Update to 1.1.6

* Fri Aug 14 2020 Leigh Scott <leigh123linux@gmail.com> - 1.1.5-3
- Add upstream patch to address rhbz#1842473

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 01 2020 Leigh Scott <leigh123linux@gmail.com> - 1.1.5-1
- Update to 1.1.5

* Mon Mar 30 2020 leigh123linux <leigh123linux@googlemail.com> - 1.1.4-4
- Use upstream commit to address missing mesa includes

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 16 2019 Leigh Scott <leigh123linux@gmail.com> - 1.1.4-2
- Add patch to add missing mesa includes

* Sun Sep 15 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.1.4-1
- Update to 1.1.4

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.1.3-1
- Update to 1.1.3

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 1.1.2-3
- Rebuild with Meson fix for #1699099

* Sat Mar 30 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.1.2-2
- Switch to upstream fix

* Fri Feb 01 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.1.2-1
- Update to 1.1.2

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Dec 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.1-3
- Fix the same crappy warning f28 generates

* Thu Dec 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.1-2
- Fix the crappy warning epel7 generates

* Thu Dec 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.1-1
- Update to 1.1.1

* Mon Nov 26 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.0-0.2.20181015git0eb29d4
- Update to latest git snapshot (rhbz#1653118)

* Mon Aug 20 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.0-0.1.20180916git1676d1d
- Update to 1.1.0 snapshot

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-0.2.20180626git395ce9f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.0.5-0.1.20180626git395ce9f
- Update to 1.0.5 snapshot

* Sat Jun 16 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.0.4-0.1.20180602git4ab0873
- Update to 1.0.4 snapshot

* Tue Feb 06 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.0.3-2.20180201git6f5f7d0
- Update to latest git snapshot
- Switch to meson
- Install .so file to -devel as it's listed in wayland-eglstream.pc
- Fix directory ownership

* Wed Jan 31 2018 Jonas Ådahl <jadahl@redhat.com> - 1.0.3-1.20180111gitb283689
- Update to 1.0.3
- Add -devel package

* Thu Aug 03 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.2-0.4.20170802git1f4b1fd
- Update to latest git snapshot

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.3.20170628git818b613
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-0.2.20170628git818b613
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jun 28 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.2-0.1.20170628git818b613
- Update to 1.0.2 git

* Wed Mar 08 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.1-0.1.20170308git582fbf3
- Update to 1.0.1 git

* Tue Feb 07 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.7.20170207git05eb000
- Add license file

* Thu Feb 02 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.6.20170120git743d702
- Add requires libglvnd-egl
- Make review changes

* Wed Feb 01 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.5.20170120git743d702
- Drop devel sub-package

* Wed Feb 01 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.4.20170120git743d702
- Add 10_nvidia_wayland.json to libs sub-package

* Wed Feb 01 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.3.20170120git743d702
- Add loader directory to common sub-package
- Move libs to sub-package

* Fri Jan 20 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.2.20170120git743d702
- Add date to release

* Fri Jan 20 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.0.0-0.1.git743d702
- First build

