Name:           javassist
Version:        3.30.2
Release:        6%{?dist}
Summary:        Java Programming Assistant for Java bytecode manipulation
License:        MPL-1.1 OR LGPL-2.1-or-later OR Apache-2.0

%global upstream_version rel_%(sed s/\\\\./_/g <<<"%{version}")_ga

URL:            https://www.javassist.org/
Source0:        https://github.com/jboss-%{name}/%{name}/archive/refs/tags/%{upstream_version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest-all)

%description
Javassist enables Java programs to define a new class at runtime and to
modify a class file when the JVM loads it. Unlike other similar
bytecode editors, Javassist provides two levels of API: source level
and bytecode level. If the users use the source-level API, they can
edit a class file without knowledge of the specifications of the Java
bytecode. The whole API is designed with only the vocabulary of the
Java language. You can even specify inserted bytecode in the form of
source text; Javassist compiles it on the fly. On the other hand, the
bytecode-level API allows the users to directly edit a class file as
other editors.


%package javadoc
Summary:        Javadocs for javassist

%description javadoc
javassist development documentation.


%prep
%setup -q -n %{name}-%{upstream_version}

# remove unnecessary maven plugins
%pom_remove_plugin :maven-source-plugin

# disable profiles that only add com.sun:tools dependency
%pom_xpath_remove "pom:profiles"

# add compatibility alias for old maven artifact coordinates
%mvn_alias : %{name}:%{name}

# add compatibility symlink for old classpath
%mvn_file : %{name}


%build
%mvn_build

# remove bundled jar and class files *after* they were used for running tests
rm javassist.jar src/test/resources/*.jar
find src/test -name "*.class" -print -delete


%install
%mvn_install


%files -f .mfiles
%license License.html
%doc README.md

%files javadoc -f .mfiles-javadoc
%license License.html


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Feb 27 2024 Jiri Vanek <jvanek@redhat.com> - 3.30.2-4
- Rebuilt for java-21-openjdk as system jdk

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.30.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 04 2024 Zuzana Miklankova <zmiklank@redhat.com> - 3.30.2-1
- Update javassist to 3.30.2 (#2256718)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.29.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.29.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Sep 19 2022 Zuzana Miklankova <zmiklank@redhat.com> - 3.29.2-1
- Update javassist to 3.29.2 (#2126887)

* Mon Aug 15 2022 Zuzana Miklankova <zmiklank@redhat.com> - 3.29.1-1
- Update javassist to 3.29.1 (#2117693)
- Replace Readme.html with README.md
- Re-add tests, that no longer depend on deprecated java.rmi

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.29.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Jiri Vanek <jvanek@redhat.com> - 3.29.0-2
- Rebuilt for Drop i686 JDKs

* Mon May 16 2022 Zuzana Miklankova <zmiklank@redhat.com> - 3.29.0-1
- Update javassist to 3.29.0 (#2085504)
- Inner.java test no longer dependent on deprecated java.rmi
- Changed source URL to actual one

* Mon May 09 2022 Zuzana Miklankova <zmiklank@redhat.com> - 3.28.0-4
- Removed tests with dependency on the deprecated java.rmi

* Sat Feb 05 2022 Jiri Vanek <jvanek@redhat.com> - 3.28.0-3
- Rebuilt for java-17-openjdk as system jdk

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.28.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 13 2021 Sérgio Basto <sergio@serjux.com> - 3.28.0-1
- Update javassist to 3.28.0 (#1958448)

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.27.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.27.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Sep 02 2020 Fabio Valentini <decathorpe@gmail.com> - 3.27.0-1
- Update to version 3.27.0.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 3.21.0-2
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Mar 25 2020 Dinesh Prasanth <dmoluguw@redhat.com> - 3.21.0-1
- Rebase to 3.21.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.18.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.18.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 16 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.18.1-3
- Simplify build dependencies

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.18.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 28 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.18.1-1
- Update to upstream version 3.18.1
- Remove workaround for rpm bug, can be removed in F-18
- Update to current packaging guidelines

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.16.1-7
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 26 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.16.1-5
- Remove unneeded BR on maven-doxia
- Resolves: rhbz#915607

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 3.16.1-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 24 2012 Andy Grimm <agrimm@gmail.com> - 3.16.1-1
- Update to latest upstream release.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Sep 20 2011 Alexander Kurtakov <akurtako@redhat.com> 3.15.0-1
- Update to latest upstream release.
- Add javassist:javassist depmap.
- The project is now triple licensed.

* Wed Aug 31 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.14.0-5
- Fixes according to current guidelines

* Tue Aug 30 2011 Andy Grimm <agrimm@gmail.com> - 3.14.0-4
- Switch to Maven 3 build.

* Tue Aug 30 2011 John5342 <john5342 at, fedoraproject.org> - 3.14.0-3
- Remove ext_ver macro usage leftover after last rebase (rhbz#734255)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.14.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Nov 4 2010 Alexander Kurtakov <akurtako@redhat.com> 3.14.0-1
- Update to 3.14.0 upstream version.
- Various fixes in preparation for merge review.

* Fri Feb 12 2010 Alexander Kurtakov <akurtako@redhat.com> 3.9.0-7
- Add maven-doxia BRs.

* Fri Feb 12 2010 Alexander Kurtakov <akurtako@redhat.com> 3.9.0-6
- Remove not needed BR. Fixes rhbz#539176.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 27 2009 John5342 <john5342 at, fedoraproject.org> - 3.9.0-3
- Correct group id for maven depmap

* Mon Jan 26 2009 John5342 <john5342 at, fedoraproject.org> - 3.9.0-2
- Build using maven and install maven stuff (fixes bug 480428)

* Tue Dec 16 2008 Sandro Mathys <red at fedoraproject.org> - 3.9.0-1
- initial build

