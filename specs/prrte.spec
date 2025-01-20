Name:           prrte
Version:        3.0.6
Release:        2%{?dist}
Summary:        PMIx Reference RunTime Environment (PRRTE)
# src/mca/prtereachable/netlink/reachable_netlink_utils_common.c is BSD-2-Clause
# -devel related licenses:
# src/docs/show-help-files/_build/text/_static/jquery.js is MIT
# docs/_build/html/_static/js/html5shiv.min.js is MIT OR GPL-2.0-or-later
# docs/_build/html/_static/css/fonts/* are (OFL-1.1 OR MIT)
License:        BSD-3-Clause-Open-MPI AND BSD-2-Clause
URL:            https://github.com/openpmix/%{name}
Source0:        https://github.com/openpmix/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.bz2
# Upstream fix for --stdfor for non-zeron ranks - fixes rhbz#2307533
Patch0:         https://patch-diff.githubusercontent.com/raw/openpmix/prrte/pull/2038.patch

BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  hwloc-devel
BuildRequires:  libevent-devel
BuildRequires:  pmix-devel >= 4.2.2
# For pmixcc - https://bugzilla.redhat.com/show_bug.cgi?id=2078048
BuildRequires:  pmix-tools
BuildRequires:  perl-interpreter
BuildRequires:  torque-devel
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

# openmpi, pmix no longer support 32-bit platforms
ExcludeArch:    %{ix86}

%description
PRRTE is the PMIx Reference Run Time Environment.

The project is formally referred to in documentation by "PRRTE", and
the GitHub repository is "openpmix/%{name}".

However, we have found that most users do not like typing the two
consecutive "r"s in the name. Hence, all of the internal API symbols,
environment variables, MCA frameworks, and CLI executables all use the
abbreviated "prte" (one "r", not two) for convenience.


%package        libs
Summary:        Libraries for %{name}

%description    libs
Runtime libraries for %{name}.


%package        devel
Summary:        Development files for %{name}
License:        BSD-3-Clause-Open-MPI AND BSD-2-Clause AND MIT AND (MIT OR GPL-2.0-or-later) AND (OFL-1.1 OR MIT)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-%{version}

# touch lexer sources to recompile them
find src -name \*.l -print -exec touch --no-create {} \;

# Remove “BSD with advertising” licensed qsort implementation, which was only
# needed to work around ancient Solaris bugs. The typedef keeps the translation
# unit from being empty.
echo '' > src/util/qsort.h
echo 'typedef int x;' > src/util/qsort.c


%build
%configure \
    --sysconfdir=%{_sysconfdir}/prte \
    --disable-static \
    --disable-silent-rules \
    --enable-shared \
    --with-sge

%make_build


%install
%make_install
# Move to openmpi dir to avoid conflict with putty
mkdir -p %{buildroot}%{_libdir}/openmpi/{bin,share/man}
mv %{buildroot}%{_bindir}/* %{buildroot}%{_libdir}/openmpi/bin
mv %{buildroot}%{_mandir}/* %{buildroot}%{_libdir}/openmpi/share/man/

# remove libtool archives
find %{buildroot} -name '*.la' -delete


%check
%make_build check


%files
%doc README.md
%{_libdir}/openmpi/bin/prte
%{_libdir}/openmpi/bin/prte_info
%{_libdir}/openmpi/bin/prted
%{_libdir}/openmpi/bin/prterun
%{_libdir}/openmpi/bin/prun
%{_libdir}/openmpi/bin/pterm
%{_libdir}/openmpi/share/man/man1/*.1*
%{_libdir}/openmpi/share/man/man5/*.5*

%files libs
%license LICENSE
%dir %{_sysconfdir}/prte
%config(noreplace) %{_sysconfdir}/prte/*
%{_datadir}/prte/
%{_libdir}/lib%{name}.so.3*
%dir %{_libdir}/prte/
%{_libdir}/prte/prte_mca_plm_tm.so

%files devel
%{_libdir}/openmpi/bin/pcc
%{_docdir}/prrte/
%{_includedir}/prte*.h
%{_includedir}/prte/
%{_libdir}/lib%{name}.so


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Oct 20 2024 Orion Poplawski <orion@nwra.com> - 3.0.6-1
- Update to 3.0.6
- Add upstream fix for rhbz#2307533

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed May 15 2024 Orion Poplawski <orion@nwra.com> - 3.0.2-5
- Move binaries and man pages into openmpi path to avoid conclicting with putty
  (bz#2247407)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Nov 07 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 3.0.2-2
- Drop obsolete pandoc dependency

* Fri Oct 27 2023 Orion Poplawski <orion@nwra.com> - 3.0.2-1
- Update to 3.0.2

* Mon Sep 25 2023 Michel Lind <salimma@fedoraproject.org> - 2.0.2-5
- Rebuild for pmix 4.1.3

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Apr 23 2022 Orion Poplawski <orion@nwra.com> - 2.0.2-1
- Update to 2.0.2

* Mon Jan 24 2022 Orion Poplawski <orion@nwra.com> - 2.0.0-5
- Add explicit BR on hwloc-devel and libevent-devel

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Oct 31 2021 Orion Poplawski <orion@nwra.com> - 2.0.0-3
- Explicitly list binaries

* Thu Oct 28 2021 Orion Poplawski <orion@nwra.com> - 2.0.0-2
- Split libraries into -libs sub-package
- Add BR make
- Remove old qsort

* Mon Oct 11 2021 Orion Poplawski <orion@nwra.com> - 2.0.0-1
- Initial Fedora package
