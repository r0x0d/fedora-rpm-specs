# The package follows LLVM's major version, but API version is still important:
%global comgr_maj_api_ver 2
# local, fedora
%global _comgr_full_api_ver %{comgr_maj_api_ver}.8
# mock, suse
%global comgr_full_api_ver %{comgr_maj_api_ver}.8.0
# Upstream tags are based on rocm releases:
%global rocm_release 6.2
%global rocm_patch 4
%global rocm_version %{rocm_release}.%{rocm_patch}
# What LLVM is upstream using (use LLVM_VERSION_MAJOR from llvm/CMakeLists.txt):
%global llvm_maj_ver 18
%global upstreamname llvm-project

%global toolchain clang


%bcond_with bundled_llvm
%if %{with bundled_llvm}
%global _smp_mflags %{nil}
%global _lto_cflags %{nil}
%define _find_debuginfo_dwz_opts %{nil}
%global bundle_prefix %{_libdir}/rocm/llvm
%global llvm_triple %{_target_platform}
%global amd_device_libs_prefix lib64/rocm/llvm/lib/clang/%{llvm_maj_ver}/lib

# /usr/lib64/rocm/llvm/lib/clang/18/lib64/amdgcn
# /usr/lib64/rocm/llvm/lib64/clang/18/lib64/amdgcn

#	Compression type and level for source/binary package payloads.
#		"w7T0.xzdio"	xz level 7 using %%{getncpus} threads
%define _source_payload	w7T0.xzdio
%define _binary_payload	w7T0.xzdio


%else
# Used to tell cmake where to install device libs (must be relative to prefix)
# We want to install to clang_resource_dir/amdgcn for FHS compliance
%global amd_device_libs_prefix lib/clang/%{llvm_maj_ver}
%endif

%bcond_without debug
%if %{with debug}
%global build_type DEBUG
%else
%global build_type RELEASE
%endif

Name:           rocm-compilersupport
Version:        %{llvm_maj_ver}
Release:        1.rocm%{rocm_version}%{?dist}
Summary:        Various AMD ROCm LLVM related services

Url:            https://github.com/ROCm/llvm-project
# hipcc is MIT, comgr and device-libs are NCSA:
License:        NCSA and MIT
Source0:        https://github.com/ROCm/%{upstreamname}/archive/refs/tags/rocm-%{rocm_version}.tar.gz#/%{name}-%{rocm_version}.tar.gz

%if %{without bundled_llvm}
# This requires a patch that's only landed in llvm 19+:
# https://github.com/ROCm/llvm-project/commit/669db884972e769450470020c06a6f132a8a065b
Patch0:         0001-Revert-ockl-Don-t-use-wave32-ballot-builtin.patch
# Upstream LLVM 18 doesn't have GFX1152 yet
Patch1:         0001-Revert-GFX11-Add-a-new-target-gfx1152.patch
# -mlink-builtin-bitcode-postopt is not supported
Patch2:         0001-remove-mlink.patch

%else
Patch0:         0001-Remove-err_drv_duplicate_config-check.patch
%endif

BuildRequires:  cmake
%if 0%{?fedora}
BuildRequires:  perl
BuildRequires:  fdupes
BuildRequires:  perl-generators
%endif
BuildRequires:  libffi-devel
BuildRequires:  zlib-devel

%if %{without bundled_llvm}
BuildRequires:  llvm-devel(major) = %{llvm_maj_ver}
BuildRequires:  clang-devel(major) = %{llvm_maj_ver}
BuildRequires:  lld-devel(major) = %{llvm_maj_ver}
%else
BuildRequires:  binutils-devel
BuildRequires:  clang
Provides:       bundled(llvm-project) = %{llvm_maj_ver}
%endif

%if 0%{?rhel} || 0%{?is_opensuse}
ExclusiveArch:  x86_64
%global targets_to_build "X86;AMDGPU"
%else
#Only the following architectures are useful for ROCm packages:
ExclusiveArch:  x86_64 aarch64 ppc64le
%global targets_to_build "X86;AMDGPU;PowerPC;AArch64"
%endif

