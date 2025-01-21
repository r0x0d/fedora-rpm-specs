Name:           xdms
Version:        1.3.2
Release:        36%{?dist}
Summary:        Extracts Amiga DMS archives
License:        LicenseRef-Fedora-Public-Domain
URL:            http://zakalwe.fi/~shd/foss/%{name}
Source0:        http://zakalwe.fi/~shd/foss/%{name}/%{name}-%{version}.tar.bz2
Patch0:         inline.patch

BuildRequires: make
BuildRequires:  gcc
%description
Extracts Amiga DMS (Disk Masher) archives which are compressed Amiga disk
images. Xdms is particularly useful with Amiga emulators.


%prep
%setup -q
%patch -P0 -p1

%build
# Non standard configure script that does not support libdir for example.
CFLAGS="%{optflags}" ./configure --prefix=%{_usr}
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m0644 xdms.1 %{buildroot}%{_mandir}/man1
install -p -m0755 src/xdms %{buildroot}%{_bindir}



%files
%{_bindir}/xdms
%{_mandir}/man1/xdms.1.*
%doc ChangeLog.txt %{name}.txt


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-36
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-34
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-33
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jul 07 2023 Gwyn Ciesla <gwync@protonmail.com> - 1.3.2-32
- Convert to SPDX license.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-31
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 21 2019 Gwyn Ciesla <gwync@protonmail.com> - 1.3.2-24
- Patch for gcc 10.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.3.2-5
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Ian Chapman <packages@amiga-hardware.com> 1.3.2-4
- Release bump for F8 mass rebuild

* Sat Nov 18 2006 Ian Chapman <packages@amiga-hardware.com> 1.3.2-3
- Minor spec cleanups

* Mon Nov 06 2006 Ian Chapman <packages@amiga-hardware.com> 1.3.2-2
- Possible migration to FE

* Mon Oct 23 2006 Ian Chapman <packages@amiga-hardware.com> 1.3.2-1
- Upgrade to 1.3.2

* Mon May 29 2006 Ian Chapman <packages@amiga-hardware.com> 1.3.1-3
- Replace %%{__rm} in clean section with rm
- Use rpmoptflags

* Mon May 01 2006 Ian Chapman <packages@amiga-hardware.com> 1.3.1-2.iss
- Altered spec file to follow Fedora style more closely
- Removed readdisk as this was actually an Amiga binary

* Sun Dec 18 2005 Ian Chapman <packages@amiga-hardware.com> 1.3.1-1.iss
- Initial Release
