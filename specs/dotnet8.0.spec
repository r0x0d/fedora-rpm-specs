%bcond_with bootstrap

# LTO triggers a compilation error for a source level issue.  Given that LTO should not
# change the validity of any given source and the nature of the error (undefined enum), I
# suspect a generator program is mis-behaving in some way.  This needs further debugging,
# until that's done, disable LTO.  This has to happen before setting the flags below.
%define _lto_cflags %{nil}

%global dotnetver 8.0

%global host_version 8.0.11
%global runtime_version 8.0.11
%global aspnetcore_runtime_version %{runtime_version}
%global sdk_version 8.0.111
%global sdk_feature_band_version %(echo %{sdk_version} | cut -d '-' -f 1 | sed -e 's|[[:digit:]][[:digit:]]$|00|')
%global templates_version %{runtime_version}
#%%global templates_version %%(echo %%{runtime_version} | awk 'BEGIN { FS="."; OFS="." } {print $1, $2, $3+1 }')

# upstream can produce releases with a different tag than the SDK version
%global upstream_tag v%{runtime_version}
%global upstream_tag_without_v %(echo %{upstream_tag} | sed -e 's|^v||')

%global host_rpm_version %{host_version}
%global runtime_rpm_version %{runtime_version}
%global aspnetcore_runtime_rpm_version %{aspnetcore_runtime_version}
%global sdk_rpm_version %{sdk_version}

%if 0%{?fedora} || 0%{?rhel} < 8
%global use_bundled_libunwind 0
%else
%global use_bundled_libunwind 1
%endif

%ifarch aarch64 ppc64le s390x
%global use_bundled_libunwind 1
%endif

%ifarch aarch64
%global runtime_arch arm64
%endif
%ifarch ppc64le
%global runtime_arch ppc64le
%endif
%ifarch s390x
%global runtime_arch s390x
%endif
%ifarch x86_64
%global runtime_arch x64
%endif

%global mono_archs ppc64le s390x

%{!?runtime_id:%global runtime_id %(. /etc/os-release ; echo "${ID}.${VERSION_ID%%.*}")-%{runtime_arch}}

Name:           dotnet%{dotnetver}
Version:        %{sdk_rpm_version}
Release:        3%{?dist}
Summary:        .NET Runtime and SDK
License:        0BSD AND Apache-2.0 AND (Apache-2.0 WITH LLVM-exception) AND APSL-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause AND BSL-1.0 AND bzip2-1.0.6 AND CC0-1.0 AND CC-BY-3.0 AND CC-BY-4.0 AND CC-PDDC AND CNRI-Python AND EPL-1.0 AND GPL-2.0-only AND (GPL-2.0-only WITH GCC-exception-2.0) AND GPL-2.0-or-later AND GPL-3.0-only AND ICU AND ISC AND LGPL-2.1-only AND LGPL-2.1-or-later AND LicenseRef-Fedora-Public-Domain AND LicenseRef-ISO-8879 AND MIT AND MIT-Wu AND MS-PL AND MS-RL AND NCSA AND OFL-1.1 AND OpenSSL AND Unicode-DFS-2015 AND Unicode-DFS-2016 AND W3C-19980720 AND X11 AND Zlib

URL:            https://github.com/dotnet/

%if %{with bootstrap}
%global bootstrap_sdk_version 8.0.100-rc.1.23410.12
%global tarball_name dotnet-%{upstream_tag}-x64-bootstrap
# The source is generated on a Fedora box via:
# ./build-dotnet-tarball --bootstrap %%{upstream_tag}
Source0:        %{tarball_name}.tar.xz
# Generated via ./build-arm64-bootstrap-tarball
Source1:        dotnet-prebuilts-%{bootstrap_sdk_version}-arm64.tar.gz
# Generated manually, same pattern as the arm64 tarball
Source2:        dotnet-prebuilts-%{bootstrap_sdk_version}-ppc64le.tar.gz
# Generated manually, same pattern as the arm64 tarball
Source3:        dotnet-prebuilts-%{bootstrap_sdk_version}-s390x.tar.gz
%else
Source0:        https://github.com/dotnet/dotnet/archive/refs/tags/%{upstream_tag}.tar.gz#/dotnet-%{upstream_tag_without_v}.tar.gz
Source1:        https://github.com/dotnet/dotnet/releases/download/%{upstream_tag}/dotnet-%{upstream_tag_without_v}.tar.gz.sig
Source2:        https://dotnet.microsoft.com/download/dotnet/release-key-2023.asc
%endif
Source5:        https://github.com/dotnet/dotnet/releases/download/%{upstream_tag}/release.json

Source10:       macros.dotnet

Source20:       check-debug-symbols.py
Source21:       dotnet.sh.in

# Disable apphost; there's no net6.0 apphost for ppc64le
Patch1:         roslyn-analyzers-ppc64le-apphost.patch
# https://github.com/dotnet/source-build/discussions/3481
Patch2:         vstest-intent-net8.0.patch
# https://github.com/dotnet/runtime/pull/95216#issuecomment-1842799314
Patch3:         runtime-re-enable-implicit-rejection.patch
# https://github.com/dotnet/msbuild/pull/9449
Patch4:         msbuild-9449-exec-stop-setting-a-locale.patch
# TODO
Patch5:         runtime-clang-19.patch
# We disable checking the signature of the last certificate in a chain if the certificate is supposedly self-signed.
# A side effect of not checking the self-signature of such a certificate is that disabled or unsupported message
# digests used for the signature are not treated as fatal errors.
# https://issues.redhat.com/browse/RHEL-25254
Patch6:         runtime-openssl-sha1.patch


ExclusiveArch:  aarch64 ppc64le s390x x86_64


BuildRequires:  clang
BuildRequires:  cmake
BuildRequires:  coreutils
%if %{without bootstrap}
BuildRequires:  dotnet-sdk-%{dotnetver}
BuildRequires:  dotnet-sdk-%{dotnetver}-source-built-artifacts
%endif
BuildRequires:  findutils
BuildRequires:  git
BuildRequires:  glibc-langpack-en
BuildRequires:  gnupg2
BuildRequires:  hostname
BuildRequires:  krb5-devel
BuildRequires:  libicu-devel
%if ! %{use_bundled_libunwind}
BuildRequires:  libunwind-devel
%endif
%ifnarch s390x
BuildRequires:  lld
%else
# lld is not supported/available/usable on s390x
BuildRequires:  binutils
%endif
# If the build ever crashes, then having lldb installed might help the
# runtime generate a backtrace for the crash
BuildRequires:  lldb
BuildRequires:  llvm
BuildRequires:  lttng-ust-devel
BuildRequires:  make
#BuildRequires:  nodejs-devel
BuildRequires:  openssl-devel
%if 0%{?fedora} >= 41
BuildRequires:  openssl-devel-engine
%endif
BuildRequires:  python3
BuildRequires:  tar
BuildRequires:  util-linux
BuildRequires:  zlib-devel


# The tracing support in CoreCLR is optional. It has a run-time
# dependency on some additional libraries like lttng-ust. The runtime
# gracefully disables tracing if the dependencies are missing.
%global __requires_exclude_from ^(%{_libdir}/dotnet/.*/libcoreclrtraceptprovider\\.so)$

