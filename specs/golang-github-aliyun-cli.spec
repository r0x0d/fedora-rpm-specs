# Generated by go2rpm 1.8.0
%bcond_without check

# https://github.com/aliyun/aliyun-cli
%global goipath         github.com/aliyun/aliyun-cli
Version:                3.0.125

# https://github.com/aliyun/aliyun-openapi-meta
%global metacommit      f044570354b0cc6a2762212246c9fd7f8b0a4078

%gometa -f

%global goaltipaths     github.com/aliyun/aliyun-openapi-meta

%global common_description %{expand:
Alibaba Cloud (Aliyun) CLI.}

%global golicenses      LICENSE LICENSE-oss
%global godocs          README-CN.md CHANGELOG.md README.md README-bin.md\\\
                        README-cli.md README-CN-oss.md README-oss.md\\\
                        CHANGELOG-oss.md README-openapi-meta.md


Name:           %{goname}
Release:        %autorelease
Summary:        Alibaba Cloud CLI

License:        MIT AND Apache-2.0
URL:            %{gourl}
Source0:        %{gosource0}
Source1:        https://github.com/aliyun/aliyun-openapi-meta/archive/%{metacommit}/aliyun-openapi-meta-%{metacommit}.tar.gz

BuildRequires:  help2man

%description %{common_description}

%gopkg

%prep
%goprep
%setup -q -T -D -a 1 -n aliyun-cli-%{version}
rmdir aliyun-openapi-meta
mv aliyun-openapi-meta-%{metacommit} aliyun-openapi-meta
mv bin/README.md README-bin.md
mv cli/README.md README-cli.md
mv oss/README.md README-oss.md
mv oss/README-CN.md README-CN-oss.md
mv oss/LICENSE LICENSE-oss
mv oss/CHANGELOG.md CHANGELOG-oss.md
mv aliyun-openapi-meta/README.md README-openapi-meta.md

%generate_buildrequires
%go_generate_buildrequires

%build
export LDFLAGS="-X %{goipath0}/cli.Version=%{version}"
%gobuild -o %{gobuilddir}/bin/aliyun %{goipath0}/main
mkdir -p %{gobuilddir}/share/man/man1
help2man --no-discard-stderr -n "%{godevelsummary0}" -s 1 -o %{gobuilddir}/share/man/man1/aliyun.1 -N --version-string="%{version}" %{gobuilddir}/bin/aliyun

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -m 0755 -vd                                %{buildroot}%{_mandir}/man1
install -m 0644 -vp %{gobuilddir}/share/man/man1/* %{buildroot}%{_mandir}/man1/

%if %{with check}
%check
cp -Trv /etc/skel %{getenv:HOME}
# Skip 'openapi' and 'oss/lib' tests due to need for credentials
%gocheck -d 'openapi' -d 'oss/lib'
%endif

%files
%license LICENSE LICENSE-oss
%doc README-CN.md CHANGELOG.md README.md README-bin.md
%doc README-cli.md README-CN-oss.md README-oss.md
%doc CHANGELOG-oss.md README-openapi-meta.md
%{_mandir}/man1/aliyun.1*
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog