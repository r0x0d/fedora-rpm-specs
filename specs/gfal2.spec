%undefine __cmake_in_source_build
%undefine __cmake3_in_source_build

# Require --with=tests in order to build functional tests
%bcond_with tests

Name:               gfal2
Version:            2.23.1
Release:            3%{?dist}
Summary:            Grid file access library 2.0
License:            Apache-2.0
URL:                https://dmc-docs.web.cern.ch/dmc-docs/gfal2/gfal2.html
# git clone --depth=1 --branch=v2.23.1 https://gitlab.cern.ch/dmc/gfal2.git gfal2-2.23.1
# tar czf gfal2-2.23.1.tar.gz --exclude-vcs gfal2-2.23.1
Source0:            %{name}-%{version}.tar.gz

#main lib dependencies
BuildRequires:      gcc-c++
BuildRequires:      cmake3
BuildRequires:      doxygen
BuildRequires:      json-c-devel
BuildRequires:      glib2-devel >= 2.28
Requires:           glib2 >= 2.28
BuildRequires:      libattr-devel
BuildRequires:      openldap-devel
BuildRequires:      pugixml-devel
BuildRequires:      libuuid-devel
#file plugin dependencies
BuildRequires:      zlib-devel
#srm plugin dependencies
BuildRequires:      srm-ifce-devel >= 1.23.1
#dcap plugin dependencies
BuildRequires:      dcap-devel
#gridftp plugin dependencies
BuildRequires:      globus-gass-copy-devel
#http plugin dependencies
BuildRequires:      davix-devel >= 0.8.4
BuildRequires:      cryptopp-devel >= 5.6.2
#xrootd plugin dependencies
BuildRequires:      xrootd-client-devel >= 1:5.0.0
# sftp plugin dependencies
BuildRequires:      libssh2-devel
#tests dependencies
BuildRequires:      gtest-devel

Obsoletes:          %{name}-core < %{version}-%{release}
Provides:           %{name}-core = %{version}-%{release}
Obsoletes:          %{name}-transfer < %{version}-%{release}
Provides:           %{name}-transfer = %{version}-%{release}

%description
GFAL 2.0 offers an a single and simple POSIX-like API
for the file operations in grids and cloud environments.
The set of supported protocols depends
of the %{name} installed plugins.

%package devel
Summary:            Development files of %{name}
Requires:           %{name}%{?_isa} = %{version}-%{release}
Requires:           glib2-devel%{?_isa}
Requires:           libattr-devel%{?_isa}
Requires:           pkgconfig

%description devel
development files for %{name}

%package doc
Summary:            Documentation for %{name}
BuildArch:          noarch

%description doc
Documentation, Doxygen and examples of %{name}.


%package plugin-file
Summary:            Provides file support for %{name}
Requires:           %{name}%{?_isa} = %{version}-%{release}

