Name:		fes
Version:	0.2
Release:	13%{?dist}
License:	GPL-2.0-or-later
Summary:	Fast Exhaustive Search
URL:		https://www-almasty.lip6.fr/~bouillaguet/implementation.html
Source0:	https://bitbucket.org/fes/fes/downloads/%{name}-%{version}.spkg
ExclusiveArch:	%{ix86} x86_64
# Fix various problems with the configure script and configuration headers
# 1. @VARIABLE@ expressions are not replaced in src/config.h
# 2. The Fedora optimization flag is overridden with -O3
# 3. -Werror causes build failures
# 4. -msse3 is added to the command line if the build CPU has SSE3 support
# 5. HAVE_SSE2 and HAVE_64_BITS are defined on all architectures
Patch0:		%{name}-configure.patch
# Update the python code from python2 to python3
Patch1:		%{name}-python3.patch
# Remove an extraneous "const"
Patch2:		%{name}-const.patch
# Remove references to undefined symbols on non-x86_64
Patch3:		%{name}-undef.patch

BuildRequires:	gcc
BuildRequires:	libtool
BuildRequires:	make
BuildRequires:	python3-devel
BuildRequires:	tex(latex)
BuildRequires:	tex(aeguill.sty)
BuildRequires:	tex(algpseudocode.sty)

%description
This external library implements an efficient implement of exhaustive
search to solve systems of low-degree boolean equations. Exhaustive
search is asymptotically faster than computing a Groebner basis,
except in special cases. This particular implementation is
particularly efficient (in the good cases it tests 3 candidate
solutions per CPU cycle on each core).

%package	devel
# GPL-2.0-or-later: fes-specific content
# Knuth-CTAN: the Computer Modern fonts embedded in the manual
License:	GPL-2.0-or-later AND Knuth-CTAN
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
This package contains the header files and development documentation
for %{name}.

%prep
%autosetup -p0

pushd src
    # Remove prebuilt objects
    rm src/{a.out,autogenerated*,print,toto,*.pyc} doc/doc.{aux,log,pdf}

    # Regenerate the configure script due to the changes in patch0
    autoreconf -fi .
popd

%build
pushd src
    export CCASFLAGS="%{build_cflags} -Wa,--noexecstack"
    export PYTHON=%{__python3}
    %configure \
%ifnarch %{ix86} x86_64
    --disable-sse2 \
%endif
    --disable-static --enable-dynamic

    %make_build

    pushd doc
	pdflatex -interaction=batchmode doc.tex
	pdflatex -interaction=batchmode doc.tex
    popd
popd

%install
%make_install -C src
rm %{buildroot}%{_libdir}/libfes.la

%check
make -C src check

%files
%doc src/AUTHORS
%doc src/COPYING
%{_libdir}/libfes.so.*

%files		devel
%doc src/TODO
%doc src/doc/doc.pdf
%{_includedir}/fes_interface.h
%{_libdir}/libfes.so

%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Jerry James <loganjerry@gmail.com> - 0.2-8
- Convert License tags to SPDX
- New project URL

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb  6 2019 Jerry James <loganjerry@gmail.com> - 0.2-1
- New upstream version, fixes FTBFS (bz 1603963, 1674882)
- Correct license from GPLv3+ to GPLv2+
- Drop upstreamed -dynamic patch
- Add -configure patch to fix multiple configuration problems
- Add -python3 patch due to python2 removal in Rawhide
- Add -const patch to fix warnings
- Add -undef patch to fix the build on non-x86_64 arches
- Build for i386 too as the SSE2 code is now optional
- Reduce texlive BRs

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 14 2017 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.1-13
- Correct FTBFS in rawhide (#1423562)

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun  8 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.1-4
- Add ldconfig to post and postun (#914936#c5).
- Mark stack as not executable in .s to .o compilation (#914936#c5).

* Fri Jun  7 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.1-3
- Add missing autoconf, automake and libtool build requires (#914936#c3).
- Remove the with_doc macro (#914936#c3).
- Change package to be x86_64 specific, as sse2 is not optional.

* Wed Jun  5 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.1-2
- Make python2 a build requires (#914936#c1).
- Patch the package to generate a dynamic library (#914936#c1).
- Add AUTHORS, COPYING and TODO to package documentation (#914936#c1).

* Fri Feb 22 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 0.1-1
- Initial fes spec.