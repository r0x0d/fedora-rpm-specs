%bcond_with bootstrap

Name:           beust-jcommander
Version:        1.82
Release:        %autorelease
Summary:        Java framework for parsing command line parameters
License:        Apache-2.0
URL:            http://jcommander.org/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/com/beust/jcommander/%{version}/jcommander-%{version}.pom
# Cleaned up bundled jars whose licensing cannot be easily verified
Source2:        generate-tarball.sh

Patch:          0001-ParseValues-NullPointerException-patch.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.testng:testng)
%endif

%description
JCommander is a very small Java framework that makes it trivial to
parse command line parameters (with annotations).

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
API documentation for %{name}.

%prep
%autosetup -p1 -C
chmod -x license.txt

cp -p %SOURCE1 pom.xml
%pom_xpath_set "pom:project/pom:version" "%{version}"

# maven-surefire-plugin requires explicit version >= 4.7
%pom_add_dep org.testng:testng:4.7:test

%mvn_file : %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license license.txt notice.md
%doc README.markdown

%files javadoc -f .mfiles-javadoc
%license license.txt notice.md

%changelog
%autochangelog
