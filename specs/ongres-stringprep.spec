Name:           ongres-stringprep
Version:        2.2
Release:        2%{?dist}
Summary:        RFC 3454 Preparation of Internationalized Strings in pure Java
License:        BSD-2-Clause
URL:            https://github.com/ongres/stringprep
Source0:        https://github.com/ongres/stringprep/archive/%{version}/stringprep-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)

%description
The stringprep protocol does not stand on its own; it has to be used by other
protocols at precisely-defined places in those other protocols.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}

%prep
%autosetup -p1 -n "stringprep-%{version}"
find \( -name '*.jar' -o -name '*.class' \) -delete

%pom_remove_dep org.junit:junit-bom parent

%pom_remove_plugin -r :maven-javadoc-plugin

# codegenerator is only needed at build time, and has extra dependencies
%mvn_package com.ongres.stringprep:codegenerator __noinstall

# codegen is only needed for specific build profile that we do not use
rm -r codegen

%pom_xpath_inject 'pom:plugin[pom:artifactId="maven-jar-plugin"]/pom:configuration/pom:archive' '
<manifestEntries>
  <Multi-Release>true</Multi-Release>
</manifestEntries>
' parent

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Aug 29 2024 Marian Koncek <mkoncek@redhat.com> - 2.2-1
- Update to upstream version 2.2

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Feb 29 2024 Yaakov Selkowitz <yselkowi@redhat.com> - 1.1-12
- Move velocity-2 dependencies to codegenerator

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.1-11
- Rebuilt for java-21-openjdk as system jdk

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jul 25 2023 Yaakov Selkowitz <yselkowi@redhat.com> - 1.1-8
- Drop codegenerator from install

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.1-4
- Rebuilt for Drop i686 JDKs

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 12 2021 Ondrej Dubaj <odubaj@redhat.com> - 1.1-1
- initial rpm
