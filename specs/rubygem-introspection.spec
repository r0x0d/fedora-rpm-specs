# Generated from introspection-0.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name introspection

Name: rubygem-%{gem_name}
Version: 0.0.4
Release: 19%{?dist}
Summary: Dynamic inspection of the hierarchy of method definitions on a Ruby object
# https://github.com/floehopper/introspection/issues/1
License: MIT
URL: http://jamesmead.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(metaclass) => 0.0.1
BuildRequires: rubygem(metaclass) < 0.1
# There is no #assert_nothing_raised in minitest 5.x
BuildRequires: rubygem(minitest)
BuildArch: noarch

%description
Dynamic inspection of the hierarchy of method definitions on a Ruby object.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -c -T
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# Disable Bundler.
sed -i '/bundler\/setup/ s/^/#/' test/test_helper.rb

# Drop BlankSlate test case. There should be no need for BlankSlate, when
# there is BasicObject available for years.
# https://github.com/floehopper/introspection/issues/11
sed -i -e '/require.*blankslate/ s/^/#/' \
  -e '/def test_should_cope_with_blankslate_object$/a\\    skip' \
  test/snapshot_test.rb

ruby -Ilib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd


%files
%license %{gem_instdir}/COPYING.txt
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/introspection.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_instdir}/README.md
%{gem_instdir}/Gemfile
%{gem_instdir}/Rakefile
%{gem_instdir}/samples
%{gem_instdir}/test
%doc %{gem_docdir}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Vít Ondruch <vondruch@redhat.com> - 0.0.4-18
- Drop BlankSlate dependency.

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Pavel Valena <pvalena@redhat.com> - 0.0.4-1
- Update to introspection 0.0.4(rhbz#1390394)
  - Remove patch0, subsumed
  - Remove patch1, subsumed

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 19 2014 Vít Ondruch <vondruch@redhat.com> - 0.0.3-3
- Fix FTBFS in Rawhide (rhbz#1107144).

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Apr 07 2014 Vít Ondruch <vondruch@redhat.com> - 0.0.3-1
- Update to introspection 0.0.3.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Feb 25 2013 Vít Ondruch <vondruch@redhat.com> - 0.0.2-8
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 19 2012 Vít Ondruch <vondruch@redhat.com> - 0.0.2-5
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 04 2011 Vít Ondruch <vondruch@redhat.com> - 0.0.2-3
- Fix BuildRequires and test suite.
- Move README.md into -doc subpackage and mark it properly.

* Tue Oct 04 2011 Vít Ondruch <vondruch@redhat.com> - 0.0.2-2
- Clarified license.

* Mon Oct 03 2011 Vít Ondruch <vondruch@redhat.com> - 0.0.2-1
- Initial package
