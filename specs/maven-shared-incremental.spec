%bcond_with bootstrap

Name:           maven-shared-incremental
Version:        1.1
Release:        %autorelease
Summary:        Maven Incremental Build support utilities
License:        Apache-2.0
URL:            https://maven.apache.org/shared/maven-shared-incremental/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

# From upstream commit 1b5c81a7
Patch:          0001-MSHARED-1374-Upgrade-parent-pom-to-41.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
%endif

%description
Various utility classes and plexus components for supporting
incremental build functionality in maven plugins.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
API documentation for %{name}.

%prep
%autosetup -p1 -C
%pom_remove_dep :plexus-component-api

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
%autochangelog
