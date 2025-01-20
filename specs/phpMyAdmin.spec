#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please, preserve the changelog entries
#
%{!?_pkgdocdir: %global _pkgdocdir %{_datadir}/doc/%{name}-%{version}}

# nginx 1.6 with nginx-filesystem
%global with_nginx     1
# httpd 2.4 with httpd-filesystem
%global with_httpd     1

%global upstream_version 5.2.1
#global upstream_prever  rc1

Name: phpMyAdmin
Version: %{upstream_version}%{?upstream_prever:~%{upstream_prever}}
Release: 6%{?dist}
Summary: A web interface for MySQL and MariaDB

# phpMyAdmin is GPL-2.0-or-later
# MIT (js/jquery/, js/jqplot, js/codemirror/, js/tracekit/)
# BSD 2-Clause (js/openlayers/)
# for PHP library see generated bundled list above
License: GPL-2.0-or-later AND MIT AND BSD-2-Clause AND BSD-3-Clause AND LGPL-3.0-or-later AND MPL-2.0 AND ISC
URL: https://www.phpmyadmin.net/
Source0: https://files.phpmyadmin.net/%{name}/%{upstream_version}%{?upstream_prever:-%upstream_prever}/%{name}-%{upstream_version}%{?upstream_prever:-%upstream_prever}-all-languages.tar.xz
Source1: https://files.phpmyadmin.net/%{name}/%{upstream_version}%{?upstream_prever:-%upstream_prever}/%{name}-%{upstream_version}%{?upstream_prever:-%upstream_prever}-all-languages.tar.xz.asc
Source2: phpMyAdmin.htaccess
Source3: phpMyAdmin.nginx
Source4: https://files.phpmyadmin.net/phpmyadmin.keyring
# List name / version / license of bundled libraries
Source5: phpMyAdmin-bundled.php

# Redirect to system certificates
Patch0:  phpMyAdmin-certs.patch

BuildArch: noarch
BuildRequires: gnupg2
# to run phpMyAdmin-bundled.php
BuildRequires: php(language) >= 7.2.5
BuildRequires: php-cli
BuildRequires: php-json

Requires(post): coreutils sed
Requires:  webserver
%if %{with_nginx}
Requires:   nginx-filesystem
%endif
%if %{with_httpd}
Requires:  httpd-filesystem
Requires:  php(httpd)
Suggests:  httpd
%endif
# From composer.json, "require": {
#        "php": "^7.2.5 || ^8.0",
#        "ext-hash": "*",
#        "ext-iconv": "*",
#        "ext-json": "*",
#        "ext-mysqli": "*",
#        "ext-openssl": "*",
#        "ext-pcre": "*",
#        "ext-xml": "*",
#        "google/recaptcha": "^1.1",
#        "nikic/fast-route": "^1.3",
#        "phpmyadmin/motranslator": "^5.0",
#        "phpmyadmin/shapefile": "^2.0",
#        "phpmyadmin/sql-parser": "^5.5",
#        "phpmyadmin/twig-i18n-extension": "^3.0",
#        "phpseclib/phpseclib": "^2.0",
#        "symfony/config": "^4.4.9",
#        "symfony/dependency-injection": "^4.4.9",
#        "symfony/expression-language": "^4.4.9",
#        "symfony/polyfill-ctype": "^1.17.0",
#        "symfony/polyfill-mbstring": "^1.17.0",
#        "twig/twig": "^2.14.9 || ^3.3.5",
#        "williamdes/mariadb-mysql-kbs": "^1.2"
Requires:  php(language) >= 7.2.5
Requires:  php-hash
Requires:  php-iconv
Requires:  php-json
Requires:  php-mysqli
Requires:  php-openssl
Requires:  php-pcre
Requires:  php-xml

# License BSD-2-Clause
Provides:  bundled(php-bacon-bacon-qr-code) = 2.0.8
Provides:  bundled(php-beberlei-assert) = v3.3.2
Provides:  bundled(php-code-lts-u2f-php-server) = v1.2.1
Provides:  bundled(php-dasprid-enum) = 1.0.3
# License BSD-3-Clause
Provides:  bundled(php-google-recaptcha) = 1.2.4
Provides:  bundled(php-nikic-fast-route) = v1.3.0
Provides:  bundled(php-twig-twig) = v3.5.0
# License GPL-2.0-or-later
Provides:  bundled(php-phpmyadmin-motranslator) = 5.3.0
Provides:  bundled(php-phpmyadmin-shapefile) = 3.0.1
Provides:  bundled(php-phpmyadmin-sql-parser) = 5.7.0
# License ISC
Provides:  bundled(php-paragonie-sodium-compat) = v1.19.0
# License LGPL-3.0-only
Provides:  bundled(php-tecnickcom-tcpdf) = 6.6.2
# License MIT
Provides:  bundled(php-brick-math) = 0.8.17
Provides:  bundled(php-composer-ca-bundle) = 1.3.5
Provides:  bundled(php-fgrosse-phpasn1) = v2.5.0
Provides:  bundled(php-fig-http-message-util) = 1.1.5
Provides:  bundled(php-league-uri) = 6.4.0
Provides:  bundled(php-league-uri-interfaces) = 2.3.0
Provides:  bundled(php-paragonie-constant-time-encoding) = v2.6.3
Provides:  bundled(php-paragonie-random-compat) = v9.99.100
Provides:  bundled(php-phpmyadmin-twig-i18n-extension) = v4.0.1
Provides:  bundled(php-pragmarx-google2fa) = v8.0.1
Provides:  bundled(php-pragmarx-google2fa-qrcode) = v2.1.1
Provides:  bundled(php-psr-cache) = 1.0.1
Provides:  bundled(php-psr-container) = 1.1.1
Provides:  bundled(php-psr-http-client) = 1.0.1
Provides:  bundled(php-psr-http-factory) = 1.0.1
Provides:  bundled(php-psr-http-message) = 1.0.1
Provides:  bundled(php-psr-log) = 1.1.4
Provides:  bundled(php-ralouphie-getallheaders) = 3.0.3
Provides:  bundled(php-ramsey-collection) = 1.1.4
Provides:  bundled(php-ramsey-uuid) = 4.2.3
Provides:  bundled(php-slim-psr7) = 1.4
Provides:  bundled(php-spomky-labs-base64url) = v2.0.4
Provides:  bundled(php-spomky-labs-cbor-php) = v1.1.1
Provides:  bundled(php-symfony-cache) = v5.4.19
Provides:  bundled(php-symfony-cache-contracts) = v2.5.2
Provides:  bundled(php-symfony-config) = v5.4.19
Provides:  bundled(php-symfony-dependency-injection) = v5.4.20
Provides:  bundled(php-symfony-deprecation-contracts) = v2.5.2
Provides:  bundled(php-symfony-expression-language) = v5.4.19
Provides:  bundled(php-symfony-filesystem) = v5.4.19
Provides:  bundled(php-symfony-polyfill-ctype) = v1.27.0
Provides:  bundled(php-symfony-polyfill-mbstring) = v1.27.0
Provides:  bundled(php-symfony-polyfill-php73) = v1.27.0
Provides:  bundled(php-symfony-polyfill-php80) = v1.27.0
Provides:  bundled(php-symfony-polyfill-php81) = v1.27.0
Provides:  bundled(php-symfony-process) = v5.4.19
Provides:  bundled(php-symfony-service-contracts) = v2.5.2
Provides:  bundled(php-symfony-var-exporter) = v5.4.19
Provides:  bundled(php-thecodingmachine-safe) = v1.3.3
Provides:  bundled(php-web-auth-cose-lib) = v3.3.12
Provides:  bundled(php-web-auth-metadata-service) = v3.3.12
Provides:  bundled(php-web-auth-webauthn-lib) = v3.3.12
Provides:  bundled(php-webmozart-assert) = 1.11.0
# License MPL-2.0
Provides:  bundled(php-williamdes-mariadb-mysql-kbs) = v1.2.14