%description
%{summary}

%package macros
Summary:        ROCm Compiler RPM macros

%description macros
This package contains ROCm compiler related RPM macros.

%package -n rocm-device-libs
Summary:        AMD ROCm LLVM bit code libraries
%if %{without bundled_llvm}
Requires:       clang-devel(major) = %{llvm_maj_ver}
Requires:       clang-resource-filesystem(major) = %{llvm_maj_ver}
Requires:       lld-devel(major) = %{llvm_maj_ver}
Requires:       llvm-devel(major) = %{llvm_maj_ver}
%else
Requires:       rocm-llvm-devel
%endif

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
%if %{without bundled_llvm}
Requires:       clang-devel(major) = %{llvm_maj_ver}
Requires:       llvm-devel(major) = %{llvm_maj_ver}
%else
Requires:       rocm-llvm-devel
%endif

%description -n rocm-comgr-devel
The AMD Code Object Manager (Comgr) development package.

%package -n hipcc
Summary:        HIP compiler driver
Requires:       rocminfo
Requires:       rocm-device-libs = %{version}-%{release}
%if %{without bundled_llvm}
Requires:       compiler-rt(major) = %{llvm_maj_ver}
%else
Requires:       rocm-llvm-devel
%endif

%description -n hipcc
hipcc is a compiler driver utility that will call clang or nvcc, depending on
target, and pass the appropriate include and library options for the target
compiler and HIP infrastructure.

hipcc will pass-through options to the target compiler. The tools calling hipcc
must ensure the compiler options are appropriate for the target compiler.

%package -n rocm-llvm-devel
Summary:        Meta package for install the LLVM devel used for ROCm
%if %{without bundled_llvm}
Requires:       llvm-devel(major) = %{llvm_maj_ver}
%else
Requires:       %{name}-macros
Requires:       gcc-c++
Requires:       libstdc++-devel
%endif

%description -n rocm-llvm-devel
LLVM devel files used when building ROCm.

%package -n hipcc-libomp-devel
Summary:        OpenMP header files for hipcc
Requires:       hipcc = %{version}-%{release}
%if %{without bundled_llvm}
Requires:       libomp-devel(major) = %{llvm_maj_ver}
%else
Requires:       libomp-devel
%endif

%description -n hipcc-libomp-devel
OpenMP header files compatible with HIPCC.

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{rocm_version}

%if %{without bundled_llvm}
# llvm_maj_ver sanity check (we should be matching the bundled llvm major ver):
if ! grep -q "set(LLVM_VERSION_MAJOR %{llvm_maj_ver})" llvm/CMakeLists.txt; then
        echo "ERROR llvm_maj_ver macro is not correctly set"
        exit 1
fi
# Make sure we only build the AMD bits by discarding the bundled llvm code:
ls | grep -xv "amd" | xargs rm -r
%endif

##Fix issue with HIP, where compilation flags are incorrect, see issue:
#https://github.com/RadeonOpenCompute/ROCm-CompilerSupport/issues/49
#Remove redundant includes:
sed -i '/Args.push_back("-isystem");/,+3d' amd/comgr/src/comgr-compiler.cpp
#Source hard codes the libdir too:
sed -i 's/lib\(\/clang\)/%{_lib}\1/' amd/comgr/src/comgr-compiler.cpp

%if %{without bundled_llvm}
# CMake's find_package Config mode doesn't work if we use older llvm packages:
sed -i 's/find_package(Clang REQUIRED CONFIG)/find_package(Clang REQUIRED)/' amd/comgr/CMakeLists.txt
sed -i 's/find_package(LLD REQUIRED CONFIG)/find_package(LLD REQUIRED)/' amd/comgr/CMakeLists.txt
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

# Default rocm path is _prefix
sed -i -e 's@/opt/rocm@%{_prefix}@' amd/hipcc/bin/hipvars.pm
sed -i -e 's@/opt/rocm@%{_prefix}@' amd/hipcc/src/hipBin_base.h

