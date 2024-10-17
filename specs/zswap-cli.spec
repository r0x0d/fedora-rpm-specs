Name: zswap-cli
Version: 0.9.1
Release: %autorelease

License: MIT
Summary: Command-line tool to control zswap options
URL: https://github.com/xvitaly/%{name}
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: fmt-devel
BuildRequires: gcc-c++
BuildRequires: glibc-headers
BuildRequires: kernel-headers
BuildRequires: ninja-build
BuildRequires: pandoc
BuildRequires: semver-devel
BuildRequires: systemd

%{?systemd_requires}

%description
Zswap-cli is a command-line tool to control zswap Linux kernel module
options.

Zswap is a compressed cache for swap pages. It takes pages that are in the
process of being swapped out to disk and tries to compress them into a
RAM-based memory pool with dynamic allocation.

It trades CPU cycles for a significant performance boost since reading from
a compressed cache is much faster than reading from a swap device.

%prep
%autosetup

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_DOCS:BOOL=OFF \
    -DBUILD_MANPAGE:BOOL=ON \
    -DSYSTEMD_INTEGRATION:BOOL=ON
%cmake_build

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%install
%cmake_install

%files
%doc docs/*
%license LICENSE
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
%{_mandir}/man1/%{name}.*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf

%changelog
%autochangelog
