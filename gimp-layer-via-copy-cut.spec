%global	addon layer-via-copy-cut

Name:		gimp-%{addon}
Version:	1.6
Release:	%autorelease
Summary:	Layer via copy/cut plug-in for GIMP
# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:	GPL-3.0-or-later
URL:		https://www.deviantart.com/slybug/art/Layer-via-Copy-Cut-305728401
Source0:	https://some-gimp-plugins.com/contents/en/extensions/002/%{addon}.zip
Source1:	%{name}.metainfo.xml
Source2:	LICENSE.txt
BuildRequires:	pkgconfig(python3)
BuildRequires:	libappstream-glib
Requires:	gimp

%description
Copy and move the selected area to a new layer in the same position.

# Upstream changed plugins path and this package is no longer noarch
%global debug_package %{nil}
%prep
%autosetup -c  %{name}
cp -p %{SOURCE2} .

# Fix Python shebangs for lessen Fedora release
%py3_shebang_fix %{addon}.py

%build
# Nothing to build

%install
install -Dpm 0755 %{addon}.py -t %{buildroot}%{_libdir}/gimp/3.0/plug-ins/

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE1} \
	%{buildroot}%{_datadir}/appdata/%{name}.metainfo.xml

%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.metainfo.xml


%files 
%license LICENSE.txt
%{_libdir}/gimp/3.0/plug-ins/%{addon}.py*
#AppStream metadata
%{_datadir}/appdata/%{name}.metainfo.xml

%changelog
%autochangelog
