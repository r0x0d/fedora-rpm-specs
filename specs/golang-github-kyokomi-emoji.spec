# Generated by go2rpm
%bcond_without check

# https://github.com/kyokomi/emoji
%global goipath         github.com/kyokomi/emoji
Version:                2.2.8

%gometa

%global goaltipaths     github.com/kyokomi/emoji/v2

%global common_description %{expand:
Emoji terminal output for Go.}

%global golicenses      LICENSE
%global godocs          example README.md

Name:           %{goname}
Release:        13%{?dist}
Summary:        Emoji terminal output for Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires:  golang(github.com/PuerkitoBio/goquery)

%description
%{common_description}

%gopkg

%prep
%goprep

%build
for cmd in cmd/generateEmojiCodeMap ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc example README.md
%{_bindir}/*

%gopkgfiles

%changelog
* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 11 2024 Maxwell G <maxwell@gtmx.me> - 2.2.8-12
- Rebuild for golang 1.22.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 2.2.8-6
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Sat Jun 18 2022 Robert-André Mauchin <zebob.m@gmail.com> - 2.2.8-5
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Jan  3 13:01:19 CET 2021 Robert-André Mauchin <zebob.m@gmail.com> - 2.2.8-1
- Update to 2.2.8
- Close: rhbz#1911613

* Tue Jul 28 21:12:39 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 2.2.5-1
- Update to 2.2.5

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 15 2020 Olivier Lemasle <o.lemasle@gmail.com> - 2.2.2-1
- Update to latest upstream - v2.2.2 (#1824009)

* Wed Apr 08 2020 Olivier Lemasle <o.lemasle@gmail.com> - 2.2.1-1
- Update to 2.2.1 (#1822119) - Fix https://github.com/kyokomi/emoji/pull/41

* Sat Apr 04 2020 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0 (#1820838)

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jun 02 18:38:54 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 2.1.0-2
- Update to new macros

* Sat Feb 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.0-1
- Update to latest version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 08 2017 Olivier Lemasle <o.lemasle@gmail.com> - 1.5-3
- Fix package description (add a period)

* Mon Mar 06 2017 Olivier Lemasle <o.lemasle@gmail.com> - 1.5-2
- Fix changelog and rpmlint issues

* Sun Mar 05 2017 Olivier Lemasle <o.lemasle@gmail.com> - 1.5-1
- Update to upstream release 1.5

* Sat Jun 11 2016 Olivier Lemasle <o.lemasle@gmail.com> - 1.4-1
- First package for Fedora