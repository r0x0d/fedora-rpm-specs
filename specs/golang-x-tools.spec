# Generated by go2rpm
%bcond check 1
%bcond bootstrap 0

%if %{with bootstrap}
%global debug_package %{nil}
%endif

# https://github.com/golang/tools
%global goipath         golang.org/x/tools
%global forgeurl        https://github.com/golang/tools
Epoch:                  1
# This package should be split per go.mod
Version:                0.22.0

%gometa -L

%global common_description %{expand:
This package holds the source for various tools that support the Go programming
language.

Some of the tools, godoc and vet for example, are included in binary Go
distributions.

Others, including the Go guru and the test coverage tool, can be fetched with go
get.

Packages include a type-checker for Go and an implementation of the Static
Single Assignment form (SSA) representation for Go programs.}

%global golicenses      LICENSE PATENTS
%global godocs          CONTRIBUTING.md README.md

%global auth_commands authtest cookieauth gitauth netrcauth
%global commands benchcmp bisect bundle callgraph compilebench digraph eg file2fuzz fiximports go-contrib-init godex godoc goimports gomvpkg gonew gorename gotype goyacc html2article present present2md splitdwarf ssadump stress stringer toolstash
%global signature_fuzzer fuzz-driver fuzz-runner

Name:           %{goname}
Release:        %autorelease
Summary:        Various packages and tools that support the Go programming language

# Upstream license specification: BSD-3-Clause
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang-tests

%description
%{common_description}

%if %{without bootstrap}
%package -n golang-godoc
Summary:        Documentation tool for the Go programming language
Epoch:          1
Obsoletes:      golang-godoc = 1.1.2

%description -n golang-godoc
Godoc extracts and generates documentation for Go programs.

%package -n golang-gotype
Summary:        Go programming language source code analysis tool

%description -n golang-gotype
The gotype command, like the front-end of a Go compiler, parses and type-checks
a single Go package. Errors are reported if the analysis fails; otherwise
gotype is quiet (unless -v is set).

%package -n golang-html2article
Summary:        Tool for creating articles from HTML files

%description -n golang-html2article
This program takes an HTML file and outputs a corresponding article file
in present format. See: golang.org/x/tools/present

%package        auth
Summary:        Tools implementing the GOAUTH protocol

%description    auth
%{summary}.

%package        bisect
Summary:        Tool to find changes responsible for causing a failure

%description    bisect
%{summary}.

%package        callgraph
Summary:        Tool for reporting the call graph of a Go program

%description    callgraph
%{summary}.

%package        compilebench
Summary:        Benchmarks the speed of the Go compiler

%description    compilebench
%{summary}.

See https://pkg.go.dev/golang.org/x/tools/cmd/compilebench for more information.

%package        digraph
Summary:        Tool for queries over unlabelled directed graphs in text form

%description    digraph
The digraph command performs queries over unlabelled directed graphs
represented in text form.

%package        gorename
Summary:        Tool for precise type-safe renaming of identifiers in Go code

%description    gorename
The gorename command performs precise type-safe renaming of identifiers in Go
source code.

%package        stringer
Summary:        Tool to automate creating methods satisfying the fmt.Stringer interface

%description    stringer
Stringer is a tool to automate the creation of methods that satisfy the
fmt.Stringer interface.

%package        godex
Summary:        Tool to dump exported information for Go packages or objects

%description    godex
The godex command prints (dumps) exported information of packages or selected
package objects.

See https://pkg.go.dev/golang.org/x/tools/cmd/godex for more information.

%package        benchcmp
Summary:        Displays performance changes between benchmarks for the Go programming language

%description    benchcmp
%{summary}.

See https://pkg.go.dev/golang.org/x/tools/cmd/benchcmp for more information.

%package        bundle
Summary:        Creates a single-source-file version of a source package

%description    bundle
%{summary}.

See https://pkg.go.dev/golang.org/x/tools/cmd/bundle for more information.

%package        eg
Summary:        Example-based refactoring for the Go programming language

%description    eg
%{summary}.

See `eg -help` for more information.

%package        file2fuzz
Summary:        Convert binary files to the Go fuzzing corpus format

%description    file2fuzz
%{summary}.

%package        fiximports
Summary:        Fixes import declarations to use the canonical import path

%description    fiximports
%{summary}.

%package        go-contrib-init
Summary:        Helps new Go contributors get their development environment set up

%description    go-contrib-init
The go-contrib-init command helps new Go contributors get their development
environment set up for the Go contribution process.

It aims to be a complement or alternative to
https://golang.org/doc/contribute.html.

%package        goimports
Summary:        Go programming language import line formatter

%description    goimports
%{summary}.

See https://pkg.go.dev/golang.org/x/tools/cmd/goimports for more information.

%package        gomvpkg
Summary:        Tool to move Go packages, updating import declarations

%description    gomvpkg
%{summary}.

See https://pkg.go.dev/golang.org/x/tools/cmd/gomvpkg for more information.

%package        gonew
Summary:        Tool to start a new Go module by copying a template module

%description    gonew
%{summary}.

See https://pkg.go.dev/golang.org/x/tools/cmd/gonew for more information.

%package        gopls
Summary:        LSP server for Go

%description    gopls
%{summary}.

See https://pkg.go.dev/golang.org/x/tools/cmd/gopls for more information.

%package        present
Summary:        Display slide presentations and articles

%description    present
%{summary}.

See https://pkg.go.dev/golang.org/x/tools/cmd/present for more information.

%package        present2md
Summary:        Tool to convert legacy-syntax present files to Markdown-syntax present files

%description    present2md
%{summary}.

