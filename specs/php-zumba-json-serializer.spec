# remirepo/fedora spec file for php-zumba-json-serializer
#
# Copyright (c) 2021-2023 Remi Collet
# License: CC-BY-SA-4.0
# http://creativecommons.org/licenses/by-sa/4.0/
#
# Please, preserve the changelog entries
#

%bcond_without       tests

%global gh_commit    c869bcb7f934f785d69c978f7d0479b54bbe0cfa
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     zumba
%global gh_project   json-serializer
%global ns_vendor    Zumba
%global ns_project   JsonSerializer
%global major        %nil

Name:           php-%{gh_owner}-%{gh_project}%{major}
Version:        3.2.1
Release:        4%{?dist}
Summary:        Serialize PHP variables

License:        MIT
URL:            https://github.com/%{gh_owner}/%{gh_project}
Source0:        %{name}-%{version}-%{?gh_short}.tgz
Source1:        makesrc.sh

BuildArch:      noarch
%if %{with tests}
BuildRequires:  php(language) >= 7.0
BuildRequires:  php-date
BuildRequires:  php-json
BuildRequires:  php-mbstring
BuildRequires:  php-pcre
BuildRequires:  php-reflection
BuildRequires:  php-spl
# For tests, from composer.json "require-dev": {
#        "phpunit/phpunit": ">=6.0 <11.0"
BuildRequires:  phpunit10
%global phpunit %{_bindir}/phpunit10
%endif
# For autoloader
BuildRequires:  php-fedora-autoloader-devel

# From composer.json, "require": {
#        "php": "^7.0 || ^8.0",
#        "ext-mbstring": "*"
Requires:       php(language) >= 7.0
Requires:       php-mbstring
# From phpcompatinfo report for 3.0.1
Requires:       php-json
Requires:       php-pcre
Requires:       php-reflection
Requires:       php-spl
# For generated autoloader
Requires:       php-composer(fedora/autoloader)

# Composer
Provides:       php-composer(%{gh_owner}/%{gh_project}) = %{version}


%description
This is a library to serialize PHP variables in JSON format. It is similar
of the serialize() function in PHP, but the output is a string JSON encoded.
You can also unserialize the JSON generated by this tool and have you PHP
content back.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php


%prep
%setup -q -n %{gh_project}-%{gh_commit}


%build
: Create autoloader
phpab --template fedora --output src/%{ns_project}/autoload.php src


%install
: Library
mkdir -p      %{buildroot}%{_datadir}/php/
cp -pr src    %{buildroot}%{_datadir}/php/%{ns_vendor}


%check
%if %{with tests}
mkdir vendor
cat << 'EOF' | tee vendor/autoload.php
<?php
require '%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php';
\Fedora\Autoloader\Autoload::addPsr4('%{ns_vendor}\\%{ns_project}\\Test\\', dirname(__DIR__).'/tests');
EOF

ret=0
# ignore testS relying on SuperClosure (deprecated and removed from repo)
for cmdarg in "php %{phpunit}" "php80 %{_bindir}/phpunit9" php81 php82 php83; do
   if which $cmdarg; then
      set $cmdarg
      $1 ${2:-%{_bindir}/phpunit10} \
          --bootstrap vendor/autoload.php \
          --filter '^((?!(testAddSerializer|testGetPreferredSerializer|testSerialize|testUnserialize)).)*$' \
          --no-coverage || ret=1
   fi
done
exit $ret
%else
: Test suite disabled
%endif


%files
%license LICENSE
%doc composer.json
%doc README.md
%dir %{_datadir}/php/%{ns_vendor}
     %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}


%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 19 2023 Remi Collet <remi@remirepo.net> - 3.2.1-1
- update to 3.2.1

* Tue Sep 26 2023 Remi Collet <remi@remirepo.net> - 3.2.0-1
- update to 3.2.0
- sources from git snapshot
- switch to phpunit10

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Dec  8 2022 Remi Collet <remi@remirepo.net> - 3.0.2-1
- update to 3.0.2 (no change)

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Dec  9 2021 Remi Collet <remi@remirepo.net> - 3.0.1-1
- initial package