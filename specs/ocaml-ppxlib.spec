%global giturl  https://github.com/ocaml-ppx/ppxlib

Name:           ocaml-ppxlib
Epoch:          1
Version:        0.34.0
Release:        1%{?dist}
Summary:        Base library and tools for ppx rewriters

License:        MIT
URL:            https://ocaml-ppx.github.io/ppxlib/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/ppxlib-%{version}.tar.gz
# Fedora does not have, and does not need, stdlib-shims
Patch:          %{name}-stdlib-shims.patch

BuildRequires:  ocaml >= 4.08.0
BuildRequires:  ocaml-cinaps-devel >= 0.12.1
BuildRequires:  ocaml-cmdliner-devel >= 1.3.0
BuildRequires:  ocaml-compiler-libs-janestreet-devel >= 0.11.0
BuildRequires:  ocaml-dune >= 3.8
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-ppx-derivers-devel >= 1.0
BuildRequires:  ocaml-re-devel >= 1.9.0
BuildRequires:  ocaml-sexplib0-devel >= 0.15

# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch:    %{ix86}

# This can be removed when F40 reaches EOL
Obsoletes:      %{name}-doc < 1:0.26.0-3

%description
The ppxlib project provides the basis for the ppx system, which is
currently the officially supported method for meta-programming in Ocaml.
It offers a principled way to generate code at compile time in OCaml
projects.  It features:
- an OCaml AST / parser/ pretty-printer snapshot, to create a full
  frontend independent of the version of OCaml;
- a library for ppx rewriters in general, and type-driven code generators
  in particular;
- a full-featured driver for OCaml AST transformers;
- a quotation mechanism for writing values representing OCaml AST in the
  OCaml syntax;
- a generator of open recursion classes from type definitions.

%package        tools
Summary:        Command line tools for %{name}
Requires:       %{name}%{?_isa} = 1:%{version}-%{release}

