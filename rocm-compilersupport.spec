# The package follows LLVM's major version, but API version is still important:
%global comgr_maj_api_ver 2
%global comgr_full_api_ver %{comgr_maj_api_ver}.8.0
# Upstream tags are based on rocm releases:
%global rocm_release 6.2
%global rocm_patch 1
%global rocm_version %{rocm_release}.%{rocm_patch}
# What LLVM is upstream using (use LLVM_VERSION_MAJOR from llvm/CMakeLists.txt):
%global llvm_maj_ver 18
#Use compat if LLVM is not latest:
%bcond_with compat_build
%global upstreamname llvm-project

# Used to tell cmake where to install device libs (must be relative to prefix)
# We want to install to clang_resource_dir/amdgcn for FHS compliance
%global amd_device_libs_prefix lib/clang/%{llvm_maj_ver}

%global toolchain clang

Name:           rocm-compilersupport
Version:        %{llvm_maj_ver}
Release:        7.rocm%{rocm_version}%{?dist}
Summary:        Various AMD ROCm LLVM related services

Url:            https://github.com/ROCm/llvm-project
# hipcc is MIT, comgr and device-libs are NCSA:
License:        NCSA and MIT
Source0:        https://github.com/ROCm/%{upstreamname}/archive/refs/tags/rocm-%{rocm_version}.tar.gz#/%{name}-%{rocm_version}.tar.gz

# This requires a patch that's only landed in llvm 19+:
# https://github.com/ROCm/llvm-project/commit/669db884972e769450470020c06a6f132a8a065b
Patch0:         0001-Revert-ockl-Don-t-use-wave32-ballot-builtin.patch
# Upstream LLVM 18 doesn't have GFX1152 yet
Patch1:         0001-Revert-GFX11-Add-a-new-target-gfx1152.patch
# -mlink-builtin-bitcode-postopt is not supported
Patch2:         0001-remove-mlink.patch

BuildRequires:  cmake
%if 0%{?fedora}
BuildRequires:  fdupes
%endif
BuildRequires:  libffi-devel
BuildRequires:  perl
BuildRequires:  perl-generators
BuildRequires:  zlib-devel

BuildRequires:  clang-devel(major) = %{llvm_maj_ver}
BuildRequires:  lld-devel(major) = %{llvm_maj_ver}
BuildRequires:  llvm-devel(major) = %{llvm_maj_ver}

#Only the following architectures are useful for ROCm packages:
ExclusiveArch:  x86_64 aarch64 ppc64le

%description
%{summary}

%package macros
Summary:        ROCm Compiler RPM macros

%description macros
This package contains ROCm compiler related RPM macros.

%package -n rocm-device-libs
Summary:        AMD ROCm LLVM bit code libraries
Requires:       clang-devel(major) = %{llvm_maj_ver}
Requires:       clang-resource-filesystem(major) = %{llvm_maj_ver}
Requires:       lld-devel(major) = %{llvm_maj_ver}
Requires:       llvm-devel(major) = %{llvm_maj_ver}

%description -n rocm-device-libs
This package contains a set of AMD specific device-side language runtime
libraries in the form of bit code. Specifically:
 - Open Compute library controls
 - Open Compute Math library
 - Open Compute Kernel library
 - OpenCL built-in library
 - HIP built-in library
 - Heterogeneous Compute built-in library

%package -n rocm-comgr
Summary:        AMD ROCm LLVM Code Object Manager
Provides:       comgr(major) = %{comgr_maj_api_ver}
Provides:       rocm-comgr = %{comgr_full_api_ver}-%{release}

%description -n rocm-comgr
The AMD Code Object Manager (Comgr) is a shared library which provides
operations for creating and inspecting code objects.

%package -n rocm-comgr-devel
Summary:        AMD ROCm LLVM Code Object Manager
Requires:       rocm-comgr%{?_isa} = %{version}-%{release}
Requires:       clang-devel(major) = %{llvm_maj_ver}
Requires:       llvm-devel(major) = %{llvm_maj_ver}

%description -n rocm-comgr-devel
The AMD Code Object Manager (Comgr) development package.

%package -n hipcc
Summary:        HIP compiler driver
Requires:       rocminfo
Requires:       rocm-device-libs = %{version}-%{release}
Requires:       compiler-rt(major) = %{llvm_maj_ver}

%description -n hipcc
hipcc is a compiler driver utility that will call clang or nvcc, depending on
target, and pass the appropriate include and library options for the target
compiler and HIP infrastructure.

hipcc will pass-through options to the target compiler. The tools calling hipcc
must ensure the compiler options are appropriate for the target compiler.

