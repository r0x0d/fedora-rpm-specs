%bcond_with bootstrap

Name:           moditect
Version:        1.1.0
Release:        %autorelease
Summary:        Tooling for the Java Module System
License:        Apache-2.0
URL:            https://github.com/moditect/moditect
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(com.beust:jcommander)
BuildRequires:  mvn(com.github.javaparser:javaparser-core)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.eclipse.aether:aether-util)
BuildRequires:  mvn(org.ow2.asm:asm)
%endif

%description
The ModiTect project aims at providing productivity tools for working with the
Java module system ("Jigsaw"). Currently the following tasks are supported:
* Generating module-info.java descriptors for given artifacts (Maven
  dependencies or local JAR files)
* Adding module descriptors to your project's JAR as well as existing JAR files
  (dependencies)
* Creating module runtime images

Compared to authoring module descriptors by hand, using ModiTect saves you work
by defining dependence clauses based on your project's dependencies, describing
exported and opened packages with patterns (instead of listing all packages
separately), auto-detecting service usages and more. You also can use ModiTect
to add a module descriptor to your project JAR while staying on Java 8 with your
own build.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
API documentation for %{name}.

%prep
%autosetup -p1 -C

%pom_remove_parent parent
%pom_xpath_inject 'pom:project' '<groupId>org.moditect</groupId>' parent

# Missing dependencies in each submodule of integration tests
%pom_disable_module integrationtest

%pom_remove_plugin com.mycila:license-maven-plugin parent
%pom_remove_plugin -r :maven-shade-plugin

%pom_remove_dep -r com.google.testing.compile:compile-testing
rm core/src/test/java/org/moditect/test/AddModuleInfoTest.java

%build
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
%autochangelog
