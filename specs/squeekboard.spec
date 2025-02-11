Name:		squeekboard
Version:	1.43.1
Release:	1%{?dist}
Summary:	a Wayland virtual keyboard

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://gitlab.gnome.org/World/Phosh/squeekboard
Source0:	https://gitlab.gnome.org/World/Phosh/squeekboard/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
Source1:	squeekboard.desktop
# https://gitlab.gnome.org/World/Phosh/squeekboard/-/merge_requests/709
# Patch also includes a revert of the xkbkeyboard 0.8 upgrade
Patch0:		0001-Fixes-to-build-on-Fedora.patch

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:	rust-packaging
BuildRequires:	pkgconfig(gio-2.0) >= 2.26
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(gnome-desktop-3.0) >= 3.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:	pkgconfig(wayland-client) >= 1.14
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(wayland-protocols) >= 1.12
BuildRequires:	pkgconfig(libfeedback-0.0)
BuildRequires:	pkgconfig(libbsd)
BuildRequires:	desktop-file-utils

Provides: %{_datadir}/applications/sm.puri.OSK0.desktop

Requires(post): %{_sbindir}/alternatives
Requires(postun): %{_sbindir}/alternatives

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%description
Squeekboard is a virtual keyboard supporting Wayland, built primarily
for the Librem 5 phone. It squeaks because some Rust got inside.

%prep
%autosetup -p1 -n %{name}-v%{version}
%cargo_prep

rm -f Cargo.lock
%generate_buildrequires
%cargo_generate_buildrequires -a

%build
# ensure standard Rust compiler flags are set
export RUSTFLAGS="%build_rustflags"
%meson
%meson_build

%install
%meson_install
mkdir -p %{buildroot}%{_sysconfdir}/xdg/autostart/
cp %{SOURCE1} %{buildroot}%{_sysconfdir}/xdg/autostart/
chmod +x %{buildroot}%{_bindir}/squeekboard-entry

cp tools/squeekboard-restyled %{buildroot}%{_bindir}
chmod +x %{buildroot}%{_bindir}/squeekboard-restyled

sed -i 's/Phosh/X-Phosh/g' %{buildroot}%{_datadir}/applications/sm.puri.Squeekboard.desktop
sed -i 's/X-X-Phosh/X-Phosh/g' %{buildroot}%{_datadir}/applications/sm.puri.Squeekboard.desktop

%find_lang %{name}

touch %{buildroot}%{_datadir}/applications/sm.puri.OSK0.desktop

%check
# ensure standard Rust compiler flags are set
export RUSTFLAGS="%build_rustflags"
%meson_test
desktop-file-validate %{buildroot}/%{_datadir}/applications/sm.puri.Squeekboard.desktop

%post
alternatives --install \
    %{_datadir}/applications/sm.puri.OSK0.desktop \
    phosh-osk \
    %{_datadir}/applications/sm.puri.Squeekboard.desktop \
    10

%preun
if [ $1 -eq 0 ] ; then
  alternatives --remove \
    phosh-osk \
    %{_datadir}/applications/sm.puri.Squeekboard.desktop
fi

%files -f %{name}.lang
%ghost %{_datadir}/applications/sm.puri.OSK0.desktop
%{_bindir}/squeekboard
%{_bindir}/squeekboard-entry
%{_bindir}/squeekboard-test-layout
%{_bindir}/squeekboard-restyled
%{_datadir}/applications/sm.puri.Squeekboard.desktop
%{_datadir}/glib-2.0/schemas/sm.puri.Squeekboard.gschema.xml
%{_sysconfdir}/xdg/autostart/squeekboard.desktop
%doc README.md
%license COPYING

%changelog
* Sun Feb 02 2025 Sam Day <me@samcday.com> - 1.43.1-1
- Update to 1.43.1
- Patch zbus dependency from 1.9 to to 4.x
- Patch xkbkeyboard dependency from 0.8 to 0.7

* Wed Jan 22 2025 David Bold <davidsch@fedoraproject.org> - 1.42.0-2
- Disable building for i686

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.42.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Oct 01 2024 David Bold <davidsch@fedoraproject.org> - 1.42.0-1
- Update to 1.42.0

* Tue Aug 20 2024 David Bold <davidsch@fedoraproject.org> - 1.41.0-1
- Update to 1.41.0

* Thu Jul 25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.39.0-3
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.39.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jun 18 2024 David Bold <davidsch@fedoraproject.org> - 1.39.0-1
- Update to 1.39.0

* Mon Apr 15 2024 David Bold <davidsch@fedoraproject.org> - 1.38.0-1
- Update to 1.38.0 ; Thanks to Sam Day for the xkb patch

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.22.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Feb 05 2023 Fabio Valentini <decathorpe@gmail.com> - 1.20.0-3
- Ensure standard Rust compiler flags are set.

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Sep 11 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.20.0-1
- Update to 1.20.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.19.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Kalev Lember <klember@redhat.com> - 1.19.0-2
- Rebuilt for libgnome-desktop soname bump

* Mon Jul 18 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.19.0-1
- Update to 1.19.0

* Thu Jun 02 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.18.0-1
- Update to 1.18.0

* Fri Jan 28 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.16.0-2
- Patch not starting bug

* Tue Jan 25 2022 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.16.0-1
- Update to 1.16.0

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun May 23 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.14.0-1
- Update to 1.14.0

* Thu Apr 15 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.13.0-1
- Update to 1.13.0

* Thu Feb 18 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.12.0-3
- Bump version for rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.12.0-1
- Update to 1.12.0

* Mon Nov 23 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.11.1-1
- Update to 1.11.1

* Sat Nov 14 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.11.0-1
- Update to 1.11.0

* Fri Oct 23 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.10.0-1
- Update to 1.10.0

* Sun Aug 09 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.9.3-1
- Update to 1.9.3 including new dependencies and new patch file and Cargo.toml

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Josh Stone <jistone@redhat.com> - 1.9.2-2
- Bump to cairo 0.9 and gtk 0.9

* Fri Jun 19 2020 Torrey Sorensen <torbuntu@fedoraproject.org> - 1.9.2-1
- Update to 1.9.2, including updated patch file.
- Remove unused libcroco
- Temporarily excluding ppc64le architecture 

* Tue Mar 24 2020 Nikhil Jha <hi@nikhiljha.com> - 1.9.1-1
- Update to 1.9.1

* Tue Mar 24 2020 Nikhil Jha <hi@nikhiljha.com> - 1.9.0-2
- Validate desktop file

* Thu Feb 27 2020 Nikhil Jha <hi@nikhiljha.com> - 1.9.0-1
- Initial packaging