%package -n rocm-llvm-devel
Summary:        Meta package for install the LLVM devel used for ROCm
Requires:       llvm-devel(major) = %{llvm_maj_ver}

%description -n rocm-llvm-devel
LLVM devel files used when building ROCm.

%package -n hipcc-libomp-devel
Summary:        OpenMP header files for hipcc
Requires:       hipcc = %{version}-%{release}
%if %{with compat_build}
Requires:       libomp%{llvm_maj_ver}-devel
%else
Requires:       libomp-devel
%endif

%description -n hipcc-libomp-devel
OpenMP header files compatible with HIPCC.

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{rocm_version}

# llvm_maj_ver sanity check (we should be matching the bundled llvm major ver):
if ! grep -q "set(LLVM_VERSION_MAJOR %{llvm_maj_ver})" llvm/CMakeLists.txt; then
        echo "ERROR llvm_maj_ver macro is not correctly set"
        exit 1
fi
# Make sure we only build the AMD bits by discarding the bundled llvm code:
ls | grep -xv "amd" | xargs rm -r

##Fix issue with HIP, where compilation flags are incorrect, see issue:
#https://github.com/RadeonOpenCompute/ROCm-CompilerSupport/issues/49
#Remove redundant includes:
sed -i '/Args.push_back("-isystem");/,+3d' amd/comgr/src/comgr-compiler.cpp
#Source hard codes the libdir too:
sed -i 's/lib\(\/clang\)/%{_lib}\1/' amd/comgr/src/comgr-compiler.cpp

# CMake's find_package Config mode doesn't work if we use older llvm packages:
sed -i 's/find_package(Clang REQUIRED CONFIG)/find_package(Clang REQUIRED)/' amd/comgr/CMakeLists.txt
sed -i 's/find_package(LLD REQUIRED CONFIG)/find_package(LLD REQUIRED)/' amd/comgr/CMakeLists.txt
%if %{with compat_build}
sed -i 's@${CLANG_CMAKE_DIR}/../../../@/usr/lib/clang/%{llvm_maj_ver}/@' amd/comgr/cmake/opencl_pch.cmake
%endif

# Fixup finding /opt/llvm
sed -i -e 's@sys::path::append(LLVMPath, "llvm");@//sys::path::append(LLVMPath, "llvm");@' amd/comgr/src/comgr-env.cpp
# Fixup finding /opt/rocm/hip
sed -i -e 's@sys::path::append(HIPPath, "hip");@//sys::path::append(HIPPath, "hip");@' amd/comgr/src/comgr-env.cpp

# Tests known to fail with upstream LLVM (as opposed to the bundled llvm):
sed -i  -e "/add_isa_test(fract/d" \
        -e "/add_isa_test(frexp/d" \
        amd/device-libs/test/compile/CMakeLists.txt
sed -i -e "/add_comgr_test(compile_source_with_device_libs_to_bc_test/d" \
        -e "/add_comgr_test(name_expression_map_test/d" \
        -e "/add_comgr_test(nested_kernel_test/d" \
        amd/comgr/test/CMakeLists.txt

# Fix script shebang (Fedora doesn't allow using "env"):
sed -i 's|\(/usr/bin/\)env perl|\1perl|' amd/hipcc/bin/hipcc.pl
# ROCm upstream uses /opt for rocm-runtime, but Fedora uses /usr
# Don't include it again since /usr/include is already included:
sed -i '/" -isystem " + hsaPath + "\/include"/d' amd/hipcc/src/hipBin_amd.h
# Same thing for hipcc.pl:
sed -i '/^# Add paths to common HIP includes:/,/^$HIPCFLAGS/d' \
        amd/hipcc/bin/hipcc.pl

# HIPCC fixes to find clang++
# Fedora places clang++ in the regular bindir:
sed -i 's|lib/llvm/bin|bin|' amd/hipcc/bin/hipvars.pm amd/hipcc/src/hipBin_amd.h
#Make sure clang-MAJOR and clang++MAJOR is used over clang and clang++
sed -i -e 's|\(/clang[+]*\)|\1-%{llvm_maj_ver}|' \
	-e 's|\("clang++\)"|\1-%{llvm_maj_ver}"|' \
	amd/hipcc/bin/hip*.p* amd/hipcc/src/hipBin_amd.h

# Fix up the location AMD_DEVICE_LIBS_PREFIX
sed -i 's|@AMD_DEVICE_LIBS_PREFIX_CODE@|set(AMD_DEVICE_LIBS_PREFIX "%{_prefix}/%{amd_device_libs_prefix}")|' amd/device-libs/AMDDeviceLibsConfig.cmake.in

