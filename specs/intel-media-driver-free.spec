Name:       intel-media-driver-free
Version:    24.4.4
Release:    %autorelease
Summary:    The Intel Media Driver for VAAPI
License:    MIT and BSD
URL:        https://github.com/intel/media-driver

# Original source has non-free and/or patented files, use following on the original source!
# $ python3 strip.py
# ref. https://github.com/intel/media-driver/wiki/Media-Driver-Shaders-(EU-Kernels)#build-with-open-source-shaders

#Source0:    %%{url}/archive/intel-media-%%{version}%%{?pre}.tar.gz
Source0:    intel-media-%{version}-free.tar.gz
Source1:    intel-media-driver.metainfo.xml
Source2:    strip.py

# GCC 15 Fix
# https://github.com/intel/media-driver/commit/46a7058714b17a13cf62c052ab1134031fa5f706
Patch01:    46a7058714b17a13cf62c052ab1134031fa5f706.patch

# This is an Intel only vaapi backend
ExclusiveArch:  i686 x86_64

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++

# AppStream metadata generation
BuildRequires:  libappstream-glib

# Enable once we start building free kernels
#BuildRequires:  intel-igc-devel
#BuildRequires:  intel-cm-compiler
#BuildRequires:  intel-compute-runtime

BuildRequires:  pkgconfig(libcmrt)
BuildRequires:  pkgconfig(igdgmm)
BuildRequires:  python3
BuildRequires:  python3-devel
BuildRequires:  python-unversioned-command
BuildRequires:  libva-devel
BuildRequires:  libpciaccess-devel
BuildRequires:  libdrm-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  ninja-build

%description
The Intel Media Driver for VAAPI is a new VA-API (Video Acceleration API)
user mode driver supporting hardware accelerated decoding, encoding,
and video post processing for GEN based graphics hardware.
https://01.org/intel-media-for-linux

%package -n     libva-intel-media-driver
Summary:        The Intel Media Driver for VAAPI.

%description -n libva-intel-media-driver
The Intel Media Driver for VAAPI is a new VA-API (Video Acceleration API)
user mode driver supporting hardware accelerated decoding, encoding,
and video post processing for GEN based graphics hardware.
https://01.org/intel-media-for-linux

%package -n     libigfxcmrt
Summary:        Library to load own GPU kernels on render engine via Intel media driver.
Requires:       libva-intel-media-driver%{?_isa} = %{version}-%{release}

%description -n libigfxcmrt
libigfxcmrt is a runtime library needed when user wants to execute their own GPU kernels on render engine.
It calls Intel media driver to load the kernels and allocate the resources.
It provides a set of APIs for user to call directly from application.

%package -n     libigfxcmrt-devel
Summary:        Development files for libigfxcmrt
Requires:       libigfxcmrt%{?_isa} = %{version}-%{release}

%description -n libigfxcmrt-devel
The libigfxcmrt-devel package contains libraries and header files for
developing applications that use libigfxcmrt.

%prep
%autosetup -p1 -n media-driver-intel-media-%{version}%{?pre}
# Fix license perm
chmod -x LICENSE.md README.md CMakeLists.txt

# Remove pre-built (but unused) files
rm -rv Tools/MediaDriverTools/UMDPerfProfiler/MediaPerfParser

%build
%ifarch %{ix86}
export CXXFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64"
%endif
%cmake \
%ifarch %{ix86}
  -DARCH:STRING=32 \
%endif
  -DENABLE_NONFREE_KERNELS:BOOL=OFF \
  -DENABLE_KERNELS:BOOL=OFF \
  -DBUILD_KERNELS:BOOL=OFF \
  -DLIBVA_DRIVERS_PATH=%{_libdir}/dri \
  -DMEDIA_BUILD_FATAL_WARNINGS=OFF \
  -DVC1_Decode_Supported="no" \
  -DAVC_Encode_VME_Supported="no" \
  -DAVC_Encode_VDEnc_Supported="no" \
  -DHEVC_Encode_VME_Supported="no" \
  -DHEVC_Encode_VDEnc_Supported="no" \
  -DAVC_Decode_Supported="no" \
  -DHEVC_Decode_Supported="no" \
  -DAVC_Decode_Supported="no" \
  -DVVC_Decode_Supported="no" \
  -G Ninja

%cmake_build

%install
%cmake_install

# Fix perm on library to be stripped
chmod +x %{buildroot}%{_libdir}/dri/iHD_drv_video.so

# install AppData and add modalias provides
mkdir -p %{buildroot}%{_metainfodir}
install -pm 0644 %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

# TODO - have pci based hw detection
%if 0
fn=%{buildroot}%{_metainfodir}/intel-media-driver.metainfo.xml
%{SOURCE9} src/i965_pciids.h | xargs appstream-util add-provide ${fn} modalias
%endif

%files -n libva-intel-media-driver
%doc README.md
%license LICENSE.md
%{_libdir}/dri/iHD_drv_video.so
%{_metainfodir}/%{name}.metainfo.xml

%files -n libigfxcmrt
%{_libdir}/libigfxcmrt.so.*

%files -n libigfxcmrt-devel
%{_libdir}/libigfxcmrt.so
%{_includedir}/igfxcmrt
%{_libdir}/pkgconfig/igfxcmrt.pc


%changelog
%autochangelog