# HIPCC fixes to find clang++
# Fedora places clang++ in the regular bindir:
%if %{without bundled_llvm}
# SYSTEM LLVM
LLVM_BINDIR=`llvm-config-%{llvm_maj_ver} --bindir`
if [ ! -x ${LLVM_BINDIR}/clang++ ]; then
    echo "Something wrong with llvm-config"
    false
fi
%else
# BUNDLED
LLVM_BINDIR=%{bundle_prefix}/bin
%endif

echo "%%rocmllvm_bindir $LLVM_BINDIR"  > macros.rocmcompiler

echo "s@\$ROCM_PATH/lib/llvm/bin@${LLVM_BINDIR}@" > pm.sed
sed -i -f pm.sed amd/hipcc/bin/hipvars.pm

echo "s@hipClangPath /= \"lib/llvm/bin\"@hipClangPath = \"${LLVM_BINDIR}\"@" > h.sed
sed -i -f h.sed amd/hipcc/src/hipBin_amd.h

# Fix up the location AMD_DEVICE_LIBS_PREFIX
sed -i 's|@AMD_DEVICE_LIBS_PREFIX_CODE@|set(AMD_DEVICE_LIBS_PREFIX "%{_prefix}/%{amd_device_libs_prefix}")|' amd/device-libs/AMDDeviceLibsConfig.cmake.in

%build
CLANG_VERSION=%llvm_maj_ver
%if %{without bundled_llvm}
LLVM_CMAKEDIR=`llvm-config-%{llvm_maj_ver} --cmakedir`
%else
LLVM_CMAKEDIR=%{bundle_prefix}/lib/cmake/llvm
%endif

echo "%%rocmllvm_version $CLANG_VERSION"  >> macros.rocmcompiler
echo "%%rocmllvm_cmakedir $LLVM_CMAKEDIR" >> macros.rocmcompiler

%if %{without bundled_llvm}

# SYSTEM LLVM
export PATH=%{_libdir}/llvm%{llvm_maj_ver}/bin:$PATH
export INCLUDE_PATH=%{_libdir}/llvm%{llvm_maj_ver}/include

pushd amd/device-libs
#TODO ROCM_DEVICE_LIBS_BITCODE_INSTALL_LOC_* should be removed in ROCm 7.0:
%cmake -DROCM_DEVICE_LIBS_BITCODE_INSTALL_LOC_NEW="%{amd_device_libs_prefix}/amdgcn" \
        -DROCM_DEVICE_LIBS_BITCODE_INSTALL_LOC_OLD="" \
        -DCMAKE_BUILD_TYPE=%{build_type}
%cmake_build
# Used by comgr to find device libs when building:
export ROCM_PATH=$(realpath %__cmake_builddir/%{amd_device_libs_prefix})
popd

pushd amd/comgr
%cmake -DCMAKE_PREFIX_PATH=../device-libs/%__cmake_builddir \
  -DCMAKE_MODULE_PATH=%{_libdir}/llvm%{llvm_maj_ver}/lib \
  -DCMAKE_BUILD_TYPE=%{build_type} -DBUILD_TESTING=ON
%cmake_build
popd

pushd amd/hipcc
%cmake -DHIPCC_BACKWARD_COMPATIBILITY=OFF
%cmake_build
popd

%else
# BUNDLED LLVM

# Real cores, No hyperthreading
COMPILE_JOBS=`cat /proc/cpuinfo | grep -m 1 'cpu cores' | awk '{ print $4 }'`
if [ ${COMPILE_JOBS}x = x ]; then
    COMPILE_JOBS=1