%build
echo "%%rocmllvm_version %llvm_maj_ver" > macros.rocmcompiler
export PATH=%{_libdir}/llvm%{llvm_maj_ver}/bin:$PATH
export INCLUDE_PATH=%{_libdir}/llvm%{llvm_maj_ver}/include

pushd amd/device-libs
#TODO ROCM_DEVICE_LIBS_BITCODE_INSTALL_LOC_* should be removed in ROCm 7.0:
%cmake -DROCM_DEVICE_LIBS_BITCODE_INSTALL_LOC_NEW="%{amd_device_libs_prefix}/amdgcn" \
        -DROCM_DEVICE_LIBS_BITCODE_INSTALL_LOC_OLD="" \
        -DCMAKE_BUILD_TYPE="RELEASE"
%cmake_build
# Used by comgr to find device libs when building:
export ROCM_PATH=$(realpath %__cmake_builddir/%{amd_device_libs_prefix})
popd

pushd amd/comgr
%cmake -DCMAKE_PREFIX_PATH=../device-libs/%__cmake_builddir \
  -DCMAKE_MODULE_PATH=%{_libdir}/llvm%{llvm_maj_ver}/lib \
  -DCMAKE_BUILD_TYPE="RELEASE" -DBUILD_TESTING=ON
%cmake_build
popd

pushd amd/hipcc
%cmake -DHIPCC_BACKWARD_COMPATIBILITY=OFF
%cmake_build
popd

%check
pushd amd/device-libs
# Workaround for bug in cmake tests not finding amdgcn:
ln -s %{amd_device_libs_prefix}/amdgcn %__cmake_builddir/amdgcn
%ctest
popd

pushd amd/comgr
%ctest
popd

# HIPCC sanity check
touch t.hip
# Build ROCM_PATH in a way that hipcc expects it when installed:
export ROCM_PATH=$(realpath amd/device-libs/%__cmake_builddir)
mkdir -p $ROCM_PATH/bin
ln -s %{_bindir}/clang++-%{llvm_maj_ver} $ROCM_PATH/bin
# Dummy rocm_agent_enumerator so it doesn't error:
touch $ROCM_PATH/bin/rocm_agent_enumerator
chmod a+x $ROCM_PATH/bin/rocm_agent_enumerator
amd/hipcc/%__cmake_builddir/hipcc -c t.hip

%install
install -Dpm 644 macros.rocmcompiler \
    %{buildroot}%{_rpmmacrodir}/macros.rocmcompiler

pushd amd/device-libs
%cmake_install
popd

pushd amd/comgr
%cmake_install
popd

pushd amd/hipcc
%cmake_install
# Fix perl module files installation:
mkdir -p %{buildroot}%{perl_vendorlib}
mv %{buildroot}%{_bindir}/hip*.pm %{buildroot}%{perl_vendorlib}
# Eventually upstream plans to deprecate Perl usage, see README.md
popd

#Clean up dupes:
%if 0%{?fedora}
%fdupes %{buildroot}%{_prefix}
%endif

%files macros
%{_rpmmacrodir}/macros.rocmcompiler