# Avoid generating provides and requires for private libraries
%global privlibs             libhostfxr
%global privlibs %{privlibs}|libclrgc
%global privlibs %{privlibs}|libclrjit
%global privlibs %{privlibs}|libcoreclr
%global privlibs %{privlibs}|libcoreclrtraceptprovider
%global privlibs %{privlibs}|libhostpolicy
%global privlibs %{privlibs}|libmscordaccore
%global privlibs %{privlibs}|libmscordbi
%global privlibs %{privlibs}|libnethost
%global privlibs %{privlibs}|libSystem.Globalization.Native
%global privlibs %{privlibs}|libSystem.IO.Compression.Native
%global privlibs %{privlibs}|libSystem.Native
%global privlibs %{privlibs}|libSystem.Net.Security.Native
%global privlibs %{privlibs}|libSystem.Security.Cryptography.Native.OpenSsl
%global __provides_exclude ^(%{privlibs})\\.so
%global __requires_exclude ^(%{privlibs})\\.so


%description
.NET is a fast, lightweight and modular platform for creating
cross platform applications that work on Linux, macOS and Windows.

It particularly focuses on creating console applications, web
applications and micro-services.

.NET contains a runtime conforming to .NET Standards a set of
framework libraries, an SDK containing compilers and a 'dotnet'
application to drive everything.

# The `dotnet` package was a bit of historical mistake. Users
# shouldn't be asked to install .NET without a version because .NET
# code (source or build) is generally version specific. We have kept
# it around in older versions of RHEL and Fedora. But no reason to
# continue this mistake.
%if ( 0%{?fedora} && 0%{?fedora} < 38 ) || ( 0%{?rhel} && 0%{?rhel} < 9 )

%package -n dotnet

Version:        %{sdk_rpm_version}
Summary:        .NET CLI tools and runtime

Requires:       dotnet-sdk-%{dotnetver}%{?_isa} >= %{sdk_rpm_version}-%{release}

%description -n dotnet
.NET is a fast, lightweight and modular platform for creating
cross platform applications that work on Linux, macOS and Windows.

It particularly focuses on creating console applications, web
applications and micro-services.

.NET contains a runtime conforming to .NET Standards a set of
framework libraries, an SDK containing compilers and a 'dotnet'
application to drive everything.

%endif

%package -n dotnet-host

Version:        %{host_rpm_version}
Summary:        .NET command line launcher

%description -n dotnet-host
The .NET host is a command line program that runs a standalone
.NET application or launches the SDK.

.NET is a fast, lightweight and modular platform for creating
cross platform applications that work on Linux, Mac and Windows.

It particularly focuses on creating console applications, web
applications and micro-services.


%package -n dotnet-hostfxr-%{dotnetver}

Version:        %{host_rpm_version}
Summary:        .NET command line host resolver

# Theoretically any version of the host should work. But lets aim for the one
# provided by this package, or from a newer version of .NET
Requires:       dotnet-host%{?_isa} >= %{host_rpm_version}-%{release}

%description -n dotnet-hostfxr-%{dotnetver}
The .NET host resolver contains the logic to resolve and select
the right version of the .NET SDK or runtime to use.

.NET is a fast, lightweight and modular platform for creating
cross platform applications that work on Linux, Mac and Windows.

It particularly focuses on creating console applications, web
applications and micro-services.


%package -n dotnet-runtime-%{dotnetver}

Version:        %{runtime_rpm_version}
Summary:        NET %{dotnetver} runtime

Requires:       dotnet-hostfxr-%{dotnetver}%{?_isa} >= %{host_rpm_version}-%{release}

# libicu is dlopen()ed
Requires:       libicu%{?_isa}

# See src/runtime/src/libraries/Native/AnyOS/brotli-version.txt
Provides: bundled(libbrotli) = 1.0.9
%if %{use_bundled_libunwind}
# See src/runtime/src/coreclr/pal/src/libunwind/libunwind-version.txt
Provides: bundled(libunwind) = 1.5.rc1.28.g9165d2a1
%endif

%description -n dotnet-runtime-%{dotnetver}
The .NET runtime contains everything needed to run .NET applications.
It includes a high performance Virtual Machine as well as the framework
libraries used by .NET applications.

.NET is a fast, lightweight and modular platform for creating
cross platform applications that work on Linux, Mac and Windows.

It particularly focuses on creating console applications, web
applications and micro-services.


%package -n dotnet-runtime-dbg-%{dotnetver}

Version:        %{runtime_rpm_version}
Summary:        Managed debug symbols NET %{dotnetver} runtime

Requires:       dotnet-runtime-%{dotnetver}%{?_isa} = %{runtime_rpm_version}-%{release}

%description -n dotnet-runtime-dbg-%{dotnetver}
This package contains the managed symbol (pdb) files useful to debug the
managed parts of the .NET runtime itself.


%package -n aspnetcore-runtime-%{dotnetver}

Version:        %{aspnetcore_runtime_rpm_version}
Summary:        ASP.NET Core %{dotnetver} runtime

Requires:       dotnet-runtime-%{dotnetver}%{?_isa} = %{runtime_rpm_version}-%{release}

%description -n aspnetcore-runtime-%{dotnetver}
The ASP.NET Core runtime contains everything needed to run .NET
web applications. It includes a high performance Virtual Machine as
well as the framework libraries used by .NET applications.

ASP.NET Core is a fast, lightweight and modular platform for creating
cross platform web applications that work on Linux, Mac and Windows.

It particularly focuses on creating console applications, web
applications and micro-services.


%package -n aspnetcore-runtime-dbg-%{dotnetver}

Version:        %{aspnetcore_runtime_rpm_version}
Summary:        Managed debug symbols for the ASP.NET Core %{dotnetver} runtime

Requires:       aspnetcore-runtime-%{dotnetver}%{?_isa} = %{aspnetcore_runtime_rpm_version}-%{release}

%description -n aspnetcore-runtime-dbg-%{dotnetver}
This package contains the managed symbol (pdb) files useful to debug the
managed parts of the ASP.NET Core runtime itself.


%package -n dotnet-templates-%{dotnetver}

Version:        %{sdk_rpm_version}
Summary:        .NET %{dotnetver} templates

# Theoretically any version of the host should work. But lets aim for the one
# provided by this package, or from a newer version of .NET
Requires:       dotnet-host%{?_isa} >= %{host_rpm_version}-%{release}

%description -n dotnet-templates-%{dotnetver}
This package contains templates used by the .NET SDK.

.NET is a fast, lightweight and modular platform for creating
cross platform applications that work on Linux, Mac and Windows.

It particularly focuses on creating console applications, web
applications and micro-services.


%package -n dotnet-sdk-%{dotnetver}

Version:        %{sdk_rpm_version}
Summary:        .NET %{dotnetver} Software Development Kit

Provides:       bundled(js-jquery)

Requires:       dotnet-runtime-%{dotnetver}%{?_isa} >= %{runtime_rpm_version}-%{release}
Requires:       aspnetcore-runtime-%{dotnetver}%{?_isa} >= %{aspnetcore_runtime_rpm_version}-%{release}

