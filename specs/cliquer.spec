Name:           cliquer
Version:        1.22
Release:        9%{?dist}
Summary:        Find cliques in arbitrary weighted graphs

License:        GPL-2.0-or-later
URL:            https://users.aalto.fi/~pat/cliquer.html
Source0:        https://github.com/dimpase/autocliquer/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        http://users.aalto.fi/~pat/%{name}/%{name}_fm.pdf
Source2:        http://users.aalto.fi/~pat/%{name}/%{name}.pdf
Source3:        http://users.aalto.fi/~pat/%{name}/%{name}_bm.pdf
# Man page formatting by Jerry James, text from the sources
Source4:        %{name}.1

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

BuildRequires:  gcc
BuildRequires:  make

%description
The main cliquer package contains a command-line interface to the
cliquer library.  Note that the upstream binary name is "cl", which is
too generic for Fedora.  Therefore, the binary is named "cliquer".

%package libs
Summary:        Library to find cliques in arbitrary weighted graphs

%description libs
Cliquer is a set of C routines for finding cliques in an arbitrary
weighted graph.  It uses an exact branch-and-bound algorithm developed
by Patric Östergård.  It is designed with the aim of being efficient
while still being flexible and easy to use.

%package devel
Summary:        Development files for cliquer
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Development files for cliquer.

%prep
%autosetup -p1
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%conf
sed -i \
    's/59 Temple Place, Suite 330, Boston, MA  02111-1307/51 Franklin Street, Suite 500, Boston, MA  02110-1335/' \
    COPYING

%build
%configure --disable-static --disable-silent-rules

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

%install
%make_install

# Add missing executable bit
chmod 0755 %{buildroot}%{_libdir}/libcliquer.so.1.*

# We do not want the libtool archive
rm %{buildroot}%{_libdir}/*.la

# We do not want to install the examples
rm -fr %{buildroot}%{_datadir}/%{name}

# The name "cl" is very short and ambiguous
mv %{buildroot}%{_bindir}/cl %{buildroot}%{_bindir}/%{name}

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
cp -p %{SOURCE4} %{buildroot}%{_mandir}/man1

%check
LD_LIBRARY_PATH=. make test CFLAGS="%build_cflags"

%files
%doc cliquer*.pdf
%{_bindir}/%{name}
%{_mandir}/man1/*

%files libs
%doc ChangeLog README
%license COPYING
%{_libdir}/libcliquer.so.1*

%files devel
%{_includedir}/%{name}/
%{_libdir}/libcliquer.so

%changelog
* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 20 2022 Jerry James <loganjerry@gmail.com> - 1.22-4
- Convert License tag to SPDX

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Jerry James <loganjerry@gmail.com> - 1.22-1
- Version 1.22
- New URLs
- Drop upstreamed -sagemath patch
- Use autotools to build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Aug 15 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.21-4
- Do not hardcode version in shell commands (#825494)
- Correct permission of generated library and binary (#825494)

* Tue Aug 14 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.21-3
- Remove %%defattr from spec (#825494)
- Correct mixed spaces and tabs in spec (#825494)
- Correct FSF address (#825494)
- Update information about sagemath patches to upstream cliquer (#825494)

* Sat May 26 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.21-2
- Add sagemath patch interface

* Wed Nov 16 2011 Jerry James <loganjerry@gmail.com> - 1.21-1
- Initial RPM
