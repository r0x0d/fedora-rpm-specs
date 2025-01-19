%{!?luaver: %global luaver %(lua -e "print(string.sub(_VERSION, 5))" || echo 0)}
%global luapkgdir %{_datadir}/lua/%{luaver}

%global luacompatver 5.1
%global luacompatpkgdir %{_datadir}/lua/%{luacompatver}

%global luapkgname http

Name:           lua-%{luapkgname}
Version:        0.3
Release:        16%{?dist}
Summary:        HTTP library for Lua

License:        MIT
URL:            https://github.com/daurnimator/lua-http
Source0:        https://github.com/daurnimator/lua-http/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

Patch1:         0001-rst_closed.patch
Patch2:         0002-throw_kill_connection.patch

BuildRequires:  lua
BuildRequires:  pandoc
BuildRequires: make

Requires:       lua-basexx >= 0.2.0
Requires:       lua-binaryheap >= 0.3
Requires:       lua-fifo
Requires:       lua-luaossl >= 20161208
Requires:       lua-lpeg
Requires:       lua-lpeg-patterns >= 0.5
Requires:       lua-cqueues >= 20171014
%if 0%{?rhel} && 0%{?rhel} <= 7
Requires:       lua-bitop
Requires:       lua-compat53
%endif

%description
lua-http is an efficient, capable HTTP and WebSocket library for Lua.

%if 0%{?fedora} || 0%{?rhel} > 7
%package -n lua%{luacompatver}-%{luapkgname}
Summary:        HTTP library for Lua
Requires:       lua%{luacompatver}-basexx >= 0.2.0
Requires:       lua%{luacompatver}-binaryheap >= 0.3
Requires:       lua%{luacompatver}-bitop
Requires:       lua%{luacompatver}-compat53 >= 0.3
Requires:       lua%{luacompatver}-fifo
Requires:       lua%{luacompatver}-luaossl >= 20161208
Requires:       lua%{luacompatver}-lpeg
Requires:       lua%{luacompatver}-lpeg-patterns >= 0.5
Requires:       lua%{luacompatver}-cqueues >= 20171014

%description -n lua%{luacompatver}-%{luapkgname}
lua-http is an efficient, capable HTTP and WebSocket library for Lua %{luacompatver}.
%endif

%package doc
Summary:        Documentation for HTTP library for Lua
Requires:       %{name} = %{version}
%if 0%{?fedora} || 0%{?rhel} > 7
Requires:       lua%{luacompatver}-%{luapkgname} = %{version}
%endif

%description doc
Documentation for the HTTP library for Lua.

%prep
%setup -q -n %{name}-%{version}
%patch -P1 -p1
%patch -P2 -p1

%build
pushd doc
%make_build lua-http.html lua-http.3
popd

%install
install -d -m 0755 "%{buildroot}%{_pkgdocdir}"
install -p -m 0644 doc/lua-http.html "%{buildroot}%{_pkgdocdir}/index.html"
install -D -p -m 0644 doc/lua-http.3 "%{buildroot}%{_mandir}/man3/lua-http.3"

install -d -m 0755 %{buildroot}%{luapkgdir}/%{luapkgname}
install -p -m 0644 %{luapkgname}/*.lua -t "%{buildroot}%{luapkgdir}/%{luapkgname}/"
install -d -m 0755 %{buildroot}%{luapkgdir}/%{luapkgname}/compat
install -p -m 0644 %{luapkgname}/compat/*.lua -t "%{buildroot}%{luapkgdir}/%{luapkgname}/compat/"

%if 0%{?fedora} || 0%{?rhel} > 7
install -d -m 0755 %{buildroot}%{luacompatpkgdir}/%{luapkgname}
install -p -m 0644 %{luapkgname}/*.lua -t "%{buildroot}%{luacompatpkgdir}/%{luapkgname}/"
install -d -m 0755 %{buildroot}%{luacompatpkgdir}/%{luapkgname}/compat
install -p -m 0644 %{luapkgname}/compat/*.lua -t "%{buildroot}%{luacompatpkgdir}/%{luapkgname}/compat/"
%endif

%files
%{_mandir}/man3/lua-http.3*
%license LICENSE.md
%{luapkgdir}/%{luapkgname}

%if 0%{?fedora} || 0%{?rhel} > 7
%files -n lua%{luacompatver}-%{luapkgname}
%{_mandir}/man3/lua-http.3*
%license LICENSE.md
%{luacompatpkgdir}/%{luapkgname}
%endif

%files doc
%{_pkgdocdir}
%doc %{_pkgdocdir}/index.html

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 07 2020 Tomas Krizek - 0.3-5
- Fix lua-http-doc dependency (rhbz#1832456)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 17 2019 Tomas Krizek <tomas.krizek@nic.cz> - 0.3-2
- Add missing dependencies for EPEL 7

* Tue Apr 09 2019 Tomas Krizek <tomas.krizek@nic.cz> - 0.3-1
- Initial package for Fedora 28+ and EPEL 7+
