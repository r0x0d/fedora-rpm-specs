# Generated by go2rpm 1.8.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/docker/libtrust
%global goipath         github.com/docker/libtrust
%global commit          aabc10ec26b754e797f9028f4589c5b7bd90dc20

%gometa

%global common_description %{expand:
Libtrust is library for managing authentication and authorization using public
key cryptography.

Authentication is handled using the identity attached to the public key.
Libtrust provides multiple methods to prove possession of the private key
associated with an identity:

 - TLS x509 certificates
 - Signature verification
 - Key Challenge

Authorization and access control is managed through a distributed trust graph.
Trust servers are used as the authorities of the trust graph and allow caching
portions of the graph for faster access.}

%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md

Name:           %{goname}
Version:        0
Release:        %autorelease -p
Summary:        Primitives for identity and authorization

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog