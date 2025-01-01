%bcond_with bootstrap

Name:           plexus-sec-dispatcher
Version:        2.0
Release:        %autorelease
Summary:        Plexus Security Dispatcher Component
License:        Apache-2.0
URL:            https://github.com/codehaus-plexus/plexus-sec-dispatcher
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.sonatype.plexus:plexus-cipher)
%endif

%description
Plexus Security Dispatcher Component

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
API documentation for %{name}.

%prep
%autosetup -p1 -C

cp %{SOURCE1} .

%pom_remove_parent

%pom_xpath_inject 'pom:project' '<groupId>org.codehaus.plexus</groupId>'

%mvn_file : plexus/%{name}

%mvn_alias org.codehaus.plexus: org.sonatype.plexus:

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc

%changelog
%autochangelog
