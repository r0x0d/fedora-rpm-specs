%global sdkver 1.4.304.0

Name:           glslang
Version:        15.1.0
Release:        %autorelease
Summary:        OpenGL and OpenGL ES shader front end and validator

License:        BSD-2-Clause AND BSD-3-Clause AND GPL-3.0-or-later AND Apache-2.0
URL:            https://github.com/KhronosGroup/%{name}
Source0:        %url/archive/vulkan-sdk-%{sdkver}.tar.gz#/%{name}-sdk-%{sdkver}.tar.gz
# Patch to build against system spirv-tools (rebased locally)
#Patch3:         https://patch-diff.githubusercontent.com/raw/KhronosGroup/glslang/pull/1722.patch#/0001-pkg-config-compatibility.patch
Patch3:         0001-pkg-config-compatibility.patch

BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  spirv-tools-devel

%description
%{name} is the official reference compiler front end for the OpenGL
ES and OpenGL shading languages. It implements a strict
interpretation of the specifications for these languages.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
%{name} is the official reference compiler front end for the OpenGL
ES and OpenGL shading languages. It implements a strict
interpretation of the specifications for these languages.

%prep
%autosetup -p1 -n %{name}-vulkan-sdk-%{sdkver}
# Fix rpmlint warning on debuginfo
find . -name '*.h' -or -name '*.cpp' -or -name '*.hpp'| xargs chmod a-x

%build
%cmake3 -DBUILD_SHARED_LIBS=OFF
%cmake_build

%install
%{cmake_install}

# we don't want them in here
rm -rf %{buildroot}%{_includedir}/SPIRV

%ifnarch s390x ppc64
%check
pushd Test
./runtests localResults ../%{_vpath_builddir}/StandAlone/glslangValidator ../%{_vpath_builddir}/StandAlone/spirv-remap
popd
%endif

%files
%doc README.md README-spirv-remap.txt
%{_bindir}/glslang
%{_bindir}/glslangValidator
%{_bindir}/spirv-remap

%files devel
%{_includedir}/glslang/
%{_libdir}/libOSDependent.a
%{_libdir}/libSPIRV.a
%{_libdir}/libSPVRemapper.a
%{_libdir}/libglslang.a
%{_libdir}/libGenericCodeGen.a
%{_libdir}/libMachineIndependent.a
%{_libdir}/libglslang-default-resource-limits.a
%{_libdir}/pkgconfig/glslang.pc
%{_libdir}/pkgconfig/spirv.pc
%{_libdir}/cmake/*

%changelog
%autochangelog
