%global upstream_version 3.1

Name:           ongres-scram
Version:        %(echo %{upstream_version} | sed 's/-/~/g')
Release:        2%{?dist}
Summary:        Salted Challenge Response Authentication Mechanism (SCRAM) - Java Implementation
License:        BSD-2-Clause
URL:            https://github.com/ongres/scram
Source0:        https://github.com/ongres/scram/archive/%{upstream_version}/scram-%{upstream_version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  jurand

BuildRequires:  maven-local
BuildRequires:  mvn(com.ongres.stringprep:saslprep)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)

%description
This is a Java implementation of SCRAM (Salted Challenge Response
Authentication Mechanism) which is part of the family of Simple
Authentication and Security Layer (SASL, RFC 4422) authentication
mechanisms. It is described as part of RFC 5802 and RFC7677.

%package client
Summary:        Client for %{name}
License:        BSD

%description client
This package contains the client for %{name}

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}

%prep
%autosetup -p1 -n "scram-%{upstream_version}"
find \( -name '*.jar' -o -name '*.class' \) -delete

%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :flatten-maven-plugin
%pom_remove_plugin -r :maven-invoker-plugin

%pom_remove_dep org.jetbrains:annotations scram-parent

%java_remove_annotations . -s -n NotNull -n Unmodifiable -n Nullable

%mvn_package com.ongres.scram:scram-aggregator __noinstall
%mvn_package com.ongres.scram:scram-parent __noinstall

%pom_xpath_inject 'pom:plugin[pom:artifactId = "maven-jar-plugin"]/pom:configuration/pom:archive' '
<manifestEntries>
  <Multi-Release>true</Multi-Release>
</manifestEntries>
' scram-parent

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-scram-common
%license LICENSE

%files client -f .mfiles-scram-client
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 29 2024 Marian Koncek <mkoncek@redhat.com> - 3.1-1
- Update to upstream version 3.1

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 2.1-13
- Rebuilt for java-21-openjdk as system jdk

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 26 2023 Zuzana Miklankova <zmiklank@redhat.com> - 2.1-9
- change of licences of ongres-scram and ongres-scram-javadoc to "BSD and MIT and ASL 2.0"

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 2.1-6
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 2.1-5
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jun 01 2021 Richard Fearn <richardfearn@gmail.com> - 2.1-2
- Remove unnecessary findbugs dependency (#1966792)

* Fri Feb 12 2021 Ondrej Dubaj <odubaj@redhat.com> - 2.1-1
- Rebase to version 2.2

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~beta.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~beta.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.0.0~beta.2-10
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~beta.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~beta.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~beta.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~beta.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.0.0~beta.2-5
- Remove explicit invocation of maven-javadoc-plugin

* Tue May 22 2018 Pavel Raiskup <praiskup@redhat.com> - 1.0.0~beta.2-4
- BR javadoc maven plugin explicitly
- use nicer Source0 format

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0~beta.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 27 2017 Pavel Raiskup <praiskup@redhat.com> - 1.0.0~beta.2-2
- drop potential pre-compiled files from release tarball

* Fri Nov 24 2017 Augusto Caringi <acaringi@redhat.com> 1.0.0~beta.2-1
- initial rpm
