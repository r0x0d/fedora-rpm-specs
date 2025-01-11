Name:           php-manual-en
Summary:        Documentation for the PHP programming language
Version:        20250109
Release:        1%{?dist}
License:        CC-BY-3.0
URL:            https://www.php.net/download-docs.php
Source0:        https://www.php.net/distributions/manual/php_manual_en.tar.gz
BuildArch:      noarch

%description
English-language documentation for the PHP programming language.

%prep
%setup -q -c

%install
mkdir -p %{buildroot}/%{_defaultdocdir}/php-manual/en
cp -pr php-chunked-xhtml %{buildroot}/%{_defaultdocdir}/php-manual/en/html
cat >LICENSE <<EOF
For licensing information please see:

%{_defaultdocdir}/php-manual/en/html/copyright.html
EOF

%files
%license LICENSE
%doc %{_defaultdocdir}/php-manual

%changelog
* Thu Jan 09 2025 Stephen Medina <stephen@lilmail.xyz> - 20250109-1
- Update to latest on 2025-01-09.

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20221028-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20221028-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 20221028-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20221028-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 20221028-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 1 2022 Stephen Medina <stephen@lilmail.xyz> - 20221028-2
- Fix license expression

* Fri Oct 28 2022 Stephen Medina <stephen@lilmail.xyz> - 20221028-1
- Update to latest on 2022-10-28

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20201202-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 20201202-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20201202-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 20201202-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Dec 02 2020 Stephen Medina <stephen@lilmail.xyz> - 20201202-1
- Update to version 20201202

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20140725-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20140725-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20140725-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 20140725-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20140725-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20140725-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20140725-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20140725-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20140725-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20140725-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jul 25 2014 Tim Jackson <rpm@timj.co.uk> 20140725-1
- Update to 20140725 version

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120803-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120803-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20120803-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 09 2012 Tim Jackson <rpm@timj.co.uk> 20120803-1
- Update to 2012-08-03 version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100611-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100611-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20100611-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jun 17 2010 Tim Jackson <rpm@timj.co.uk> 20100611-1
- Update to 2010-06-11 version

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090619-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Jun 21 2009 Tim Jackson <rpm@timj.co.uk> 20090619-1
- Update to 2009-06-19 version

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20090213-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Feb 14 2009 Tim Jackson <rpm@timj.co.uk> 20090213-1
- Update to 2009-02-13 version

* Wed Sep 24 2008 Tim Jackson <rpm@timj.co.uk> 20080919-1
- Update to 2008-09-19 version
- License is now Creative Commons Attribution License

* Thu Nov 15 2007 Tim Jackson <rpm@timj.co.uk> 20070617-1
- Update to 2007-06-17 version
- Rename license to "Open Publication"
- Add versioning on php-manual-en-us Provide

* Sat Dec 09 2006 Tim Jackson <rpm@timj.co.uk> 20061119-1
- Update to 2006-11-19 version

* Sat Oct 28 2006 Tim Jackson <rpm@timj.co.uk> 20061026-1
- Update to 2006-10-26 version

* Mon Sep 25 2006 Tim Jackson <rpm@timj.co.uk> 20060920-1
- Update to 2006-09-20 version

* Sat Sep 09 2006 Tim Jackson <rpm@timj.co.uk> 20060906-1
- Update to 2006-09-06 version

* Sat Aug 19 2006 Tim Jackson <rpm@timj.co.uk> 20060813-1
- Update to 2006-08-13 version
- Add LICENSE as pointer to licensing information

* Sun Aug 06 2006 Tim Jackson <rpm@timj.co.uk> 20060725-1
- Update to 2006-07-25 version
- Own defaultdocdir/php-manual
- Macro change: datadir/docs -> defaultdocdir
- Rename License tag to stop rpmlint whinging

* Mon Jun 26 2006 Tim Jackson <rpm@timj.co.uk> 20060527-2
- Update Source to an absolute URL
- Provide php-manual-en-us (in case of a future split into en-gb etc.)

* Thu Jun 22 2006 Tim Jackson <rpm@timj.co.uk> 20060527-1
- Update to 2006-05-27 version of the manual

* Tue May 09 2006 Tim Jackson <rpm@timj.co.uk> 20060421-1
- Initial RPM build
