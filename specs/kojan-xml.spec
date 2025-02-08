%bcond_with bootstrap

Name:           kojan-xml
Version:        1.0.1
Release:        %autorelease
Summary:        Java library for modeling data in XML format
License:        Apache-2.0
URL:            https://github.com/mizdebsk/kojan-xml
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/mizdebsk/kojan-xml/archive/refs/tags/1.0.1.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(io.kojan:kojan-parent:pom:)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.xmlunit:xmlunit-assertj3)

%description
The Kojan XML library is used to model data according to the
entity–relationship (ER) model and write and read data in XML
format. It allows you to define data entities with their properties,
such as attributes and relationships, and serialize and deserialize
data in XML format.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
API documentation for %{name}.

%prep
%autosetup -p1 -C

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
%autochangelog
