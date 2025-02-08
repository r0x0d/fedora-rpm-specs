Name:           exfatprogs
Version:        1.2.7
Release:        1%{?dist}
Summary:        Userspace utilities for exFAT filesystems
License:        GPL-2.0-only
URL:            https://github.com/%{name}/%{name}

Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make

%description
Utilities for formatting and repairing exFAT filesystems.

%prep
%autosetup

%build
autoreconf -vif
%configure \
    --enable-shared=yes \
    --enable-static=no
%make_build

%install
%make_install

%files
%license COPYING
%doc README.md
%{_sbindir}/dump.exfat
%{_sbindir}/exfat2img
%{_sbindir}/exfatlabel
%{_sbindir}/fsck.exfat
%{_sbindir}/mkfs.exfat
%{_sbindir}/tune.exfat
%{_mandir}/man8/dump.exfat.*
%{_mandir}/man8/exfat2img.*
%{_mandir}/man8/exfatlabel.*
%{_mandir}/man8/fsck.exfat.*
%{_mandir}/man8/mkfs.exfat.*
%{_mandir}/man8/tune.exfat.*

%changelog
* Thu Feb 06 2025 Simone Caronni <negativo17@gmail.com> - 1.2.7-1
- Update to 1.2.7.

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 21 2024 Pavel Reichl <preichl@redhat.com> - 1.2.6-1
- new version
- Related rhbz#2327575

* Wed Aug 07 2024 Simone Caronni <negativo17@gmail.com> - 1.2.5-1
- Update to 1.2.5.

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jun 17 2024 Simone Caronni <negativo17@gmail.com> - 1.2.4-1
- Update to 1.2.4.

* Mon May 27 2024 Simone Caronni <negativo17@gmail.com> - 1.2.3-1
- Update to 1.2.3.

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 30 2023 Pavel Reichl <preichl@redhat.com> - 1.2.2-2
- Convert License tag to SPDX format

* Sat Oct 28 2023 Simone Caronni <negativo17@gmail.com> - 1.2.2-1
- Update to 1.2.2.

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 22 2023 Simone Caronni <negativo17@gmail.com> - 1.2.1-1
- Update to 1.2.1.

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Oct 28 2022 Simone Caronni <negativo17@gmail.com> - 1.2.0-1
- Update to 1.2.0.

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Nov 21 2021 Simone Caronni <negativo17@gmail.com> - 1.1.3-1
- Update to 1.1.3.

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue May 25 2021 Simone Caronni <negativo17@gmail.com> - 1.1.2-1
- Update to 1.1.2.

* Thu Apr 22 2021 Simone Caronni <negativo17@gmail.com> - 1.1.1-1
- Update to 1.1.1.

* Tue Mar 23 2021 Simone Caronni <negativo17@gmail.com> - 1.1.0-1
- Update to 1.1.0.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Dec 04 2020 Simone Caronni <negativo17@gmail.com> - 1.0.4-1
- Update to 1.0.4.

* Wed May 20 2020 Simone Caronni <negativo17@gmail.com> - 1.0.3-1
- Update to 1.0.3, no more shared libraries.

* Mon Apr 27 2020 Simone Caronni <negativo17@gmail.com> - 1.0.2-1
- Review fixes.
- Update to 1.0.2.

* Thu Apr 23 2020 Simone Caronni <negativo17@gmail.com> - 1.0.1-2
- Rename to exfatprogs.
- Removed provides/obsoletes on Fuse implementation.

* Wed Apr 15 2020 Simone Caronni <negativo17@gmail.com> - 1.0.1-1
- First build.
