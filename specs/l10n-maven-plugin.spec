%global giturl  https://github.com/mojohaus/l10n-maven-plugin

Name:           l10n-maven-plugin
Version:        1.1.0
Release:        %{autorelease}
Summary:        Localization Tools Maven Plugin
License:        Apache-2.0

URL:            https://www.mojohaus.org/l10n-maven-plugin/
VCS:            git:%{giturl}.git
Source:         %{giturl}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-api)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)

%description
The Localization Tools Maven Plugin helps with internationalization and
localization of your projects.

%package        javadoc
# Apache-2.0: the content
# MIT: jquery and jquery-ui
# GPL-2.0-only: script.js, search.js, jquery-ui.overrides.css
License:        Apache-2.0 AND MIT AND GPL-2.0-only WITH Classpath-exception-2.0
Summary:        API documentation for %{name}
Provides:       bundled(js-jquery) = 3.7.1

%description    javadoc
API documentation for %{name}.

%prep
%autosetup

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
%autochangelog
