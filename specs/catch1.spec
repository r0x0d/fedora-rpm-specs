%global debug_package %{nil}

Name:           catch1
Version:        1.12.2
Release:        18%{?dist}
Summary:        A modern, C++-native, header-only, framework for unit-tests, TDD and BDD

License:        BSL-1.0
URL:            https://github.com/catchorg/Catch2
Source0:        https://github.com/catchorg/Catch2/archive/v%{version}/%{name}-%{version}.tar.gz
# https://github.com/catchorg/Catch2/issues/2178
Patch0:         catch1-sigstksz.patch

BuildRequires:  cmake make gcc-c++

%description
Catch stands for C++ Automated Test Cases in Headers and is a
multi-paradigm automated test framework for C++ and Objective-C (and,
maybe, C). It is implemented entirely in a set of header files, but
is packaged up as a single header for extra convenience.


%package        devel
Summary:        Development files for %{name}
Provides:       %{name}-static = %{version}-%{release}

%description    devel
Catch stands for C++ Automated Test Cases in Headers and is a
multi-paradigm automated test framework for C++ and Objective-C (and,
maybe, C). It is implemented entirely in a set of header files, but
is packaged up as a single header for extra convenience.


%prep
%autosetup -p 1 -n Catch2-%{version}


%build
%cmake
%cmake_build


%install
mkdir -p %{buildroot}%{_includedir}
cp -pr include  %{buildroot}%{_includedir}/catch


%check
%ctest


%files devel
%doc README.md catch-logo-small.png docs
%license LICENSE.txt
%{_includedir}/catch


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Feb 22 2023 Tom Hughes <tom@compton.nu> - 1.12.2-13
- Drop unnecessary conflict with catch-devel

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 19 2021 Tom Hughes <tom@compton.nu> - 1.12.2-8
- Add patch for non-constant SIGSTKSZ

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 15 2018 Tom Hughes <tom@compton.nu> - 1.12.2-1
- Update to 1.12.2 upstream release

* Sat Mar  3 2018 Tom Hughes <tom@compton.nu> - 1.12.1-1
- Update to 1.12.1 upstream release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.12.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 14 2018 Tom Hughes <tom@compton.nu> - 1.12.0-1
- Update to 1.12.0 upstream release

* Wed Nov  1 2017 Tom Hughes <tom@compton.nu> - 1.11.0-1
- Update to 1.11.0 upstream release

* Sun Aug 27 2017 Tom Hughes <tom@compton.nu> - 1.10.0-1
- Update to 1.10.0 upstream release

* Fri Aug 11 2017 Tom Hughes <tom@compton.nu> - 1.9.7-1
- Update to 1.9.7 upstream release

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Tom Hughes <tom@compton.nu> - 1.9.6-1
- Update to 1.9.6 upstream release

* Fri Jun 16 2017 Tom Hughes <tom@compton.nu> - 1.9.5-1
- Update to 1.9.5 upstream release

* Tue May 16 2017 Tom Hughes <tom@compton.nu> - 1.9.4-1
- Update to 1.9.4 upstream release

* Wed Apr 26 2017 Tom Hughes <tom@compton.nu> - 1.9.3-1
- Update to 1.9.3 upstream release

* Tue Apr 25 2017 Tom Hughes <tom@compton.nu> - 1.9.2-1
- Update to 1.9.2 upstream release

* Mon Apr 10 2017 Tom Hughes <tom@compton.nu> - 1.9.1-1
- Update to 1.9.1 upstream release

* Sat Apr  8 2017 Tom Hughes <tom@compton.nu> - 1.9.0-1
- Update to 1.9.0 upstream release

* Wed Mar 15 2017 Tom Hughes <tom@compton.nu> - 1.8.2-1
- Update to 1.8.2 upstream release

* Sat Mar  4 2017 Tom Hughes <tom@compton.nu> - 1.8.1-1
- Update to 1.8.1 upstream release

* Wed Mar  1 2017 Tom Hughes <tom@compton.nu> - 1.8.0-1
- Update to 1.8.0 upstream release

* Fri Feb 10 2017 Tom Hughes <tom@compton.nu> - 1.7.1-1
- Update to 1.7.1 upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb  3 2017 Tom Hughes <tom@compton.nu> - 1.7.0-1
- Update to 1.7.0 upstream release

* Sun Jan 29 2017 Tom Hughes <tom@compton.nu> - 1.6.1-1
- Update to 1.6.1 upstream release

* Sun Jan 15 2017 Tom Hughes <tom@compton.nu> - 1.6.0-1
- Update to 1.6.0 upstream release

* Tue Dec 13 2016 Tom Hughes <tom@compton.nu> - 1.5.9-1
- Update to 1.5.9 upstream release

* Thu Nov 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.5.8-1
- Update to 1.5.8

* Sat May 14 2016 Tom Hughes <tom@compton.nu> - 1.5.4-1
- Update to 1.5.4 upstream release

* Thu Apr 28 2016 Tom Hughes <tom@compton.nu> - 1.5.1-1
- Update to 1.5.1 upstream release

* Sun Apr 24 2016 Tom Hughes <tom@compton.nu> - 1.5.0-1
- Update to 1.5.0 upstream release

* Wed Mar 30 2016 Tom Hughes <tom@compton.nu> - 1.4.0-1
- Update to 1.4.0 upstream release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Sep 18 2015 Tom Hughes <tom@compton.nu> - 1.2.1-1
- Initial build
