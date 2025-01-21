%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
%global alphatag r12

Name:          scannotation
Version:       1.0.3
Release:       0.36.%{alphatag}%{?dist}
Summary:       A Java annotation scanner
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:       Apache-2.0
URL:           http://scannotation.sourceforge.net
# Also available here https://github.com/jharting/scannotation
# How we created tarball:
# svn export -r 12  https://scannotation.svn.sourceforge.net/svnroot/scannotation scannotation-1.0.3.Final
# tar -caJf scannotation-1.0.3.Final.tar.xz scannotation-1.0.3.Final
Source0:       %{name}-%{namedversion}.tar.xz
# Adding License file
Source1:       License.txt

BuildArch:     noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires: maven-local
BuildRequires: mvn(javassist:javassist)
BuildRequires: mvn(javax.servlet:javax.servlet-api)
BuildRequires: mvn(junit:junit)

%description
Scannotation is a Java library that creates an annotation database 
from a set of .class files.This database is really just a set of maps that index
what annotations are used and what classes are using them. Why do you need this? 
What if you are an annotation framework like an EJB 3.0 container and you want 
to automatically scan your classpath for EJB annotations so that you know what 
to deploy? Scannotation gives you apis that allow you to find archives in your 
classpath or WAR (web application) that you want to scan, then automatically 
scans them without loading each and every class within those archives

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

%pom_disable_module titan-test-jar
%pom_remove_dep :titan-cruise %{name}

# Force use servlet 3.1 apis
%pom_change_dep :servlet-api javax.servlet:javax.servlet-api:3.1.0 %{name}

# remove maven-compiler-plugin configurations that are broken with Java 11
%pom_xpath_remove -r 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration'

cp -p %SOURCE1 .

%mvn_file org.%{name}:%{name} %{name}

%build
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8 -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license License.txt

%files javadoc -f .mfiles-javadoc
%license License.txt

%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.36.r12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.3-0.35.r12
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.34.r12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 1.0.3-0.33.r12
- Rebuilt for java-21-openjdk as system jdk

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.32.r12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.31.r12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.30.r12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.29.r12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 1.0.3-0.28.r12
- Rebuilt for Drop i686 JDKs

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 1.0.3-0.27.r12
- Rebuilt for java-17-openjdk as system jdk

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.26.r12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.25.r12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.24.r12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.23.r12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 18 2020 Fabio Valentini <decathorpe@gmail.com> - 1.0.3-0.22.r12
- Set javac source and target to 1.8 to fix Java 11 builds.

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 1.0.3-0.21.r12
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.20.r12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.19.r12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.18.r12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.17.r12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.16.r12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.15.r12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.14.r12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.3-0.13.r12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Aug 08 2015 gil cattaneo <puntogil@libero.it> 1.0.3-0.12.r12
- fix FTBFS rhbz#1239715
- switch to java-headless rhbz#1068519
- switch to XMvn
- switch to glassfish-servlet-api
- use pom macros
- use BR mvn()-like
- fix some rpmlint problem
- introduce license macro

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-0.11.r12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Aug 07 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 1.0.3-0.10.r12
- Fix for junit and xmvn changes in F21 (#1107281)

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-0.9.r12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Feb 25 2014 Kashyap Chamarthy <kashyapc@fedoraproject.org> - 1.0.3.0 -8.r12
- Switch to java-headless in Requires. Fix rhbz#1068519

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-0.7.r12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-0.6.r12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.3-0.5.r12
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-0.4.r12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-0.3.r12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 14 2011 Kashyap Chamarthy <kashyapc@fedoraproject.org> 1.0.3-0.2.r12
- Preserve time stamps of files(License.txt in this case) being installed

* Thu Dec 1 2011 Kashyap Chamarthy <kashyapc@fedoraproject.org> 1.0.3-0.1.r12
- Initial packaging. With help from Ade Lee <vakwetu@fedoraproject.org>