Requires:  php-dom
Requires:  php-intl
Requires:  php-posix
# php-tidy required by tcpdf is not used (fixHTMLCode)
Requires:  php-ctype
Requires:  php-curl
Requires:  php-zlib
Requires:  php-bz2
Requires:  php-zip
Requires:  php-gd
Requires:  php-mbstring
# From phpcompatinfo reports for 4.8.0
#   notice: recode is optional (iconv or mbstring are preferred / used first)
Requires:  php-date
Requires:  php-filter
Requires:  php-libxml
Requires:  php-session
Requires:  php-simplexml
Requires:  php-spl
Requires:  php-xmlwriter
# System certificates
Requires:  ca-certificates

# Bundled JS library
Provides:  bundled(js-codemirror)
Provides:  bundled(js-jqplot) = 1.0.9
Provides:  bundled(js-jquery) = 3.2.1
Provides:  bundled(js-openlayers)
Provides:  bundled(js-tracekit)

Provides:  php-composer(phpmyadmin/phpmyadmin) = %{version}
# Allow lowercase in install command
Provides:  phpmyadmin   =  %{version}-%{release}


%description
phpMyAdmin is a tool written in PHP intended to handle the administration of
MySQL over the Web. Currently it can create and drop databases,
create/drop/alter tables, delete/edit/add fields, execute any SQL statement,
manage keys on fields, manage privileges,export data into various formats and
is available in 50 languages


%prep
%{?gpgverify:%{gpgverify} --keyring='%{SOURCE4}' --signature='%{SOURCE1}' --data='%{SOURCE0}'}

%setup -qn phpMyAdmin-%{upstream_version}%{?upstream_prever:-%upstream_prever}-all-languages
%patch -P0 -p1
rm -r vendor/composer/ca-bundle/res/

# Minimal configuration file
sed -e "/'blowfish_secret'/s@''@'MUSTBECHANGEDONINSTALL'@"  \
    -e "/'UploadDir'/s@''@'%{_localstatedir}/lib/%{name}/upload'@"  \
    -e "/'SaveDir'/s@''@'%{_localstatedir}/lib/%{name}/save'@" \
    config.sample.inc.php >CONFIG

# Setup vendor config file
sed -e "/'changeLogFile'/s@ROOT_PATH@'%{_pkgdocdir}/'@" \
    -e "/'licenseFile'/s@ROOT_PATH@'%{_pkgdocdir}/'@" \
    -e "/'configFile'/s@ROOT_PATH@'%{_sysconfdir}/%{name}/'@" \
%if 0%{?_licensedir:1}
    -e '/licenseFile/s:%_defaultdocdir:%_defaultlicensedir:' \
%endif
    -e "/versionSuffix/s/''/'-%{release}'/" \
    -e "/tempDir/s@ROOT.*tmp'@'%{_localstatedir}/lib/%{name}/temp'@" \
    -e "/cacheDir/s@ROOT.*cache'@'%{_localstatedir}/lib/%{name}/cache'@" \
    -i libraries/vendor_config.php

# For debug
grep '=>' libraries/vendor_config.php

php %{SOURCE5} vendor/composer/installed.json


%build
# Nothing to do


