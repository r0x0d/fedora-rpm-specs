%global talloc_version 2.4.3

Name:           libtevent
Version:        0.16.2
Release:        %autorelease
Summary:        The tevent library
License:        LGPL-3.0-or-later
URL:            http://tevent.samba.org/
Source0:        http://samba.org/ftp/tevent/tevent-%{version}.tar.gz
Source1:        http://samba.org/ftp/tevent/tevent-%{version}.tar.asc
# gpg2 --no-default-keyring --keyring ./tevent.keyring --recv-keys 9147A339719518EE9011BCB54793916113084025
Source2:        tevent.keyring

# Patches

BuildRequires: docbook-style-xsl
BuildRequires: doxygen
BuildRequires: gcc
BuildRequires: gnupg2
BuildRequires: libcmocka-devel >= 1.1.3
BuildRequires: libtalloc-devel >= %{talloc_version}
BuildRequires: libxslt
BuildRequires: make
BuildRequires: python3-devel
BuildRequires: python3-talloc-devel >= %{talloc_version}

Provides: bundled(libreplace)
Obsoletes: python2-tevent < 0.10.0-1

%description
Tevent is an event system based on the talloc memory management library.
Tevent has support for many event types, including timers, signals, and
the classic file descriptor events.
Tevent also provide helpers to deal with asynchronous code providing the
tevent_req (Tevent Request) functions.

%package devel
Summary:        Developer tools for the Tevent library

Requires: libtevent%{?_isa} = %{version}-%{release}
Requires: libtalloc-devel%{?_isa} >= %{talloc_version}

%description devel
Header files needed to develop programs that link against the Tevent library.


%package -n python3-tevent
Summary:        Python 3 bindings for the Tevent library

Requires: libtevent%{?_isa} = %{version}-%{release}
%{?python_provide:%python_provide python3-tevent}

%description -n python3-tevent
Python 3 bindings for libtevent

%prep
zcat %{SOURCE0} | gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} -
%autosetup -n tevent-%{version} -p1

%build
%configure --disable-rpath \
           --bundled-libraries=NONE \
           --builtin-libraries=replace

%make_build

doxygen doxy.config

%check
%make_build check

%install
%make_install

# Install API docs
rm -f doc/man/man3/todo*
install -d -m0755 %{buildroot}%{_mandir}
cp -a doc/man/man3 %{buildroot}%{_mandir}

%files
%{_libdir}/libtevent.so.*

%files devel
%{_includedir}/tevent.h
%{_libdir}/libtevent.so
%{_libdir}/pkgconfig/tevent.pc
%{_mandir}/man3/tevent*.gz

%files -n python3-tevent
%{python3_sitearch}/tevent.py
%{python3_sitearch}/__pycache__/tevent.*
%{python3_sitearch}/_tevent.cpython*.so

%ldconfig_scriptlets

%changelog
%autochangelog
