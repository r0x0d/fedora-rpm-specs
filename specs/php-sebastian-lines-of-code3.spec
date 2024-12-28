# remirepo/fedora spec file for php-sebastian-lines-of-code3
#
# SPDX-FileCopyrightText:  Copyright 2020-2024 Remi Collet
# SPDX-License-Identifier: CECILL-2.1
# http://www.cecill.info/licences/Licence_CeCILL_V2-en.txt
#
# Please, preserve the changelog entries
#

# disabled until phpunit11 available
%bcond_with          tests

# github
%global gh_commit    d36ad0d782e5756913e42ad87cb2890f4ffe467a
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   lines-of-code
%global gh_date      2024-07-03
# packagist
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
%global major        3
# namespace
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   LinesOfCode

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        3.0.1
Release:        1%{?dist}
Summary:        Counting the lines of code in PHP source code, version %{major}

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
# run makesrc.sh to create a git snapshot with test suite
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 8.2
BuildRequires: (php-composer(nikic/php-parser)     >= 5.0   with php-composer(nikic/php-parser)     < 6)
BuildRequires:  php-spl
# Autoloader
BuildRequires:  php-fedora-autoloader-devel >= 1.0.0
%if %{with tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^11.0"
BuildRequires:  phpunit11
%endif

# from composer.json, "require": {
#        "php": ">=8.1",
#        "nikic/php-parser": "^5.0"
Requires:       php(language) >= 8.2
Requires:      (php-composer(nikic/php-parser)     >= 5.0   with php-composer(nikic/php-parser)     < 6)
# from phpcompatinfo report for version 2.0.0
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
Library for counting the lines of code in PHP source code.

This package provides version %{major} of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
# Generate the Autoloader
phpab --template fedora --output src/autoload.php src

cat <<EOF | tee -a src/autoload.php
\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/PhpParser5/autoload.php',
]);
EOF


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with tests}
mkdir vendor
touch vendor/autoload.php

: Run upstream test suite
ret=0
for cmd in php php82 php83; do
  if which $cmd; then
   $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
     %{_bindir}/phpunit11 || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif


%files
%license LICENSE
%doc *.md
%doc composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Wed Jul  3 2024 Remi Collet <remi@remirepo.net> - 3.0.1-1
- update to 3.0.1

* Mon Feb  5 2024 Remi Collet <remi@remirepo.net> - 3.0.0-1
- update to 3.0.0
- raise dependency on PHP 8.2
- raise dependency on nikic/php-parser 5.0
- rename to php-sebastian-lines-of-code3
- move to /usr/share/php/SebastianBergmann/LinesOfCode3

* Thu Dec 21 2023 Remi Collet <remi@remirepo.net> - 2.0.2-1
- update to 2.0.2
- raise dependency on nikic/php-parser 4.18 and allow 5.0

* Thu Aug 31 2023 Remi Collet <remi@remirepo.net> - 2.0.1-1
- update to 2.0.1

* Wed Aug 23 2023 Remi Collet <remi@remirepo.net> - 2.0.0-3
- Enable test suite

* Fri Feb  3 2023 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0
- raise dependency on PHP 8.1
- raise dependency on nikic/php-parser 4.10
- rename to php-sebastian-lines-of-code2
- move to /usr/share/php/SebastianBergmann/LinesOfCode2

* Mon Nov 30 2020 Remi Collet <remi@remirepo.net> - 1.0.3-1
- update to 1.0.3

* Tue Oct 27 2020 Remi Collet <remi@remirepo.net> - 1.0.2-1
- update to 1.0.2

* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 1.0.1-1
- update to 1.0.1

* Mon Aug 10 2020 Remi Collet <remi@remirepo.net> - 1.0.0-1
- initial package