%install
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -ad ./* %{buildroot}/%{_datadir}/%{name}
install -Dpm 0640 CONFIG %{buildroot}/%{_sysconfdir}/%{name}/config.inc.php
# Apache
install -Dpm 0644 %{SOURCE2} %{buildroot}/%{_sysconfdir}/httpd/conf.d/phpMyAdmin.conf
# Nginx
%if %{with_nginx}
install -Dpm 0644 %{SOURCE3} %{buildroot}/%{_sysconfdir}/nginx/default.d/phpMyAdmin.conf
%endif

mkdir -p %{buildroot}/%{_localstatedir}/lib/%{name}/{upload,save,config,temp}

rm -f %{buildroot}/%{_datadir}/%{name}/config.sample.inc.php
rm -f %{buildroot}/%{_datadir}/%{name}/*txt
rm -f %{buildroot}/%{_datadir}/%{name}/[CDLR]*
rm -f %{buildroot}/%{_datadir}/%{name}/libraries/.htaccess
rm -f %{buildroot}/%{_datadir}/%{name}/setup/lib/.htaccess
rm -f %{buildroot}/%{_datadir}/%{name}/setup/frames/.htaccess
rm -rf %{buildroot}%{_datadir}/%{name}/contrib
rm     %{buildroot}%{_datadir}/%{name}/composer.*
rm -rf %{buildroot}%{_datadir}/%{name}/tmp/
mv     %{buildroot}%{_datadir}/%{name}/libraries/cache %{buildroot}/%{_localstatedir}/lib/%{name}/cache

# JS libraries sources
#rm -r %%{buildroot}%%{_datadir}/%{name}/js/jquery/src
#rm -r %%{buildroot}%%{_datadir}/%{name}/js/openlayers/src

# documentation
rm -rf    %{buildroot}%{_datadir}/%{name}/examples/
rm -rf    %{buildroot}%{_datadir}/%{name}/doc/
mkdir -p  %{buildroot}%{_datadir}/%{name}/doc/
ln -s %{_pkgdocdir}/html  %{buildroot}%{_datadir}/%{name}/doc/html

mv -f %{buildroot}%{_datadir}/%{name}/js/vendor/jquery/MIT-LICENSE.txt LICENSE-jquery
mv -f %{buildroot}%{_datadir}/%{name}/js/vendor/codemirror/LICENSE LICENSE-codemirror


%pretrans
# allow dir to link upgrade
if  [ -d %{_datadir}/%{name}/doc/html ]; then
  rm -rf %{_datadir}/%{name}/doc/html
fi

%post
# generate a 32 chars secret key for this install
SECRET=$(printf "%04x%04x%04x%04x%04x%04x%04x%04x" $RANDOM $RANDOM $RANDOM $RANDOM $RANDOM $RANDOM $RANDOM $RANDOM)
sed -e "/'blowfish_secret'/s/MUSTBECHANGEDONINSTALL/$SECRET/" \
    -i %{_sysconfdir}/%{name}/config.inc.php


%files
%{!?_licensedir:%global license %%doc}
%license LICENSE*
%doc ChangeLog README CONTRIBUTING.md config.sample.inc.php
%doc doc/html/
%doc examples/
%doc composer.json
%{_datadir}/%{name}
%attr(0750,root,apache) %dir %{_sysconfdir}/%{name}
%config(noreplace) %attr(0640,root,apache) %{_sysconfdir}/%{name}/config.inc.php
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%if %{with_nginx}
%config(noreplace) %{_sysconfdir}/nginx/default.d/%{name}.conf
%endif
%dir %{_localstatedir}/lib/%{name}/
%dir %attr(0750,apache,apache) %{_localstatedir}/lib/%{name}/upload
%dir %attr(0750,apache,apache) %{_localstatedir}/lib/%{name}/save
%dir %attr(0750,apache,apache) %{_localstatedir}/lib/%{name}/config
%dir %attr(0750,apache,apache) %{_localstatedir}/lib/%{name}/temp
%dir %attr(0750,apache,apache) %{_localstatedir}/lib/%{name}/cache
     %attr(0640,apache,apache) %{_localstatedir}/lib/%{name}/cache/*


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb  8 2023 Remi Collet <remi@remirepo.net> - 5.2.1-1
- update to 5.2.1 (2023-02-08, security and bugfix release)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu May 12 2022 Remi Collet <remi@remirepo.net> - 5.2.0-1
- update to 5.2.0 (2022-10-12, new features release)

* Fri Feb 11 2022 Remi Collet <remi@remirepo.net> - 5.1.3-1
- update to 5.1.3 (2022-02-10, security and bugfix release)

* Sun Jan 23 2022 Remi Collet <remi@remirepo.net> - 5.1.2-1
- update to 5.1.2 (2022-01-22, security and bugfix release)
- always use bundled libraries

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jan 13 2022 Remi Collet <remi@remirepo.net> - 5.1.1-4
- fix Licence name
- add build dependency on json ext

* Fri Dec 10 2021 Remi Collet <remi@remirepo.net> - 5.1.1-3
- add flag to use all PHP bundled libraries instead of system ones

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun  4 2021 Remi Collet <remi@remirepo.net> - 5.1.1-1
- update to 5.1.1 (2021-06-04, bugfix release)

* Wed May  5 2021 Remi Collet <remi@remirepo.net> - 5.1.0-3
- add VERSION_SUFFIX in vendor_config.php
- fix autoloader for pragmarx/google2fa-qrcode

* Wed Feb 24 2021 Remi Collet <remi@remirepo.net> - 5.1.0-1
- update to 5.1.0 (2021-02-24, new features release)
- add dependency on nikic/fast-route
- raise dependency on phpmyadmin/motranslator 5.0
- raise dependency on phpmyadmin/twig-i18n-extension 3.0
- raise dependency on Symfony 4.4.9

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 16 2020 Remi Collet <remi@remirepo.net> - 5.0.4-1
- update to 5.0.4 (2020-10-15, bug fix release)

* Sat Oct 10 2020 Remi Collet <remi@remirepo.net> - 5.0.3-1
- update to 5.0.3 (2020-10-10, security release)
- raise dependency on twig 2.9 and allow v3
- allow phpmyadmin/twig-i18n-extension v3

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 24 2020 Remi Collet <remi@remirepo.net> 5.0.2-2
- cleanup httpd configuration

* Sat Mar 21 2020 Remi Collet <remi@remirepo.net> 5.0.2-1
- update to 5.0.2 (2020-03-21, security release)
- use phpmyadmin/twig-i18n-extension instead of twig/extensions

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Remi Collet <remi@remirepo.net> 5.0.1-2
- add missing depependency on williamdes/mariadb-mysql-kbs

* Wed Jan  8 2020 Remi Collet <remi@remirepo.net> 5.0.1-1
- update to 5.0.1 (2020-01-08, security release)

* Fri Dec 27 2019 Remi Collet <remi@remirepo.net> 5.0.0-1
- update to 5.0.0 (2019-12-26, new features release)
- raise dependency on PHP 7.1.3
- raise dependency on phpmyadmin/sql-parser 5.0
- raise dependency on twig 2.1
- add dependency on pragmarx/google2fa-qrcode
- drop dependency on pragmarx/google2fa and bacon/bacon-qr-code
- drop dependency on psr/container
- sync spec file with remirepo one

* Mon Dec  2 2019 Remi Collet <remi@remirepo.net> - 4.9.2-2
- drop dependency on php-recode (mbstring preferred)

* Fri Nov 22 2019 Remi Collet <remi@remirepo.net> - 4.9.2-1
- update to 4.9.2 (2019-11-22, bugfix and security release)

* Sat Sep 21 2019 Remi Collet <remi@remirepo.net> - 4.9.1-1
- update to 4.9.1 (2019-09-21, bug fix release)
- add tarball signature check
- allow twig version 2

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.9.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun  4 2019 Remi Collet <remi@remirepo.net> - 4.9.0.1-1
- update to 4.9.0.1 (2019-06-04, important security fixes)
- raise dependency on phpmyadmin/sql-parser version 4.3.2

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 29 2019 Remi Collet <remi@remirepo.net> - 4.8.5-1
- update to 4.8.5 (2019-01-26, security fix)

* Tue Dec 11 2018 Remi Collet <remi@remirepo.net> - 4.8.4-1
- update to 4.8.4 (2018-12-11, security fix)

* Wed Aug 22 2018 Remi Collet <remi@remirepo.net> - 4.8.3-1
- update to 4.8.3 (2018-08-22, security fix)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Remi Collet <remi@remirepo.net> - 4.8.2-1
- update to 4.8.2 (2018-06-21, important security fix)

* Fri May 25 2018 Remi Collet <remi@remirepo.net> - 4.8.1-1
- update to 4.8.1 (2018-05-25, bug fix release)

* Thu Apr 19 2018 Remi Collet <remi@remirepo.net> - 4.8.0.1-1
- update to 4.8.0.1 (2018-04-19, security release)
- add dependency on symfony/polyfill-mbstring for PHP < 7.2

* Mon Apr  9 2018 Remi Collet <remi@remirepo.net> 4.8.0-1
- update to 4.8.0 (2018-04-07, new features release)
- add dependency on psr/container
- add dependency on twig/twig
- add dependency on twig/extensions
- add dependency on symfony/expression-language
- add optional dependency on bacon/bacon-qr-code
- add optional dependency on pragmarx/google2fa, review #1552442
- add optional dependency on samyoul/u2f-php-server, review #1552450
- dependency on tecnickcom/tcpdf is now optional

* Tue Mar  6 2018 Remi Collet <remi@remirepo.net> - 4.7.9-1
- Update to 4.7.9 (2018-03-05, maintenance release)

* Wed Feb 21 2018 Remi Collet <remi@remirepo.net> 4.7.8-1
- update to 4.7.8 (2018-02-20, security release)
- raise dependency on phpmyadmin/motranslator version 4.0
- use range dependencies on F27+

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 4.7.7-3
- Escape macros in %%changelog

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Dec 23 2017 Remi Collet <remi@remirepo.net> 4.7.7-1
- update to 4.7.7 (2017-12-23, security release)
- raise dependency on phpmyadmin/motranslator version 3.4

* Fri Dec 1 2017 Remi Collet <remi@remirepo.net> 4.7.6-1
- update to 4.7.6 (2017-12-01, regular maintenance release)
- raise dependency on phpseclib/phpseclib 2.0.9

* Tue Oct 24 2017 Remi Collet <remi@remirepo.net> 4.7.5-2
- simplify scriptlet to avoid hang during update #1502966

* Mon Oct 23 2017 Remi Collet <remi@remirepo.net> 4.7.5-1
- update to 4.7.5 (2017-10-23, regular maintenance release)
- raise dependency on phpmyadmin/sql-parser version 4.2.3

* Thu Aug 24 2017 Remi Collet <remi@remirepo.net> 4.7.4-1
- update to 4.7.4 (2017-07-24, regular maintenance release)
- raise dependency on phpmyadmin/sql-parser version 4.1.10

* Tue Aug  1 2017 Remi Collet <remi@remirepo.net> 4.7.3-1
- update to 4.7.3 (2017-07-20, regular maintenance release)
- raise dependency on phpmyadmin/sql-parser version 4.1.9

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Remi Collet <remi@remirepo.net> 4.7.2-1
- update to 4.7.2 (2017-06-29, regular maintenance release)
- raise dependency on phpmyadmin/sql-parser version 4.1.7
- always use system certificates

* Fri Jun  2 2017 Remi Collet <remi@remirepo.net> 4.7.1-1
- update to 4.7.1
- raise dependency on phpmyadmin/sql-parser version 4.1.2
- add dependency on phpmyadmin/motranslator
- add dependency on phpmyadmin/shapefile
- add dependency on google/recaptcha
- use fedora autoloader instead of composer one

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Remi Collet <remi@remirepo.net> 4.6.6-1
- update to 4.6.6 (2017-01-23, bug and security fixes)
- ensure phpmyadmin/sql-parser v3 is used

* Sat Nov 26 2016 Remi Collet <remi@remirepo.net> 4.6.5.1-2
- update to 4.6.5.1 (2016-11-26, bug fixes)

* Fri Nov 25 2016 Remi Collet <remi@fedoraproject.org> 4.6.5-1
- update to 4.6.5 (2016-11-25, security and bug fixes)
- bump dependency on sql-parser 3.4.13

* Sun Aug 28 2016 Robert Scheck <robert@fedoraproject.org> 4.6.4-2
- Use 'blowfish_secret' with 32 characters for new installation

* Sun Aug 28 2016 Robert Scheck <robert@fedoraproject.org> 4.6.4-1
- Upgrade to 4.6.4 (#1370778)

* Tue Jul 26 2016 Remi Collet <remi@remirepo.net> 4.6.3-2
- bump dependency on sql-parser 3.4.4

* Thu Jun 23 2016 Robert Scheck <robert@fedoraproject.org> 4.6.3-1
- Upgrade to 4.6.3 (#1349500)

* Thu May 26 2016 Robert Scheck <robert@fedoraproject.org> 4.6.2-1
- Upgrade to 4.6.2 (#1339852, #1340065)

* Wed May 04 2016 Robert Scheck <robert@fedoraproject.org> 4.6.1-1
- Upgrade to 4.6.1 (#1332531)

* Tue Mar 22 2016 Remi Collet <remi@remirepo.net> 4.6.0-1
- update to 4.6.0 (2016-03-22, features release)

* Thu Mar 03 2016 Robert Scheck <robert@fedoraproject.org> 4.5.5.1-1
- Upgrade to 4.5.5.1 (#1310918, #1313221, #1313224, #1313695,
  #1313696, thanks to Remi Collet)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.5.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 30 2016 Robert Scheck <robert@fedoraproject.org> 4.5.4.1-1
- Upgrade to 4.5.4.1

* Thu Jan 28 2016 Robert Scheck <robert@fedoraproject.org> 4.5.4-1
- Upgrade to 4.5.4

* Fri Dec 25 2015 Robert Scheck <robert@fedoraproject.org> 4.5.3.1-1
- Upgrade to 4.5.3.1 (#1294254)

* Thu Dec 24 2015 Robert Scheck <robert@fedoraproject.org> 4.5.3-1
- Upgrade to 4.5.3

* Mon Nov 23 2015 Robert Scheck <robert@fedoraproject.org> 4.5.2-1
- Upgrade to 4.5.2

* Sun Oct 25 2015 Robert Scheck <robert@fedoraproject.org> 4.5.1-1
- Upgrade to 4.5.1 (#1274938)

* Fri Sep 25 2015 Robert Scheck <robert@fedoraproject.org> 4.5.0.2-1
- Upgrade to 4.5.0.2 (#1266494)

* Fri Sep 25 2015 Robert Scheck <robert@fedoraproject.org> 4.5.0.1-1
- Upgrade to 4.5.0.1 (#1265647)

* Wed Sep 23 2015 Robert Scheck <robert@fedoraproject.org> 4.5.0-1
- Upgrade to 4.5.0 (#1265647)

* Sun Sep 20 2015 Robert Scheck <robert@fedoraproject.org> 4.4.15-1
- Upgrade to 4.4.15

* Tue Sep 08 2015 Robert Scheck <robert@fedoraproject.org> 4.4.14.1-1
- Upgrade to 4.4.14.1

* Thu Aug 20 2015 Robert Scheck <robert@fedoraproject.org> 4.4.14-1
- Upgrade to 4.4.14

* Sat Aug 08 2015 Robert Scheck <robert@fedoraproject.org> 4.4.13.1-1
- Upgrade to 4.4.13.1

* Fri Aug 07 2015 Robert Scheck <robert@fedoraproject.org> 4.4.13-1
- Upgrade to 4.4.13

* Tue Jul 21 2015 Robert Scheck <robert@fedoraproject.org> 4.4.12-1
- Upgrade to 4.4.12 (thanks to Remi Collet)

* Mon Jul 06 2015 Robert Scheck <robert@fedoraproject.org> 4.4.11-1
- Upgrade to 4.4.11

* Sat Jun 20 2015 Robert Scheck <robert@fedoraproject.org> 4.4.10-1
- Upgrade to 4.4.10 (#1232982)

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 04 2015 Robert Scheck <robert@fedoraproject.org> 4.4.9-1
- Upgrade to 4.4.9

* Thu May 28 2015 Robert Scheck <robert@fedoraproject.org> 4.4.8-1
- Upgrade to 4.4.8

* Sat May 16 2015 Robert Scheck <robert@fedoraproject.org> 4.4.7-1
- Upgrade to 4.4.7 (#1222215)

* Thu May 14 2015 Robert Scheck <robert@fedoraproject.org> 4.4.6.1-1
- Upgrade to 4.4.6.1 (#1221418, #1221580, #1221581)

* Thu May 07 2015 Robert Scheck <robert@fedoraproject.org> 4.4.6-1
- Upgrade to 4.4.6

* Tue May 05 2015 Robert Scheck <robert@fedoraproject.org> 4.4.5-1
- Upgrade to 4.4.5 (#1218633)

* Sun Apr 26 2015 Robert Scheck <robert@fedoraproject.org> 4.4.4-1
- Upgrade to 4.4.4 (#1215417)

* Mon Apr 20 2015 Robert Scheck <robert@fedoraproject.org> 4.4.3-1
- Upgrade to 4.4.3

* Mon Apr 13 2015 Robert Scheck <robert@fedoraproject.org> 4.4.2-1
- Upgrade to 4.4.2

* Fri Apr 10 2015 Robert Scheck <robert@fedoraproject.org> 4.4.1.1-1
- Upgrade to 4.4.1.1 (#1208320)

- Mon Apr 06 2015 Robert Scheck <robert@fedoraproject.org> 4.4.0-1
- Upgrade to 4.4.0 (thanks to Remi Collet)

* Mon Mar 30 2015 Robert Scheck <robert@fedoraproject.org> 4.3.13-1
- Upgrade to 4.3.13

* Sat Mar 14 2015 Robert Scheck <robert@fedoraproject.org> 4.3.12-1
- Upgrade to 4.3.12

* Wed Mar 04 2015 Robert Scheck <robert@fedoraproject.org> 4.3.11.1-1
- Upgrade to 4.3.11.1

* Tue Mar 03 2015 Robert Scheck <robert@fedoraproject.org> 4.3.11-1
- Upgrade to 4.3.11

* Sat Feb 21 2015 Robert Scheck <robert@fedoraproject.org> 4.3.10-1
- Upgrade to 4.3.10 (#1194949)

* Fri Feb 06 2015 Robert Scheck <robert@fedoraproject.org> 4.3.9-1
- Upgrade to 4.3.9

* Sat Jan 24 2015 Robert Scheck <robert@fedoraproject.org> 4.3.8-1
- Upgrade to 4.3.8

* Sat Jan 24 2015 Robert Scheck <robert@fedoraproject.org> 4.3.7-1
- Upgrade to 4.3.7 (#1183602)

* Wed Jan 07 2015 Robert Scheck <robert@fedoraproject.org> 4.3.6-1
- Upgrade to 4.3.6

* Mon Jan 05 2015 Robert Scheck <robert@fedoraproject.org> 4.3.5-1
- Upgrade to 4.3.5

* Sun Jan 04 2015 Robert Scheck <robert@fedoraproject.org> 4.3.4-1
- Upgrade to 4.3.4 (#1178413)

* Sun Dec 21 2014 Robert Scheck <robert@fedoraproject.org> 4.3.3-1
- Upgrade to 4.3.3

* Fri Dec 12 2014 Robert Scheck <robert@fedoraproject.org> 4.3.2-1
- Upgrade to 4.3.2

* Thu Dec 11 2014 Robert Scheck <robert@fedoraproject.org> 4.3.1-2
- Use %%{pkgname} rather %%{name} in %%post scriptlet (#1173189)

* Tue Dec 09 2014 Robert Scheck <robert@fedoraproject.org> 4.3.1-1
- Upgrade to 4.3.1

* Sat Dec 06 2014 Robert Scheck <robert@fedoraproject.org> 4.3.0-1
- Upgrade to 4.3.0 (thanks to Remi Collet)

* Thu Dec 04 2014 Robert Scheck <robert@fedoraproject.org> 4.2.13.1-1
- Upgrade to 4.2.13.1

* Sun Nov 30 2014 Robert Scheck <robert@fedoraproject.org> 4.2.13-1
- Upgrade to 4.2.13

* Thu Nov 20 2014 Robert Scheck <robert@fedoraproject.org> 4.2.12-1
- Upgrade to 4.2.12 (#1166397)

* Sat Nov 01 2014 Robert Scheck <robert@fedoraproject.org> 4.2.11-1
- Upgrade to 4.2.11 (#1159524)

* Wed Oct 22 2014 Robert Scheck <robert@fedoraproject.org> 4.2.10.1-1
- Upgrade to 4.2.10.1 (#1155272, #1155362)

* Mon Oct 13 2014 Robert Scheck <robert@fedoraproject.org> 4.2.10-1
- Upgrade to 4.2.10 (#1152115)

* Sat Oct  4 2014 Remi Collet <remi@fedoraproject.org> 4.2.9.1-2
- provide nginx configuration (Fedora >= 21)
- fix license handling

* Thu Oct 02 2014 Robert Scheck <robert@fedoraproject.org> 4.2.9.1-1
- Upgrade to 4.2.9.1 (#1148664)

* Sun Sep 21 2014 Robert Scheck <robert@fedoraproject.org> 4.2.9-1
- Upgrade to 4.2.9
- Set default charset for Apache explicitly

* Wed Sep 17 2014 Robert Scheck <robert@fedoraproject.org> 4.2.8.1-2
- Move rm(1) calls from %%install to %%prep (#1121355 #c10)

* Tue Sep 16 2014 Robert Scheck <robert@fedoraproject.org> 4.2.8.1-1
- Upgrade to 4.2.8.1 (#1141635)

* Mon Sep 01 2014 Robert Scheck <robert@fedoraproject.org> 4.2.8-1
- Upgrade to 4.2.8

* Mon Aug 18 2014 Robert Scheck <robert@fedoraproject.org> 4.2.7.1-1
- Upgrade to 4.2.7.1 (#1130865, #1130866, #1131104)

* Thu Jul 31 2014 Robert Scheck <robert@fedoraproject.org> 4.2.7-1
- Upgrade to 4.2.7

* Sat Jul 19 2014 Robert Scheck <robert@fedoraproject.org> 4.2.6-1
- Upgrade to 4.2.6 (#548260, #959946, #989660, #989668, #993613
  and #1000261, #1067713, #1110877, #1117600, #1117601)
- Switch from HTTP- to cookie-based authentication (for php-fpm)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Dec 12 2013 Ville Skyttä <ville.skytta@iki.fi> - 3.5.8.2-2
- Fix paths to changelog and license when doc dir is unversioned (#994036).
- Fix source URL, use xz compressed tarball.

* Wed Oct 09 2013 Paul Wouters <pwouters@redhat.com> - 3.5.8.2-1
- Upgrade to 3.5.8.2 (Various security issues)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 25 2013 Robert Scheck <robert@fedoraproject.org> 3.5.8.1-1
- Upgrade to 3.5.8.1 (#956398, #956401)

* Sat Apr 13 2013 Robert Scheck <robert@fedoraproject.org> 3.5.8-1
- Upgrade to 3.5.8 (#949868)

* Sat Feb 23 2013 Robert Scheck <robert@fedoraproject.org> 3.5.7-1
- Upgrade to 3.5.7 (#912097)

* Sun Feb 10 2013 Robert Scheck <robert@fedoraproject.org> 3.5.6-1
- Upgrade to 3.5.6 (#889450)

* Sun Nov 18 2012 Robert Scheck <robert@fedoraproject.org> 3.5.4-1
- Upgrade to 3.5.4 (#877727)

* Tue Oct 09 2012 Robert Scheck <robert@fedoraproject.org> 3.5.3-1
- Upgrade to 3.5.3

* Wed Aug 15 2012 Robert Scheck <robert@fedoraproject.org> 3.5.2.2-1
- Upgrade to 3.5.2.2 (#845736)

* Sat Aug 11 2012 Robert Scheck <robert@fedoraproject.org> 3.5.2.1-1
- Upgrade to 3.5.2.1 (#845736)

* Mon Jul 30 2012 Robert Scheck <robert@fedoraproject.org> 3.5.2-1
- Upgrade to 3.5.2 (#838310)

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun May 06 2012 Robert Scheck <robert@fedoraproject.org> 3.5.1-1
- Upgrade to 3.5.1 (#819171)

* Sat May 05 2012 Remi Collet <remi@fedoraproject.org> 3.5.0-2
- make configuration compatible apache 2.2 / 2.4

* Sun Apr 08 2012 Robert Scheck <robert@fedoraproject.org> 3.5.0-1
- Upgrade to 3.5.0 (#790782, #795020, #809146)

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.4.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Dec 22 2011 Robert Scheck <robert@fedoraproject.org> 3.4.9-1
- Upgrade to 3.4.9 (#769818)

* Sun Dec 04 2011 Robert Scheck <robert@fedoraproject.org> 3.4.8-1
- Upgrade to 3.4.8 (#759441)

* Sat Nov 12 2011 Robert Scheck <robert@fedoraproject.org> 3.4.7.1-1
- Upgrade to 3.4.7.1 (#753119)

* Sat Nov 05 2011 Robert Scheck <robert@fedoraproject.org> 3.4.7-1
- Upgrade to 3.4.7 (#746630, #746880)

* Sun Sep 18 2011 Robert Scheck <robert@fedoraproject.org> 3.4.5-1
- Upgrade to 3.4.5 (#733638, #738681, #629214)

* Thu Aug 25 2011 Robert Scheck <robert@fedoraproject.org> 3.4.4-1
- Upgrade to 3.4.4 (#733475, #733477, #733480)

* Tue Jul 26 2011 Robert Scheck <robert@fedoraproject.org> 3.4.3.2-2
- Disabled the warning for missing internal database relation
- Reworked spec file to build phpMyAdmin3 for RHEL 5 (#725885)

* Mon Jul 25 2011 Robert Scheck <robert@fedoraproject.org> 3.4.3.2-1
- Upgrade to 3.4.3.2 (#725377, #725381, #725382, #725383, #725384)

* Wed Jul 06 2011 Robert Scheck <robert@fedoraproject.org> 3.4.3.1-1
- Upgrade to 3.4.3.1 (#718964)

* Mon Jun 13 2011 Robert Scheck <robert@fedoraproject.org> 3.4.2-1
- Upgrade to 3.4.2 (#711743)

* Sun May 29 2011 Robert Scheck <robert@fedoraproject.org> 3.4.1-1
- Upgrade to 3.4.1 (#704171)

* Mon Mar 21 2011 Robert Scheck <robert@fedoraproject.org> 3.3.10-1
- Upstream released 3.3.10 (#661335, #662366, #662367, #689213)

* Sun Feb 13 2011 Robert Scheck <robert@fedoraproject.org> 3.3.9.2-1
- Upstream released 3.3.9.2 (#676172)

* Thu Feb 10 2011 Robert Scheck <robert@fedoraproject.org> 3.3.9.1-1
- Upstream released 3.3.9.1 (#676172)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 03 2011 Robert Scheck <robert@fedoraproject.org> 3.3.9-1
- Upstream released 3.3.9 (#666925)

* Mon Nov 29 2010 Robert Scheck <robert@fedoraproject.org> 3.3.8.1-1
- Upstream released 3.3.8.1

* Fri Oct 29 2010 Robert Scheck <robert@fedoraproject.org> 3.3.8-1
- Upstream released 3.3.8 (#631748)

* Wed Sep 08 2010 Robert Scheck <robert@fedoraproject.org> 3.3.7-1
- Upstream released 3.3.7 (#631824, #631829)

* Sun Aug 29 2010 Robert Scheck <robert@fedoraproject.org> 3.3.6-1
- Upstream released 3.3.6 (#628301)

* Fri Aug 20 2010 Robert Scheck <robert@fedoraproject.org> 3.3.5.1-1
- Upstream released 3.3.5.1 (#625877, #625878)
- Added patch to fix wrong variable check at nopassword (#622428)

* Tue Jul 27 2010 Robert Scheck <robert@fedoraproject.org> 3.3.5-1
- Upstream released 3.3.5 (#618586)

* Tue Jun 29 2010 Robert Scheck <robert@fedoraproject.org> 3.3.4-1
- Upstream released 3.3.4 (#609057)

* Sat Jun 26 2010 Robert Scheck <robert@fedoraproject.org> 3.3.3-1
- Upstream released 3.3.3 (#558322, #589288, #589487)

* Sun Jan 10 2010 Robert Scheck <robert@fedoraproject.org> 3.2.5-1
- Upstream released 3.2.5

* Thu Dec 03 2009 Robert Scheck <robert@fedoraproject.org> 3.2.4-1
- Upstream released 3.2.4 (#540871, #540891)

* Thu Nov 05 2009 Robert Scheck <robert@fedoraproject.org> 3.2.3-1
- Upstream released 3.2.3

* Tue Oct 13 2009 Robert Scheck <robert@fedoraproject.org> 3.2.2.1-1
- Upstream released 3.2.2.1 (#528769)
- Require php-mcrypt for cookie authentication (#526979)

* Sun Sep 13 2009 Robert Scheck <robert@fedoraproject.org> 3.2.2-1
- Upstream released 3.2.2

* Sun Sep 06 2009 Robert Scheck <robert@fedoraproject.org> 3.2.1-2
- Added ::1 for localhost/loopback access (for IPv6 users)

* Mon Aug 10 2009 Robert Scheck <robert@fedoraproject.org> 3.2.1-1
- Upstream released 3.2.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jun 30 2009 Robert Scheck <robert@fedoraproject.org> 3.2.0.1-1
- Upstream released 3.2.0.1 (#508879)

* Tue Jun 30 2009 Robert Scheck <robert@fedoraproject.org> 3.2.0-1
- Upstream released 3.2.0

* Fri May 15 2009 Robert Scheck <robert@fedoraproject.org> 3.1.5-1
- Upstream released 3.1.5

* Sat Apr 25 2009 Robert Scheck <robert@fedoraproject.org> 3.1.4-1
- Upstream released 3.1.4

* Tue Apr 14 2009 Robert Scheck <robert@fedoraproject.org> 3.1.3.2-1
- Upstream released 3.1.3.2 (#495768)

* Wed Mar 25 2009 Robert Scheck <robert@fedoraproject.org> 3.1.3.1-1
- Upstream released 3.1.3.1 (#492066)

* Sun Mar 01 2009 Robert Scheck <robert@fedoraproject.org> 3.1.3-1
- Upstream released 3.1.3

* Mon Feb 23 2009 Robert Scheck <robert@fedoraproject.org> 3.1.2-2
- Rebuilt against rpm 4.6

* Tue Jan 20 2009 Robert Scheck <robert@fedoraproject.org> 3.1.2-1
- Upstream released 3.1.2

* Thu Dec 11 2008 Robert Scheck <robert@fedoraproject.org> 3.1.1-1
- Upstream released 3.1.1 (#475954)

* Sat Nov 29 2008 Robert Scheck <robert@fedoraproject.org> 3.1.0-1
- Upstream released 3.1.0
- Replaced LocationMatch with Directory directive (#469451)

* Thu Oct 30 2008 Robert Scheck <robert@fedoraproject.org> 3.0.1.1-1
- Upstream released 3.0.1.1 (#468974)

* Wed Oct 22 2008 Robert Scheck <robert@fedoraproject.org> 3.0.1-1
- Upstream released 3.0.1

* Sun Oct 19 2008 Robert Scheck <robert@fedoraproject.org> 3.0.0-1
- Upstream released 3.0.0

* Mon Sep 22 2008 Robert Scheck <robert@fedoraproject.org> 2.11.9.2-1
- Upstream released 2.11.9.2 (#463260)

* Tue Sep 16 2008 Robert Scheck <robert@fedoraproject.org> 2.11.9.1-1
- Upstream released 2.11.9.1 (#462430)

* Fri Aug 29 2008 Robert Scheck <robert@fedoraproject.org> 2.11.9-1
- Upstream released 2.11.9

* Mon Jul 28 2008 Robert Scheck <robert@fedoraproject.org> 2.11.8.1-1
- Upstream released 2.11.8.1 (#456637, #456950)

* Mon Jul 28 2008 Robert Scheck <robert@fedoraproject.org> 2.11.8-1
- Upstream released 2.11.8 (#456637)

* Tue Jul 15 2008 Robert Scheck <robert@fedoraproject.org> 2.11.7.1-1
- Upstream released 2.11.7.1 (#455520)

* Mon Jun 23 2008 Robert Scheck <robert@fedoraproject.org> 2.11.7-1
- Upstream released 2.11.7 (#452497)

* Tue Apr 29 2008 Robert Scheck <robert@fedoraproject.org> 2.11.6-1
- Upstream released 2.11.6

* Tue Apr 22 2008 Robert Scheck <robert@fedoraproject.org> 2.11.5.2-1
- Upstream released 2.11.5.2 (#443683)

* Sat Mar 29 2008 Robert Scheck <robert@fedoraproject.org> 2.11.5.1-1
- Upstream released 2.11.5.1

* Mon Mar 03 2008 Robert Scheck <robert@fedoraproject.org> 2.11.5-1
- Upstream released 2.11.5

* Sun Jan 13 2008 Robert Scheck <robert@fedoraproject.org> 2.11.4-1
- Upstream released 2.11.4
- Corrected mod_security example in configuration file (#427119)

* Sun Dec 09 2007 Robert Scheck <robert@fedoraproject.org> 2.11.3-1
- Upstream released 2.11.3
- Removed the RPM scriptlets doing httpd restarts (#227025)
- Patched an information disclosure known as CVE-2007-0095 (#221694)
- Provide virtual phpmyadmin package and a httpd alias (#231431)

* Wed Nov 21 2007 Robert Scheck <robert@fedoraproject.org> 2.11.2.2-1
- Upstream released 2.11.2.2 (#393771)

* Tue Nov 20 2007 Mike McGrath <mmcgrath@redhat.com> 2.11.2.1-1
- Upstream released new version

* Mon Oct 29 2007 Mike McGrath <mmcgrath@redhat.com> 2.11.2-1
- upstream released new version

* Mon Oct 22 2007 Mike McGrath <mmcgrath@redhat.com> 2.11.1.2-1
- upstream released new version

* Thu Sep 06 2007 Mike McGrath <mmcgrath@redhat.com> 2.11.0-1
- Upstream released new version
- Altered sources file as required
- Added proper license

* Mon Jul 23 2007 Mike McGrath <mmcgrath@redhat.com> 2.10.3-1
- Upstream released new version

* Sat Mar 10 2007 Mike McGrath <mmcgrath@redhat.com> 2.10.0.2-3
- Switched to the actual all-languages, not just utf-8

* Sun Mar 04 2007 Mike McGrath <mmcgrath@redhat.com> 2.10.0.2-1
- Upstream released new version

* Sat Jan 20 2007 Mike McGrath <imlinux@gmail.com> 2.9.2-1
- Upstream released new version

* Fri Dec 08 2006 Mike McGrath <imlinux@gmail.com> 2.9.1.1-2
- Fixed bug in spec file

* Fri Dec 08 2006 Mike McGrath <imlinux@gmail.com> 2.9.1.1-1
- Upstream released new version

* Wed Nov 15 2006 Mike McGrath <imlinux@gmail.com> 2.9.1-3alpha
- Added dist tag

* Wed Nov 15 2006 Mike McGrath <imlinux@gmail.com> 2.9.1-2alpha
- Fixed 215159

* Fri Nov 10 2006 Mike McGrath <imlinux@gmail.com> 2.9.1-1alpha
- Added alpha tag since this is a release candidate

* Tue Nov 07 2006 Mike McGrath <imlinux@gmail.com> 2.9.1-1
- Upstream released new version

* Wed Oct 04 2006 Mike McGrath <imlinux@gmail.com> 2.9.0.2-1
- Upstream released new version

* Thu Jul 06 2006 Mike McGrath <imlinux@gmail.com> 2.8.2-2
- Fixed a typo in the Apache config

* Mon Jul 03 2006 Mike McGrath <imlinux@gmail.com> 2.8.2-1
- Upstream released 2.8.2
- Added more restrictive directives to httpd/conf.d/phpMyAdmin.conf
- removed htaccess file from the libraries dir
- Specific versions for various requires

* Sat May 13 2006 Mike McGrath <imlinux@gmail.com> 2.8.0.4-1
- Upstream released 2.8.0.4
- Added requires php, instead of requires httpd, now using webserver

* Sun May 07 2006 Mike McGrath <imlinux@gmail.com> 2.8.0.3-2
- Added mysql-php and php-mbstring as a requires

* Fri Apr 07 2006 Mike McGrath <imlinux@gmail.com> 2.8.0.3-1
- Fixed XSS vulnerability: PMASA-2006-1
- It was possible to conduct an XSS attack with a direct call to some scripts
- under the themes directory.

* Tue Apr 04 2006 Mike McGrath <imlinux@gmail.com> 2.8.0.2-3
- Made config files actually configs
- Moved doc files to the doc dir

* Tue Apr 04 2006 Mike McGrath <imlinux@gmail.com> 2.8.0.2-2
- Moved everything to %%{_datadir}
- Moved config file to /etc/
- Used description from phpMyAdmin project info

* Mon Apr 03 2006 Mike McGrath <imlinux@gmail.com> 2.8.0.2-1
- Initial Spec file creation for Fedora
