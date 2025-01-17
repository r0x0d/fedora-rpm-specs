# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

# The topkg-care part has dependencies that themselves depend on the main
# package.  We do not build the care part for now.
%bcond care 0

Name:           ocaml-topkg
Version:        1.0.7
Release:        14%{?dist}
Summary:        The transitory OCaml software packager

License:        ISC
URL:            https://erratique.ch/software/topkg/
VCS:            git:https://erratique.ch/repos/topkg.git
Source:         https://github.com/dbuenzli/topkg/archive/v%{version}/topkg-%{version}.tar.gz

BuildRequires:  ocaml >= 4.05.0
BuildRequires:  ocaml-compiler-libs
BuildRequires:  ocaml-findlib >= 1.6.1
BuildRequires:  ocaml-ocamlbuild
BuildRequires:  ocaml-rpm-macros

%if %{with care}
BuildRequires:  ocaml-bos-devel >= 0.1.5
BuildRequires:  ocaml-cmdliner-devel >= 1.0.0
BuildRequires:  ocaml-fmt-devel
BuildRequires:  ocaml-logs-devel
BuildRequires:  ocaml-webbrowser-devel
BuildRequires:  ocaml-opam-format-devel >= 2.0.0
%endif

# This can be removed when F40 reaches EOL
Obsoletes:      ocaml-topkg-doc < 1.0.5-4

%global _desc %{expand:
Topkg is a packager for distributing OCaml software.  It provides an
API to describe the files a package installs in a given build
configuration and to specify information about the package's
distribution, creation and publication procedures.}

%description %_desc

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%if %{with care}
%package        care
Summary:        Command line tool for the transitory OCaml software packager
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ocaml-ocamlbuild%{?_isa}

%description    care %_desc

This package provides a command line tool which helps with various
aspects of a package's life cycle: creating and linting a distribution,
releasing it on the web, publishing its documentation, adding it to the
OCaml opam repository, etc.

%package        care-devel
Summary:        Development files for %{name}-care
Requires:       %{name}-care%{?_isa} = %{version}-%{release}
Requires:       ocaml-bos-devel%{?_isa}
Requires:       ocaml-cmdliner-devel%{?_isa}
Requires:       ocaml-fmt-devel%{?_isa}
Requires:       ocaml-logs-devel%{?_isa}
Requires:       ocaml-opam-format-devel%{?_isa}
Requires:       ocaml-webbrowser-devel%{?_isa}

%description    care-devel
The %{name}-care-devel package contains libraries and signature files
for developing applications that use %{name}-care.
%endif

%prep
%autosetup -n topkg-%{version} -p1

%conf
# This package can replace "watermarks" in software that it builds.  However,
# we are building from scratch, rather than using topkg to build itself, so we
# have to do the job manually.
for fil in $(find . -type f); do
  sed -e 's,%%%%NAME%%%%,topkg,' \
      -e 's,%%%%PKG_DOC%%%%,%{url}doc/,' \
      -e 's,%%%%PKG_HOMEPAGE%%%%,%{url},' \
      -e 's,%%%%VERSION%%%%,v%{version},' \
      -e 's,%%%%VERSION_NUM%%%%,%{version},' \
      -i.orig $fil
  touch -r $fil.orig $fil
  rm $fil.orig
done

%build
# Build the library and the tests
ocaml pkg/pkg.ml build --pkg-name topkg --tests true

%if %{with care}
# Build topkg-care
ocaml pkg/pkg.ml build --pkg-name topkg-care --tests true
%endif

%install
%ocaml_install -s

%if %{with care}
%check
ocaml pkg/pkg.ml test
%endif

%files -f .ofiles-topkg
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-topkg-devel

%if %{with care}
%files care -f .ofiles-care

%files care-devel -f .ofiles-care-devel
%endif

%changelog
* Thu Jan  9 2025 Jerry James <loganjerry@gmail.com> - 1.0.7-14
- OCaml 5.3.0 rebuild for Fedora 42

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 1.0.7-12
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 1.0.7-11
- OCaml 5.2.0 for Fedora 41

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 1.0.7-8
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 1.0.7-7
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 1.0.7-6
- OCaml 5.1 rebuild for Fedora 40

* Wed Oct  4 2023 Jerry James <loganjerry@gmail.com> - 1.0.7-5
- Use the %%ocaml_install macro

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 1.0.7-4
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 1.0.7-3
- OCaml 5.0.0 rebuild

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 1.0.7-2
- Rebuild OCaml packages for F38

* Fri Jan 20 2023 Jerry James <loganjerry@gmail.com> - 1.0.7-1
- Version 1.0.7

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Nov  4 2022 Jerry James <loganjerry@gmail.com> - 1.0.6-1
- Version 1.0.6

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 1.0.5-3
- Conditionally build ocaml-topkg-care
- Use new OCaml macros

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 1.0.5-3
- OCaml 4.14.0 rebuild

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1.0.5-2
- OCaml 4.13.1 rebuild to remove package notes

* Thu Feb  3 2022 Jerry James <loganjerry@gmail.com> - 1.0.5-1
- Version 1.0.5
- Drop upstreamed -labels patch

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Oct  6 2021 Jerry James <loganjerry@gmail.com> - 1.0.4-1
- Version 1.0.4
- ocaml-result is no longer needed
- Add -labels patch to silence warnings

* Mon Oct 04 2021 Richard W.M. Jones <rjones@redhat.com> - 1.0.3-5
- OCaml 4.13.1 build

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Mar  1 2021 Richard W.M. Jones <rjones@redhat.com> - 1.0.3-3
- OCaml 4.12.0 build

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec  1 2020 Jerry James <loganjerry@gmail.com> - 1.0.3-1
- Version 1.0.3

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.2-2
- OCaml 4.11.1 rebuild

* Tue Sep  1 2020 Jerry James <loganjerry@gmail.com> - 1.0.2-1
- Version 1.0.2

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.1-11
- OCaml 4.11.0 rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 05 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.1-8
- OCaml 4.11.0+dev2-2020-04-22 rebuild

* Tue Apr 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.1-7
- OCaml 4.11.0 pre-release attempt 2

* Fri Apr 17 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.1-6
- OCaml 4.11.0 pre-release

* Thu Apr 02 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.1-5
- Update all OCaml dependencies for RPM 4.16.

* Wed Feb 26 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.1-4
- OCaml 4.10.0 final.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Richard W.M. Jones <rjones@redhat.com> - 1.0.1-2
- OCaml 4.10.0+beta1 rebuild.

* Thu Jan  9 2020 Jerry James <loganjerry@gmail.com> - 1.0.1-1
- Initial RPM
