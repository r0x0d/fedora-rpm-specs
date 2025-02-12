# remirepo/fedora spec file for php-phpunit-php-timer8
#
# Copyright (c) 2010-2025 Christof Damian, Remi Collet
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    f258ce36aa457f3aa3339f9ed4c81fc66dc8c2cc
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   php-timer
%global gh_date      2025-02-07
# Packagist
%global pk_vendor    phpunit
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    SebastianBergmann
%global ns_project   Timer

%global major        8
%global php_home     %{_datadir}/php

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        8.0.0
Release:        2%{?dist}
Summary:        PHP Utility class for timing, version %{major}

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
# run makesrc.sh to create a git snapshot with test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 8.3
BuildRequires:  php-fedora-autoloader-devel
%if %{with tests}
# From composer.json"require-dev": {
#        "phpunit/phpunit": "^12.0"
BuildRequires:  phpunit12
%endif

# From composer.json
#        "php": ">=8.3"
Requires:       php(language) >= 8.3
# From phpcompatinfo report for version 6.0.0
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Utility class for timing things, factored out of PHPUnit into a stand-alone
component.

This package provides version %{major} of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
phpab \
   --template fedora \
   --output  src/autoload.php \
   src


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%if %{with tests}
%check
mkdir vendor
touch vendor/autoload.php

: Run upstream test suite
ret=0
for cmd in php php83 php84; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      %{_bindir}/phpunit12 || ret=1
  fi
done
exit $ret
%endif


%files
%license LICENSE
%doc README.md
%doc composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Mon Feb 10 2025 Remi Collet <remi@remirepo.net> - 8.0.0-2
- enable test suite

* Fri Feb  7 2025 Remi Collet <remi@remirepo.net> - 8.0.0-1
- update to 8.0.0
- raise dependency on PHP 8.3
- rename to php-phpunit-php-timer8
- move to /usr/share/php/SebastianBergmann/Timer8

* Tue Feb  4 2025 Remi Collet <remi@remirepo.net> - 7.0.1-2
- enable test suite

* Wed Jul  3 2024 Remi Collet <remi@remirepo.net> - 7.0.1-1
- update to 7.0.1

* Mon Feb  5 2024 Remi Collet <remi@remirepo.net> - 7.0.0-1
- update to 7.0.0
- raise dependency on PHP 8.2
- rename to php-phpunit-php-timer7
- move to /usr/share/php/SebastianBergmann/Timer7

* Wed Aug 23 2023 Remi Collet <remi@remirepo.net> - 6.0.0-3
- Enable test suite

* Fri Feb  3 2023 Remi Collet <remi@remirepo.net> - 6.0.0-1
- update to 6.0.0
- drop patch merged upstream
- raise dependency on PHP 8.1
- rename to php-phpunit-php-timer6
- move to /usr/share/php/SebastianBergmann/Timer6

* Tue Oct 27 2020 Remi Collet <remi@remirepo.net> - 5.0.3-2
- add patch for test suite on 32-bit from
  https://github.com/sebastianbergmann/php-timer/pull/36

* Mon Oct 26 2020 Remi Collet <remi@remirepo.net> - 5.0.3-1
- update to 5.0.3
- open https://github.com/sebastianbergmann/php-timer/issues/34
  32-bit compatibility

* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 5.0.2-1
- update to 5.0.2 (no change)

* Fri Jun 26 2020 Remi Collet <remi@remirepo.net> - 5.0.1-1
- update to 5.0.1

* Mon Jun  8 2020 Remi Collet <remi@remirepo.net> - 5.0.0-1
- update to 5.0.0
- rename to php-phpunit-php-timer5
- move to /usr/share/php/SebastianBergmann/Timer5

* Fri Jun  5 2020 Remi Collet <remi@remirepo.net> - 4.0.0-1
- update to 4.0.0
- rename to php-phpunit-php-timer4
- move to /usr/share/php/SebastianBergmann/Timer4
- sources from git snapshot
- bootstrap build

* Mon Apr 20 2020 Remi Collet <remi@remirepo.net> - 3.1.4-1
- update to 3.1.4

* Fri Apr 17 2020 Remi Collet <remi@remirepo.net> - 3.1.2-1
- update to 3.1.2

* Fri Feb  7 2020 Remi Collet <remi@remirepo.net> - 3.0.0-1
- update to 3.0.0
- raise dependency on PHP 7.3
- rename to php-phpunit-php-timer3
- move to /usr/share/php/SebastianBergmann/Timer3

* Fri Jun  7 2019 Remi Collet <remi@remirepo.net> - 2.1.2-1
- update to 2.1.2
- drop patch merged upstream

* Wed Feb 20 2019 Remi Collet <remi@remirepo.net> - 2.1.1-2
- add patch from https://github.com/sebastianbergmann/php-timer/pull/21
  fix for 32-bit where large value are converted to float

* Wed Feb 20 2019 Remi Collet <remi@remirepo.net> - 2.1.1-1
- update to 2.1.1

* Wed Feb  7 2018 Remi Collet <remi@remirepo.net> - 2.0.0-1
- normal build

* Fri Feb  2 2018 Remi Collet <remi@remirepo.net> - 2.0.0-0
- update to 2.0.0
- rename to php-phpunit-php-timer2
- move to /usr/share/php/SebastianBergmann/Timer
- raise dependency on PHP 7.1
- use phpunit 7
- bootstrap build

* Sun Feb 26 2017 Remi Collet <remi@fedoraproject.org> - 1.0.9-1
- update to 1.0.9
- switch to fedora/autoloader

* Fri May 13 2016 Remi Collet <remi@fedoraproject.org> - 1.0.8-1
- update to 1.0.8
- run test with both PHP 5 and 7 when available

* Sun Jul 26 2015 Remi Collet <remi@fedoraproject.org> - 1.0.7-1
- update to 1.0.7 (only CS)

* Mon Jun 15 2015 Remi Collet <remi@fedoraproject.org> - 1.0.6-1
- update to 1.0.6
- generate autoloader, no more provided by upstream
- enable test suite during build
- add explicit spec license header

* Fri Jul 18 2014 Remi Collet <remi@fedoraproject.org> - 1.0.5-5
- add composer dependencies

* Wed Apr 30 2014 Remi Collet <remi@fedoraproject.org> - 1.0.5-3
- cleanup pear registry

* Wed Apr 23 2014 Remi Collet <remi@fedoraproject.org> - 1.0.5-2
- get sources from github
- run test suite when build --with tests

* Fri Aug 02 2013 Remi Collet <remi@fedoraproject.org> - 1.0.5-1
- Update to 1.0.5

* Sat Oct  6 2012 Remi Collet <rpms@famillecollet.com> 1.0.4-1
- update to 1.0.4

* Mon Sep 24 2012 Remi Collet <rpms@famillecollet.com> 1.0.3-1
- update to 1.0.3

* Sun Oct 23 2011 Remi Collet <rpms@famillecollet.com> 1.0.2-1
- update to 1.0.2

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Sep 26 2010 Christof Damian <christof@damian.net> - 1.0.0-2
- fix timezone warnings

* Thu Jul 15 2010 Christof Damian <christof@damian.net> - 1.0.0-1
- initial package
