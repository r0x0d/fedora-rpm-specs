%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

# No more Java on i686
%ifarch %{java_arches}
%bcond_without java
%else
%bcond_with java
%endif

# Patch version?
#global snaprel -beta

# NOTE: Try not to release new versions to released versions of Fedora
# You need to recompile all users of HDF5 for each version change
Name: hdf5
Version: 1.14.5
Release: 3%{?dist}
Summary: A general purpose library and file format for storing scientific data
License: BSD-3-Clause
URL: https://www.hdfgroup.org/solutions/hdf5/
Source0: https://github.com/HDFGroup/hdf5/archive/hdf5_%{version}/hdf5-%{version}.tar.gz

%global so_version 310

Source1: h5comp
# For man pages
Source2: http://ftp.us.debian.org/debian/pool/main/h/hdf5/hdf5_1.14.4.3+repack-1~exp3.debian.tar.xz
# Fix java build
Patch0: hdf5-build.patch
# Get size of __float128
# https://github.com/HDFGroup/hdf5/pull/4924
Patch1: hdf5-float128.patch
# Remove Fedora build flags from h5cc/h5c++/h5fc
# https://bugzilla.redhat.com/show_bug.cgi?id=1794625
Patch2: hdf5-wrappers.patch

BuildRequires: gcc-gfortran
%if %{with java}
BuildRequires: java-devel
BuildRequires: javapackages-tools
BuildRequires: hamcrest
BuildRequires: junit
BuildRequires: slf4j
%else
Obsoletes:     java-hdf5 < %{version}-%{release}
%endif
BuildRequires: krb5-devel
BuildRequires: openssl-devel
BuildRequires: time
BuildRequires: zlib-devel
BuildRequires: hostname
# For patches/rpath
BuildRequires: automake
BuildRequires: libtool
# Needed for mpi tests
BuildRequires: openssh-clients
BuildRequires: libaec-devel
BuildRequires: gcc, gcc-c++
BuildRequires: git-core

%global with_mpich %{undefined flatpak}
%if 0%{?fedora} >= 40
%ifarch %{ix86}
%global with_openmpi 0
%else
%global with_openmpi %{undefined flatpak}
%endif
%else
%global with_openmpi %{undefined flatpak}
%endif

%if %{with_mpich}
%global mpi_list mpich
%endif
%if %{with_openmpi}
%global mpi_list %{?mpi_list} openmpi
%endif

%description
HDF5 is a general purpose library and file format for storing scientific data.
HDF5 can store two primary objects: datasets and groups. A dataset is
essentially a multidimensional array of data elements, and a group is a
structure for organizing objects in an HDF5 file. Using these two basic
objects, one can create and store almost any kind of scientific data
structure, such as images, arrays of vectors, and structured and unstructured
grids. You can also mix and match them in HDF5 files according to your needs.


%package devel
Summary: HDF5 development files
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libaec-devel%{?_isa}
Requires: zlib-devel%{?_isa}
Requires: gcc-gfortran%{?_isa}

%description devel
HDF5 development headers and libraries.

%if %{with java}
%package -n java-hdf5
Summary: HDF5 java library
Requires:  slf4j
Obsoletes: jhdf5 < 3.3.2^

%description -n java-hdf5
HDF5 java library
%endif

%package static
Summary: HDF5 static libraries
Requires: %{name}-devel = %{version}-%{release}

%description static
HDF5 static libraries.


%if %{with_mpich}
%package mpich
Summary: HDF5 mpich libraries
BuildRequires: mpich-devel
Provides: %{name}-mpich2 = %{version}-%{release}
Obsoletes: %{name}-mpich2 < 1.8.11-4

%description mpich
HDF5 parallel mpich libraries


%package mpich-devel
Summary: HDF5 mpich development files
Requires: %{name}-mpich%{?_isa} = %{version}-%{release}
Requires: libaec-devel%{?_isa}
Requires: zlib-devel%{?_isa}
Requires: mpich-devel%{?_isa}
Provides: %{name}-mpich2-devel = %{version}-%{release}
Obsoletes: %{name}-mpich2-devel < 1.8.11-4

%description mpich-devel
HDF5 parallel mpich development files


%package mpich-static
Summary: HDF5 mpich static libraries
Requires: %{name}-mpich-devel%{?_isa} = %{version}-%{release}
Provides: %{name}-mpich2-static = %{version}-%{release}
Obsoletes: %{name}-mpich2-static < 1.8.11-4

%description mpich-static
HDF5 parallel mpich static libraries
%endif


%if %{with_openmpi}
%package openmpi
Summary: HDF5 openmpi libraries
BuildRequires: openmpi-devel
BuildRequires: make

%description openmpi
HDF5 parallel openmpi libraries


%package openmpi-devel
Summary: HDF5 openmpi development files
Requires: %{name}-openmpi%{?_isa} = %{version}-%{release}
Requires: libaec-devel%{?_isa}
Requires: zlib-devel%{?_isa}
Requires: openmpi-devel%{?_isa}

%description openmpi-devel
HDF5 parallel openmpi development files


%package openmpi-static
Summary: HDF5 openmpi static libraries
Requires: %{name}-openmpi-devel%{?_isa} = %{version}-%{release}

%description openmpi-static
HDF5 parallel openmpi static libraries
%endif


%prep
%autosetup -a 2 -n %{name}-%{name}_%{version} -p1