Requires:       dotnet-apphost-pack-%{dotnetver}%{?_isa} >= %{runtime_rpm_version}-%{release}
Requires:       dotnet-targeting-pack-%{dotnetver}%{?_isa} >= %{runtime_rpm_version}-%{release}
Requires:       aspnetcore-targeting-pack-%{dotnetver}%{?_isa} >= %{aspnetcore_runtime_rpm_version}-%{release}
Requires:       netstandard-targeting-pack-2.1%{?_isa} >= %{sdk_rpm_version}-%{release}

Requires:       dotnet-templates-%{dotnetver}%{?_isa} >= %{sdk_rpm_version}-%{release}

%description -n dotnet-sdk-%{dotnetver}
The .NET SDK is a collection of command line applications to
create, build, publish and run .NET applications.

.NET is a fast, lightweight and modular platform for creating
cross platform applications that work on Linux, Mac and Windows.

It particularly focuses on creating console applications, web
applications and micro-services.


%package -n dotnet-sdk-dbg-%{dotnetver}

Version:        %{sdk_rpm_version}
Summary:        Managed debug symbols for the .NET %{dotnetver} Software Development Kit

Requires:       dotnet-sdk-%{dotnetver}%{?_isa} = %{sdk_rpm_version}-%{release}

%description -n dotnet-sdk-dbg-%{dotnetver}
This package contains the managed symbol (pdb) files useful to debug the .NET
Software Development Kit (SDK) itself.


%global dotnet_targeting_pack() %{expand:
%package -n %{1}

Version:        %{2}
Summary:        Targeting Pack for %{3} %{4}

Requires:       dotnet-host%{?_isa}

%description -n %{1}
This package provides a targeting pack for %{3} %{4}
that allows developers to compile against and target %{3} %{4}
applications using the .NET SDK.

%files -n %{1}
%dir %{_libdir}/dotnet/packs
%{_libdir}/dotnet/packs/%{5}
}

%dotnet_targeting_pack dotnet-apphost-pack-%{dotnetver} %{runtime_rpm_version} Microsoft.NETCore.App %{dotnetver} Microsoft.NETCore.App.Host.%{runtime_id}
%dotnet_targeting_pack dotnet-targeting-pack-%{dotnetver} %{runtime_rpm_version} Microsoft.NETCore.App %{dotnetver} Microsoft.NETCore.App.Ref
%dotnet_targeting_pack aspnetcore-targeting-pack-%{dotnetver} %{aspnetcore_runtime_rpm_version} Microsoft.AspNetCore.App %{dotnetver} Microsoft.AspNetCore.App.Ref
%dotnet_targeting_pack netstandard-targeting-pack-2.1 %{sdk_rpm_version} NETStandard.Library 2.1 NETStandard.Library.Ref


%package -n dotnet-sdk-%{dotnetver}-source-built-artifacts

Version:        %{sdk_rpm_version}
Summary:        Internal package for building .NET %{dotnetver} Software Development Kit

%description -n dotnet-sdk-%{dotnetver}-source-built-artifacts
The .NET source-built archive is a collection of packages needed
to build the .NET SDK itself.

These are not meant for general use.


%prep
%if %{without bootstrap}
# check gpg signatures only for non-bootstrap builds; bootstrap "sources" are hand-crafted
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%endif

release_json_tag=$(grep tag %{SOURCE5} | cut -d: -f2 | sed -E 's/[," ]*//g')
if [[ ${release_json_tag} != %{upstream_tag} ]]; then
   echo "error: tag in release.json doesn't match tag in spec file"
   exit 1
fi

%if %{without bootstrap}
%setup -q -n dotnet-%{upstream_tag_without_v}

# Remove all prebuilts
find -iname '*.dll' -type f -delete
find -iname '*.so' -type f -delete
find -iname '*.tar.gz' -type f -delete
find -iname '*.nupkg' -type f -delete
find -iname '*.zip' -type f -delete

rm -rf .dotnet/
rm -rf packages/source-built

mkdir -p prereqs/packages/archive
ln -s %{_libdir}/dotnet/source-built-artifacts/Private.SourceBuilt.Artifacts.*.tar.gz prereqs/packages/archive/

%else

%setup -q -T -b 0 -n dotnet-%{upstream_tag}-x64-bootstrap

%ifnarch x86_64

rm -rf .dotnet
%ifarch aarch64
tar -x --strip-components=1 -f %{SOURCE1} -C prereqs/packages/prebuilt/
%endif
%ifarch ppc64le
tar -x --strip-components=1 -f %{SOURCE2} -C prereqs/packages/prebuilt/
%endif
%ifarch s390x
tar -x --strip-components=1 -f %{SOURCE3} -C prereqs/packages/prebuilt/
%endif

mkdir -p .dotnet
tar xf prereqs/packages/prebuilt/dotnet-sdk*.tar.gz -C .dotnet/
rm prereqs/packages/prebuilt/dotnet-sdk*.tar.gz

boot_sdk_version=$(ls -1 .dotnet/sdk/)
sed -i -E 's|"dotnet": "[^"]+"|"dotnet" : "'$boot_sdk_version'"|' global.json

%ifarch ppc64le s390x
ilasm_version=$(ls prereqs/packages/prebuilt| grep -i ilasm | tr 'A-Z' 'a-z' | sed -E 's|runtime.linux-'%{runtime_arch}'.microsoft.netcore.ilasm.||' | sed -E 's|.nupkg$||')
echo $ilasm_version

mkdir -p packages-customized-local
pushd packages-customized-local
tar xf ../prereqs/packages/archive/Private.SourceBuilt.Artifacts.*.tar.gz
sed -i -E 's|<MicrosoftNETCoreILAsmVersion>[^<]+</MicrosoftNETCoreILAsmVersion>|<MicrosoftNETCoreILAsmVersion>'$ilasm_version'</MicrosoftNETCoreILAsmVersion>|' PackageVersions.props
sed -i -E 's|<MicrosoftNETCoreILDAsmVersion>[^<]+</MicrosoftNETCoreILDAsmVersion>|<MicrosoftNETCoreILDAsmVersion>'$ilasm_version'</MicrosoftNETCoreILDAsmVersion>|' PackageVersions.props
tar czf ../prereqs/packages/archive/Private.SourceBuilt.Artifacts.*.tar.gz *
popd

%endif

%endif

%endif

%autopatch -p1 -M 999

%if ! %{use_bundled_libunwind}
sed -i -E 's|( /p:BuildDebPackage=false)|\1 --cmakeargs -DCLR_CMAKE_USE_SYSTEM_LIBUNWIND=TRUE|' src/runtime/eng/SourceBuild.props
%endif


%build
cat /etc/os-release

%if %{without bootstrap}
# We need to create a copy because we will mutate this
cp -a %{_libdir}/dotnet previously-built-dotnet
find previously-built-dotnet
%endif

%if 0%{?fedora} || 0%{?rhel} >= 9
# Setting this macro ensures that only clang supported options will be
# added to ldflags and cflags.
%global toolchain clang
%set_build_flags
%else
# Filter flags not supported by clang
%global dotnet_cflags %(echo %optflags | sed -re 's/-specs=[^ ]*//g')
%global dotnet_ldflags %(echo %{__global_ldflags} | sed -re 's/-specs=[^ ]*//g')
export CFLAGS="%{dotnet_cflags}"
export CXXFLAGS="%{dotnet_cflags}"
export LDFLAGS="%{dotnet_ldflags}"
%endif

