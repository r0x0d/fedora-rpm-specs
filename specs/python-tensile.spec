%global upstreamname Tensile

%global rocm_release 6.2
%global rocm_patch 4
%global rocm_version %{rocm_release}.%{rocm_patch}

# This doesn't work quite yet:
# Also depends on local gpu hw
%bcond_with check

%global toolchain rocm
# hipcc does not support some clang flags
%global build_cxxflags %(echo %{optflags} | sed -e 's/-fstack-protector-strong/-Xarch_host -fstack-protector-strong/' -e 's/-fcf-protection/-Xarch_host -fcf-protection/')

Name:           python-tensile
Version:        %{rocm_version}
%if 0%{?fedora}
Release:        %autorelease
%else
Release:        100%{?dist}
%endif
Summary:        Tool for creating benchmark-driven backend libraries for GEMMs

Url:            https://github.com/ROCmSoftwarePlatform/Tensile
License:        MIT
Source0:        %{url}/archive/refs/tags/rocm-%{version}.tar.gz#/%{upstreamname}-%{version}.tar.gz

Patch1:         0001-More-gfx1151.patch
Patch2:         0001-Add-gfx1103.patch
Patch3:         0001-Add-gfx1035.patch

#Patch0:         0001-enable-gfx1103-for-Tensile.patch
# In 6.1, work around  this error
# Tensile::FATAL: Cached asm caps differ from derived asm caps for (9, 0, 10)
# Patch1:         0001-tensile-workaround-cache-problem.patch

BuildRequires:  python3-devel
%if 0%{?suse_version}
# TW
BuildRequires:  python311-setuptools
%else
BuildRequires:  python3dist(setuptools)
%endif

%if %{with check}
# Some of these might not be needed
BuildRequires:  compiler-rt
BuildRequires:  clang-devel
BuildRequires:  lld
BuildRequires:  llvm-devel
BuildRequires:  rocm-cmake
BuildRequires:  rocm-comgr-devel
BuildRequires:  rocm-hip-devel
BuildRequires:  rocm-rpm-macros
BuildRequires:  rocm-runtime-devel
%endif

Requires:       hipcc
Requires:       rocminfo
Requires:       python3dist(joblib)
Requires:       python3dist(msgpack)

# Straight python, but only usable for ROCm which is only on x86_64
BuildArch:      noarch
ExclusiveArch:  x86_64

%description
Tensile is a tool for creating benchmark-driven backend libraries for GEMMs,
GEMM-like problems (such as batched GEMM), and general N-dimensional tensor
contractions on a GPU. The Tensile library is mainly used as backend library to
rocBLAS. Tensile acts as the performance backbone for a wide variety of
'compute' applications running on AMD GPUs.

%package -n python3-tensile
Summary:        %{summary}
Requires:       cmake

%description -n python3-tensile
Tensile is a tool for creating benchmark-driven backend libraries for GEMMs,
GEMM-like problems (such as batched GEMM), and general N-dimensional tensor
contractions on a GPU. The Tensile library is mainly used as backend library to
rocBLAS. Tensile acts as the performance backbone for a wide variety of
'compute' applications running on AMD GPUs.

%prep
%autosetup -p1 -n %{upstreamname}-rocm-%{version}

#Fix a few things:
chmod 755 Tensile/Configs/miopen/convert_cfg.py
sed -i -e 's@bin/python@bin/python3@' Tensile/Configs/miopen/convert_cfg.py
sed -i -e 's@bin/python@bin/python3@' Tensile/Tests/create_tests.py

# I'm assuming we don't need these:
rm -r %{upstreamname}/Configs/miopen/archives

# hack where TensileGetPath is located
sed -i -e 's@${Tensile_PREFIX}/bin/TensileGetPath@TensileGetPath@g' Tensile/cmake/TensileConfig.cmake

# Use /usr instead of /opt/rocm for prefix
sed -i -e 's@opt/rocm@usr@g' Tensile/Common.py
sed -i -e 's@opt/rocm@usr@g' Tensile/Tests/yaml_only/test_config.py

# Ignora asm cap
sed -i -e 's@globalParameters["IgnoreAsmCapCache"] = False@globalParameters["IgnoreAsmCapCache"] = True@' Tensile/Common.py
sed -i -e 's@arguments["IgnoreAsmCapCache"] = args.IgnoreAsmCapCache@arguments["IgnoreAsmCapCache"] = True@' Tensile/TensileCreateLibrary.py
sed -i -e 's@if not ignoreCacheCheck and derivedAsmCaps@if False and derivedAsmCaps@' Tensile/Common.py

%build
%py3_build

%install
%py3_install

mkdir -p %{buildroot}%{_datadir}/cmake/Tensile
mv %{buildroot}%{_prefix}/cmake/* %{buildroot}%{_datadir}/cmake/Tensile/
rm -rf %{buildroot}%{_prefix}/cmake

# Do not distribute broken bins
rm %{buildroot}%{_bindir}/tensile*

# Do not distribute tests
rm -rf %{buildroot}%{python3_sitelib}/%{upstreamname}/Tests

%check
%if %{with check}
%tox
%endif

%files -n python3-tensile
%dir %{_datadir}/cmake/Tensile
%dir %{_datadir}/cmake/Tensile
%dir %{python3_sitelib}/%{upstreamname}
%dir %{python3_sitelib}/%{upstreamname}*.egg-info
%doc README.md
%license LICENSE.md
%{_bindir}/%{upstreamname}*
%{_datadir}/cmake/Tensile/*.cmake
%{python3_sitelib}/%{upstreamname}/*
%{python3_sitelib}/%{upstreamname}*.egg-info/*

%changelog
%if 0%{?fedora}
%autochangelog
%endif

