# Generated by go2rpm 1
# Needs network access
%bcond_with check
%global debug_package %{nil}


# https://gitlab.com/yawning/utls.git
%global goipath         gitlab.com/yawning/utls.git
%global forgeurl        https://gitlab.com/yawning/utls
Version:                0.0.11
%global tag             v0.0.11-1
%global distprefix      %{nil}

%gometa

%global common_description %{expand:
uTLS is a fork of "crypto/tls", which provides ClientHello fingerprinting
resistance, low-level access to handshake, fake session tickets and some other
features. Handshake is still performed by "crypto/tls", this library merely
changes ClientHello part of it and provides low-level access.}

%global golicenses      LICENSE LICENSE.upstream.txt
%global godocs          examples CONTRIBUTING.md CONTRIBUTORS_GUIDE.md\\\
                        README.md README.upstream.md

Name:           %{goname}
Release:        %autorelease
Summary:        Fork of the Go standard TLS library, providing access to the ClientHello

# Upstream license specification: BSD-3-Clause and GPL-3.0-only
# Automatically converted from old format: BSD and GPLv3 - review is highly recommended.
License:        LicenseRef-Callaway-BSD AND GPL-3.0-only
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(git.schwanenlied.me/yawning/bsaes.git)
BuildRequires:  golang(github.com/dsnet/compress/brotli)
BuildRequires:  golang(golang.org/x/crypto/chacha20poly1305)
BuildRequires:  golang(golang.org/x/crypto/cryptobyte)
BuildRequires:  golang(golang.org/x/crypto/curve25519)
BuildRequires:  golang(golang.org/x/crypto/hkdf)
BuildRequires:  golang(golang.org/x/crypto/sha3)
BuildRequires:  golang(golang.org/x/net/http2)

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog