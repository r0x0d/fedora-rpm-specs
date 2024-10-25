%global     npm_name cjs-module-lexer
%global     prebuilt_blobs lib/lexer.wasm

%bcond      wasm_opt %{undefined rhel}

Name:       nodejs-%{npm_name}
Summary:    A very fast lexer used to detect the named exports of a CommonJS module
Version:    1.4.1
Release:    %autorelease

License:    MIT
URL:        https://www.npmjs.com/package/cjs-module-lexer
# The npmjs.org archive does not contain sources, only built artifacts
Source:     https://github.com/nodejs/%{npm_name}/archive/%{version}/%{npm_name}-%{version}.tar.gz
# Production archive is not needed
Source2:     %{npm_name}-%{version}-nm-dev.tgz
Source3:     %{npm_name}-%{version}-bundled-licenses.txt

# Binary files in this package are aimed at the wasm32-wasi "architecture".
%global     _binaries_in_noarch_packages_terminate_build 0
BuildArch:  noarch
# LLVM/lld 19 added support for s390x
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 11
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 aarch64 ppc64le riscv64 noarch
%endif

BuildRequires: clang lld make wasi-libc-devel
BuildRequires: nodejs-devel npm
%if %{with wasm_opt}
BuildRequires: binaryen
%endif
# for autosetup -S git_am
BuildRequires: git-core

%description
A very fast JS CommonJS module syntax lexer used to detect the most likely list
of named exports of a CommonJS module.  This project is used in Node.js core
for detecting the named exports available when importing a CJS module into ESM,
and is maintained for this purpose.

%prep
%autosetup -n %{npm_name}-%{version} -S git_am
cp -p %{S:3} .

%build
rm -rf %{prebuilt_blobs}
tar -xzf %{S:2} && ln -rsf node_modules_dev node_modules

%make_build -j1 \
    WASM_CC=clang \
    WASM_CFLAGS='--target=wasm32-wasi --sysroot=/usr/wasm32-wasi' \
    WASM_LDFLAGS='-nostartfiles -nodefaultlibs -lc' \
    %{?with_wasm_opt:WASM_OPT=/usr/bin/wasm-opt} \
    clean lib/lexer.wasm %{?with_wasm_opt:optimize}

npm --offline run build
npm --offline pack

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
tar --strip-components=1 -xzf %{npm_name}-%{version}.tgz -C %{buildroot}%{nodejs_sitelib}/%{npm_name}

%check
%{__nodejs} -e 'require("./")'
%nodejs_symlink_deps --check
npm --offline run test

%files
%license LICENSE %{npm_name}-%{version}-bundled-licenses.txt
%doc README.md
%dir %{nodejs_sitelib}
%{nodejs_sitelib}/%{npm_name}/

%changelog
%autochangelog
