Name:       onnx
Version:    1.17.0
Release:    3%{?dist}
Summary:    Open standard for machine learning interoperability
License:    Apache-2.0

URL:        https://github.com/onnx/onnx
Source0:    https://github.com/onnx/onnx/archive/v%{version}/%{name}-%{version}.tar.gz
# Build shared libraries and fix install location 
Patch0:     0000-Build-shared-libraries-and-fix-install-location.patch
# Use system protobuf and require parameterized
Patch2:     0002-Use-system-protobuf-and-require-parameterized.patch
# Let pyproject_wheel use binaries from cmake_build
Patch3:     0003-Let-pyproject_wheel-use-binaries-from-cmake_build.patch
# Add fixes for use with onnxruntime
Patch4:     0004-Add-fixes-for-use-with-onnxruntime.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=2212096
ExcludeArch:    s390x
%if %{undefined fc40} && %{undefined fc41}
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}
%endif

BuildRequires:  cmake >= 3.13
BuildRequires:  make
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  zlib-devel
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-pybind11
BuildRequires:  python3-pytest
BuildRequires:  protobuf-devel

%global _description %{expand:
%{name} provides an open source format for AI models, both deep learning and
traditional ML. It defines an extensible computation graph model, as well as
definitions of built-in operators and standard data types.}

%description %_description

%package libs
Summary:    Libraries for %{name}

%description libs %_description

%package devel
Summary:    Development files for %{name}
Requires:   %{name}-libs = %{version}-%{release} 

%description devel %_description

%package -n python3-onnx
Summary:    %{summary}
Requires:   %{name}-libs = %{version}-%{release}

%description -n python3-onnx %_description

%prep
%autosetup -p1 -n onnx-%{version}

# Use system protobuf
sed -r -i 's/protobuf>=3.20.2/protobuf>=3.14.0/' pyproject.toml

# Drop nbval options from pytest. Plugin is not available in Fedora.
sed -r \
    -e 's/--nbval //' \
    -e 's/--nbval-current-env //' \
    -i pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -t requirements-reference.txt

%build
%cmake \
    -DONNX_USE_LITE_PROTO=OFF \
    -DONNX_USE_PROTOBUF_SHARED_LIBS=ON \
    -DBUILD_ONNX_PYTHON=ON \
    -DPYTHON_EXECUTABLE=%{python3} \
    -DPY_EXT_SUFFIX=%{python3_ext_suffix} \
    -DPY_SITEARCH=%{python3_sitearch} \
    -DCMAKE_SKIP_RPATH:BOOL=ON
# Generate protobuf header and source files
%cmake_build -- gen_onnx_proto
# Build 
%cmake_build
# Build python libs
%pyproject_wheel

%install
%cmake_install
# Need to remove empty directories
find "%{buildroot}/%{_includedir}" -type d -empty -delete
find "%{buildroot}/%{python3_sitearch}" -type d -empty -delete
# Install *.proto files
install -p "./onnx/"*.proto -t "%{buildroot}/%{_includedir}/onnx/"

%pyproject_install
%pyproject_save_files onnx

%check
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}
%pytest

%files libs
%license LICENSE
%doc README.md
%{_libdir}/libonnx.so.%{version}
%{_libdir}/libonnx_proto.so.%{version}

%files devel
%{_libdir}/libonnx.so
%{_libdir}/libonnx_proto.so
%{_libdir}/cmake/ONNX
%{_includedir}/%{name}/

%files -n python3-onnx -f %{pyproject_files}
%{_bindir}/backend-test-tools
%{_bindir}/check-model
%{_bindir}/check-node

%changelog
* Sat Jan 18 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 1.17.0-3
- Drop i686 support (leaf package on that architecture)

* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Oct 25 2024 Sandro <devel@penguinpee.nl> - 1.17.0-1
- Update to 1.17.0 (RHBZ#2235011)
- Add support for NumPy 2.x

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 02 2024 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 1.15.0-3
- Backport of fix for CVE-2024-5187

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 1.15.0-2
- Rebuilt for Python 3.13

* Thu Apr 11 2024 Diego Herrera C <dherrera@redhat.com> - 1.15.0-1
- Release 1.15.0

* Sat Feb 24 2024 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 1.14.1-2
- Backport of fixes for CVE-2024-27318 and CVE-2024-27319

* Wed Feb 21 2024 Diego Herrera C <dherrera@redhat.com>- 1.14.1-1
- Release 1.14.1

* Tue Jan 23 2024 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 1.14.0-10
- Build using protobuf-devel

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Sep 20 2023 Diego Herrera C <dherrera@redhat.com> - 1.14.0-8
- Fix onnxruntime patch

* Wed Aug 30 2023 Diego Herrera C <dherrera@redhat.com> - 1.14.0-7
- Add fix to use with onnxruntime

* Sat Aug 5 2023 Diego Herrera C <dherrera@redhat.com> - 1.14.0-6
- Lower version requirement for parameterized.
- Lower version requirement for protobuf.

* Sat Aug 5 2023 Diego Herrera C <dherrera@redhat.com> - 1.14.0-5
- Build python libs using the proper macros.

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.14.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 19 2023 Python Maint <python-maint@redhat.com> - 1.14.0-3
- Rebuilt for Python 3.12

* Wed Jun 07 2023 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 1.14.0-2
- Patch protobuf headers with ONNX_API
- Ship .proto files

* Sat Jun 03 2023 Alejandro Alvarez Ayllon <a.alvarezayllon@gmail.com> - 1.14.0-1
- Release 1.14.0

* Thu May 18 2023 Diego Herrera <dherrera@redhat.com> - 1.13.0-3
- Fix License entry to comply with SPDX
- Add onnx-libs as an explicit dependency to the python package

* Sat Dec 17 2022 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 1.13.0-2
- Release 1.13.0

* Wed Nov 23 2022 Alejandro Alvarez Ayllon <aalvarez@fedoraproject.org> - 1.12.0-1
- Release 1.12.0