fi
# Take into account memmory usage per core, do not thrash real memory
BUILD_MEM=2
MEM_KB=0
MEM_KB=`cat /proc/meminfo | grep MemTotal | awk '{ print $2 }'`
MEM_MB=`eval "expr ${MEM_KB} / 1024"`
MEM_GB=`eval "expr ${MEM_MB} / 1024"`
COMPILE_JOBS_MEM=`eval "expr 1 + ${MEM_GB} / ${BUILD_MEM}"`
if [ "$COMPILE_JOBS_MEM" -lt "$COMPILE_JOBS" ]; then
    COMPILE_JOBS=$COMPILE_JOBS_MEM
fi
LINK_MEM=4
LINK_JOBS=`eval "expr 1 + ${MEM_GB} / ${LINK_MEM}"`
JOBS=${COMPILE_JOBS}
if [ "$LINK_JOBS" -lt "$JOBS" ]; then
    JOBS=$LINK_JOBS
fi

p=$PWD
cd llvm
%cmake \
	-DBUILD_SHARED_LIBS=OFF \
	-DBUILD_TESTING=OFF \
	-DCLANG_ENABLE_ARCMT=OFF \
	-DCLANG_ENABLE_STATIC_ANALYZER=OFF \
	-DCMAKE_BUILD_TYPE=%{build_type} \
	-DCMAKE_INSTALL_PREFIX=%{bundle_prefix} \
	-DCMAKE_INSTALL_LIBDIR=lib \
	-DLLVM_BINUTILS_INCDIR=%{_includedir} \
	-DLLVM_BUILD_LLVM_DYLIB=ON \
	-DLLVM_BUILD_RUNTIME=ON \
	-DLLVM_BUILD_TOOLS=ON \
	-DLLVM_BUILD_UTILS=ON \
	-DLLVM_DEFAULT_TARGET_TRIPLE=%{llvm_triple} \
	-DLLVM_ENABLE_PROJECTS="llvm;clang;lld" \
	-DLLVM_ENABLE_RUNTIMES="compiler-rt" \
	-DLLVM_ENABLE_ZLIB=ON \
	-DLLVM_ENABLE_ZSTD=ON \
	-DLLVM_EXTERNAL_PROJECTS="devicelibs;comgr;hipcc" \
	-DLLVM_EXTERNAL_COMGR_SOURCE_DIR=$p/amd/comgr \
	-DLLVM_EXTERNAL_DEVICELIBS_SOURCE_DIR=$p/amd/device-libs \
	-DLLVM_EXTERNAL_HIPCC_SOURCE_DIR=$p/amd/hipcc \
	-DLLVM_INCLUDE_BENCHMARKS=OFF \
	-DLLVM_INCLUDE_EXAMPLES=OFF \
	-DLLVM_INCLUDE_TESTS=OFF \
	-DLLVM_TARGETS_TO_BUILD=%{targets_to_build} \
	-DROCM_DIR=%{_prefix}

%cmake_build -j ${JOBS}

%endif

%if %{without bundled_llvm}
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

%endif

%install
install -Dpm 644 macros.rocmcompiler \
    %{buildroot}%{_rpmmacrodir}/macros.rocmcompiler

%if %{without bundled_llvm}
# SYSTEM LLVM

pushd amd/device-libs
%cmake_install
popd

pushd amd/comgr
%cmake_install
popd

pushd amd/hipcc
%cmake_install
popd

%else
# BUNDLED
cd llvm
%cmake_install

# Remove some things
rm -rf %{buildroot}%{bundle_prefix}/share
rm -rf %{buildroot}%{bundle_prefix}/hip

#
# Links to system locations
# comgr header
mkdir -p %{buildroot}%{_includedir}/amd_comgr
cd %{buildroot}%{_includedir}/amd_comgr
ln -s ../../lib64/rocm/llvm/include/amd_comgr/amd_comgr.h amd_comgr.h
cd -
# comgr libs
mkdir -p %{buildroot}%{_libdir}
cd %{buildroot}%{_libdir}/
if [ ! -f rocm/llvm/lib/libamd_comgr.so.%{comgr_full_api_ver} ]; then
    echo "Problem building comgr"
    false
