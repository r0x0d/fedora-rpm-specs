# remirepo/fedora spec file for php-sebastian-resource-operations3
#
# Copyright (c) 2015-2024 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    05d5692a7993ecccd56a03e40cd7e5b09b1d404e
#global gh_date      20150728
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     sebastianbergmann
%global gh_project   resource-operations
%global php_home     %{_datadir}/php
# Packagist
%global pk_vendor    sebastian
%global pk_project   %{gh_project}
# Namespace
%global ns_vendor    SebastianBergmann
%global ns_project   ResourceOperations
%global major        3

Name:           php-%{pk_vendor}-%{pk_project}%{major}
Version:        3.0.4
Release:        3%{?dist}
Summary:        Provides a list of PHP built-in functions that operate on resources, version %{major}

License:        BSD-3-Clause
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
BuildRequires:  php(language) >= 7.3
BuildRequires:  php-fedora-autoloader-devel
%if %{with tests}
# from composer.json
#        "phpunit/phpunit": "^9.0"
BuildRequires:  phpunit9
%endif

# from composer.json
#        "php": ">=7.3"
Requires:       php(language) >= 7.3
# Autoloader
Requires:       php-composer(fedora/autoloader)
# from phpcompatinfo report for version 3.0.0: nothing

Provides:       php-composer(%{pk_vendor}/%{pk_project}) = %{version}


%description
%{summary}.

This package provides version %{major} of %{pk_vendor}/%{pk_project} library.

Autoloader: %{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
# Generate the Autoloader
phpab --template fedora --output src/autoload.php src


%install
mkdir -p   %{buildroot}%{php_home}/%{ns_vendor}
cp -pr src %{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}


%check
%if %{with tests}
mkdir vendor
touch vendor/autoload.php

: Run upstream test suite
ret=0
for cmd in php php81 php82 php83; do
  if which $cmd; then
    $cmd -d auto_prepend_file=%{buildroot}%{php_home}/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
      %{_bindir}/phpunit9  --verbose tests || ret=1
  fi
done
exit $ret
%else
: bootstrap build with test suite disabled
%endif


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE
%doc README.md composer.json
%dir %{php_home}/%{ns_vendor}
     %{php_home}/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Mar 15 2024 Remi Collet <remi@remirepo.net> - 3.0.4-1
- update to 3.0.4 (no change)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Apr 21 2023 Remi Collet <remi@remirepo.net> - 3.0.3-2
- use SPDX License id

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-1.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-1.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-1.2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 28 2020 Remi Collet <remi@remirepo.net> - 3.0.3-1
- update to 3.0.3 (no change)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 29 2020 Remi Collet <remi@remirepo.net> - 3.0.2-1
- update to 3.0.2 (no change)

* Tue Jun 16 2020 Remi Collet <remi@remirepo.net> - 3.0.1-1
- update to 3.0.1 (no change)
- sources from git snapshot

* Fri Feb  7 2020 Remi Collet <remi@remirepo.net> - 3.0.0-1
- update to 3.0.0
- raise dependency on PHP 7.3
- rename to php-sebastian-resource-operations3
- move to /usr/share/php/SebastianBergmann/ResourceOperations3

* Thu Oct  4 2018 Remi Collet <remi@remirepo.net> - 2.0.1-1
- update to 2.0.1
- drop patch merged upstream

* Fri Sep 28 2018 Remi Collet <remi@remirepo.net> - 2.0.0-1
- update to 2.0.0
- raise dependency on PHP 7.1
- rename to php-sebastian-resource-operations2
- move to /usr/share/php/SebastianBergmann/ResourceOperations2

* Mon Oct 31 2016 Remi Collet <remi@fedoraproject.org> - 1.0.0-2
- switch to fedora/autoloader

* Fri Oct  2 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0 (no change)

* Tue Sep 29 2015 Remi Collet <remi@fedoraproject.org> - 1.0.0-0.1.20150728gitce990bb
- initial package
