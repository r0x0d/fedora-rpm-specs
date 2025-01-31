%global commit       b1ae9c96a2244184aa8c0e1303e3bcc1e8d78117
%global shortcommit  %(c=%{commit}; echo ${c:0:7})
%global commitdate   20240602
Name:    blogc
Version: 0.20.1^%{commitdate}.%{shortcommit}
Release: 1%{?dist}
# All code is BSD-3-Clause except src/common/utf8.c which is MIT
License: BSD-3-Clause AND MIT
Summary: A blog compiler

URL:     https://blogc.rgm.io/
VCS:     git:https://github.com/blogc/blogc.git
Source0: blogc.tar.gz
# Need Git files for build version from a commit
Source1: getsource.sh
# https://github.com/blogc/blogc/pull/17
Patch0:   https://github.com/blogc/blogc/pull/17.patch#/getaddrinfo.patch
# https://github.com/blogc/blogc/pull/18
Patch1:   https://github.com/blogc/blogc/pull/18.patch#/mitlicense.patch

BuildRequires: bash
BuildRequires: cmake
BuildRequires: coreutils
BuildRequires: diffutils
BuildRequires: gcc
BuildRequires: git-core
BuildRequires: libcmocka-devel
BuildRequires: rubygem-ronn-ng
BuildRequires: tar

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%description
blogc(1) is a blog compiler. It compiles source files and templates into
blog/website resources.

%package git-receiver
Summary: A simple login shell/git hook to deploy blogc websites
Requires: git-core
Requires: make
Requires: tar
Requires: %{name}-make%{?_isa} = %{version}-%{release}

%description git-receiver
blogc-git-receiver is a simple login shell/git hook to deploy blogc websites.

%package make
Summary: A simple build tool for blogc
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-runserver%{?_isa} = %{version}-%{release}

%description make
blogc-make is a simple build tool for blogc websites.

%package runserver
Summary: A simple HTTP server to test blogc websites

%description runserver
blogc-runserver is a simple HTTP server to test blogc websites.

%prep
%autosetup  -n blogc -p 1

%build
%cmake -DBUILD_BLOGC_GIT_RECEIVER=ON \
       -DBUILD_BLOGC_MAKE=ON \
       -DBUILD_BLOGC_RUNSERVER=ON \
       -DBUILD_MANPAGES=ON \
       -DBUILD_TESTING=ON \
       -DCMAKE_C_COMPILER=gcc
%cmake_build


%install
%cmake_install

%check
%ctest

%files
%{_mandir}/man*/blogc.*
%{_mandir}/man*/blogc-source.*
%{_mandir}/man*/blogc-template.*
%{_mandir}/man*/blogc-toctree.*
%{_mandir}/man*/blogc-pagination.*
%{_bindir}/blogc
%doc README.md
%license LICENSE

%files git-receiver
%{_mandir}/man*/blogc-git-receiver.*
%{_bindir}/blogc-git-receiver
%license LICENSE

%files make
%{_mandir}/man*/blogc-make.*
%{_mandir}/man*/blogcfile.*
%{_bindir}/blogc-make
%license LICENSE

%files runserver
%{_mandir}/man*/blogc-runserver.*
%{_bindir}/blogc-runserver
%license LICENSE

%changelog
* Thu Jan 16 2025 Benson Muite <fed500@fedoraproject.org> 0.20.1^20240602.b1ae9c9-1
- Prepare for Fedora packaging

* Sat Jan 02 2021 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.20.1-1
- New release.

* Tue Sep 15 2020 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.20.0-1
- New release.

* Sun May 31 2020 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.19.0-1
- New release.

* Tue Sep 10 2019 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.18.0-1
- New release.

* Thu May 2 2019 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.17.0-1
- New release.

* Sun Apr 21 2019 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.16.1-1
- New release.

* Sat Apr 13 2019 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.16.0-1
- New release.

* Tue Feb 26 2019 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.15.1-1
- New release.

* Mon Feb 11 2019 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.15.0-1
- New release.

* Tue Jan 15 2019 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.14.1-1
- New release.

* Thu Jul 26 2018 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.14.0-1
- New release.

* Sun Jul 22 2018 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.13.10-1
- New release.

* Tue Jun 12 2018 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.13.9-1
- New release.

* Sun Jun 10 2018 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.13.8-1
- New release.

* Sun Jun 10 2018 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.13.7-1
- New release.

* Mon May 14 2018 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.13.6-1
- New release.

* Sun May 13 2018 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.13.5-1
- New release.

* Tue Mar 20 2018 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.13.4-1
- New release.

* Wed Mar 14 2018 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.13.3-1
- New release.

* Mon Mar 12 2018 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.13.2-1
- New release.

* Thu Feb 22 2018 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.13.1-1
- New release.

* Sun Nov 19 2017 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.13.0-1
- New release.

* Sun Oct 30 2016 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.12.0-1
- New release.

* Sun Jul 17 2016 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.11.1-1
- New release.

* Tue Jul 5 2016 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.11.0-1
- New release.

* Thu Jun 30 2016 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.10.2-1
- New release.

* Sun Jun 19 2016 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.10.1-1
- New release.

* Mon May 30 2016 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.10.0-1
- New release.

* Sat Apr 30 2016 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.9.0-1
- New release. Merged blogc-git-receiver and blogc-runserver.

* Sun Apr 17 2016 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.8.1-1
- New release.

* Wed Apr 6 2016 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.8.0-1
- New release.

* Mon Feb 29 2016 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.7.6-1
- New release. Added new dependency.

* Sun Feb 21 2016 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.7.5-1
- New release.

* Sun Feb 21 2016 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.7.4-1
- New release.

* Sat Feb 20 2016 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.7.3-1
- New release.

* Mon Jan 25 2016 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.7.2-1
- New release.

* Fri Jan 22 2016 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.7.1-1
- New release.

* Thu Jan 14 2016 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.7-1
- New release.

* Sun Jan 10 2016 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.6.1-1
- New release.

* Thu Jan 07 2016 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.6-1
- New release.

* Thu Dec 03 2015 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.5.1-1
- New release.

* Thu Nov 05 2015 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.5-1
- New release.

* Sun Oct 25 2015 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.4-1
- New release.

* Fri Oct 16 2015 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.3-1
- New release.

* Thu Oct 08 2015 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.2.1-1
- New release.

* Wed Sep 16 2015 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.1-1
- First stable release.

* Mon Sep 14 2015 Rafael G. Martins <rafael@rafaelmartins.eng.br> 0.1-0.1.beta4
- Initial package.