%description    tools
The %{name}-tools package contains command line tools for
%{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = 1:%{version}-%{release}
Requires:       %{name}-tools%{?_isa} = 1:%{version}-%{release}
Requires:       ocaml-compiler-libs-janestreet-devel%{?_isa}
Requires:       ocaml-ppx-derivers-devel%{?_isa}
Requires:       ocaml-sexplib0-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and
signature files for developing applications that use
%{name}.

%prep
%autosetup -n ppxlib-%{version} -p1

%build
# Do not build the benchmark suite
%dune_build -p ppxlib,ppxlib-tools

%install
# Do not install the benchmark suite
%dune_install -s ppxlib ppxlib-tools

# Merge the tools devel package into the tools package
cat .ofiles-ppxlib-tools-devel >> .ofiles-ppxlib-tools

%check
# Do not run the benchmark suite
%dune_check -p ppxlib,ppxlib-tools

%files -f .ofiles-ppxlib
%doc CHANGES.md HISTORY.md README.md
%license LICENSE.md

%files tools -f .ofiles-ppxlib-tools

%files devel -f .ofiles-ppxlib-devel

%changelog
* Wed Jan  8 2025 Jerry James <loganjerry@gmail.com> - 1:0.34.0-1
- OCaml 5.3.0 rebuild for Fedora 42
- Version 0.34.0
- New tools subpackage

* Mon Aug  5 2024 Jerry James <loganjerry@gmail.com> - 1:0.33.0-1
- Version 0.33.0

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.32.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jun 27 2024 Jerry James <loganjerry@gmail.com> - 1:0.32.1-4
- Rebuild for ocaml-sexplib0 0.17.0

* Wed Jun 19 2024 Richard W.M. Jones <rjones@redhat.com> - 1:0.32.1-3
- OCaml 5.2.0 ppc64le fix

* Wed May 29 2024 Richard W.M. Jones <rjones@redhat.com> - 1:0.32.1-2
- OCaml 5.2.0 for Fedora 41

* Thu May 23 2024 Jerry James <loganjerry@gmail.com> - 1:0.32.1-1
- Version 0.32.1

* Mon Jan 29 2024 Richard W.M. Jones <rjones@redhat.com> - 1:0.31.0-7
- Bump and rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.31.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.31.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 18 2023 Richard W.M. Jones <rjones@redhat.com> - 1:0.31.0-4
- OCaml 5.1.1 + s390x code gen fix for Fedora 40

* Tue Dec 12 2023 Richard W.M. Jones <rjones@redhat.com> - 1:0.31.0-3
- OCaml 5.1.1 rebuild for Fedora 40

* Thu Oct 05 2023 Richard W.M. Jones <rjones@redhat.com> - 1:0.31.0-2
- OCaml 5.1 rebuild for Fedora 40

* Wed Oct  4 2023 Jerry James <loganjerry@gmail.com> - 1:0.31.0-1
- Version 0.31.0

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.30.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jul 11 2023 Richard W.M. Jones <rjones@redhat.com> - 1:0.30.0-2
- OCaml 5.0 rebuild for Fedora 39

* Mon Jul 10 2023 Jerry James <loganjerry@gmail.com> - 1:0.30.0-1
- Version 0.30.0

* Tue Jan 24 2023 Richard W.M. Jones <rjones@redhat.com> - 1:0.28.0-3
- Rebuild OCaml packages for F38

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Oct 31 2022 Jerry James <loganjerry@gmail.com> - 1:0.28.0-1
- Version 0.28.0
- Drop upstreamed test patch
- Drop upstreamed grep 3.8 adaptation

* Tue Sep  6 2022 Jerry James <loganjerry@gmail.com> - 1:0.27.0-2
- Adapt to grep 3.8

* Mon Aug  8 2022 Jerry James <loganjerry@gmail.com> - 1:0.27.0-1
- Version 0.27.0

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jul 20 2022 Jerry James <loganjerry@gmail.com> - 1:0.26.0-2
- Use new OCaml macros

* Sat Jun 18 2022 Richard W.M. Jones <rjones@redhat.com> - 1:0.26.0-2
- OCaml 4.14.0 rebuild

* Wed Apr 27 2022 Jerry James <loganjerry@gmail.com> - 1:0.26.0-1
- Version 0.26.0

* Mon Feb 28 2022 Jerry James <loganjerry@gmail.com> - 1:0.24.0-5
- Rebuild due to changed base, sexplib0, and stdio
- Drop unused ocaml-migrate-parsetree-devel BR

* Fri Feb 04 2022 Richard W.M. Jones <rjones@redhat.com> - 1:0.24.0-4
- OCaml 4.13.1 rebuild to remove package notes

* Wed Jan 26 2022 Richard W.M. Jones <rjones@redhat.com> - 1:0.24.0-3
- Rebuild to pick up new ocaml dependency

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec 30 2021 Jerry James <loganjerry@gmail.com> - 1:0.24.0-1
- Version 0.24.0
- Drop upstreamed OCaml 4.13 compatibility patches

* Tue Nov 30 2021 Jerry James <loganjerry@gmail.com> - 1:0.23.0-3
- Rebuild for ocaml-stdio 0.15.0
- Add -ocaml413 patch from upstream to address OCaml 4.13 issues

* Tue Oct 05 2021 Richard W.M. Jones <rjones@redhat.com> - 1:0.23.0-2
- OCaml 4.13.1 build

* Wed Sep  1 2021 Jerry James <loganjerry@gmail.com> - 1:0.23.0-1
- Version 0.23.0
- Reenable tests on ARM

* Thu Jul 29 2021 Jerry James <loganjerry@gmail.com> - 1:0.22.2-1
- Version 0.22.2

* Tue Jul 27 2021 Richard W.M. Jones <rjones@redhat.com> - 1:0.22.1-4
- Rebuild for changed ocamlx(Dynlink)

* Tue Jul 27 2021 Richard W.M. Jones <rjones@redhat.com> - 1:0.22.1-3
- Rebuild for changed ocamlx(Dynlink)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.22.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 22 2021 Jerry James <loganjerry@gmail.com> - 1:0.22.1-1
- Version 0.22.1

* Mon Mar  1 15:56:36 GMT 2021 Richard W.M. Jones <rjones@redhat.com> - 1:0.22.0-2
- OCaml 4.12.0 build

* Sat Feb 20 2021 Jerry James <loganjerry@gmail.com> - 1:0.22.0-1
- Version 0.22.0
- Drop upstreamed -longident-parse patch
- Do not build documentation by default due to circular dependency

* Tue Feb  2 2021 Richard W.M. Jones <rjones@redhat.com> - 1:0.15.0-3
- Bump and rebuild for updated ocaml Dynlink dependency.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Dec  7 2020 Jerry James <loganjerry@gmail.com> - 1:0.15.0-1
- Version 0.15.0
- Drop upstreamed patches: -execption-format and -whitespace
- Add -stdlib-shims patch

* Tue Sep 01 2020 Richard W.M. Jones <rjones@redhat.com> - 1:0.13.0-6
- OCaml 4.11.1 rebuild

* Fri Aug 21 2020 Richard W.M. Jones <rjones@redhat.com> - 1:0.13.0-5
- OCaml 4.11.0 rebuild

* Fri Aug  7 2020 Jerry James <loganjerry@gmail.com> - 1:0.13.0-4
- Add Epoch to Requires from -devel to main package

* Fri Aug  7 2020 Jerry James <loganjerry@gmail.com> - 1:0.13.0-3
- Some ppx rewriters do not work with version 0.14.0 or 0.15.0, so revert to
  version 0.13.0 until they can be updated

* Thu Aug  6 2020 Jerry James <loganjerry@gmail.com> - 0.15.0-1
- Version 0.15.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Dan Čermák <dan.cermak@cgc-instruments.com> - 0.14.0-1
- New upstream release 0.14.0

* Thu Jun 18 2020 Jerry James <loganjerry@gmail.com> - 0.13.0-2
- Rebuild for ocaml-stdio 0.14.0

* Thu May  7 2020 Jerry James <loganjerry@gmail.com> - 0.13.0-1
- Initial RPM