%build
%if %{with java}
# Replace jars with system versions
# hamcrest-core is obsoleted in hamcrest-2.2
# Junit tests are failing with junit-4.13.1
%if 0%{?rhel} >= 9 || 0%{?fedora}
find . ! -name junit.jar -name "*.jar" -delete
ln -s $(build-classpath hamcrest) java/lib/hamcrest-core.jar
%else
find . -name "*.jar" -delete
ln -s $(build-classpath hamcrest/core) java/lib/hamcrest-core.jar
ln -s $(build-classpath junit) java/lib/junit.jar
# Fix test output
junit_ver=$(sed -n '/<version>/{s/^.*>\([0-9]\.[0-9.]*\)<.*/\1/;p;q}' /usr/share/maven-poms/junit.pom)
sed -i -e "s/JUnit version .*/JUnit version $junit_ver/" java/test/testfiles/JUnit-*.txt
%endif
ln -s $(build-classpath slf4j/api) java/lib/slf4j-api-2.0.6.jar
ln -s $(build-classpath slf4j/nop) java/lib/ext/slf4j-nop-2.0.6.jar
ln -s $(build-classpath slf4j/simple) java/lib/ext/slf4j-simple-2.0.6.jar
%endif

# Force shared by default for compiler wrappers (bug #1266645)
sed -i -e '/^STATIC_AVAILABLE=/s/=.*/=no/' */*/h5[cf]*.in
sh ./autogen.sh

# Modify low optimization level for gnu compilers
sed -e 's|-O -finline-functions|-O3 -finline-functions|g' -i config/gnu-flags

#Do out of tree builds
%global _configure ../configure
#Common configure options
%global configure_opts \\\
  --disable-silent-rules \\\
  --enable-fortran \\\
  --enable-hl \\\
  --enable-shared \\\
  --with-szlib \\\
%{nil}
# --enable-cxx and --enable-parallel flags are incompatible
# --with-mpe=DIR Use MPE instrumentation [default=no]
# --enable-cxx/fortran/parallel and --enable-threadsafe flags are incompatible

#Serial build
export CC=gcc
export CXX=g++
export F9X=gfortran
export LDFLAGS="%{__global_ldflags} -fPIC -Wl,-z,now -Wl,--as-needed"
mkdir build
pushd build
ln -s ../configure .
%configure \
  %{configure_opts} \
  --enable-cxx \
%if %{with java}
  --enable-java \
%endif
  --with-default-plugindir=%{_libdir}/hdf5/plugin
sed -i -e 's| -shared | -Wl,--as-needed\0|g' libtool
sed -r -i 's|^prefix=/usr|prefix=%{buildroot}/usr|' java/test/junit.sh
%make_build LDFLAGS="%{__global_ldflags} -fPIC -Wl,-z,now -Wl,--as-needed"
popd

#MPI builds
export LDFLAGS="%{__global_ldflags} -fPIC -Wl,-z,now -Wl,--as-needed"
for mpi in %{?mpi_list}
do
  mkdir $mpi
  pushd $mpi
  module load mpi/$mpi-%{_arch}
  ln -s ../configure .
  %configure \
    %{configure_opts} \
    CC=mpicc CXX=mpicxx F9X=mpif90 \
    FCFLAGS="$FCFLAGS -I$MPI_FORTRAN_MOD_DIR" \
    --enable-parallel \
    --exec-prefix=%{_libdir}/$mpi \
    --libdir=%{_libdir}/$mpi/lib \
    --bindir=%{_libdir}/$mpi/bin \
    --sbindir=%{_libdir}/$mpi/sbin \
    --includedir=%{_includedir}/$mpi-%{_arch} \
    --datarootdir=%{_libdir}/$mpi/share \
    --mandir=%{_libdir}/$mpi/share/man \
    --with-default-plugindir=%{_libdir}/$mpi/hdf5/plugin
  sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool
  %make_build LDFLAGS="%{__global_ldflags} -fPIC -Wl,-z,now -Wl,--as-needed"
  module purge
  popd
done


%install
%make_install -C build
rm %{buildroot}%{_libdir}/*.la
# Fortran modules
mkdir -p %{buildroot}%{_fmoddir}
mv %{buildroot}%{_includedir}/*.mod %{buildroot}%{_fmoddir}
# Fix fortran module include dir https://bugzilla.redhat.com/show_bug.cgi?id=1971826
sed -i -e 's,%{_includedir},%{_fmoddir},' %{buildroot}%{_bindir}/h5fc
# Plugin directory
mkdir -p %{buildroot}%{_libdir}/hdf5/plugin
for mpi in %{?mpi_list}
do
  module load mpi/$mpi-%{_arch}
  %make_install -C $mpi
  rm %{buildroot}/%{_libdir}/$mpi/lib/*.la
  # Fortran modules
  mkdir -p %{buildroot}${MPI_FORTRAN_MOD_DIR}
  mv %{buildroot}%{_includedir}/${mpi}-%{_arch}/*.mod %{buildroot}${MPI_FORTRAN_MOD_DIR}/
  # Fix fortran module include dir https://bugzilla.redhat.com/show_bug.cgi?id=1971826
  sed -i -e "s,%{_includedir},${MPI_FORTRAN_MOD_DIR}," %{buildroot}%{_libdir}/$mpi/bin/h5pfc
  # Plugin directory
  mkdir -p %{buildroot}%{_libdir}/$mpi/hdf5/plugin
  module purge
done

#Fixup headers and scripts for multiarch
%ifarch x86_64 ppc64 ia64 s390x sparc64 alpha
sed -i -e s/H5pubconf.h/H5pubconf-64.h/ %{buildroot}%{_includedir}/H5public.h
mv %{buildroot}%{_includedir}/H5pubconf.h \
   %{buildroot}%{_includedir}/H5pubconf-64.h
for x in h5c++ h5cc h5fc
do
  mv %{buildroot}%{_bindir}/${x} \
     %{buildroot}%{_bindir}/${x}-64
  install -m 0755 %SOURCE1 %{buildroot}%{_bindir}/${x}
done
%else
sed -i -e s/H5pubconf.h/H5pubconf-32.h/ %{buildroot}%{_includedir}/H5public.h
mv %{buildroot}%{_includedir}/H5pubconf.h \
   %{buildroot}%{_includedir}/H5pubconf-32.h
for x in h5c++ h5cc h5fc
do
  mv %{buildroot}%{_bindir}/${x} \
     %{buildroot}%{_bindir}/${x}-32
  install -m 0755 %SOURCE1 %{buildroot}%{_bindir}/${x}
done
%endif
# rpm macro for version checking
mkdir -p %{buildroot}%{macrosdir}
cat > %{buildroot}%{macrosdir}/macros.hdf5 <<EOF
# HDF5 version is
%%_hdf5_version %{version}
EOF

# Install man pages from debian
mkdir -p %{buildroot}%{_mandir}/man1
cp -p debian/man/*.1 %{buildroot}%{_mandir}/man1/
rm %{buildroot}%{_mandir}/man1/*gif*
for mpi in %{?mpi_list}
do
  mkdir -p %{buildroot}%{_libdir}/$mpi/share/man/man1
  cp -p debian/man/h5p[cf]c.1 %{buildroot}%{_libdir}/$mpi/share/man/man1/
done
rm %{buildroot}%{_mandir}/man1/h5p[cf]c*.1

%if %{with java}
# Java
mkdir -p %{buildroot}%{_libdir}/%{name}
mv %{buildroot}%{_libdir}/libhdf5_java.so %{buildroot}%{_libdir}/%{name}/
%endif


%check
%ifarch %{ix86} ppc64le riscv64 s390x
# i686: t_bigio test segfaults - https://github.com/HDFGroup/hdf5/issues/2510
# ppc64le - t_multi_dset is flaky on ppc64le
# riscv64: test failed https://github.com/HDFGroup/hdf5/issues/4056
# s390x t_mpi fails with mpich
make -C build check || :
fail=0
%else
make -C build check
fail=1
%endif
# This will preserve generated .c files on errors if needed
#export HDF5_Make_Ignore=yes
export OMPI_MCA_rmaps_base_oversubscribe=1
# openmpi 5+
export PRTE_MCA_rmaps_default_mapping_policy=:oversubscribe
# mpich test is taking longer
export HDF5_ALARM_SECONDS=8000
for mpi in %{?mpi_list}
do
  # t_pmulti_dset hangs sometimes with mpich-aarch64 so do not test on that architecture
  # https://github.com/HDFGroup/hdf5/issues/3768
  if [ "$mpi-%{_arch}" != mpich-aarch64 ]
  then
    module load mpi/$mpi-%{_arch}
    make -C $mpi check || exit $fail
    module purge
  fi
done

# I have no idea why those get installed. But it's easier to just
# delete them, than to fight with the byzantine build system.
# And yes, it's using /usr/lib not %_libdir.
if [ %_libdir != /usr/lib ]; then
   rm -vf \
      %{buildroot}/usr/lib/*.jar \
      %{buildroot}/usr/lib/*.la  \
      %{buildroot}/usr/lib/*.lai \
      %{buildroot}/usr/lib/libhdf5*
fi


%files
%license COPYING
%doc ACKNOWLEDGMENTS README.md release_docs/RELEASE.txt
%{_bindir}/h5clear
%{_bindir}/h5copy
%{_bindir}/h5debug
%{_bindir}/h5diff
%{_bindir}/h5delete
%{_bindir}/h5dump
%{_bindir}/h5format_convert
%{_bindir}/h5fuse
%{_bindir}/h5import
%{_bindir}/h5jam
%{_bindir}/h5ls
%{_bindir}/h5mkgrp
%{_bindir}/h5perf_serial
%{_bindir}/h5repack
%{_bindir}/h5repart
%{_bindir}/h5stat
%{_bindir}/h5unjam
%{_bindir}/h5watch
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/plugin/
%{_libdir}/libhdf5.so.%{so_version}*
%{_libdir}/libhdf5_cpp.so.%{so_version}*
%{_libdir}/libhdf5_fortran.so.%{so_version}*
%{_libdir}/libhdf5hl_fortran.so.%{so_version}*
%{_libdir}/libhdf5_hl.so.%{so_version}*
%{_libdir}/libhdf5_hl_cpp.so.%{so_version}*
%{_mandir}/man1/h5copy.1*
%{_mandir}/man1/h5diff.1*
%{_mandir}/man1/h5dump.1*
%{_mandir}/man1/h5import.1*
%{_mandir}/man1/h5jam.1*
%{_mandir}/man1/h5ls.1*
%{_mandir}/man1/h5mkgrp.1*
%{_mandir}/man1/h5perf_serial.1*
%{_mandir}/man1/h5repack.1*
%{_mandir}/man1/h5repart.1*
%{_mandir}/man1/h5stat.1*
%{_mandir}/man1/h5unjam.1*

%files devel
%{macrosdir}/macros.hdf5
%{_bindir}/h5c++*
%{_bindir}/h5cc*
%{_bindir}/h5fc*
%{_bindir}/h5redeploy
%{_includedir}/*.h
%{_includedir}/*.inc
%{_libdir}/*.so
%{_libdir}/*.settings
%{_fmoddir}/*.mod
%{_mandir}/man1/h5c++.1*
%{_mandir}/man1/h5cc.1*
%{_mandir}/man1/h5debug.1*
%{_mandir}/man1/h5fc.1*
%{_mandir}/man1/h5redeploy.1*

%files static
%{_libdir}/*.a

%if %{with java}
%files -n java-hdf5
%{_jnidir}/hdf5.jar
%{_libdir}/%{name}/*
%endif

%if %{with_mpich}
%files mpich
%license COPYING
%doc README.md release_docs/RELEASE.txt
%{_libdir}/mpich/bin/h5clear
%{_libdir}/mpich/bin/h5copy
%{_libdir}/mpich/bin/h5debug
%{_libdir}/mpich/bin/h5delete
%{_libdir}/mpich/bin/h5diff
%{_libdir}/mpich/bin/h5dump
%{_libdir}/mpich/bin/h5format_convert
%{_libdir}/mpich/bin/h5fuse
%{_libdir}/mpich/bin/h5import
%{_libdir}/mpich/bin/h5jam
%{_libdir}/mpich/bin/h5ls
%{_libdir}/mpich/bin/h5mkgrp
%{_libdir}/mpich/bin/h5redeploy
%{_libdir}/mpich/bin/h5repack
%{_libdir}/mpich/bin/h5perf
%{_libdir}/mpich/bin/h5perf_serial
%{_libdir}/mpich/bin/h5repart
%{_libdir}/mpich/bin/h5stat
%{_libdir}/mpich/bin/h5unjam
%{_libdir}/mpich/bin/h5watch
%{_libdir}/mpich/bin/ph5diff
%{_libdir}/mpich/%{name}/
%{_libdir}/mpich/lib/*.so.%{so_version}*

%files mpich-devel
%{_includedir}/mpich-%{_arch}
%{_fmoddir}/mpich/*.mod
%{_libdir}/mpich/bin/h5pcc
%{_libdir}/mpich/bin/h5pfc
%{_libdir}/mpich/lib/lib*.so
%{_libdir}/mpich/lib/lib*.settings
%{_libdir}/mpich/share/man/man1/h5pcc.1*
%{_libdir}/mpich/share/man/man1/h5pfc.1*

%files mpich-static
%{_libdir}/mpich/lib/*.a
%endif

%if %{with_openmpi}
%files openmpi
%license COPYING
%doc README.md release_docs/RELEASE.txt
%{_libdir}/openmpi/bin/h5clear
%{_libdir}/openmpi/bin/h5copy
%{_libdir}/openmpi/bin/h5debug
%{_libdir}/openmpi/bin/h5delete
%{_libdir}/openmpi/bin/h5diff
%{_libdir}/openmpi/bin/h5dump
%{_libdir}/openmpi/bin/h5format_convert
%{_libdir}/openmpi/bin/h5fuse
%{_libdir}/openmpi/bin/h5import
%{_libdir}/openmpi/bin/h5jam
%{_libdir}/openmpi/bin/h5ls
%{_libdir}/openmpi/bin/h5mkgrp
%{_libdir}/openmpi/bin/h5perf
%{_libdir}/openmpi/bin/h5perf_serial
%{_libdir}/openmpi/bin/h5redeploy
%{_libdir}/openmpi/bin/h5repack
%{_libdir}/openmpi/bin/h5repart
%{_libdir}/openmpi/bin/h5stat
%{_libdir}/openmpi/bin/h5unjam
%{_libdir}/openmpi/bin/h5watch
%{_libdir}/openmpi/bin/ph5diff
%{_libdir}/openmpi/%{name}/
%{_libdir}/openmpi/lib/*.so.%{so_version}*

%files openmpi-devel
%{_includedir}/openmpi-%{_arch}
%{_fmoddir}/openmpi/*.mod
%{_libdir}/openmpi/bin/h5pcc
%{_libdir}/openmpi/bin/h5pfc
%{_libdir}/openmpi/lib/lib*.so
%{_libdir}/openmpi/lib/lib*.settings
%{_libdir}/openmpi/share/man/man1/h5pcc.1*
%{_libdir}/openmpi/share/man/man1/h5pfc.1*

%files openmpi-static
%{_libdir}/openmpi/lib/*.a
%endif


%changelog
* Mon Jan 20 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jan 03 2025 Orion Poplawski <orion@nwra.com> - 1.14.5-2
- Fix ownership of %%{_libdir}/hdf5

* Wed Oct 02 2024 Orion Poplawski <orion@nwra.com> - 1.14.3-1
- Update to 1.14.5
- Use SPDX License tag

* Mon Sep  2 2024 Miroslav Suchý <msuchy@redhat.com> - 1.12.1-21
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 29 2024 Liu Yang <Yang.Liu.sn@gmail.com> - 1.12.1-19
- Disable failed tests for riscv64.

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.12.1-18
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 29 2023 Orion Poplawski <orion@nwra.com> - 1.12.1-15
- Rebuild for openmpi 5.0.0, drops support for i686

* Sat Aug 26 2023 Orion Poplawski <orion@nwra.com> - 1.12.1-14
- Apply upstream fix for CVE-2021-37501 buffer overflow in h5dump

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Apr 11 2023 Florian Weimer <fweimer@redhat.com> - 1.12.1-12
- Apply upstream patch to fix C99 compatibility issue

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 10 2022 Orion Poplawski <orion@nwra.com> - 1.12.1-9
- Drop java for i686 (bz#2104046)

* Sat Jun 25 2022 Orion Poplawski <orion@nwra.com> - 1.12.1-8
- Define and create default plugin directory

* Mon May  9 2022 Orion Poplawski <orion@nwra.com> - 1.12.1-7
- Fix fortran module include dir in h5fc (bz#1971826)

* Sun Feb 27 2022 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.12.1-6
- Bump obsoleted jdfh5 version to be above F35

* Tue Feb 08 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.12.1-5
- Rebuilt for java-17-openjdk as system jdk (again)

* Mon Feb 07 2022 Orion Poplawski <orion@nwra.com> - 1.12.1-4
- Add patch to fix build with gfortran-12

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.12.1-3
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Nov 20 2021 Orion Poplawski <orion@nwra.com> - 1.12.1-1
- Update to 1.12.1

* Mon Aug 30 2021 Orion Poplawski <orion@nwra.com> - 1.10.7-2
- Fix typo in h5fc (bz#1998879)

* Mon Aug 09 2021 Orion Poplawski <orion@nwra.com> - 1.10.7-1
- Update to 1.10.7

* Thu Jul 29 2021 Antonio Trande <sagitter@fedoraproject.org> - 1.10.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild
- Use bundled junit
- Fix hamcrest symlinks in Fedora 35+

* Sun May 30 2021 Orion Poplawski <orion@nwra.com> - 1.10.6-6
- Handle junit versions better

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Oct 14 2020 Orion Poplawski <orion@nwra.com> - 1.10.6-4
- Drop MPI tests for now - hanging
- Build openmpi for EL s390x again

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 1.10.6-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jun 25 2020 Orion Poplawski <orion@nwra.com> - 1.10.6-1
- Update to 1.10.6

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 26 2020 Orion Poplawski <orion@nwra.com> - 1.10.5-5
- Remove Fedora build flags from h5cc/h5c++/h5fc (bz#1794625)

* Mon Nov 11 2019 Orion Poplawski <orion@nwra.com> - 1.10.5-4
- Add upstream patch to fix 32-bit java tests

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Apr  6 2019 Orion Poplawski <orion@nwra.com> - 1.10.5-2
- Enable java

* Sat Mar 16 2019 Orion Poplawski <orion@nwra.com> - 1.10.5-1
- Update to 1.10.5

* Thu Feb 14 2019 Orion Poplawski <orion@nwra.com> - 1.8.20-6
- Rebuild for openmpi 3.1.3

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.20-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 23 2018 Antonio Trande <sagitter@fedoraproject.com> - 1.8.20-3
- Force default ldflags for Fedora (bz#1548533)
- Switch -shared flag to -Wl,--as-needed
- Modify low optimization level for gnu compilers
- New URL

* Tue Feb 20 2018 Antonio Trande <sagitter@fedoraproject.com> - 1.8.20-2
- Devel package with full versioned dependency
- Use %%make_install

* Wed Feb 7 2018 Orion Poplawski <orion@nwra.com> - 1.8.20-1
- Update to 1.8.20

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.18-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Feb 02 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.8.18-13
- Switch to %%ldconfig_scriptlets

* Wed Jan 31 2018 Orion Poplawski <orion@cora.nwra.com> - 1.8.18-12
- Rebuild for gfortran-8

* Fri Sep 08 2017 Dan Horák <dan[at]danny.cz> - 1.8.18-11
- fix the compiler wrapper - s390x is 64-bit (#1489954)

* Wed Aug 16 2017 Orion Poplawski <orion@cora.nwra.com> - 1.8.18-10
- Bump for rebuild

* Wed Aug 16 2017 Orion Poplawski <orion@nwra.com> - 1.8.18-9
- Make hdf5-devel require libaec

* Sun Aug 06 2017 Christoph Junghans <junghans@votca.org> - 1.8.18-8
- enable szip support through libaec

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.18-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.18-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Feb 05 2017 Kalev Lember <klember@redhat.com> - 1.8.18-5
- Enable testsuite again now that gcc fixes have landed

* Wed Feb 01 2017 Björn Esser <me@besser82.io> - 1.8.18-4
- Ignore testsuite on PPC64LE until GCC-7 is fixed

* Sat Jan 28 2017 Björn Esser <besser82@fedoraproject.org> - 1.8.18-4
- Rebuilt for GCC-7

* Fri Dec 30 2016 Orion Poplawski <orion@cora.nwra.com> - 1.8.18-3
- Install MPI Fortran module into proper location (bug #1409229)
- Use %%license

* Thu Dec 8 2016 Dan Horák <dan[at]danny.cz> - 1.8.18-2
- Enable openmpi for s390(x) on F>=26

* Mon Dec 5 2016 Orion Poplawski <orion@cora.nwra.com> - 1.8.18-1
- Update to 1.8.18
- Add patch to fix build with -Werror=implicit-function-declaration

* Fri Oct 21 2016 Orion Poplawski <orion@cora.nwra.com> - 1.8.17-2
- Rebuild for openmpi 2.0

* Wed Jun 29 2016 Orion Poplawski <orion@cora.nwra.com> - 1.8.17-1
- Update to 1.8.17

* Sun Mar 20 2016 Orion Poplawski <orion@cora.nwra.com> - 1.8.16-4
- Add patch to properly call MPI_Finalize() in t_pflush1

* Wed Mar 2 2016 Orion Poplawski <orion@cora.nwra.com> - 1.8.16-3
- Make hdf5-mpich-devel require mpich-devel (bug #1314091)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 20 2015 Orion Poplawski <orion@cora.nwra.com> - 1.8.16-1
- Update to 1.8.16

* Fri Nov 20 2015 Orion Poplawski <orion@cora.nwra.com> - 1.8.15-9.patch1
- Use MPI_FORTRAN_MOD_DIR to locate MPI Fortran module

* Fri Sep 25 2015 Orion Poplawski <orion@cora.nwra.com> - 1.8.15-8.patch1
- Force shared by default for compiler wrappers (bug #1266645)

* Tue Sep 15 2015 Orion Poplawski <orion@cora.nwra.com> - 1.8.15-7.patch1
- Rebuild for openmpi 1.10.0

* Sat Aug 15 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.8.15-6.patch1
- Rebuild for MPI provides

* Sun Jul 26 2015 Sandro Mani <manisandro@gmail.com> - 1.8.15-5.patch1
- Rebuild for RPM MPI Requires Provides Change

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.15-4.patch1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 8 2015 Orion Poplawski <orion@cora.nwra.com> - 1.8.15-3.patch1
- Update to 1.8.15-patch1

* Fri Jun 05 2015 Dan Horák <dan[at]danny.cz> - 1.8.15-2
- drop unnecessary patch, issue seems fixed with gcc5

* Sat May 16 2015 Orion Poplawski <orion@cora.nwra.com> - 1.8.15-1
- Update to 1.8.15

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.8.14-4
- Rebuilt for GCC 5 C++11 ABI change

* Wed Mar 11 2015 Orion Poplawski <orion@cora.nwra.com> - 1.8.14-3
- Rebuild for mpich 3.1.4 soname change

* Mon Feb 16 2015 Orion Poplawski <orion@cora.nwra.com> - 1.8.14-2
- Rebuild for gcc 5 fortran module

* Tue Jan 6 2015 Orion Poplawski <orion@cora.nwra.com> - 1.8.14-1
- Update to 1.8.14

* Wed Sep 3 2014 Orion Poplawski <orion@cora.nwra.com> - 1.8.13-7
- No longer build with -O0, seems to be working

* Wed Aug 27 2014 Orion Poplawski <orion@cora.nwra.com> - 1.8.13-6
- Rebuild for openmpi Fortran ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.13-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 27 2014 Orion Poplawski <orion@cora.nwra.com> - 1.8.13-4
- Make build work if not building any mpi pacakges (bug #1113610)

* Fri Jun 27 2014 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 1.8.13-3
- Drop gnu-config patches replaced by %%configure macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 15 2014 Orion Poplawski <orion@cora.nwra.com> - 1.8.13-1
- Update to 1.8.13

* Mon Mar 24 2014 Orion Poplawski <orion@cora.nwra.com> - 1.8.12-6
- Add patch to add ppc64le to config.guess (bug #1080122)

* Wed Mar 19 2014 Orion Poplawski <orion@cora.nwra.com> - 1.8.12-5
- Add patch to fix long double conversions on ppc64le (bug #1078173)
- Run autoreconf for patches and to remove rpaths

* Sat Feb 22 2014 Deji Akingunola <dakingun@gmail.com> - 1.8.12-4
- Rebuild for mpich-3.1

* Fri Jan 31 2014 Orion Poplawski <orion@cora.nwra.com> 1.8.12-4
- Fix rpm macros install dir

* Wed Jan 29 2014 Orion Poplawski <orion@cora.nwra.com> 1.8.12-3
- Fix rpm/macros.hdf5 generation (bug #1059161)

* Wed Jan 8 2014 Orion Poplawski <orion@cora.nwra.com> 1.8.12-2
- Update debian source
- Add patch for aarch64 support (bug #925545)

* Fri Dec 27 2013 Orion Poplawski <orion@cora.nwra.com> 1.8.12-1
- Update to 1.8.12

* Fri Aug 30 2013 Dan Horák <dan[at]danny.cz> - 1.8.11-6
- disable parallel tests on s390(x)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jul 20 2013 Deji Akingunola <dakingun@gmail.com> - 1.8.11-4
- Rename mpich2 sub-packages to mpich and rebuild for mpich-3.0

* Thu Jul 11 2013 Orion Poplawski <orion@cora.nwra.com> 1.8.11-3
- Rebuild for openmpi 1.7.2

* Fri Jun 7 2013 Orion Poplawski <orion@cora.nwra.com> 1.8.11-2
- Add man pages from debian (bug #971551)

* Wed May 15 2013 Orion Poplawski <orion@cora.nwra.com> 1.8.11-1
- Update to 1.8.11

* Mon Mar 11 2013 Ralf Corsépius <corsepiu@fedoraproject.org> - 1.8.10-3
- Remove %%config from %%{_sysconfdir}/rpm/macros.*
  (https://fedorahosted.org/fpc/ticket/259).

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 14 2012 Orion Poplawski <orion@cora.nwra.com> 1.8.10-1
- Update to 1.8.10
- Rebase LD_LIBRARY_PATH patch
- Drop ph5diff patch fixed upstream

* Mon Nov 12 2012 Peter Robinson <pbrobinson@fedoraproject.org> 1.8.9-5
- Enable openmpi support on ARM as we now have it

* Mon Nov 5 2012 Orion Poplawski <orion@cora.nwra.com> 1.8.9-4
- Rebuild for fixed openmpi f90 soname

* Thu Nov 1 2012 Orion Poplawski <orion@cora.nwra.com> 1.8.9-3
- Rebuild for openmpi and mpich2 soname bumps

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 15 2012 Orion Poplawski <orion@cora.nwra.com> 1.8.9-1
- Update to 1.8.9

* Mon Feb 20 2012 Dan Horák <dan[at]danny.cz> 1.8.8-9
- use %%{mpi_list} also for tests

* Wed Feb 15 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.8.8-8
- disable openmpi for ARM as we currently don't have it

* Fri Feb 10 2012 Orion Poplawski <orion@cora.nwra.com> 1.8.8-7
- Add patch to fix parallel mpi tests
- Add patch to fix bug in parallel h5diff

* Sat Jan 7 2012 Orion Poplawski <orion@cora.nwra.com> 1.8.8-6
- Enable Fortran 2003 support (bug 772387)

* Wed Dec 21 2011 Dan Horák <dan[at]danny.cz> 1.8.8-5
- reintroduce the tstlite patch for ppc64 and s390x

* Thu Dec 01 2011 Caolán McNamara <caolanm@redhat.com> 1.8.8-4
- Related: rhbz#758334 hdf5 doesn't build on ppc64

* Fri Nov 25 2011 Orion Poplawski <orion@cora.nwra.com> 1.8.8-3
- Enable static MPI builds

* Wed Nov 16 2011 Orion Poplawski <orion@cora.nwra.com> 1.8.8-2
- Add rpm macro %%{_hdf5_version} for convenience

* Tue Nov 15 2011 Orion Poplawski <orion@cora.nwra.com> 1.8.8-1
- Update to 1.8.8
- Drop tstlite patch
- Add patch to avoid setting LD_LIBRARY_PATH

* Wed Jun 01 2011 Karsten Hopp <karsten@redhat.com> 1.8.7-2
- drop ppc64 longdouble patch, not required anymore

* Tue May 17 2011 Orion Poplawski <orion@cora.nwra.com> 1.8.7-1
- Update to 1.8.7

* Tue Mar 29 2011 Deji Akingunola <dakingun@gmail.com> - 1.8.6-2
- Rebuild for mpich2 soname bump

* Fri Feb 18 2011 Orion Poplawski <orion@cora.nwra.com> 1.8.6-1
- Update to 1.8.6-1
- Update tstlite patch - not fixed yet

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.5.patch1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 6 2011 Orion Poplawski <orion@cora.nwra.com> 1.8.5.patch1-7
- Add Requires: zlib-devel to hdf5-devel

* Sun Dec 12 2010 Dan Horák <dan[at]danny.cz> 1.8.5.patch1-6
- fully conditionalize MPI support

* Wed Dec 8 2010 Orion Poplawski <orion@cora.nwra.com> 1.8.5.patch1-5
- Add EL6 compatibility - no mpich2 on ppc64

* Wed Oct 27 2010 Orion Poplawski <orion@cora.nwra.com> 1.8.5.patch1-4
- Really fixup all permissions

* Wed Oct 27 2010 Orion Poplawski <orion@cora.nwra.com> 1.8.5.patch1-3
- Add docs to the mpi packages
- Fixup example source file permissions

* Tue Oct 26 2010 Orion Poplawski <orion@cora.nwra.com> 1.8.5.patch1-2
- Build parallel hdf5 packages for mpich2 and openmpi
- Rework multiarch support and drop multiarch patch

* Tue Sep 7 2010 Orion Poplawski <orion@cora.nwra.com> 1.8.5.patch1-1
- Update to 1.8.5-patch1

* Wed Jun 23 2010 Orion Poplawski <orion@cora.nwra.com> 1.8.5-4
- Re-add rebased tstlite patch - not fixed yet

* Wed Jun 23 2010 Orion Poplawski <orion@cora.nwra.com> 1.8.5-3
- Update longdouble patch for 1.8.5

* Wed Jun 23 2010 Orion Poplawski <orion@cora.nwra.com> 1.8.5-2
- Re-add longdouble patch on ppc64 for EPEL builds

* Mon Jun 21 2010 Orion Poplawski <orion@cora.nwra.com> 1.8.5-1
- Update to 1.8.5
- Drop patches fixed upstream

* Mon Mar 1 2010 Orion Poplawski <orion@cora.nwra.com> 1.8.4.patch1-1
- Update to 1.8.4-patch1

* Wed Jan 6 2010 Orion Poplawski <orion@cora.nwra.com> 1.8.4-1
- Update to 1.8.4
- Must compile with -O0 due to gcc-4.4 incompatability
- No longer need -fno-strict-aliasing

* Thu Oct 1 2009 Orion Poplawski <orion@cora.nwra.com> 1.8.3-3.snap12
- Update to 1.8.3-snap12
- Update signal patch
- Drop detect and filter-as-option patch fixed upstream
- Drop ppc only patch
- Add patch to skip tstlite test for now, problem reported upstream
- Fixup some source file permissions

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 2 2009 Orion Poplawski <orion@cora.nwra.com> 1.8.3-1
- Update to 1.8.3
- Update signal and detect patches
- Drop open patch fixed upstream

* Sat Apr 18 2009 Karsten Hopp <karsten@redhat.com> 1.8.2-1.1
- fix s390x builds, s390x is 64bit, s390 is 32bit

* Mon Feb 23 2009 Orion Poplawski <orion@cora.nwra.com> 1.8.2-1
- Update to 1.8.2
- Add patch to compile H5detect without optimization - make detection
  of datatype characteristics more robust - esp. long double
- Update signal patch
- Drop destdir patch fixed upstream
- Drop scaleoffset patch
- Re-add -fno-strict-aliasing
- Keep settings file needed for -showconfig (bug #481032)
- Wrapper script needs to pass arguments (bug #481032)

* Wed Oct 8 2008 Orion Poplawski <orion@cora.nwra.com> 1.8.1-3
- Add sparc64 to 64-bit conditionals

* Fri Sep 26 2008 Orion Poplawski <orion@cora.nwra.com> 1.8.1-2
- Add patch to filter -little as option used on sh arch (#464052)

* Thu Jun 5 2008 Orion Poplawski <orion@cora.nwra.com> 1.8.1-1
- Update to 1.8.1

* Tue May 27 2008 Orion Poplawski <orion@cora.nwra.com> 1.8.1-0.rc1.1
- Update to 1.8.1-rc1

* Tue May 13 2008 Orion Poplawski <orion@cora.nwra.com> 1.8.0.snap5-2
- Use new %%{_fmoddir} macro
- Re-enable ppc64, disable failing tests.  Failing tests are for
  experimental long double support.

* Mon May 5 2008 Orion Poplawski <orion@cora.nwra.com> 1.8.0.snap5-1
- Update to 1.8.0-snap5
- Remove --enable-threadsafe, incompatible with --enable-cxx and
  --enable-fortran
- ExcludeArch ppc64 until we can get it to build (bug #445423)

* Tue Mar 4 2008 Orion Poplawski <orion@cora.nwra.com> 1.8.0-2
- Remove failing test for now

* Fri Feb 29 2008 Orion Poplawski <orion@cora.nwra.com> 1.8.0-1
- Update to 1.8.0, drop upstreamed patches
- Update signal patch
- Move static libraries into -static sub-package
- Make -devel multiarch (bug #341501)

* Wed Feb  6 2008 Orion Poplawski <orion@cora.nwra.com> 1.6.6-7
- Add patch to fix strict-aliasing
- Disable production mode to enable debuginfo

* Tue Feb  5 2008 Orion Poplawski <orion@cora.nwra.com> 1.6.6-6
- Add patch to fix calling free() in H5PropList.cpp

* Tue Feb  5 2008 Orion Poplawski <orion@cora.nwra.com> 1.6.6-5
- Add patch to support s390 (bug #431510)

* Mon Jan  7 2008 Orion Poplawski <orion@cora.nwra.com> 1.6.6-4
- Add patches to support sparc (bug #427651)

* Tue Dec  4 2007 Orion Poplawski <orion@cora.nwra.com> 1.6.6-3
- Rebuild against new openssl

* Fri Nov 23 2007 Orion Poplawski <orion@cora.nwra.com> 1.6.6-2
- Add patch to build on alpha (bug #396391)

* Wed Oct 17 2007 Orion Poplawski <orion@cora.nwra.com> 1.6.6-1
- Update to 1.6.6, drop upstreamed patches
- Explicitly set compilers

* Fri Aug 24 2007 Orion Poplawski <orion@cora.nwra.com> 1.6.5-9
- Update license tag to BSD
- Rebuild for BuildID

* Wed Aug  8 2007 Orion Poplawski <orion@cora.nwra.com> 1.6.5-8
- Fix memset typo
- Pass mode to open with O_CREAT

* Mon Feb 12 2007 Orion Poplawski <orion@cora.nwra.com> 1.6.5-7
- New project URL
- Add patch to use POSIX sort key option
- Remove useless and multilib conflicting Makefiles from html docs
  (bug #228365)
- Make hdf5-devel own %%{_docdir}/%%{name}

* Tue Aug 29 2006 Orion Poplawski <orion@cora.nwra.com> 1.6.5-6
- Rebuild for FC6

* Wed Mar 15 2006 Orion Poplawski <orion@cora.nwra.com> 1.6.5-5
- Change rpath patch to not need autoconf
- Add patch for libtool on x86_64
- Fix shared lib permissions

* Mon Mar 13 2006 Orion Poplawski <orion@cora.nwra.com> 1.6.5-4
- Add patch to avoid HDF setting the compiler flags

* Mon Feb 13 2006 Orion Poplawski <orion@cora.nwra.com> 1.6.5-3
- Rebuild for gcc/glibc changes

* Wed Dec 21 2005 Orion Poplawski <orion@cora.nwra.com> 1.6.5-2
- Don't ship h5perf with missing library

* Wed Dec 21 2005 Orion Poplawski <orion@cora.nwra.com> 1.6.5-1
- Update to 1.6.5

* Wed Dec 21 2005 Orion Poplawski <orion@cora.nwra.com> 1.6.4-9
- Rebuild

* Wed Nov 30 2005 Orion Poplawski <orion@cora.nwra.com> 1.6.4-8
- Package fortran files properly
- Move compiler wrappers to devel

* Fri Nov 18 2005 Orion Poplawski <orion@cora.nwra.com> 1.6.4-7
- Add patch for fortran compilation on ppc

* Wed Nov 16 2005 Orion Poplawski <orion@cora.nwra.com> 1.6.4-6
- Bump for new openssl

* Tue Sep 20 2005 Orion Poplawski <orion@cora.nwra.com> 1.6.4-5
- Enable fortran since the gcc bug is now fixed

* Tue Jul 05 2005 Orion Poplawski <orion@cora.nwra.com> 1.6.4-4
- Make example scripts executable

* Wed Jun 29 2005 Orion Poplawski <orion@cora.nwra.com> 1.6.4-3
- Add --enable-threads --with-pthreads to configure
- Add %%check
- Add some %%docs
- Use %%makeinstall
- Add patch to fix test for h5repack
- Add patch to fix h5diff_attr.c

* Mon Jun 27 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.6.4-2
- remove szip from spec, since szip license doesn't meet Fedora standards

* Sun Apr 3 2005 Tom "spot" Callaway <tcallawa@redhat.com> 1.6.4-1
- inital package for Fedora Extras
