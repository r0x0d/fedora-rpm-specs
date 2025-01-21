Name:           tetgen
Version:        1.5.0
Release:        28%{?dist}
Summary:        A Quality Tetrahedral Mesh Generator

License:        AGPL-3.0-or-later
URL:            http://wias-berlin.de/software/tetgen/
Source0:        http://www.tetgen.org/1.5/src/%{name}%{version}.tar.gz
Source1:        http://www.tetgen.org/1.5/doc/manual/manual.pdf
# - Fix cmake file to build a shared library and support installation
# - Don't compile the entire code twice, once for the library and once for the
#   executable, but link the executable against the library instead
# - Split off main function to separate file
Patch0:         tetgen_build.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  make

%description
TetGen is a program to generate tetrahedral meshes of any 3D polyhedral
domains.
TetGen generates exact constrained Delaunay tetrahedralizations, boundary
conforming Delaunay meshes, and Voronoi partitions.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        doc
Summary:        Manual for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains the %{name} manual.


%prep
%autosetup -p1 -n%{name}%{version}
cp -a %{SOURCE1} .

# Fix line endings
sed -i 's|\r||g' example.poly


%build
%cmake
%cmake_build


%install
%cmake_install


%files
%doc README
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/libtet.so.*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/libtet.so

%files doc
%doc example.poly manual.pdf
%license LICENSE


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sun Aug 04 2024 Sandro Mani <manisandro@gmail.com> - 1.5.0-27
- Modernize spec

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-18
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Sandro Mani <manisandro@gmail.com> - 1.5.0-12
- Add missing BR: gcc-c++, make

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.5.0-5
- Rebuilt for GCC 5 C++11 ABI change

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 20 2014 Sandro Mani <manisandro@gmail.com> - 1.5.0-3
- Add doc subpackage

* Thu Jun 19 2014 Sandro Mani <manisandro@gmail.com> - 1.5.0-2
- Fix line endings of example.poly
- Fix libtet.so in main package
- Replace tetgen_cmake.patch with tetgen_build.patch

* Sat Jun 14 2014 Sandro Mani <manisandro@gmail.com> - 1.5.0-1
- Initial package