CFLAGS="$CFLAGS -Wno-used-but-marked-unused"
CXXFLAGS="$CXXFLAGS -Wno-used-but-marked-unused"

# -fstack-clash-protection breaks CoreCLR
CFLAGS=$(echo $CFLAGS  | sed -e 's/-fstack-clash-protection//' )
CXXFLAGS=$(echo $CXXFLAGS  | sed -e 's/-fstack-clash-protection//' )

%ifarch aarch64
# -mbranch-protection=standard breaks unwinding in CoreCLR through libunwind
CFLAGS=$(echo $CFLAGS | sed -e 's/-mbranch-protection=standard //')
CXXFLAGS=$(echo $CXXFLAGS | sed -e 's/-mbranch-protection=standard //')
%endif

%ifarch s390x
# -march=z13 -mtune=z14 makes clang crash while compiling .NET
CFLAGS=$(echo $CFLAGS | sed -e 's/ -march=z13//')
CFLAGS=$(echo $CFLAGS | sed -e 's/ -mtune=z14//')
CXXFLAGS=$(echo $CXXFLAGS | sed -e 's/ -march=z13//')
CXXFLAGS=$(echo $CXXFLAGS | sed -e 's/ -mtune=z14//')
%endif

%if 0%{rhel} >= 10
# Workaround for https://github.com/dotnet/runtime/issues/109611
# FIXME: Remove this, and replace with upstream fix
CFLAGS=$(echo $CFLAGS | sed -e 's/-march=x86-64-v3 //')
CXXFLAGS=$(echo $CXXFLAGS | sed -e 's/-march=x86-64-v3 //')
LDFLAGS=$(echo $LDFLAGS | sed -e 's/-march=x86-64-v3 //')
%endif

export EXTRA_CFLAGS="$CFLAGS"
export EXTRA_CXXFLAGS="$CXXFLAGS"
export EXTRA_LDFLAGS="$LDFLAGS"

# Disable tracing, which is incompatible with certain versions of
# lttng See https://github.com/dotnet/runtime/issues/57784. The
# suggested compile-time change doesn't work, unfortunately.
export COMPlus_LTTng=0

VERBOSE=1 timeout 5h \
    ./build.sh \
%if %{without bootstrap}
    --with-sdk previously-built-dotnet \
%endif
%ifarch %{mono_archs}
    --use-mono-runtime \
%endif
    --release-manifest %{SOURCE5} \
    -- \
    /p:MinimalConsoleLogOutput=false \
    /p:ContinueOnPrebuiltBaselineError=true \
    /v:n \
    /p:LogVerbosity=n \


sed -e 's|[@]LIBDIR[@]|%{_libdir}|g' %{SOURCE21} > dotnet.sh


%install
install -dm 0755 %{buildroot}%{_libdir}/dotnet
ls artifacts/%{runtime_arch}/Release
mkdir -p built-sdk
tar xf artifacts/%{runtime_arch}/Release/dotnet-sdk-%{sdk_version}-%{runtime_id}.tar.gz -C built-sdk/