fi
ln -s ./rocm/llvm/lib/libamd_comgr.so.%{comgr_full_api_ver} libamd_comgr.so.%{comgr_full_api_ver}
ln -s ./rocm/llvm/lib/libamd_comgr.so.%{comgr_full_api_ver} libamd_comgr.so.%{comgr_maj_api_ver}
ln -s ./rocm/llvm/lib/libamd_comgr.so.%{comgr_full_api_ver} libamd_comgr.so
ls -al
cd -
# hipcc
mkdir -p %{buildroot}%{_bindir}
cd %{buildroot}%{_bindir}
C="hipcc hipcc.bin hipcc.pl hipconfig hipconfig.bin hipconfig.pl"
for c in $C; do
    ln -s ../lib64/rocm/llvm/bin/$c $c
done
cd -

mkdir -p %{buildroot}%{_prefix}/%{amd_device_libs_prefix}
mv %{buildroot}%{bundle_prefix}/amdgcn %{buildroot}%{_prefix}/%{amd_device_libs_prefix}/
if [ ! -d %{buildroot}%{_prefix}/%{amd_device_libs_prefix}/amdgcn ]; then
    echo "Problem with amdgcn"
    find %{buildroot} -name 'amdgcn'
    false
fi
mkdir -p %{buildroot}%{_libdir}/cmake/AMDDeviceLibs
cd %{buildroot}%{_libdir}/cmake/AMDDeviceLibs
C="AMDDeviceLibsConfig.cmake"
for c in $C; do
    ln -s ../../rocm/llvm/lib/cmake/AMDDeviceLibs/$c $c
done
cd -

if [ ! -f %{buildroot}%{bundle_prefix}/lib/LLVMgold.so ]; then
    echo "Problem with LLVMgold.so"
    find %{buildroot} -name 'LLVMgold.so'
    false
fi

%endif

# Fix perl module files installation:
# Eventually upstream plans to deprecate Perl usage, see README.md
mkdir -p %{buildroot}%{perl_vendorlib}
%if %{without bundled_llvm}
mv %{buildroot}%{_bindir}/hip*.pm %{buildroot}%{perl_vendorlib}
%else
mv %{buildroot}%{bundle_prefix}/bin/hip*.pm %{buildroot}%{perl_vendorlib}
%endif

#Clean up dupes:
%if 0%{?fedora}
%fdupes %{buildroot}%{_prefix}
%endif

%files macros
%{_rpmmacrodir}/macros.rocmcompiler

