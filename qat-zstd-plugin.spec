Name:		qat-zstd-plugin
Version:	0.2.0
Release:	%autorelease
Summary:	Intel QuickAssist Technology ZSTD Plugin

License:	BSD-3-Clause
URL:		https://github.com/intel/QAT-ZSTD-Plugin
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:		qat-fedora.patch

BuildRequires:	automake
BuildRequires:	gcc
BuildRequires:	libzstd-devel
BuildRequires:	libzstd-static
BuildRequires:	qatlib-devel

# Upstream only supports x86_64
ExclusiveArch:	x86_64

%description
Intel QuickAssist Technology ZSTD is a plugin to Zstandard for accelerating
compression by QAT. ZSTD* is a fast lossless compression algorithm, targeting
real-time compression scenarios at zlib-level and better compression ratios.

%prep
%autosetup -p1 -n QAT-ZSTD-Plugin-%{version}

%build
%make_build
make test

%install
install -D -p -m 644 src/qatseqprod.h %{buildroot}%{_includedir}/qatseqprod.h
install -D -p -m 755 src/libqatseqprod.so %{buildroot}%{_libdir}/libqatseqprod.so

%check
export LD_LIBRARY_PATH=%{buildroot}/%{_libdir}
./test/test README.md

%files
%license LICENSE
%{_includedir}/qatseqprod.h
%{_libdir}/libqatseqprod.so

%changelog
%autochangelog
