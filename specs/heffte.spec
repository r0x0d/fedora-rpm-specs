Name:           heffte
Version:        2.4.1
%global         sover 2
Release:        2%{?dist}
Summary:        Highly Efficient FFT for Exascale

License:        BSD-3-Clause
URL:            https://icl.utk.edu/fft/
Source0:        https://github.com/icl-utk-edu/heffte/archive/v%{version}/%{name}-%{version}.tar.gz

# no openmpi on ix86
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
# mpi is broken on s390x see, bug #2322073
ExcludeArch: %{ix86} s390x

BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  cmake >= 3.16
BuildRequires:  doxygen
BuildRequires:  openmpi-devel
BuildRequires:  mpich-devel
BuildRequires:  fftw-devel

%global heffte_desc \
The Highly Efficient FFT for Exascale (heFFTe) library is being developed \
as part of the Exascale Computing Project (ECP).  HeFFTe delivers algorithms \
for distributed fast-Fourier transforms in on a heterogeneous systems, \
targeting the upcoming exascale machines.

%description
%{heffte_desc}

%package openmpi
Summary:    Openmpi libraries for %{name}

%description openmpi
%{heffte_desc}

This package contains %{name} libraries compiled with openmpi.

%package openmpi-devel
Summary:    Openmpi development headers and libraries for %{name}
Requires:   %{name}-openmpi%{?_isa} = %{version}-%{release}
Requires:   openmpi-devel

%description openmpi-devel
%{heffte_desc}

This package contains openmpi development files of %{name}.

%package mpich
Summary:    Mpich libraries for %{name}

%description mpich
%{heffte_desc}

This package contains %{name} libraries compiled with mpich.

%package mpich-devel
Summary:    Mpich development headers and libraries for %{name}
Requires:   %{name}-mpich%{?_isa} = %{version}-%{release}
Requires:   mpich-devel

%description mpich-devel
%{heffte_desc}

This package contains mpich development files of %{name}.

%package examples
Summary:   Example file for %{name}
Requires:  (%{name}-openmpi-devel = %{version} or %{name}-mpich-devel = %{version})
BuildArch: noarch

%description examples
%{heffte_desc}

This package contains example files for %{name}.

%package doc
Summary:   Documentation for %{name}
Requires:  (%{name}-openmpi-devel = %{version} or %{name}-mpich-devel = %{version})
BuildArch: noarch

%description doc 
%{heffte_desc}

This package contains documentation for %{name}.

%prep
%autosetup -p1

%build
%global _vpath_builddir %{_target_platform}-${mpi}
export PRTE_MCA_rmaps_default_mapping_policy=:oversubscribe

for mpi in  mpich openmpi; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
  %cmake \
    -DHeffte_ENABLE_FFTW=ON \
    -DHeffte_ENABLE_FORTRAN=ON \
    -DHeffte_ENABLE_TESTING=ON \
    -DHeffte_ENABLE_DOXYGEN=ON \
    -DCMAKE_SKIP_INSTALL_RPATH=ON \
    -DHeffte_SEQUENTIAL_TESTING=ON \
    -DCMAKE_INSTALL_LIBDIR=${MPI_LIB:-%{_libdir}} \
    -DCMAKE_INSTALL_INCLUDEDIR=${MPI_INCLUDE:-%{_includedir}} \
    %{nil}
  %cmake_build
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done

%install
for mpi in mpich openmpi; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
  %cmake_install
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done

# files for testing install are not useful to package
rm -rf %{buildroot}%{_datadir}/%{name}/testing

%check
# allow openmpi to oversubscribe, i.e. runs test with more
# cores than the builder has
export PRTE_MCA_rmaps_default_mapping_policy=:oversubscribe

for mpi in mpich openmpi; do
  test -n "${mpi}" && module load mpi/${mpi}-%{_arch}
  %ctest %{?testargs}
  test -n "${mpi}" && module unload mpi/${mpi}-%{_arch}
done

%files openmpi
%doc README.md
%license LICENSE
%{_libdir}/openmpi*/lib/lib%{name}*.so.%{version}

%files openmpi-devel
%{_includedir}/openmpi*/%{name}*
%dir %{_includedir}/openmpi*/stock_fft
%{_includedir}/openmpi*/stock_fft/*.h
%{_libdir}/openmpi*/lib/cmake/Heffte
%{_libdir}/openmpi*/lib/lib%{name}*.so
%{_libdir}/openmpi*/lib/lib%{name}*.so.%{sover}

%files mpich
%doc README.md
%license LICENSE
%{_libdir}/mpich*/lib/lib%{name}*.so.%{version}

%files mpich-devel
%{_includedir}/mpich*/%{name}*
%dir %{_includedir}/mpich*/stock_fft
%{_includedir}/mpich*/stock_fft/*.h
%{_libdir}/mpich*/lib/cmake/Heffte
%{_libdir}/mpich*/lib/lib%{name}*.so
%{_libdir}/mpich*/lib/lib%{name}*.so.%{sover}

%files examples
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/examples
%{_datadir}/%{name}/HeffteMakefile.in

%files doc
%{_datadir}/%{name}/docs

%changelog
* Sun Dec 01 2024 Christoph Junghans <junghans@votca.org> - 2.4.1-2
- Comments from package review (bug #2321925)

* Fri Oct 25 2024 Christoph Junghans <junghans@votca.org> - 2.4.1-1
- Initial commit

