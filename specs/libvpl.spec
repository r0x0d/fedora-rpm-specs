%global mfx_major 2
%global mfx_minor 14

Name:           libvpl
Epoch:          1
Version:        2.14.0
Release:        2%{?dist}
Summary:        Intel Video Processing Library
License:        MIT
URL:            https://intel.github.io/libvpl/latest/index.html
ExclusiveArch:  x86_64

Source0:        https://github.com/intel/libvpl/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libdrm) >= 2.4.91
BuildRequires:  pkgconfig(libva) >= 1.2
BuildRequires:  pkgconfig(libva-drm) >= 1.2
BuildRequires:  pkgconfig(libva-x11) >= 1.10.0
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.15
BuildRequires:  pkgconfig(x11)

Recommends:     intel-mediasdk
Recommends:     intel-vpl-gpu-rt

Obsoletes:      oneVPL <= 2023.4.0
Provides:       oneVPL%{?_isa} == %{?epoch:%{epoch}:}%{version}-%{release}

%description
The oneAPI Video Processing Library (oneVPL) provides a single video processing
API for encode, decode, and video processing that works across a wide range of
accelerators.

The base package is limited to the dispatcher and samples. To use oneVPL for
video processing you need to install at least one implementation. Current
implementations:

- intel-vpl-gpu-rt for use on Intel Xe graphics and newer
- intel-mediasdk for use on legacy Intel graphics

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:      oneVPL-devel <= 2023.4.0
Provides:       oneVPL-devel%{?_isa} == %{?epoch:%{epoch}:}%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package        samples
Summary:        Sample programs and source code for %{name}
Requires:       %{name}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:      oneVPL-samples <= 2023.4.0
Provides:       oneVPL-samples%{?_isa} == %{?epoch:%{epoch}:}%{version}-%{release}

%description    samples
This package contains sample programs and applications that use %{name}.

%prep
%autosetup -p1 -n libvpl-%{version}

%build
%cmake -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}
%cmake_build

%install
%cmake_install

# Let RPM pick up documents in the files section
rm -fr %{buildroot}%{_datadir}/vpl/licensing

%files
%license LICENSE
%doc README.md CONTRIBUTING.md third-party-programs.txt
%dir %{_sysconfdir}/vpl
%{_sysconfdir}/vpl/vars.sh
%{_libdir}/libvpl.so.%{mfx_major}
%{_libdir}/libvpl.so.%{mfx_major}.%{mfx_minor}

%files devel
%{_includedir}/vpl
%dir %{_libdir}/cmake/vpl
%{_libdir}/cmake/vpl/VPLConfig.cmake
%{_libdir}/cmake/vpl/VPLConfigVersion.cmake
%{_libdir}/libvpl.so
%{_libdir}/pkgconfig/vpl.pc

%files samples
%dir %{_datadir}/vpl
%{_datadir}/vpl/examples

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Dec 27 2024 Simone Caronni <negativo17@gmail.com> - 1:2.14.0-1
- Update to 2.14.0.

* Tue Sep 10 2024 Simone Caronni <negativo17@gmail.com> - 1:2.13.0-1
- Update to 2.13.0.

* Sun Aug 25 2024 Simone Caronni <negativo17@gmail.com> - 1:2.12.0-1
- Update to 2.12.0.
- Update GPU requirements.

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat May 04 2024 Simone Caronni <negativo17@gmail.com> - 1:2.11.0-1
- Update to 2.11.0.

* Wed Feb 21 2024 Simone Caronni <negativo17@gmail.com> - 1:2.10.2-1
- Update to 2.10.2.

* Tue Feb 13 2024 Simone Caronni <negativo17@gmail.com> - 1:2.10.1-2
- Switch from Intel® to Intel in pkgconfig file.

* Thu Jan 18 2024 Simone Caronni <negativo17@gmail.com> - 1:2.10.1-1
- Rename to libvpl with new versioning scheme.

* Thu Dec 14 2023 Simone Caronni <negativo17@gmail.com> - 2023.4.0-2
- Drop patch, adjust file section.

* Mon Dec 11 2023 Ali Erdinc Koroglu <aekoroglu@fedoraproject.org> - 2023.4.0-1
- Update to 2023.4.0

* Tue Oct 03 2023 Simone Caronni <negativo17@gmail.com> - 2023.3.1-1
- Update to 2023.3.1.

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2023.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 22 2023 Nicolas Chauvet <kwizart@gmail.com> - 2023.1.3-2
- Rebuilt for libva

* Mon Mar 13 2023 Adam Williamson <awilliam@redhat.com> - 2023.1.3-1
- Update to 2023.1.3
- Drop Python bindings (removed upstream)
- Fix install path for config files (#2177912)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Aug 24 2022 Simone Caronni <negativo17@gmail.com> - 2022.2.2-1
- Update to 2022.2.2.
- Patch system_analyzer so it works without devel subpackage installed.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2022.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Simone Caronni <negativo17@gmail.com> - 2022.1.5-1
- Update to 2022.1.5.

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2022.1.3-2
- Rebuilt for Python 3.11

* Wed May 25 2022 Simone Caronni <negativo17@gmail.com> - 2022.1.3-1
- Update to 2022.1.3.

* Tue Apr 26 2022 Simone Caronni <negativo17@gmail.com> - 2022.1.1-1
- Update to 2022.1.1.
- Recommend implementations (at least one must be installed).

* Sat Mar 19 2022 Simone Caronni <negativo17@gmail.com> - 2022.1.0-1
- Update to 2022.1.0.

* Sun Mar 13 2022 Simone Caronni <negativo17@gmail.com> - 2022.0.6-1
- Update to 2022.0.6.

* Wed Mar 02 2022 Simone Caronni <negativo17@gmail.com> - 2022.0.5-2
- Rebuild for updated libva.

* Wed Mar 02 2022 Simone Caronni <negativo17@gmail.com> - 2022.0.5-1
- Update to 2022.0.5.

* Tue Feb 08 2022 Simone Caronni <negativo17@gmail.com> - 2022.0.4-1
- Update to 2022.0.4.

* Mon Feb 07 2022 Simone Caronni <negativo17@gmail.com> - 2022.0.0-2
- Enable Python binding.

* Sat Feb 05 2022 Simone Caronni <negativo17@gmail.com> - 2022.0.0-1
- First build.
