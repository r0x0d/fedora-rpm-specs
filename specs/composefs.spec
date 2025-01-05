%ifarch %{golang_arches}
%bcond man 1
%endif

Name:           composefs
Version:        1.0.8
Release:        1%{?dist}
Summary:        Tools to handle creating and mounting composefs images

License:        LGPL-2.0-or-later AND Apache-2.0
URL:            https://github.com/containers/composefs
Source0:        https://github.com/containers/composefs/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc meson openssl-devel fuse3-devel
%if %{with man}
BuildRequires:  go-md2man
%endif

Requires:       %{name}-libs = %{version}-%{release}

%description
Tools to handle creating and mounting composefs images. The composefs
project combines several underlying Linux features to provide a very
flexible mechanism to support read-only mountable filesystem trees,
stacking on top of an underlying "lower" Linux filesystem.

Please see https://github.com/containers/composefs for more information.

%package        devel
Summary:        Devel files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
Devel files for %{name}.

%package        libs
Summary:        Libraries for %{name}
License:        LGPL-2.1-or-later AND (GPL-2.0-only OR Apache-2.0)

%description    libs
Library files for %{name}.

%prep
%autosetup -p1

%build
%meson --default-library=shared -Dfuse=enabled \
%if %{with man}
  -Dman=enabled 
%endif
%meson_build

%install
%meson_install
rm -v $RPM_BUILD_ROOT/%{_libdir}/libcomposefs*.a

%files devel
%{_includedir}/libcomposefs
%{_libdir}/libcomposefs.so
%{_libdir}/pkgconfig/%{name}.pc

%files libs
%license COPYING COPYING.GPL-2.0-only COPYING.GPL-2.0-or-later COPYING.LGPL-2.1-or-later LICENSE.Apache-2.0
%{_libdir}/libcomposefs.so.*

%files
%license COPYING COPYING.GPL-2.0-only COPYING.GPL-2.0-or-later COPYING.LGPL-2.1-or-later LICENSE.Apache-2.0
%doc README.md
%{_bindir}/mkcomposefs
%{_bindir}/composefs-info
%{_sbindir}/mount.composefs
%if %{with man}
%{_mandir}/man*/*
%endif

%changelog
%autochangelog
