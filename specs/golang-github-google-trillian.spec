# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/google/trillian
%global goipath         github.com/google/trillian
Version:                1.4.2

%gometa

%global common_description %{expand:
Trillian is an implementation of the concepts described in the Verifiable Data
Structures white paper, which in turn is an extension and generalisation of the
ideas which underpin Certificate Transparency.

Trillian implements a Merkle tree whose contents are served from a data storage
layer, to allow scalability to extremely large trees.}

%global golicenses      LICENSE
%global godocs          docs examples CONTRIBUTING.md AUTHORS CHANGELOG.md\\\
                        CONTRIBUTORS README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Transparent, highly scalable and cryptographically verifiable data store

License:        Apache-2.0
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

sed -i "s|github.com/go-redis/redis|gopkg.in/redis.v6|" $(find . -name "*.go")

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
# client/rpcflags, cmd/get_tree_public_key, storage/testdb, quota/redis/redistb: needs network
%gocheck -d client/rpcflags \
         -t cmd \
         -d server \
         -d storage/testdb \
         -d util/election \
         -d quota/redis/redistb \
         -d crypto
%endif

%gopkgfiles

%changelog
%autochangelog