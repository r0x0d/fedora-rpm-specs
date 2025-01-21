Name:           xscope
Version:        1.4.4
Release:        6%{?dist}
Summary:        X Window Protocol Viewer

License:        MIT AND HPND-sell-variant
URL:            https://gitlab.freedesktop.org/xorg/app/xscope
Source0:        https://www.x.org/releases/individual/app//%{name}-%{version}.tar.xz

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  xorg-x11-xtrans-devel, xorg-x11-proto-devel


%description
xscope sits in-between an X11 client and an X11 server and prints the contents
of each request, reply, error, or event that is communicated between them.
This information can be useful in debugging and performance tuning of X11 
servers and clients.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc AUTHORS NEWS ChangeLog README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul  7 2023 Yanko Kaneti <yaneti@declera.com> 1.4.4-2
- SPDX migration

* Sat Jun  3 2023 Yanko Kaneti <yaneti@declera.com> 1.4.4-1
- Update to 1.4.4

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 11 2022 Yanko Kaneti <yaneti@declera.com> 1.4.3-1
- Update to 1.4.3

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Dec  7 2021 Yanko Kaneti <yaneti@declera.com> 1.4.2-1
- Update to 1.4.2

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jan 28 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 21 2019 Adam Jackson <ajax@redhat.com> - 1.4.1-11
- Rebuild for xtrans 1.4.0

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Yanko Kaneti <yaneti@declera.com>
- Remove defattr. Use license.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun  8 2014 Yanko Kaneti <yaneti@declera.com> 1.4.1-1
- Update to 1.4.1. Autoreconf no longer required

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Mar 25 2013 Yanko Kaneti <yaneti@declera.com> 1.4-3
- autoreconf for now for aarch64

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Nov 20 2012 Yanko Kaneti <yaneti@declera.com> 1.4-1
- Latest upstream release - 1.4

* Sat Oct 13 2012 Yanko Kaneti <yaneti@declera.com> 1.3.99.901-1
- Upstream pre-release for 1.4

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 22 2012 Yanko Kaneti <yaneti@declera.com> 1.3.1-1
- Upstream release 1.3.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Oct 31 2010 Yanko Kaneti <yaneti@declera.com> 1.3-1
- New upstream release. Drop patches. 
  Remove explicit buildroot, clean.

* Sat Jul 24 2010 Yanko Kaneti <yaneti@declera.com> 1.2-2
- Include an upstream patch for basic GLX support

* Thu Oct  1 2009 Yanko Kaneti <yaneti@declera.com> 1.2-1
- New upstream release. Drop patches.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4.gitfccbbd6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 28 2009 Yanko Kaneti <yaneti@declera.com> 1.1-3.gitfccbbd6
- The software has a MIT not BSD license

* Sat Jun 27 2009 Yanko Kaneti <yaneti@declera.com> 1.1-2.gitfccbbd6
- Implement review feedback
- Patch to build on Fedora 10

* Sun Jun 14 2009 Yanko Kaneti <yaneti@declera.com> 1.1-1.gitfccbbd6
- First attempt at packaging.