See https://pkg.go.dev/golang.org/x/tools/cmd/present2md for more information.

%package        splitdwarf
Summary:        Uncompress and copy the DWARF segment of a Mach-O executable into the "dSYM" file

%description    splitdwarf
%{summary}.

See https://pkg.go.dev/golang.org/x/tools/cmd/splitdwarf for more information.

%package        ssadump
Summary:        Tool for displaying and interpreting the SSA form of Go programs

%description    ssadump
%{summary}.

%package        stress
Summary:        Tool for catching sporadic failures

%description    stress
%{summary}.

See https://pkg.go.dev/golang.org/x/tools/cmd/stress for more information.

%package        toolstash
Summary:        Provides a way to save, run, and restore a known good copy of the Go toolchain

%description    toolstash
%{summary}.

See https://pkg.go.dev/golang.org/x/tools/cmd/toolstash for more information.

%package        signature-fuzzer
Summary:        Utilities for fuzz testing of Go function signatures

%description    signature-fuzzer
%{summary}.

See https://pkg.go.dev/golang.org/x/tools/cmd/signature-fuzzer for more information.

%package        goyacc
Summary:        Goyacc is a version of yacc for Go

%description    goyacc
%{summary}.

See https://pkg.go.dev/golang.org/x/tools/cmd/goyacc for more information.
%endif

%gopkg

%prep
%goprep
find . -type f -name "*.go" -exec sed -i "s|mvdan.cc/xurls/v2|mvdan.cc/xurls|" "{}" +;

%if %{without bootstrap}
%generate_buildrequires
%go_generate_buildrequires
%endif

%if %{without bootstrap}
%build
for cmd in %auth_commands; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/cmd/auth/$cmd
done
for cmd in %signature_fuzzer; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/cmd/signature-fuzzer/$cmd
done
for cmd in %commands; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/cmd/$cmd
done
%gobuild -o %{gobuilddir}/bin/gopls %{goipath}/gopls
%endif

%install
%gopkginstall
%if %{without bootstrap}
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

# Fix conflict with rubygem-bundler
mv %{buildroot}%{_bindir}/bundle %{buildroot}%{_bindir}/gobundle
%endif

%if %{without bootstrap}
%if %{with check}
%check
%gocheck -t cmd -d imports -t internal/lsp -d go/pointer -d internal/imports -t gopls/internal -d internal/packagesdriver -t go/packages -d go/analysis/unitchecker -d go/ssa -t internal/refactor
%endif
%endif

%if %{without bootstrap}
%files -n golang-godoc
%doc %{godocs}
%license %{golicenses}
%{_bindir}/godoc

%files -n golang-gotype
%doc %{godocs}
%license %{golicenses}
%{_bindir}/gotype

%files -n golang-html2article
%doc %{godocs}
%license %{golicenses}
%{_bindir}/html2article

%files    godex
%doc %{godocs}
%license %{golicenses}
%{_bindir}/godex

%files    auth
%doc %{godocs}
%license %{golicenses}
%{_bindir}/authtest
%{_bindir}/cookieauth
%{_bindir}/gitauth
%{_bindir}/netrcauth

%files    bisect
%doc %{godocs}
%license %{golicenses}
%{_bindir}/bisect

%files    callgraph
%doc %{godocs}
%license %{golicenses}
%{_bindir}/callgraph

%files    compilebench
%doc %{godocs}
%license %{golicenses}
%{_bindir}/compilebench

%files    digraph
%doc %{godocs}
%license %{golicenses}
%{_bindir}/digraph

%files    gorename
%doc %{godocs}
%license %{golicenses}
%{_bindir}/gorename

%files    stringer
%doc %{godocs}
%license %{golicenses}
%{_bindir}/stringer

%files    eg
%doc %{godocs}
%license %{golicenses}
%{_bindir}/eg

%files    file2fuzz
%doc %{godocs}
%license %{golicenses}
%{_bindir}/file2fuzz

%files    fiximports
%doc %{godocs}
%license %{golicenses}
%{_bindir}/fiximports

%files    go-contrib-init
%doc %{godocs}
%license %{golicenses}
%{_bindir}/go-contrib-init

%files    benchcmp
%doc %{godocs}
%license %{golicenses}
%{_bindir}/benchcmp

%files    bundle
%doc %{godocs}
%license %{golicenses}
%{_bindir}/gobundle

%files    goimports
%doc %{godocs}
%license %{golicenses}
%{_bindir}/goimports

%files    gomvpkg
%doc %{godocs}
%license %{golicenses}
%{_bindir}/gomvpkg

%files    gonew
%doc %{godocs}
%license %{golicenses}
%{_bindir}/gonew

%files    gopls
%doc %{godocs}
%license %{golicenses}
%{_bindir}/gopls

%files    present
%doc %{godocs}
%license %{golicenses}
%{_bindir}/present

%files    present2md
%doc %{godocs}
%license %{golicenses}
%{_bindir}/present2md

%files    splitdwarf
%doc %{godocs}
%license %{golicenses}
%{_bindir}/splitdwarf

%files    ssadump
%doc %{godocs}
%license %{golicenses}
%{_bindir}/ssadump

%files    stress
%doc %{godocs}
%license %{golicenses}
%{_bindir}/stress

%files    toolstash
%doc %{godocs}
%license %{golicenses}
%{_bindir}/toolstash

%files    signature-fuzzer
%doc %{godocs}
%license %{golicenses}
%{_bindir}/fuzz-driver
%{_bindir}/fuzz-runner

%files    goyacc
%doc %{godocs}
%license %{golicenses}
%{_bindir}/goyacc
%endif

%gopkgfiles

%changelog
%autochangelog