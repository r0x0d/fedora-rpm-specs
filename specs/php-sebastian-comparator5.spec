# remirepo/fedora spec file for php-sebastian-comparator5
#
# Copyright (c) 2014-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

# disabled until phpunit10 available
%bcond_without       tests

%global gh_commit    a18251eb0b7a2dcd2f7aa3d6078b18545ef0558e
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   comparator
# Packagist
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
# Namespace
%global major        5
%global php_home     %{_datadir}/php
%global ns_vendor    SebastianBergmann
%global ns_project   Comparator

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        5.0.3
Release:        2%{?dist}
Summary:        Compare PHP values for equality, version %{major}

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh


BuildArch:      noarch
BuildRequires:  php(language) >= 8.1
BuildRequires:  php-date
BuildRequires:  php-dom
BuildRequires:  php-mbstring
BuildRequires:  php-spl
BuildRequires:  (php-composer(%{pk_vendor}/diff)     >= 5.0   with php-composer(%{pk_vendor}/diff)     < 6)
BuildRequires:  (php-composer(%{pk_vendor}/exporter) >= 5.0   with php-composer(%{pk_vendor}/exporter) < 6)
BuildRequires:  php-fedora-autoloader-devel
%if %{with tests}
# from composer.json, "require-dev": {
#        "phpunit/phpunit": "^10.5"
BuildRequires:  phpunit10 >= 10.5
%endif

# from composer.json
#        "php": ">=8.1",
#        "sebastian/diff": "^5.0",
#        "sebastian/exporter": "^5.0"
#        "ext-dom": "*",
#        "ext-mbstring": "*"
Requires:       php(language) >= 8.1
Requires:       php-dom
Requires:       php-mbstring
Requires:       (php-composer(%{pk_vendor}/diff)     >= 5.0   with php-composer(%{pk_vendor}/diff)     < 6)
Requires:       (php-composer(%{pk_vendor}/exporter) >= 5.0   with php-composer(%{pk_vendor}/exporter) < 6)
# from phpcompatinfo report for version 5.0.0
Requires:       php-date
Requires:       php-spl
# Autoloader
Requires:       php-composer(fedora/autoloader)

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
This component provides the functionality to compare PHP values for equality.

This package provides version %{major} of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
# Generate the Autoloader
phpab --template fedora --output src/autoload.php src

# Rely on include_path as in PHPUnit dependencies
cat <<EOF | tee -a src/autoload.php

\Fedora\Autoloader\Dependencies::required([
    '%{php_home}/%{ns_vendor}/Diff5/autoload.php',
    '%{php_home}/%{ns_vendor}/Exporter5/autoload.php',
]);
EOF


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with tests}
mkdir vendor
%{_bindir}/phpab --template fedora --output vendor/autoload.php tests/_fixture

: Run upstream test suite
ret=0
for cmd in php php81 php82 php83 php84; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      %{_bindir}/phpunit10 --no-coverage || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif


%files
%doc README.md composer.json
%license LICENSE
%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Oct 21 2024 Remi Collet <remi@remirepo.net> - 5.0.3-1
- update to 5.0.3

* Mon Aug 12 2024 Remi Collet <remi@remirepo.net> - 5.0.2-1
- update to 5.0.2

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 30 2024 Remi Collet <remi@remirepo.net> - 5.0.1-4
- add upstream patch for phpunit >= 10.4 FTBFS #2261508

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Aug 18 2023 Remi Collet <remi@remirepo.net> - 5.0.1-1
- update to 5.0.1

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Feb  3 2023 Remi Collet <remi@remirepo.net> - 5.0.0-1
- update to 5.0.0
- raise dependency on PHP 8.1
- raise dependency on sebastian/diff 5
- raise dependency on sebastian/exporter 5
- rename to php-sebastian-comparator5
- move to /usr/share/php/SebastianBergmann/Comparator5
- add dependency on mbstring extension

* Wed Sep 14 2022 Remi Collet <remi@remirepo.net> - 4.0.8-1
- update to 4.0.8

* Wed Sep 14 2022 Remi Collet <remi@remirepo.net> - 4.0.7-1
- update to 4.0.7

* Tue Oct 27 2020 Remi Collet <remi@remirepo.net> - 4.0.6-1
- update to 4.0.6