# Convert hardlinks to actual copies. This takes up quite a bit of
# extra disk space, but works around issues in post-rpmbuild tools
# when they encounter hardlinks.
cp -r --preserve=mode,ownership,timestamps built-sdk/* %{buildroot}%{_libdir}/dotnet/
ls %{buildroot}%{_libdir}/dotnet

# Delete bundled certificates: we want to use the system store only,
# except for when we have no other choice and ca-certificates doesn't
# provide it. Currently ca-ceritificates has no support for
# timestamping certificates (timestamp.ctl).
find %{buildroot}%{_libdir}/dotnet -name 'codesignctl.pem' -delete
if [[ $(find %{buildroot}%{_libdir}/dotnet -name '*.pem' -print | wc -l) != 1 ]]; then
    find %{buildroot}%{_libdir}/dotnet -name '*.pem' -print
    echo "too many certificate bundles"
    exit 2
fi

# Install managed symbols
tar xf artifacts/%{runtime_arch}/Release/dotnet-symbols-sdk-%{sdk_version}*-%{runtime_id}.tar.gz \
   -C %{buildroot}%{_libdir}/dotnet/
find %{buildroot}%{_libdir}/dotnet/packs -iname '*.pdb' -delete

# Fix executable permissions on files
find %{buildroot}%{_libdir}/dotnet/ -type f -name 'apphost' -exec chmod +x {} \;
find %{buildroot}%{_libdir}/dotnet/ -type f -name 'singlefilehost' -exec chmod +x {} \;
find %{buildroot}%{_libdir}/dotnet/ -type f -name 'lib*so' -exec chmod +x {} \;
find %{buildroot}%{_libdir}/dotnet/ -type f -name '*.a' -exec chmod -x {} \;
find %{buildroot}%{_libdir}/dotnet/ -type f -name '*.dll' -exec chmod -x {} \;
find %{buildroot}%{_libdir}/dotnet/ -type f -name '*.h' -exec chmod 0644 {} \;
find %{buildroot}%{_libdir}/dotnet/ -type f -name '*.json' -exec chmod -x {} \;
find %{buildroot}%{_libdir}/dotnet/ -type f -name '*.pdb' -exec chmod -x {} \;
find %{buildroot}%{_libdir}/dotnet/ -type f -name '*.props' -exec chmod -x {} \;
find %{buildroot}%{_libdir}/dotnet/ -type f -name '*.pubxml' -exec chmod -x {} \;
find %{buildroot}%{_libdir}/dotnet/ -type f -name '*.targets' -exec chmod -x {} \;
find %{buildroot}%{_libdir}/dotnet/ -type f -name '*.txt' -exec chmod -x {} \;
find %{buildroot}%{_libdir}/dotnet/ -type f -name '*.xml' -exec chmod -x {} \;

install -dm 0755 %{buildroot}%{_sysconfdir}/profile.d/
install dotnet.sh %{buildroot}%{_sysconfdir}/profile.d/

install -dm 0755 %{buildroot}/%{_datadir}/bash-completion/completions
# dynamic completion needs the file to be named the same as the base command
install src/sdk/scripts/register-completions.bash %{buildroot}/%{_datadir}/bash-completion/completions/dotnet

# TODO: the zsh completion script needs to be ported to use #compdef
#install -dm 755 %%{buildroot}/%%{_datadir}/zsh/site-functions
#install src/cli/scripts/register-completions.zsh %%{buildroot}/%%{_datadir}/zsh/site-functions/_dotnet

install -dm 0755 %{buildroot}%{_bindir}
ln -s ../../%{_libdir}/dotnet/dotnet %{buildroot}%{_bindir}/

for section in 1 7; do
    install -dm 0755 %{buildroot}%{_mandir}/man${section}/
    find -iname 'dotnet*'.${section} -type f -exec install -m 0644 {} %{buildroot}%{_mandir}/man${section}/ \;
done

install -dm 0755 %{buildroot}%{_sysconfdir}/dotnet
echo "%{_libdir}/dotnet" >> install_location
install install_location %{buildroot}%{_sysconfdir}/dotnet/
echo "%{_libdir}/dotnet" >> install_location_%{runtime_arch}
install install_location_%{runtime_arch} %{buildroot}%{_sysconfdir}/dotnet/

install -dm 0755 %{buildroot}%{_libdir}/dotnet/source-built-artifacts
install -m 0644 artifacts/%{runtime_arch}/Release/Private.SourceBuilt.Artifacts.*.tar.gz %{buildroot}/%{_libdir}/dotnet/source-built-artifacts/


# Quick and dirty check for https://github.com/dotnet/source-build/issues/2731
test -f %{buildroot}%{_libdir}/dotnet/sdk/%{sdk_version}/Sdks/Microsoft.NET.Sdk/Sdk/Sdk.props

# Check debug symbols in all elf objects. This is not in %%check
# because native binaries are stripped by rpm-build after %%install.
# So we need to do this check earlier.
echo "Testing build results for debug symbols..."
%{SOURCE20} -v %{buildroot}%{_libdir}/dotnet/

install -dm 0755 %{buildroot}%{_rpmmacrodir}/
install -m 0644 %{SOURCE10} %{buildroot}%{_rpmmacrodir}/

find %{buildroot}%{_libdir}/dotnet/shared/Microsoft.NETCore.App -type f -and -not -name '*.pdb' | sed -E 's|%{buildroot}||' > dotnet-runtime-non-dbg-files
find %{buildroot}%{_libdir}/dotnet/shared/Microsoft.NETCore.App -type f -name '*.pdb'  | sed -E 's|%{buildroot}||' > dotnet-runtime-dbg-files
find %{buildroot}%{_libdir}/dotnet/shared/Microsoft.AspNetCore.App -type f -and -not -name '*.pdb'  | sed -E 's|%{buildroot}||' > aspnetcore-runtime-non-dbg-files
find %{buildroot}%{_libdir}/dotnet/shared/Microsoft.AspNetCore.App -type f -name '*.pdb' | sed -E 's|%{buildroot}||' > aspnetcore-runtime-dbg-files
find %{buildroot}%{_libdir}/dotnet/sdk -type d | tail -n +2 | sed -E 's|%{buildroot}||' | sed -E 's|^|%dir |' > dotnet-sdk-non-dbg-files
find %{buildroot}%{_libdir}/dotnet/sdk -type f -and -not -name '*.pdb' | sed -E 's|%{buildroot}||' >> dotnet-sdk-non-dbg-files
find %{buildroot}%{_libdir}/dotnet/sdk -type f -name '*.pdb'  | sed -E 's|%{buildroot}||' > dotnet-sdk-dbg-files


%check
%if 0%{?fedora} > 35
# lttng in Fedora > 35 is incompatible with .NET
export COMPlus_LTTng=0
%endif

%{buildroot}%{_libdir}/dotnet/dotnet --info
%{buildroot}%{_libdir}/dotnet/dotnet --version


%if ( 0%{?fedora} && 0%{?fedora} < 38 ) || ( 0%{?rhel} && 0%{?rhel} < 9 )
%files -n dotnet
# empty package useful for dependencies
%endif

%files -n dotnet-host
%dir %{_libdir}/dotnet
%{_libdir}/dotnet/dotnet
%dir %{_libdir}/dotnet/host
%dir %{_libdir}/dotnet/host/fxr
%{_bindir}/dotnet
%license %{_libdir}/dotnet/LICENSE.txt
%license %{_libdir}/dotnet/ThirdPartyNotices.txt
%doc %{_mandir}/man1/dotnet*.1.*
%doc %{_mandir}/man7/dotnet*.7.*
%config(noreplace) %{_sysconfdir}/profile.d/dotnet.sh
%config(noreplace) %{_sysconfdir}/dotnet
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/dotnet
%{_rpmmacrodir}/macros.dotnet

%files -n dotnet-hostfxr-%{dotnetver}
%dir %{_libdir}/dotnet/host/fxr
%{_libdir}/dotnet/host/fxr/%{host_version}

%files -n dotnet-runtime-%{dotnetver} -f dotnet-runtime-non-dbg-files
%dir %{_libdir}/dotnet/shared
%dir %{_libdir}/dotnet/shared/Microsoft.NETCore.App
%dir %{_libdir}/dotnet/shared/Microsoft.NETCore.App/%{runtime_version}

%files -n dotnet-runtime-dbg-%{dotnetver} -f dotnet-runtime-dbg-files

%files -n aspnetcore-runtime-%{dotnetver} -f aspnetcore-runtime-non-dbg-files
%dir %{_libdir}/dotnet/shared
%dir %{_libdir}/dotnet/shared/Microsoft.AspNetCore.App
%dir %{_libdir}/dotnet/shared/Microsoft.AspNetCore.App/%{aspnetcore_runtime_version}

%files -n aspnetcore-runtime-dbg-%{dotnetver} -f aspnetcore-runtime-dbg-files

%files -n dotnet-templates-%{dotnetver}
%dir %{_libdir}/dotnet/templates
%{_libdir}/dotnet/templates/%{templates_version}

%files -n dotnet-sdk-%{dotnetver} -f dotnet-sdk-non-dbg-files
%dir %{_libdir}/dotnet/sdk
%dir %{_libdir}/dotnet/sdk-manifests
%{_libdir}/dotnet/sdk-manifests/%{sdk_feature_band_version}*
%{_libdir}/dotnet/metadata
%dir %{_libdir}/dotnet/packs
%dir %{_libdir}/dotnet/packs/Microsoft.AspNetCore.App.Runtime.%{runtime_id}
%{_libdir}/dotnet/packs/Microsoft.AspNetCore.App.Runtime.%{runtime_id}/%{aspnetcore_runtime_version}
%dir %{_libdir}/dotnet/packs/Microsoft.NETCore.App.Runtime.%{runtime_id}
%{_libdir}/dotnet/packs/Microsoft.NETCore.App.Runtime.%{runtime_id}/%{runtime_version}

%files -n dotnet-sdk-dbg-%{dotnetver} -f dotnet-sdk-dbg-files

%files -n dotnet-sdk-%{dotnetver}-source-built-artifacts
%dir %{_libdir}/dotnet
%{_libdir}/dotnet/source-built-artifacts


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Dec 10 2024 Omair Majid <omajid@redhat.com> - 8.0.111-2
- Fix ELN build
- Resolves: RHBZ#2321109

* Mon Nov 18 2024 Omair Majid <omajid@redhat.com> - 8.0.111-1
- Update to .NET SDK 8.0.111 and Runtime 8.0.11

* Fri Oct 11 2024 Omair Majid <omajid@redhat.com> - 8.0.110-1
- Update to .NET SDK 8.0.110 and Runtime 8.0.10

* Fri Sep 27 2024 Omair Majid <omajid@redhat.com> - 8.0.108-2
- Support building without ENGINE support in OpenSSL

* Tue Aug 13 2024 Omair Majid <omajid@redhat.com> - 8.0.108-1
- Update to .NET SDK 8.0.108 and Runtime 8.0.8

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.107-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jul 09 2024 Omair Majid <omajid@redhat.com> - 8.0.107-1
- Update to .NET SDK 8.0.107 and Runtime 8.0.7

* Wed Jul 03 2024 Omair Majid <omajid@redhat.com> - 8.0.105-1
- Fix ownership of some missed directories

* Tue May 14 2024 Omair Majid <omajid@redhat.com> - 8.0.105-1
- Update to .NET SDK 8.0.105 and Runtime 8.0.5

* Tue Apr 09 2024 Omair Majid <omajid@redhat.com> - 8.0.104-1
- Update to .NET SDK 8.0.104 and Runtime 8.0.4

* Tue Mar 26 2024 Omair Majid <omajid@redhat.com> - 8.0.103-1
- Update to .NET SDK 8.0.103 and Runtime 8.0.3
- Add dotnet.macros with %%dotnet_runtime_arch and %%dotnet_runtime_id

* Wed Feb 14 2024 Omair Majid <omajid@redhat.com> - 8.0.102-1
- Update to .NET SDK 8.0.102 and Runtime 8.0.2

* Fri Jan 26 2024 Omair Majid <omajid@redhat.com> - 8.0.101-4
- Rebuild to add new -dbg subpackages

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.101-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 09 2024 Omair Majid <omajid@redhat.com> - 8.0.101-1
- Update to .NET SDK 8.0.101 and Runtime 8.0.1

* Tue Dec 12 2023 Omair Majid <omajid@redhat.com> - 8.0.100-2
- Enable gpg signature verification

* Sat Dec 09 2023 Omair Majid <omajid@redhat.com> - 8.0.100-1
- Update to .NET SDK 8.0.100 and Runtime 8.0.0

* Fri Dec 08 2023 Omair Majid <omajid@redhat.com> - 8.0.100~rc.2-0.1
- Update to .NET SDK 8.0.100 RC 2 and Runtime 8.0.0 RC 2

* Fri Dec 08 2023 Omair Majid <omajid@redhat.com> - 8.0.100~rc.1-0.2
- Add various fixes from CentOS Stream 9

* Fri Sep 15 2023 Omair Majid <omajid@redhat.com> - 8.0.100~rc.1-0.1
- Update to .NET SDK 8.0.100 RC 1 and Runtime 8.0.0 RC 1

* Fri Aug 11 2023 Omair Majid <omajid@redhat.com> - 8.0.100~preview.7-0.1
- Update to .NET SDK 8.0.100 Preview 7 and Runtime 8.0.0 Preview 7

* Tue Jul 18 2023 Omair Majid <omajid@redhat.com> - 8.0.100~preview.6-0.2
- Remove lttng and other tracing-specific dependencies from the runtime package

* Mon Jul 17 2023 Omair Majid <omajid@redhat.com> - 8.0.100~preview.6-0.1
- Update to .NET SDK 8.0.100 Preview 6 and Runtime 8.0.0 Preview 6

* Fri Jun 23 2023 Omair Majid <omajid@redhat.com> - 8.0.100~preview.5-0.2
- Fix release.json and sourcelink references

* Mon Jun 19 2023 Omair Majid <omajid@redhat.com> - 8.0.100~preview.5-0.1
- Update to .NET SDK 8.0.100 Preview 5 and Runtime 8.0.0 Preview 5

* Wed Apr 12 2023 Omair Majid <omajid@redhat.com> - 8.0.100~preview.3-0.1
- Update to .NET SDK 8.0.100 Preview 3 and Runtime 8.0.0 Preview 3

* Wed Mar 15 2023 Omair Majid <omajid@redhat.com> - 8.0.100~preview.2-0.1
- Update to .NET SDK 8.0.100 Preview 2 and Runtime 8.0.0 Preview 2

* Wed Feb 22 2023 Omair Majid <omajid@redhat.com> - 8.0.100~preview.1-0.1
- Update to .NET SDK 8.0.100 Preview 1 and Runtime 8.0.0 Preview 1

* Thu Jan 12 2023 Omair Majid <omajid@redhat.com> - 7.0.102-1
- Update to .NET SDK 7.0.102 and Runtime 7.0.2

* Wed Jan 11 2023 Omair Majid <omajid@redhat.com> - 7.0.101-1
- Update to .NET SDK 7.0.101 and Runtime 7.0.1

* Tue Jan 10 2023 Omair Majid <omajid@redhat.com> - 7.0.100-1
- Update to .NET SDK 7.0.100 and Runtime 7.0.0

* Thu Nov 10 2022 Omair Majid <omajid@redhat.com> - 7.0.100-0.1
- Update to .NET 7 RC 2

* Wed May 11 2022 Omair Majid <omajid@redhat.com> - 6.0.105-1
- Update to .NET SDK 6.0.105 and Runtime 6.0.5

* Tue Apr 12 2022 Omair Majid <omajid@redhat.com> - 6.0.104-1
- Update to .NET SDK 6.0.104 and Runtime 6.0.4

* Thu Mar 10 2022 Omair Majid <omajid@redhat.com> - 6.0.103-1
- Update to .NET SDK 6.0.103 and Runtime 6.0.3

* Mon Feb 14 2022 Omair Majid <omajid@redhat.com> - 6.0.102-1
- Update to .NET SDK 6.0.102 and Runtime 6.0.2

* Fri Jan 28 2022 Omair Majid <omajid@redhat.com> - 6.0.101-3
- Update to .NET SDK 6.0.101 and Runtime 6.0.1

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.100-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 20 2021 Omair Majid <omajid@redhat.com> - 6.0.100-2
- Disable bootstrap

* Sun Dec 19 2021 Omair Majid <omajid@redhat.com> - 6.0.100-1
- Update to .NET 6

* Fri Oct 22 2021 Omair Majid <omajid@redhat.com> - 6.0.0-0.7.rc2
- Update to .NET 6 RC2

* Fri Oct 08 2021 Omair Majid <omajid@redhat.com> - 6.0.0-0.6.28be3e9a006d90d8c6e87d4353b77882829df718
- Enable building on arm64
- Related: RHBZ#1986017

* Sun Oct 03 2021 Omair Majid <omajid@redhat.com> - 6.0.0-0.5.28be3e9a006d90d8c6e87d4353b77882829df718
- Enable building on s390x
- Related: RHBZ#1986017

* Sun Oct 03 2021 Omair Majid <omajid@redhat.com> - 6.0.0-0.4.28be3e9a006d90d8c6e87d4353b77882829df718
- Clean up tarball and add initial support for s390x
- Related: RHBZ#1986017

* Sun Sep 26 2021 Omair Majid <omajid@redhat.com> - 6.0.0-0.3.28be3e9a006d90d8c6e87d4353b77882829df718
- Update to work-in-progress RC2 release

* Wed Aug 25 2021 Omair Majid <omajid@redhat.com> - 6.0.0-0.2.preview6
- Updated to build the latest source-build preview

* Fri Jul 23 2021 Omair Majid <omajid@redhat.com> - 6.0.0-0.1.preview6
- Initial package for .NET 6

* Thu Jun 10 2021 Omair Majid <omajid@redhat.com> - 5.0.204-1
- Update to .NET SDK 5.0.204 and Runtime 5.0.7

* Wed May 12 2021 Omair Majid <omajid@redhat.com> - 5.0.203-1
- Update to .NET SDK 5.0.203 and Runtime 5.0.6

* Wed Apr 14 2021 Omair Majid <omajid@redhat.com> - 5.0.202-1
- Update to .NET SDK 5.0.202 and Runtime 5.0.5

* Tue Apr 06 2021 Omair Majid <omajid@redhat.com> - 5.0.104-2
- Mark files under /etc/ as config(noreplace)
- Add an rpm-inspect configuration file
- Add an rpmlintrc file
- Enable gating for release branches and ELN too

* Tue Mar 16 2021 Omair Majid <omajid@redhat.com> - 5.0.104-1
- Update to .NET SDK 5.0.104 and Runtime 5.0.4
- Drop unneeded/upstreamed patches

* Wed Feb 17 2021 Omair Majid <omajid@redhat.com> - 5.0.103-2
- Add Fedora 35 RIDs

* Thu Feb 11 2021 Omair Majid <omajid@redhat.com> - 5.0.103-1
- Update to .NET SDK 5.0.103 and Runtime 5.0.3

* Fri Jan 29 2021 Omair Majid <omajid@redhat.com> - 5.0.102-2
- Disable bootstrap

* Fri Dec 18 2020 Omair Majid <omajid@redhat.com> - 5.0.100-2
- Update to .NET Core Runtime 5.0.0 and SDK 5.0.100 commit 9c4e5de

* Fri Dec 04 2020 Omair Majid <omajid@redhat.com> - 5.0.100-1
- Update to .NET Core Runtime 5.0.0 and SDK 5.0.100

* Thu Dec 03 2020 Omair Majid <omajid@redhat.com> - 5.0.100-0.4.20201202git337413b
- Update to latest 5.0 pre-GA commit

* Tue Nov 24 2020 Omair Majid <omajid@redhat.com> - 5.0.100-0.4.20201123gitdee899c
- Update to 5.0 pre-GA commit

* Mon Sep 14 2020 Omair Majid <omajid@redhat.com> - 5.0.100-0.3.preview8
- Update to Preview 8

* Fri Jul 10 2020 Omair Majid <omajid@redhat.com> - 5.0.100-0.2.preview4
- Fix building with custom CFLAGS/CXXFLAGS/LDFLAGS
- Clean up patches

* Mon Jul 06 2020 Omair Majid <omajid@redhat.com> - 5.0.100-0.1.preview4
- Initial build

* Sat Jun 27 2020 Omair Majid <omajid@redhat.com> - 3.1.105-4
- Disable bootstrap

* Fri Jun 26 2020 Omair Majid <omajid@redhat.com> - 3.1.105-3
- Re-bootstrap aarch64

* Fri Jun 19 2020 Omair Majid <omajid@redhat.com> - 3.1.105-3
- Disable bootstrap

* Thu Jun 18 2020 Omair Majid <omajid@redhat.com> - 3.1.105-1
- Bootstrap aarch64

* Tue Jun 16 2020 Chris Rummel <crummel@microsoft.com> - 3.1.105-1
- Update to .NET Core Runtime 3.1.5 and SDK 3.1.105

* Fri Jun 05 2020 Chris Rummel <crummel@microsoft.com> - 3.1.104-1
- Update to .NET Core Runtime 3.1.4 and SDK 3.1.104

* Thu Apr 09 2020 Chris Rummel <crummel@microsoft.com> - 3.1.103-1
- Update to .NET Core Runtime 3.1.3 and SDK 3.1.103

* Mon Mar 16 2020 Omair Majid <omajid@redhat.com> - 3.1.102-1
- Update to .NET Core Runtime 3.1.2 and SDK 3.1.102

* Fri Feb 28 2020 Omair Majid <omajid@redhat.com> - 3.1.101-4
- Disable bootstrap

* Fri Feb 28 2020 Omair Majid <omajid@redhat.com> - 3.1.101-3
- Enable bootstrap
- Add Fedora 33 runtime ids

* Thu Feb 27 2020 Omair Majid <omajid@redhat.com> - 3.1.101-2
- Disable bootstrap

* Tue Jan 21 2020 Omair Majid <omajid@redhat.com> - 3.1.101-1
- Update to .NET Core Runtime 3.1.1 and SDK 3.1.101

* Thu Dec 05 2019 Omair Majid <omajid@redhat.com> - 3.1.100-1
- Update to .NET Core Runtime 3.1.0 and SDK 3.1.100

* Mon Nov 18 2019 Omair Majid <omajid@redhat.com> - 3.1.100-0.4.preview3
- Fix apphost permissions

* Fri Nov 15 2019 Omair Majid <omajid@redhat.com> - 3.1.100-0.3.preview3
- Update to .NET Core Runtime 3.1.0-preview3.19553.2 and SDK
  3.1.100-preview3-014645

* Wed Nov 06 2019 Omair Majid <omajid@redhat.com> - 3.1.100-0.2
- Update to .NET Core 3.1 Preview 2

* Wed Oct 30 2019 Omair Majid <omajid@redhat.com> - 3.1.100-0.1
- Update to .NET Core 3.1 Preview 1

* Thu Oct 24 2019 Omair Majid <omajid@redhat.com> - 3.0.100-5
- Add cgroupv2 support to .NET Core

* Wed Oct 16 2019 Omair Majid <omajid@redhat.com> - 3.0.100-4
- Include fix from coreclr for building on Fedora 32

* Wed Oct 16 2019 Omair Majid <omajid@redhat.com> - 3.0.100-3
- Harden built binaries to pass annocheck

* Fri Oct 11 2019 Omair Majid <omajid@redhat.com> - 3.0.100-2
- Export DOTNET_ROOT in profile to make apphost lookup work

* Fri Sep 27 2019 Omair Majid <omajid@redhat.com> - 3.0.100-1
- Update to .NET Core Runtime 3.0.0 and SDK 3.0.100

* Wed Sep 25 2019 Omair Majid <omajid@redhat.com> - 3.0.100-0.18.rc1
- Update to .NET Core Runtime 3.0.0-rc1-19456-20 and SDK 3.0.100-rc1-014190

* Tue Sep 17 2019 Omair Majid <omajid@redhat.com> - 3.0.100-0.16.preview9
- Fix files duplicated between dotnet-apphost-pack-3.0 and dotnet-targeting-pack-3.0
- Fix dependencies between .NET SDK and the targeting packs

* Mon Sep 16 2019 Omair Majid <omajid@redhat.com> - 3.0.100-0.15.preview9
- Update to .NET Core Runtime 3.0.0-preview 9 and SDK 3.0.100-preview9

* Mon Aug 19 2019 Omair Majid <omajid@redhat.com> - 3.0.100-0.11.preview8
- Update to .NET Core Runtime 3.0.0-preview8-28405-07 and SDK
  3.0.100-preview8-013656

* Tue Jul 30 2019 Omair Majid <omajid@redhat.com> - 3.0.100-0.9.preview7
- Update to .NET Core Runtime 3.0.0-preview7-27912-14 and SDK
  3.0.100-preview7-012821

* Fri Jul 26 2019 Omair Majid <omajid@redhat.com> - 3.0.100-0.8.preview7
- Update to .NET Core Runtime 3.0.0-preview7-27902-19 and SDK
  3.0.100-preview7-012802

* Wed Jun 26 2019 Omair Majid <omajid@redhat.com> - 3.0.0-0.7.preview6
- Obsolete dotnet-sdk-3.0.1xx
- Add supackages for targeting packs
- Add -fcf-protection to CFLAGS

* Wed Jun 26 2019 Omair Majid <omajid@redhat.com> - 3.0.0-0.6.preview6
- Update to .NET Core Runtime 3.0.0-preview6-27804-01 and SDK 3.0.100-preview6-012264
- Set dotnet installation location in /etc/dotnet/install_location
- Update targeting packs
- Install managed symbols
- Completely conditionalize libunwind bundling

* Tue May 07 2019 Omair Majid <omajid@redhat.com> - 3.0.0-0.3.preview4
- Update to .NET Core 3.0 preview 4

* Tue Dec 18 2018 Omair Majid <omajid@redhat.com> - 3.0.0-0.1.preview1
- Update to .NET Core 3.0 preview 1

* Fri Dec 07 2018 Omair Majid <omajid@redhat.com> - 2.2.100
- Update to .NET Core 2.2.0

* Wed Nov 07 2018 Omair Majid <omajid@redhat.com> - 2.2.100-0.2.preview3
- Update to .NET Core 2.2.0-preview3

* Fri Nov 02 2018 Omair Majid <omajid@redhat.com> - 2.1.403-3
- Add host-fxr-2.1 subpackage

* Mon Oct 15 2018 Omair Majid <omajid@redhat.com> - 2.1.403-2
- Disable telemetry by default
- Users have to manually export DOTNET_CLI_TELEMETRY_OPTOUT=0 to enable

* Tue Oct 02 2018 Omair Majid <omajid@redhat.com> - 2.1.403-1
- Update to .NET Core Runtime 2.1.5 and SDK 2.1.403

* Wed Sep 26 2018 Omair Majid <omajid@redhat.com> - 2.1.402-2
- Add ~/.dotnet/tools to $PATH to make it easier to use dotnet tools

* Thu Sep 13 2018 Omair Majid <omajid@redhat.com> - 2.1.402-1
- Update to .NET Core Runtime 2.1.4 and SDK 2.1.402

* Wed Sep 05 2018 Omair Majid <omajid@redhat.com> - 2.1.401-2
- Use distro-standard flags when building .NET Core

* Tue Aug 21 2018 Omair Majid <omajid@redhat.com> - 2.1.401-1
- Update to .NET Core Runtime 2.1.3 and SDK 2.1.401

* Mon Aug 20 2018 Omair Majid <omajid@redhat.com> - 2.1.302-1
- Update to .NET Core Runtime 2.1.2 and SDK 2.1.302

* Fri Jul 20 2018 Omair Majid <omajid@redhat.com> - 2.1.301-1
- Update to .NET Core 2.1

* Thu May 03 2018 Omair Majid <omajid@redhat.com> - 2.0.7-1
- Update to .NET Core 2.0.7

* Wed Mar 28 2018 Omair Majid <omajid@redhat.com> - 2.0.6-2
- Enable bash completion for dotnet
- Remove redundant buildrequires and requires

* Wed Mar 14 2018 Omair Majid <omajid@redhat.com> - 2.0.6-1
- Update to .NET Core 2.0.6

* Fri Feb 23 2018 Omair Majid <omajid@redhat.com> - 2.0.5-1
- Update to .NET Core 2.0.5

* Wed Jan 24 2018 Omair Majid <omajid@redhat.com> - 2.0.3-5
- Don't apply corefx clang warnings fix on clang < 5

* Fri Jan 19 2018 Omair Majid <omajid@redhat.com> - 2.0.3-4
- Add a test script to sanity check debug and symbol info.
- Build with clang 5.0
- Make main package real instead of using a virtual provides (see RHBZ 1519325)

* Wed Nov 29 2017 Omair Majid <omajid@redhat.com> - 2.0.3-3
- Add a Provides for 'dotnet'
- Fix conditional macro

* Tue Nov 28 2017 Omair Majid <omajid@redhat.com> - 2.0.3-2
- Fix build on Fedora 27

* Fri Nov 17 2017 Omair Majid <omajid@redhat.com> - 2.0.3-1
- Update to .NET Core 2.0.3

* Thu Oct 19 2017 Omair Majid <omajid@redhat.com> - 2.0.0-4
- Add a hack to let omnisharp work

* Wed Aug 30 2017 Omair Majid <omajid@redhat.com> - 2.0.0-3
- Add a patch for building coreclr and core-setup correctly on Fedora >= 27

* Fri Aug 25 2017 Omair Majid <omajid@redhat.com> - 2.0.0-2
- Move libicu/libcurl/libunwind requires to runtime package
- Make sdk depend on the exact version of the runtime package

* Thu Aug 24 2017 Omair Majid <omajid@redhat.com> - 2.0.0-1
- Update to 2.0.0 final release

* Wed Jul 26 2017 Omair Majid <omajid@redhat.com> - 2.0.0-0.3.preview2
- Add man pages

* Tue Jul 25 2017 Omair Majid <omajid@redhat.com> - 2.0.0-0.2.preview2
- Add Requires on libicu
- Split into multiple packages
- Do not repeat first-run message

* Fri Jul 21 2017 Omair Majid <omajid@redhat.com> - 2.0.0-0.1.preview2
- Update to .NET Core 2.0 Preview 2

* Thu Mar 16 2017 Nemanja Milošević <nmilosevnm@gmail.com> - 1.1.0-7
- rebuilt with latest libldb
* Wed Feb 22 2017 Nemanja Milosevic <nmilosev@fedoraproject.org> - 1.1.0-6
- compat-openssl 1.0 for F26 for now
* Sun Feb 19 2017 Nemanja Milosevic <nmilosev@fedoraproject.org> - 1.1.0-5
- Fix wrong commit id's
* Sat Feb 18 2017 Nemanja Milosevic <nmilosev@fedoraproject.org> - 1.1.0-4
- Use commit id's instead of branch names
* Sat Feb 18 2017 Nemanja Milosevic <nmilosev@fedoraproject.org> - 1.1.0-3
- Improper patch5 fix
* Sat Feb 18 2017 Nemanja Milosevic <nmilosev@fedoraproject.org> - 1.1.0-2
- SPEC cleanup
- git removal (using all tarballs for reproducible builds)
- more reasonable versioning
* Thu Feb 09 2017 Nemanja Milosevic <nmilosev@fedoraproject.org> - 1.1.0-1
- Fixed debuginfo going to separate package (Patch1)
- Added F25/F26 RIL and fixed the version info (Patch2)
- Added F25/F26 RIL in Microsoft.NETCore.App suported runtime graph (Patch3)
- SPEC file cleanup
* Wed Jan 11 2017 Nemanja Milosevic <nmilosev@fedoraproject.org> - 1.1.0-0
- Initial RPM for Fedora 25/26.
