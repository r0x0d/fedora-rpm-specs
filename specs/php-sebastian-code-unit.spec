# remirepo/fedora spec file for php-sebastian-code-unit
#
# Copyright (c) 2020-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

# Sources
%global gh_commit    1fc9f64c0927627ef78ba436c9b17d967e68e120
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   code-unit
# Packagist
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
# Namespace
%global major        %nil
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   CodeUnit

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        1.0.8
Release:        12%{?dist}
Summary:        Collection of value objects that represent the PHP code units, version 1

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-reflection
BuildRequires:  php-spl
# Autoloader
BuildRequires:  php-fedora-autoloader-devel
%if %{with tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^9.3"
BuildRequires:  phpunit9 >= 9.3
%endif

# from composer.json, "require": {
#        "php": ">=7.3"
Requires:       php(language) >= 7.3
# From phpcompatinfo report for 1.0.0
Requires:       php-reflection
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Collection of value objects that represent the PHP code units.

This package provides version 1 of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
# Generate the library Autoloader
%{_bindir}/phpab \
   --template fedora \
   --output src/autoload.php \
   src

# Generate the fixture Autoloader
%{_bindir}/phpab \
   --template fedora \
   --output tests/_fixture/autoload.php \
   tests/_fixture


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%if %{with tests}
%check
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php

require_once dirname(__DIR__) . '/tests/_fixture/autoload.php';
require_once dirname(__DIR__) . '/tests/_fixture/file_with_multiple_code_units.php';
require_once dirname(__DIR__) . '/tests/_fixture/function.php';
EOF

: Run tests
ret=0
for cmd in php php80 php81 php82; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
     %{_bindir}/phpunit9 --verbose || ret=1
  fi
done
exit $ret
%endif


%files
%license LICENSE
%doc README.md composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Remi Collet <remi@remirepo.net> - 1.0.8-7
- use SPDX License id

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Oct 26 2020 Remi Collet <remi@remirepo.net> - 1.0.8-1
- update to 1.0.8

* Sat Oct  3 2020 Remi Collet <remi@remirepo.net> - 1.0.7-1
- update to 1.0.7

* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 1.0.6-1
- update to 1.0.6 (no change)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Remi Collet <remi@remirepo.net> - 1.0.5-1
- update to 1.0.5

* Tue Jun 16 2020 Remi Collet <remi@remirepo.net> - 1.0.3-1
- update to 1.0.3 (no change)
- sources from git snapshot

* Thu Apr 30 2020 Remi Collet <remi@remirepo.net> - 1.0.2-1
- update to 1.0.2

* Mon Apr 27 2020 Remi Collet <remi@remirepo.net> - 1.0.1-1
- update to 1.0.1

* Fri Apr  3 2020 Remi Collet <remi@remirepo.net> - 1.0.0-1
- initial package