%description plugin-file
Provides the file support (file://) for %{name}.
The file plugin provides local file operations, as copying from local
to remote or the other way around.


%package plugin-dcap
Summary:            Provides the support access for %{name}
Requires:           %{name}%{?_isa} = %{version}-%{release}
Requires:           dcap-tunnel-gsi%{?_isa}

%description plugin-dcap
Provides the dcap support (gsidcap://, dcap://) for %{name}.
The dcap plugin provides the POSIX operations for the dcap \
URLs, the dcap protocol is used on the DCACHE storage system


%package plugin-srm
Summary:            Provides the srm access for %{name}
Requires:           %{name}%{?_isa} = %{version}-%{release}
Requires:           srm-ifce >= 1.23.1

%description plugin-srm
Provides the srm support (srm://) for %{name}.
The srm plugin provides the POSIX operations and
the third party transfer support on the SRM URLs.


%package plugin-gridftp
Summary:            Provides the gridftp support for %{name}
Requires:           %{name}%{?_isa} = %{version}-%{release}

%description plugin-gridftp
Provides the gridftp support (gsiftp://) for %{name}.
The gridftp plugin provides the POSIX operations and
the third party transfer support on the GSIFTP URLs.


%package plugin-http
Summary:            Provides the HTTP/DAV support for %{name}
Requires:           %{name}%{?_isa} = %{version}-%{release}
Requires:           davix-libs >= 0.8.4

%description plugin-http
Provides the HTTP (http[s]://) and WevDAV (dav[s]://) support for %{name}.
This plugin is able to do Third-Party Copy with WebDAV,
if the storage supports it.


%package plugin-xrootd
Summary:            Provide xrootd support for GFAL2
Requires:           %{name}%{?_isa} = %{version}-%{release}

%description plugin-xrootd
The Grid File Access Library, GFAL2, provides a simple POSIX-like API for file
operations in grid and cloud environments. Plug-ins are available to allow
access via a variety of protocols. This package contains a plugin for the
xrootd protocol (root://).


%package plugin-sftp
Summary:            Provide sftp support for GFAL2
Requires:           %{name}%{?_isa} = %{version}-%{release}

%description plugin-sftp
The Grid File Access Library, GFAL2, provides a simple POSIX-like API for file
operations in grid and cloud environments. Plug-ins are available to allow
access via a variety of protocols. This package contains a plugin for the
sftp protocol (sftp://).


%package plugin-mock
Summary:            Provides a Mock dummy protocol for %{name}
Requires:           %{name}%{?_isa} = %{version}-%{release}

%description plugin-mock
Provides a dummy mock:// protocol for %{name}.


%package all
Summary:            Meta package for GFAL 2.0 install
Requires:           %{name}%{?_isa} = %{version}-%{release}
Requires:           %{name}-plugin-file%{?_isa} = %{version}-%{release}
Requires:           %{name}-plugin-dcap%{?_isa} = %{version}-%{release}
Requires:           %{name}-plugin-srm%{?_isa} = %{version}-%{release}
Requires:           %{name}-plugin-gridftp%{?_isa} = %{version}-%{release}
Requires:           %{name}-plugin-http%{?_isa} = %{version}-%{release}
Requires:           %{name}-plugin-xrootd%{?_isa} = %{version}-%{release}
Requires:           %{name}-plugin-sftp%{?_isa} = %{version}-%{release}

%description all
Meta-package for complete install of GFAL2
with all the protocol plugins.

%package tests
Summary:            gfal2 tests
Requires:           gfal2-all%{?_isa} = %{version}-%{release}
Requires:           gfal2-plugin-mock%{?_isa} = %{version}-%{release}

%description tests
gfal2 tests

%clean
%cmake3_build --target clean

%prep
%autosetup

%build
# Make sure the version in the spec file and the version used
# for building matches
gfal2_cmake_ver=`sed -n 's/^set *(VERSION_\(MAJOR\|MINOR\|PATCH\) \+\([0-9]\+\).*/\2/p' CMakeLists.txt | paste -sd '.'`
gfal2_spec_ver=`expr "%{version}" : '\([0-9]*\\.[0-9]*\\.[0-9]*\)'`
if [ "$gfal2_cmake_ver" != "$gfal2_spec_ver" ]; then
    echo "The version in the spec file does not match the CMakeLists.txt version!"
    echo "$gfal2_cmake_ver != %{version}"
    exit 1
fi

%cmake3 \
    -DDOC_INSTALL_DIR=%{_pkgdocdir} \
    -DUNIT_TESTS=TRUE \
    -DPLUGIN_MOCK=TRUE \
    -DFUNCTIONAL_TESTS=%{?with_tests:ON}%{?!with_tests:OFF}

%cmake3_build
%cmake3_build --target doc

%install
%cmake3_install

%ldconfig_scriptlets

%files
%{_bindir}/gfal2_version
%{_libdir}/libgfal2.so.*
%{_libdir}/libgfal_transfer.so.*
%dir %{_libdir}/%{name}-plugins
%dir %{_sysconfdir}/%{name}.d
%config(noreplace) %{_sysconfdir}/%{name}.d/bdii.conf
%config(noreplace) %{_sysconfdir}/%{name}.d/gfal2_core.conf
%config(noreplace) %{_sysconfdir}/%{name}.d/x509.conf

%{_mandir}/man1/gfal2_version.1*
%dir %{_pkgdocdir}
%{_pkgdocdir}/DESCRIPTION
%{_pkgdocdir}/README.md
%{_pkgdocdir}/LICENSE
%{_pkgdocdir}/RELEASE-NOTES

%files devel
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/gfal2.pc
%{_libdir}/pkgconfig/gfal_transfer.pc
%{_libdir}/libgfal2.so
%{_libdir}/libgfal_transfer.so

%files doc
%{_pkgdocdir}/readme.html
%{_pkgdocdir}/html/
%{_pkgdocdir}/examples/

%files plugin-file
%{_libdir}/%{name}-plugins/libgfal_plugin_file.so*
%{_pkgdocdir}/README_PLUGIN_FILE

%files plugin-dcap
%{_libdir}/%{name}-plugins/libgfal_plugin_dcap.so*
%{_pkgdocdir}/README_PLUGIN_DCAP
%config(noreplace) %{_sysconfdir}/%{name}.d/dcap_plugin.conf

%files plugin-srm
%{_libdir}/%{name}-plugins/libgfal_plugin_srm.so*
%{_pkgdocdir}/README_PLUGIN_SRM
%config(noreplace) %{_sysconfdir}/%{name}.d/srm_plugin.conf

%files plugin-gridftp
%{_libdir}/%{name}-plugins/libgfal_plugin_gridftp.so*
%{_pkgdocdir}/README_PLUGIN_GRIDFTP
%config(noreplace) %{_sysconfdir}/%{name}.d/gsiftp_plugin.conf

%files plugin-http
%{_libdir}/%{name}-plugins/libgfal_plugin_http.so*
%{_pkgdocdir}/README_PLUGIN_HTTP
%config(noreplace) %{_sysconfdir}/%{name}.d/http_plugin.conf

%files plugin-xrootd
%{_libdir}/%{name}-plugins/libgfal_plugin_xrootd.so*
%{_pkgdocdir}/README_PLUGIN_XROOTD
%config(noreplace) %{_sysconfdir}/%{name}.d/xrootd_plugin.conf

%files plugin-sftp
%{_libdir}/%{name}-plugins/libgfal_plugin_sftp.so*
%{_pkgdocdir}/README_PLUGIN_SFTP
%config(noreplace) %{_sysconfdir}/%{name}.d/sftp_plugin.conf

%files plugin-mock
%{_libdir}/%{name}-plugins/libgfal_plugin_mock.so*
%{_pkgdocdir}/README_PLUGIN_MOCK
%config(noreplace) %{_sysconfdir}/%{name}.d/mock_plugin.conf

%files tests
%{_bindir}/gfal2-unit-tests
%{_libdir}/libgfal2_test_shared.so

%files all


%changelog
* Wed Jan 22 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 2.23.1-3
- Rebuilt for gtest 1.15.2

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.23.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Oct 23 2024 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 2.23.1-1
- Upstream release 2.23.1

* Fri Aug 02 2024 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 2.23.0-1
- Upstream release 2.23.0

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 2.22.2-3
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Apr 02 2024 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 2.22.2-1
- Upgrade to upstream release 2.22.2

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Dec 13 2023 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 2.22.1-1
- Upgrade to upstream release 2.22.1

* Tue Oct 31 2023 Terje Rosten <terje.rosten@ntnu.no> - 2.21.5-2
- Rebuild for gtest 1.14.0 (bugzilla #2228663)

* Tue Aug 08 2023 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 2.21.5-1
- Upgrade to upstream release 2.21.5

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.21.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 09 2023 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 2.21.4-2
- Patch to correctly find cryptopp dependency on 32-bit architectures

* Mon May 08 2023 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 2.21.4-1
- Upgrade to upstream release 2.21.4

* Mon Feb 20 2023 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 2.21.3-1
- Upgrade to upstream release 2.21.3
- Drop patches accepted upstream

* Tue Jan 24 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 2.21.2-3
- Rebuild for gtest 1.13.0 (close RHBZ#2163832)

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.21.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 13 2022 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 2.21.2-1
- Upgrade to upstream release 2.21.2

* Mon Oct 10 2022 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 2.21.1-1
- Upgrade to upstream release 2.21.1

* Mon Aug 15 2022 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 2.21.0-1
- Upgrade to upstream release 2.21.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 10 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.20.5-3
- Rebuild for new gtest

* Tue Jun 28 2022 Benjamin A. Beasley <code@musicinmybrain.net> - 2.20.5-2
- Rebuilt for gtest 1.12.0 (close RHBZ#2101746)

* Fri Mar 04 2022 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 2.20.5-1
- Upgrade to upstream release 2.20.5

* Tue Mar 01 2022 Mihai Patrascoiu <mihai.patrascoiu@cern.ch> - 2.20.4-1
- Upgrade to upstream release 2.20.4

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Aug 31 2021 Michal Simon <michal.simon@cern.ch> - 2.19.2-2
- Do not build SRM plug-in on Fedora platforms

* Tue Aug 31 2021 Michal Simon <michal.simon@cern.ch> - 2.19.2-1
- Upgrade to upstream release 2.19.2

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Björn Esser <besser82@fedoraproject.org> - 2.18.2-9
- Rebuild for versioned symbols in json-c

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 15 2020 Michal Simon <michal.simon@cern.ch> - 2.18.2-1
- Upgrade to upstream release 2.18.2

* Fri Nov 27 2020 Richard Shaw <hobbes1069@gmail.com> - 2.18.1-7
- Rebuild for pugixml 1.11.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 16 2020 Michal Simon <michal.simon@cern.ch> - 2.18.0-1
- Upgrade to upstream release 2.18.0

* Fri May 15 2020 Michal Simon <michal.simon@cern.ch> - 2.17.3-1
- Upgrade to upstream release 2.17.3

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 2.17.2-2
- Rebuild (json-c)

* Tue Feb 25 2020 Michal Simon <michal.simon@cern.ch> - 2.17.2-1
- Upgrade to upstream release 2.17.2

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 13 2019 Georgios Bitzes <georgios.bitzes at cern.ch> - 2.17.1-1
- Upgraded to upstream release 2.17.1

* Mon Oct 28 2019 Andrea Manzi <amanzi at cern.ch> - 2.17.0-1
- Upgraded to upstream release 2.17.0

* Mon Sep 02 2019 Andrea Manzi <amanzi at cern.ch> - 2.16.3-3
- stop builing LFC and RFIO plugins in Rawhide and F31

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Andrea Manzi <amanzi at cern.ch> - 2.16.3-1
- Upgraded to upstream release 2.16.3

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 01 2018 Andrea Manzi <amanzi at cern.ch> - 2.16.1-1
- Upgraded to upstream release 2.16.1

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Andrea Manzi <amanzi at cern.ch> - 2.15.5-2
- Upgraded to upstream release 2.15.5-2

* Thu Apr 05 2018 Andrea Manzi <amanzi at cern.ch> - 2.15.4-1
- Upgraded to upstream release 2.15.4

* Tue Mar 27 2018 Björn Esser <besser82@fedoraproject.org> - 2.15.3-2
- Rebuilt for libjson-c.so.4 (json-c v0.13.1) on fc28

* Mon Mar 12 2018 Andrea Manzi <amanzi at cern.ch> - 2.15.3-1
- Upgraded to upstream release 2.15.3

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 2.15.2-2
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Mon Feb 12 2018 Andrea Manzi <amanzi at cern.ch> - 2.15.2-1
- Upgraded to upstream release 2.15.2

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Andrea Manzi <amanzi at cern.ch> - 2.15.1-1
- Upgraded to upstream release 2.15.1

* Sun Dec 10 2017 Björn Esser <besser82@fedoraproject.org> - 2.14.2-4
- Rebuilt for libjson-c.so.3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Sun Jul 30 2017 Florian Weimer <fweimer@redhat.com> - 2.14.2-2
- Rebuild with binutils fix for ppc64le (#1475636)

* Thu Jul 27 2017 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.14.2-1
- Upgraded to upstream release 2.14.2

* Wed Jul 26 2017 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.14.1-1
- Upgraded to upstream release 2.14.1

* Mon May 29 2017 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.13.4-1
- Upgraded to upstream release 2.13.4
- Fix Fedora rpm checks

* Mon Apr 03 2017 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.13.3-1
- Upgraded to upstream release 2.13.3

* Mon Feb 20 2017 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.13.1-1
- Upgraded to upstream release 2.13.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 26 2017 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.12.3-3
- Remove trailing whitespaces on pkgconfig file

* Mon Nov 14 2016 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.12.3-2
- Enable build of mock plugin

* Thu Nov 10 2016 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.12.3-1
- Upgraded to upstream release 2.12.3

* Thu Sep 22 2016 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.12.2-1
- Upgraded to upstream release 2.12.2

* Tue Apr 19 2016 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.11.1-1
- Upgraded to upstream release 2.11.1

* Mon Mar 07 2016 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.11.0-1
- Upgraded to upstream release 2.11.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Dec 09 2015 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.10.3-1
- Upgraded to upstream release 2.10.3

* Fri Nov 06 2015 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.10.2-1
- Upgraded to upstream release 2.10.2

* Fri Jul 03 2015 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.9.3-1
- Upgraded to upstream release 2.9.3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 16 2015 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.9.1-1
- Upgraded to upstream release 2.9.1

* Mon Mar 02 2015 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.8.4-1
- Upgraded to upstream release 2.8.4

* Mon Jan 12 2015 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.8.1-1
- Upgraded to upstream release 2.8.1

* Mon Dec 15 2014 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.7.8-3
- Applied patch moving buffer to heap to avoid SIGSEGV when the stack size is limited

* Tue Dec 02 2014 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.7.8-2
- Patched a bug in a call to gfal2_set_error

* Mon Nov 17 2014 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.7.8-1
- Upstream backported fix for protocol honoring on SRM GET and PUT

* Mon Nov 10 2014 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.7.7-1
- Upgraded to upstream release 2.7.7

* Fri Nov 07 2014 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.7.6-1
- New upstream release

* Mon Sep 08 2014 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.6.8-6
- Patch to use lseek64 instead of lseek in the http plugin

* Thu Sep 04 2014 Orion Poplawski <orion@cora.nwra.com> - 2.6.8-5
- Rebuild for pugixml 1.4

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 11 2014 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.6.8-3
- Disable GridFTP session reuse by default (see LCGUTIL-448)

* Fri Aug 08 2014 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.6.8-2
- Patch for symbol that dissapeared in Davix

* Mon Jul 28 2014 Alejandro Alvarez Ayllon <aalvarez at cern.ch> - 2.6.8-1
- Release 2.6.8 of GFAL2

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 13 2014 Alejandro Alvarez <aalvarez at cern.ch> - 2.5.5-2
- Backported patch that fixes segfault on the SRM plugin when
  listing empty directories

* Wed Feb 26 2014 Adrien Devresse <adevress at cern.ch> - 2.5.5-1
- Release 2.5.5 of GFAL2

* Thu Dec 05 2013 Alejandro Alvarez <aalvarez at cern.ch> - 2.4.8-1
- Release 2.4.8 of GFAL2

* Mon Dec 02 2013 Alejandro Alvarez <aalvarez at cern.ch> - 2.4.7-1
- Release 2.4.7 of GFAL2

* Thu Nov 07 2013 Alejandro Alvarez <aalvarez at cern.ch> - 2.4.6-1
- Release 2.4.6 of GFAL 2

* Wed Oct 23 2013 Alejandro Alvarez <aalvarez at cern.ch> - 2.4.5-3
- Release 2.4.5 of GFAL 2

* Tue Jul 02 2013 Adrien Devresse <adevress at cern.ch> - 2.3.0-0
- Release 2.3.0 of GFAL 2.0

* Tue Apr 30 2013 Adrien Devresse <adevress at cern.ch> - 2.2.1-0
- export transfer plugin API ( needed for xrootd plugin )

* Mon Apr 29 2013 Michail Salichos <msalicho at cern.ch> - 2.2.0-5
- make all gridftp ops async to avoid stalling processes

* Fri Apr 26 2013 Michail Salichos <msalicho at cern.ch> - 2.2.0-4
- replace gass stat with gridftp stat

* Mon Apr 22 2013 Michail Salichos <msalicho at cern.ch> - 2.2.0-3
- change gridftp error string pattern to satisfy Griffin

* Wed Apr 10 2013 Michail Salichos <msalicho at cern.ch> - 2.2.0-2
- display turls in verbose mode, needed by fts3

* Mon Mar 25 2013 Michail Salichos <msalicho at cern.ch> - 2.2.0-1
- fix memory leaks in bringonline SRM op

* Wed Mar 20 2013 Adrien Devresse <adevress at cern.ch> - 2.2.0-0
- fix thread safety issue with gsiftp plugin
- add the bring online API
- support for the http plugin by default
- remove executable stack need
- remove openMP dependency
- add synchronous cancellation API
- add gsiftp performance marker timeout
- support for srm session reuse
- reduce memory footprint

* Fri Feb 22 2013 Adrien Devresse <adevress at cern.ch> - 2.1.6-0
- FTS 3.0 EMI 3 update
- minor fix on the cancel logic
- change the performance marker auto-cancel threading model
- change the performance marker default timeout value

* Mon Feb 11 2013 Adrien Devresse <adevress at cern.ch> - 2.1.5-0
- FTS 3.0 EMI 3 release sync
- include event hooks support
- include cancel logic support
- include performance marker auto-cancel for gsiftp
- include checksum timeout support for gsiftp
- include srm session re-use support

* Thu Jan 10 2013 Adrien Devresse <adevress at cern.ch> - 2.1.1-0
- fix a minor memory issue with the gfal_transfer stack
- fix a wrong error report problem with srm third party copy

* Wed Dec 05 2012 Adrien Devresse <adevress at cern.ch> - 2.1.0-2
- fix an issue this surl to turl resolution for SRM third party copy

* Fri Nov 30 2012 Adrien Devresse <adevress at cern.ch> - 2.1.0-0
- One-globus session system for gsiftp plugin ( FTS 3.0 need )
- correct a major issue with the gass attribute system in gsiftp plugin
- change the lfc set/get env var for a one compatible with set/get opt
- add set/nb streams option for gsiftp
- add the mkdir rec function for SRM transfer
- correct an issue with opendir and srm_ls ( ENOTDIR error silent )
- correct a memory leak in the cache system
- correct timeout support for gsiftp transfer
- implement tcp buffer size support for gsiftp layer
- apply a correction on the SRM over-write logic, related to a BeStMan errcode problem on File Not Found with srmRm ( EOS )
- apply a fix on the transfer gsiftp timeout ( protection against multiple cancel )
- fix for SRM filesize problem ( defined to 0, workaround ) related to globus 426 error bad filesize
- secure the callback system for globus gass timeout
- base implementation of the http plugin
- improve reliability of the bdii resolution
- add a fallback mechanism in case of bdii bad resolution
- correct several race conditions in the bdii layer
- add thread safe support for set/get variables in liblfc
- correct a deadlock problem with globus and gisftp plugin
- implement the mkdir_rec logic for general purpose
- implement the parent folder creation logic with gridftp
- add support for lfc://host/path URL style for the lfc plugin
- switch off_t to 64bits size by default ( _FILE_OFFSET_BITS=64)
- provide a "nobdii" like option
- provide the choice of turl protocol resolution for srm plugin

* Fri Jul 20 2012 Adrien Devresse <adevress at cern.ch> - 2.0.0-1
- Official initial release candidate of gfal 2.0
- Transfer API is official
- gridftp support for performance marker, checksum
- gridftp support for gridftpv2, dcau param
- SRM support for spacetoken in transfer
- SRM abort auto-management
- parallel operations in transfers
- file protocol dedicated in a plugin
- configuration file support
- srm timeout support
- general purpose checksum operation support
- POSIX operation support for gridftp
- cleaner plugin API
- new documentation
- I hope that you will enjoy gfal 2.0 :)

* Sat Jun 23 2012 Adrien Devresse <adevress at cern.ch> - 2.0.0-0.10.2012062323snap
- Snapshot of the 0.10 version for testing

* Fri Jun 15 2012 Adrien Devresse <adevress at cern.ch> - 2.0.0-0.9.2012061511snap
- Snapshot of the 0.9 version for testing

* Fri May 04 2012 Adrien Devresse <adevress at cern.ch> - 2.0.0-0.8.2012052812snap
- Snapshot of the 0.8 version for testing.

* Fri May 04 2012 Adrien Devresse <adevress at cern.ch> - 2.0.0-0.7.2012050413snap
- Improve gridftp plugin with severals other calls
- Correct dcap/rfio/srm bugs related to error report
- big work on the documentation

* Mon Dec 12 2011 Adrien Devresse <adevress at cern.ch> - 2.0.0-0.6.2012041515snap
- Initial gfal 2.0 preview release