%if %{without bundled_llvm}
# SYSTEM LLVM
%files -n rocm-device-libs
%license amd/device-libs/LICENSE.TXT
%doc amd/device-libs/README.md amd/device-libs/doc/*.md
%{_libdir}/cmake/AMDDeviceLibs
%{_prefix}/%{amd_device_libs_prefix}/amdgcn
%{_docdir}/ROCm-Device-Libs

%files -n rocm-comgr
%license amd/comgr/LICENSE.txt
%license amd/comgr/NOTICES.txt
%doc amd/comgr/README.md
%{_docdir}/amd_comgr
%{_libdir}/libamd_comgr.so.*

%files -n rocm-comgr-devel
%{_includedir}/amd_comgr/amd_comgr.h
%{_libdir}/libamd_comgr.so
%{_libdir}/cmake/amd_comgr/


%files -n hipcc
%license amd/hipcc/LICENSE.txt
%doc amd/hipcc/README.md
%{_docdir}/hipcc
%{_bindir}/hipcc{,.pl,.bin}
%{_bindir}/hipconfig{,.pl,.bin}
%{perl_vendorlib}/hip*.pm

%files -n rocm-llvm-devel

%else
# BUNDLED LLVM
%files -n rocm-device-libs
%license amd/device-libs/LICENSE.TXT
%{_libdir}/cmake/AMDDeviceLibs
%{bundle_prefix}/lib/cmake/AMDDeviceLibs
%doc amd/device-libs/README.md amd/device-libs/doc/*.md

%files -n rocm-comgr
%license amd/comgr/LICENSE.txt
%license amd/comgr/NOTICES.txt
%{_libdir}/libamd_comgr.so.%{comgr_full_api_ver}
%{_libdir}/libamd_comgr.so.%{comgr_maj_api_ver}
%{_libdir}/rocm/llvm/lib/libamd_comgr.so.%{comgr_full_api_ver}
%{_libdir}/rocm/llvm/lib/libamd_comgr.so.%{comgr_maj_api_ver}

%files -n rocm-comgr-devel
%{_includedir}/amd_comgr/amd_comgr.h
%{_libdir}/libamd_comgr.so
%{_libdir}/rocm/llvm/include/amd_comgr/amd_comgr.h
%{_libdir}/rocm/llvm/lib/libamd_comgr.so
%{_libdir}/rocm/llvm/lib/cmake/amd_comgr/

%files -n hipcc
%license amd/hipcc/LICENSE.txt
%doc amd/hipcc/README.md

%files -n rocm-llvm-devel
%{_bindir}/hipcc{,.pl,.bin}
%{_bindir}/hipconfig{,.pl,.bin}
%{perl_vendorlib}/hip*.pm
%{bundle_prefix}/bin/
%{bundle_prefix}/include/{clang,lld,llvm,clang-c,llvm-c}
%{bundle_prefix}/lib/{libclang*,libLLVM*,libLTO*,libRemarks*,liblld*,LLVMgold.so}
%{bundle_prefix}/lib/clang/
%{bundle_prefix}/lib/cmake/{amd_comgr,clang,lld,llvm,AMDDeviceLibs}

%endif

%files -n hipcc-libomp-devel

%changelog
* Thu Nov 7 2024 Tom Rix <Tom.Rix@amd.com> - 18-1.rocm6.2.4
- Update to 6.2.4

* Wed Nov 6 2024 Tom Rix <Tom.Rix@amd.com> - 18-20.rocm6.2.0
- Remove double config check

* Mon Nov 4 2024 Tom Rix <Tom.Rix@amd.com> - 18-19.rocm6.2.0
- Fix c++ isystem.
- Build LLVMgold.so
- Remove link to comgr cmake

* Fri Nov 1 2024 Tom Rix <Tom.Rix@amd.com> - 18-18.rocm6.2.0
- Mockable rocm llvm.

* Thu Oct 31 2024 Tom Rix <Tom.Rix@amd.com> - 18-17.rocm6.2.0
- Change bundle llvm to build rocm llvm.

* Wed Oct 30 2024 Tom Rix <Tom.Rix@amd.com> - 18-16.rocm6.2.0
- Improve macros

* Wed Oct 30 2024 Tom Rix <Tom.Rix@amd.com> - 18-15.rocm6.2.0
- RHEL is only x86_64

* Tue Oct 29 2024 Tom Rix <Tom.Rix@amd.com> - 18-14.rocm6.2.0
- Force device-libs location on bundling

* Tue Oct 29 2024 Tom Rix <Tom.Rix@amd.com> - 18-13.rocm6.2.0
- Fix opt/rocm path

* Tue Oct 29 2024 Tom Rix <Tom.Rix@amd.com> - 18-12.rocm6.2.0
- Use system clang with bundled llvm

* Sun Oct 27 2024 Tom Rix <Tom.Rix@amd.com> - 18-11.rocm6.2.0
- bundle llvm

* Thu Oct 10 2024 Tom Rix <Tom.Rix@amd.com> - 18-10.rocm6.2.0
- Fix hipcc-libomp-devel

* Mon Oct 07 2024 Tom Rix <Tom.Rix@amd.com> - 18-9.rocm6.2.0
- Work around broken clang++-18 link

* Tue Oct 01 2024 Jeremy Newton <alexjnewt at hotmail dot com> - 18-8.rocm6.2.0
- Drop compat build option (be more agnostic to llvm packaging)
- Add hip sanity test
- Spec cleanup

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
