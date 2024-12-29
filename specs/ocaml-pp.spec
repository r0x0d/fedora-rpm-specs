# OCaml packages not built on i686 since OCaml 5 / Fedora 39.
ExcludeArch: %{ix86}

%ifnarch %{ocaml_native_compiler}
%global debug_package %{nil}
%endif

# This package is needed to build dune.  To avoid circular dependencies, this
# package cannot depend on dune, or any package that depends on dune.
# Therefore, we:
# - hack up our own build, rather than using dune to do the build
# - skip tests, which require ppx_expect, which is built with dune
# If you know what you are doing, build with dune anyway using this conditional.
%bcond dune 0

%global giturl  https://github.com/ocaml-dune/pp

Name:           ocaml-pp
Version:        2.0.0
Release:        %autorelease
Summary:        Pretty printing library for OCaml

License:        MIT
URL:            https://ocaml-dune.github.io/pp/
VCS:            git:%{giturl}.git
Source:         %{giturl}/releases/download/%{version}/pp-%{version}.tbz

BuildRequires:  ocaml >= 4.08
%if %{with dune}
BuildRequires:  ocaml-dune >= 2.8
%else
BuildRequires:  ocaml-rpm-macros
%endif

%description
This library provides a lean alternative to the Format [1] module of the
OCaml standard library.  It aims to make it easy for users to do the
right thing.  If you have tried Format before but find its API
complicated and difficult to use, then Pp might be a good choice for
you.

Pp uses the same concepts of boxes and break hints, and the final
rendering is done by formatter from the Format module.  However it
defines its own algebra which some might find easier to work with and
reason about.  No previous knowledge is required to start using this
library, however the various guides for the Format module such as this
one [2] should be applicable to Pp as well.

[1]: https://caml.inria.fr/pub/docs/manual-ocaml/libref/Format.html
[2]: https://caml.inria.fr/resources/doc/guides/format.en.html

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n pp-%{version}

%build
%if %{with dune}
%dune_build
%else
OFLAGS="-w -40 -g"
OCFLAGS="$OFLAGS -bin-annot"
cd src
ocamlc $OCFLAGS -no-alias-deps -o pp.cmi -c -intf pp.mli
ocamlc $OCFLAGS -intf-suffix .ml -no-alias-deps -o pp.cmo -c -impl pp.ml
ocamlc $OFLAGS -a -o pp.cma pp.cmo
%ifarch %{ocaml_native_compiler}
ocamlopt $OFLAGS -intf-suffix .ml -no-alias-deps -o pp.cmx -c -impl pp.ml
ocamlopt $OFLAGS -a -o pp.cmxa pp.cmx
ocamlopt $OFLAGS -shared -linkall -I . -o pp.cmxs pp.cmxa
%endif
%endif

%install
%if %{with dune}
%dune_install
%else
# Install without dune.  See comment at the top.
mkdir -p %{buildroot}%{ocamldir}/pp
cp -p src/pp.{cma,cmi,cmt,cmti,mli} %{buildroot}%{ocamldir}/pp
%ifarch %{ocaml_native_compiler}
cp -p src/pp.{a,cmx,cmxa,cmxs} %{buildroot}%{ocamldir}/pp
%endif
cp -p pp.opam %{buildroot}%{ocamldir}/pp/opam

cat >> %{buildroot}%{ocamldir}/pp/META << EOF
version = "%{version}"
description = "Pretty printing library for OCaml"
requires = ""
archive(byte) = "pp.cma"
%ifarch %{ocaml_native_compiler}
archive(native) = "pp.cmxa"
%endif
plugin(byte) = "pp.cma"
%ifarch %{ocaml_native_compiler}
plugin(native) = "pp.cmxs"
%endif
EOF

cat >> %{buildroot}%{ocamldir}/pp/dune-package << EOF
(lang dune 3.17)
(name pp)
(version %{version})
(sections (lib .) (libexec .) (doc ../../doc/pp))
(files
 (lib
  (META
   dune-package
   opam
   pp.a
   pp.cma
   pp.cmi
   pp.cmt
   pp.cmti
   pp.cmx
%ifarch %{ocaml_native_compiler}
   pp.cmxa
%endif
   pp.ml
   pp.mli))
%ifarch %{ocaml_native_compiler}
 (libexec (pp.cmxs))
%endif
 (doc (CHANGES.md LICENSE.md README.md)))
(library
 (name pp)
 (kind normal)
%ifarch %{ocaml_native_compiler}
 (archives (byte pp.cma) (native pp.cmxa))
 (plugins (byte pp.cma) (native pp.cmxs))
 (native_archives pp.a)
%else
 (archives (byte pp.cma))
 (plugins (byte pp.cma))
%endif
 (main_module_name Pp)
%ifarch %{ocaml_native_compiler}
 (modes byte native)
%else
 (modes byte)
%endif
 (modules
  (singleton
   (obj_name pp)
   (visibility public)
   (source (path Pp) (intf (path pp.mli)) (impl (path pp.ml))))))
EOF

%ocaml_files
%endif

%files -f .ofiles
%doc CHANGES.md README.md
%license LICENSE.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