* Wed Sep 30 2020 Remi Collet <remi@remirepo.net> - 4.0.5-1
- update to 4.0.5

* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 4.0.4-1
- update to 4.0.4 (no change)

* Mon Jun 29 2020 Remi Collet <remi@remirepo.net> - 4.0.3-1
- update to 4.0.3

* Tue Jun 16 2020 Remi Collet <remi@remirepo.net> - 4.0.2-1
- update to 4.0.2
- sources from git snapshot

* Fri Feb  7 2020 Remi Collet <remi@remirepo.net> - 4.0.0-1
- update to 4.0.0
- raise dependency on PHP 7.3
- raise dependency on sebastian/diff 4
- raise dependency on sebastian/exporter 4
- rename to php-sebastian-comparator4
- move to /usr/share/php/SebastianBergmann/Comparator4

* Thu Jul 12 2018 Remi Collet <remi@remirepo.net> - 3.0.2-1
- update to 3.0.2

* Tue Jun 19 2018 Remi Collet <remi@remirepo.net> - 3.0.1-1
- update to 3.0.1

* Wed Apr 18 2018 Remi Collet <remi@remirepo.net> - 3.0.0-1
- update to 3.0.0
- rename to php-sebastian-comparator3
- raise dependency on PHP 7.1
- raise dependency on sebastian/diff 3.0
- use phpunit7

* Fri Feb  2 2018 Remi Collet <remi@remirepo.net> - 2.1.3-1
- Update to 2.1.3 (no change)
- allow sebastian/diff v3
- use range dependencies on F27+

* Fri Jan 12 2018 Remi Collet <remi@remirepo.net> - 2.1.2-1
- Update to 2.1.2

* Sat Dec 23 2017 Remi Collet <remi@remirepo.net> - 2.1.1-1
- Update to 2.1.1

* Fri Nov  3 2017 Remi Collet <remi@remirepo.net> - 2.1.0-1
- Update to 2.1.0
- raise dependency on sebastian/exporter 3.1

* Fri Aug  4 2017 Remi Collet <remi@remirepo.net> - 2.0.2-1
- Update to 2.0.2
- raise dependency on sebastian/diff 2.0
- raise various dependencies on latest minor version

* Wed Jul 12 2017 Remi Collet <remi@remirepo.net> - 2.0.1-1
- Update to 2.0.1

* Fri Mar  3 2017 Remi Collet <remi@fedoraproject.org> - 2.0.0-1
- update to 3.0.0
- rename to php-sebastian-comparator2
- raise dependency on PHP 7
- raise dependency on sebastian/exporter 3

* Sun Jan 29 2017 Remi Collet <remi@fedoraproject.org> - 1.2.4-1
- update to 1.2.4

* Sun Jan 29 2017 Remi Collet <remi@fedoraproject.org> - 1.2.3-1
- update to 1.2.3

* Tue Nov 22 2016 Remi Collet <remi@fedoraproject.org> - 1.2.2-1
- update to 1.2.2 (no change)
- allow sebastian/exporter 2.0

* Thu Nov 17 2016 Remi Collet <remi@fedoraproject.org> - 1.2.1-1
- update to 1.2.1
- switch to fedora/autoloader

* Sun Jul 26 2015 Remi Collet <remi@fedoraproject.org> - 1.2.0-1
- update to 1.2.0

* Mon Jun 29 2015 Remi Collet <remi@fedoraproject.org> - 1.1.1-3
- manage dependencies in autoloader

* Fri Jan 30 2015 Remi Collet <remi@fedoraproject.org> - 1.1.1-1
- update to 1.1.1
- raise dependency on sebastian/diff >= 1.2
- raise dependency on sebastian/exporter >= 1.2

* Thu Dec  4 2014 Remi Collet <remi@fedoraproject.org> - 1.1.0-1
- update to 1.1.0

* Sun Oct  5 2014 Remi Collet <remi@fedoraproject.org> - 1.0.1-1
- update to 1.0.1
- enable test suite

* Fri Jul 18 2014 Remi Collet <remi@fedoraproject.org> - 1.0.0-2
- add composer dependencies

* Sat May  3 2014 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- initial package
