Name:           oneko
Summary:        Cat chases the cursor
Version:        1.2
Release:        41%{?dist}
License:        LicenseRef-Fedora-Public-Domain
# Modified Source to remove BSD images, due to copyright.
# Source0:      http://www.daidouji.com/oneko/distfiles/oneko-1.2.sakura.5.tar.gz
Source0:        oneko-1.2.sakura.5.noBSD.tar.gz
Source1:        oneko.desktop
Source2:        oneko.png
URL:            http://www.daidouji.com/oneko/
Patch0:         oneko-1.2.sakura.5-nobsd.patch
Patch1:         oneko-1.2.sakura.5-typo-fix.patch
Patch2:         oneko-c99.patch
BuildRequires: make
BuildRequires:  libX11-devel, imake, libXext-devel, gcc
BuildRequires:  desktop-file-utils

%description
A cat (neko) chases the cursor (now a mouse) around the screen while you
work. Alternatively, a dog chases a bone.

%prep
%setup -q -n %{name}-%{version}.sakura.5
%patch -P0 -p1
%patch -P1 -p1 -b .typo
%patch -P2 -p1

%build
xmkmf -a
make CFLAGS="$RPM_OPT_FLAGS -Dlinux -D_POSIX_C_SOURCE=199309L-D_POSIX_SOURCE -D_XOPEN_SOURCE -D_BSD_SOURCE -D_SVID_SOURCE -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -DFUNCPROTO=15 -DNARROWPROTO -DSHAPE "

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_mandir}/ja/man1
install -p -m0644 oneko.man $RPM_BUILD_ROOT%{_mandir}/man1/oneko.1
install -p -m0644 oneko.man.jp $RPM_BUILD_ROOT%{_mandir}/ja/man1/oneko.1
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m0644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps
desktop-file-install \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications         \
        %{SOURCE1}
mv README README.jp
mv README-SUPP README-SUPP.jp

%files
%doc README.jp README-NEW README-SUPP.jp sample.resource
%{_bindir}/oneko
%{_datadir}/applications/*oneko.desktop
%{_datadir}/pixmaps/oneko.png
%{_mandir}/ja/man1/*
%{_mandir}/man1/*

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-39
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-38
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov 25 2022 Florian Weimer <fweimer@redhat.com> - 1.2-35
- Port to C99 (mostly) (#2148554)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-32
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 07 2018 Adam Williamson <awilliam@redhat.com> - 1.2-25
- Rebuild to fix GCC 8 mis-compilation
  See https://da.gd/YJVwk ("GCC 8 ABI change on x86_64")

* Mon Feb 19 2018 Matěj Cepl <mcepl@redhat.com> - 1.2-24
- Add gcc as BuildRequires.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 30 2013 Jon Ciesla <limburgher@gmail.com> - 1.2-14
- Drop desktop vendor tag.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 15 2010 Tom Callaway <spot@fedoraproject.org> - 1.2-9
- fix typos in man page
- fix man page file naming
- update desktop file to modern specs

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2-6
- Autorebuild for GCC 4.3

* Fri Aug 24 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.2-5
- rebuild for BuildID

* Thu Sep 14 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.2-4
- FC-6 rebuild

* Tue Mar  7 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.2-3
- remove includedir macro, not needed
- rename japanese man page to not have .jp extension

* Thu Jan 19 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.2-2
- use _includedir macro
- remove _i386_ hardcode
- fix blatant typo in patch
- rename docs to jp
- use -p for install
- remove xorg-x11-proto-devel, unnecessary

* Wed Jan 18 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.2-1
- Initial package for Fedora Extras