%files -n rocm-device-libs
%license %{_docdir}/ROCm-Device-Libs/LICENSE.TXT
%doc amd/device-libs/README.md amd/device-libs/doc/*.md
%{_libdir}/cmake/AMDDeviceLibs
%{_prefix}/%{amd_device_libs_prefix}/amdgcn

%files -n rocm-comgr
%license %{_docdir}/amd_comgr/LICENSE.txt
%license %{_docdir}/amd_comgr/NOTICES.txt
%dir %{_docdir}/amd_comgr
%doc %{_docdir}/amd_comgr/README.md
%{_libdir}/libamd_comgr.so.%{comgr_full_api_ver}
%{_libdir}/libamd_comgr.so.%{comgr_maj_api_ver}

%files -n rocm-comgr-devel
%{_includedir}/amd_comgr/amd_comgr.h
%{_libdir}/libamd_comgr.so
%{_libdir}/cmake/amd_comgr

%files -n hipcc
%license %{_docdir}/hipcc/LICENSE.txt
%doc %{_docdir}/hipcc/README.md
%dir %{_docdir}/hipcc
%{_bindir}/hipcc{,.pl,.bin}
%{_bindir}/hipconfig{,.pl,.bin}
%{perl_vendorlib}/hip*.pm

%files -n rocm-llvm-devel

%files -n hipcc-libomp-devel

%changelog
* Thu Sep 19 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 18-7.rocm6.2.0
- Spec cleanup
- Add rocm-llvm-devel
- Build with clang (fixes builds on EL9)

* Sat Sep 07 2024 Tom Rix <Tom.Rix@amd.com> - 18-6.rocm6.2.0
- Revert change to location of amdgcn

* Fri Sep 06 2024 Tom Rix <Tom.Rix@amd.com> - 18-5.rocm6.2.0
- Fix finding hip path
- Fix dangling -isystem

* Thu Sep 05 2024 Tom Rix <Tom.Rix@amd.com> - 18-4.rocm6.2.0
- location of amdgcn/ changed in llvm18
- Fix the finding of the llvm root path

* Mon Sep 02 2024 Tom Rix <Tom.Rix@amd.com> - 18-3.rocm6.2.0
- -mlink-builtin-bitcode-postopt is not a system clang option

* Fri Aug 09 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 18-2.rocm6.2.0
- Fix hipcc.bin patch for finding clang

* Thu Aug 08 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 18-1.rocm6.2.0
- Update to 6.2

* Thu Aug 01 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 17.3-7.rocm6.1.2
- Add libomp package

* Tue Jul 23 2024 Tom Rix <trix@redhat.com> - 17.3-6.rocm6.1.2
- Fix AMD_DEVICE_LIBS_PREFIX

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.3-5.rocm6.1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 06 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 17.3-4.rocm6.1.2
- Update to 6.1.2

* Thu May 16 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 17.3-3.rocm6.1.1
- Fix rocminfo requires

* Thu May 09 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 17.3-2.rocm6.1.1
- Fix rocm-device-libs requires

* Thu May 09 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 17.3-1.rocm6.1.1
- Bump version to override existing rocm-device-libs package

* Thu May 09 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 17.1-9.rocm6.1.1
- Add macros package

* Thu May 09 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 17.1-8.rocm6.1.1
- Fix requires

* Thu May 09 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 17.1-7.rocm6.1.1
- Update to ROCm 6.1.1
- Fix devel requires (should be on rocm-comgr-devel instead of hipcc)

* Mon May 06 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 17.1-6.rocm6.1.0
- Update to ROCm 6.1
- This package now owns hipcc and rocm-device-libs subpackages

* Sat Mar 9 2024 Tom Rix <trix@redhat.com> - 17.1-5
- Fix mock build

* Thu Mar 7 2024 Tom Rix <trix@redhat.com> - 17.1-4
- Add with compat_build for llvm17

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Dec 14 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 17.1-1
- Update to 17.1

* Fri Oct 20 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 17.0-3
- Rebuild against rocm-device-libs 17.1

* Wed Sep 06 2023 Tulio Magno Quites Machado Filho <tuliom@redhat.com> - 17.0-2
- Rebuild against LLVM 17.0.0

* Tue Aug 15 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 17.0-1
- Update to 17.0

* Tue Aug 08 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 16.2-3
- Rebuild against rocm-device-libs 16.4

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 18 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 16.2-1
- Update to 16.2

* Thu May 25 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 16.1-4
- Roll back last change, as it didn't work

* Thu May 25 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 16.1-3
- Add fix for RHBZ#2207599

* Wed Apr 19 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 16.1-2
- Rebuild against 16.1 rocm-device-libs

* Wed Apr 19 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 16.1-1
- Update to 16.1
- Add rocm-comgr full api provides (currently 2.5.0)

* Tue Apr 11 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 16.0-2
- Fix comgr provides (should be major api version of comgr), for RHBZ#2185838

* Wed Mar 29 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 16.0-1
- Update to 16.0 (forked sources for Fedora)

* Mon Feb 27 2023 Jeremy Newton <alexjnewt at hotmail dot com> - 5.4.1-3
- Use patch from Gentoo to improve test failures

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Dec 18 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.4.1-1
- Update to 5.4.1

* Tue Oct 04 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.3.0-1
- Update to 5.3.0

* Mon Sep 19 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.2.0-3
- Rebuilt against LLVM 15

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jul 03 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.2.0-1
- Update to 5.2.0

* Fri Jun 10 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.1.0-3
- Add comgr(rocm) provide

* Tue Apr 05 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.1.0-2
- Enable ppc64le

* Tue Mar 29 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.1.0-1
- Update to 5.1.0

* Fri Feb 11 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 5.0.0-1
- Update to 5.0.0

* Mon Jan 24 2022 Jeremy Newton <alexjnewt at hotmail dot com> - 4.5.2-1
- Initial package
