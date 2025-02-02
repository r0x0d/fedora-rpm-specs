# Generated from activerecord-1.15.5.gem by gem2rpm -*- rpm-spec -*-
%global gem_name activerecord

Name: rubygem-%{gem_name}
Epoch: 1
Version: 7.0.8
Release: 7%{?dist}
Summary: Object-relational mapper framework (part of Rails)
License: MIT
URL: http://rubyonrails.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}%{?prerelease}.gem
# The gem doesn't ship with the test suite.
# You may check it out like so
# git clone http://github.com/rails/rails.git
# cd rails/activerecord && git archive -v -o activerecord-7.0.8-tests.txz v7.0.8 test/
Source1: activerecord-%{version}%{?prerelease}-tests.txz
# The tools are needed for the test suite, are however unpackaged in gem file.
# You may check it out like so
# git clone http://github.com/rails/rails.git --no-checkout
# cd rails && git archive -v -o rails-7.0.8-tools.txz v7.0.8 tools/
Source2: rails-%{version}%{?prerelease}-tools.txz
# Fixes for Minitest 5.16+
# https://github.com/rails/rails/pull/45380
Patch1: rubygem-activerecord-7.0.2.3-Remove-the-multi-call-form-of-assert_called_with.patch
# https://github.com/rails/rails/pull/45370
Patch2: rubygem-activerecord-7.0.2.3-Fix-tests-for-minitest-5.16.patch
# https://github.com/rails/rails/pull/46831
Patch3: rubygem-activerecord-7.0.5-remove-require-pathname-from-drop-method.patch
Patch4: rubygem-activerecord-7.0.5-remove-require-pathname-from-drop-method-tests.patch
# Drop mutex_m dependency to ease Ruby 3.4 compatibility.
# https://github.com/rails/rails/pull/49674
Patch5: rubygem-activerecord-7.2.0-Drop-dependency-on-mutex-m.patch
# This is inspired by https://github.com/rails/rails/commit/a1c0173ee3f5fef4ea0d6d2c90dc2b1d8672d473
# but upstream rather added the dependency in AS:
# https://github.com/rails/rails/commit/81699b52d2acff1840e3ace5e59412f4fa3934ab
Patch6: rubygem-activerecord-7.0.8-Replace-Mutex_m-by-MonitorMixin.patch
# Ruby 3.4 `Hash#inspect` compatibility.
# https://github.com/rails/rails/pull/53202/commits/2fc43621ff0b965d25b0140be0c9599baa52501b
Patch7: rubygem-activerecord-8.0.0-Update-Active-Record-test-suite-for-Ruby-3-4-Hash-inspect.patch
# Unlock Sqlite3 2.x+
# https://github.com/rails/rails/issues/52309
# https://github.com/rails/rails/commit/3271c4f6d221a73af801d7d57905f0cece374e05
Patch8: rubygem-activerecord-7.1.4-Allow-sqlite3-to-float-to-version-2.patch
# Sqlite3 2.x freezes some fields.
# https://github.com/rails/rails/pull/50859
Patch9: rubygem-activerecord-7.1.4-Don-t-mutate-row-arrays-that-come-back-from-the-database.patch

# Database dump/load reuires the executable.
Suggests: %{_bindir}/sqlite3
BuildRequires: rubygems-devel
BuildRequires: rubygem(bcrypt)
BuildRequires: rubygem(activesupport) = %{version}
BuildRequires: rubygem(activemodel)   = %{version}
BuildRequires: rubygem(actionpack)   = %{version}
BuildRequires: rubygem(builder)
BuildRequires: rubygem(sqlite3)
BuildRequires: rubygem(mocha)
BuildRequires: rubygem(rack)
BuildRequires: rubygem(pg)
BuildRequires: rubygem(benchmark-ips)
BuildRequires: rubygem(zeitwerk)
BuildRequires: %{_bindir}/sqlite3
BuildRequires: tzdata
BuildArch: noarch

%description
Implements the ActiveRecord pattern (Fowler, PoEAA) for ORM. It ties database
tables and classes together for business objects, like Customer or
Subscription, that can find, save, and destroy themselves without resorting to
manual SQL.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{epoch}:%{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}%{?prerelease} -b1 -b2

%patch 3 -p2

pushd %{_builddir}
%patch 1 -p2
%patch 2 -p2
%patch 4 -p2
%patch 7 -p2
%patch 9 -p2
popd
%patch 5 -p2
%patch 6 -p2
%patch 8 -p2

%build
gem build ../%{gem_name}-%{version}%{?prerelease}.gemspec
%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/tools ..
# Move the tests into place.
mv %{_builddir}/test .

# Remove unnecessary dependency
sed -i '/require .byebug./ s/^/#/g' test/cases/base_prevent_writes_test.rb

# Build system is slower than expected
sed -i '/assert_slower_by_at_most/ s/1\.4/2.5/' \
  test/cases/encryption/performance/envelope_encryption_performance_test.rb

# Test adapters separately
mv -v test/cases/adapters/ %{_builddir}/.

# Run without adapters
ruby -Itest:lib -e '
  Dir.glob("./test/cases/**/*_test.rb")
    .sort
    .reject { |f| f =~ %r|/encryption/performance/| }
    .each { |f| require f }'

# Return the adapters to test them
mv -v %{_builddir}/adapters/ test/cases/.

# Run tests for adapters only, but without postgresql
ruby -Itest:lib -e '
  Dir.glob("./test/cases/adapters/**/*_test.rb")
    .sort
    .reject {|x| x =~ %r|/postgresql/| }
    .each { |f| require f }'

# TODO: Run postgresql adapter tests, in isolation.
# Adapter and database needs to be set up beforehand.
#ruby -Itest:lib -e '
#  Dir.glob("./test/cases/adapters/**/*_test.rb")
#    .sort
#    .select { |x| x =~ %r|/postgresql/| }
#    .each { |f| fork { require f } }'
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/MIT-LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/examples

%changelog
* Thu Jan 30 2025 Vít Ondruch <vondruch@redhat.com> - 1:7.0.8-7
- Unlock Sqlite3 2.x+

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Nov 20 2024 Vít Ondruch <vondruch@redhat.com> - 1:7.0.8-5
- Ruby 3.4 compatibility fixes.

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Sep 10 2023 Pavel Valena <pvalena@redhat.com> - 1:7.0.8-1
- Update to activerecord 7.0.8.

* Mon Aug 28 2023 Pavel Valena <pvalena@redhat.com> - 1:7.0.7.2-1
- Update to activerecord 7.0.7.2.

* Thu Aug 10 2023 Pavel Valena <pvalena@redhat.com> - 1:7.0.7-1
- Update to activerecord 7.0.7.

* Sun Jul 23 2023 Pavel Valena <pvalena@redhat.com> - 1:7.0.6-1
- Update to activerecord 7.0.6.

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue May 30 2023 Pavel Valena <pvalena@redhat.com> - 1:7.0.5-1
- Update to activerecord 7.0.5.

* Tue Mar 14 2023 Pavel Valena <pvalena@redhat.com> - 1:7.0.4.3-1
- Update to activerecord 7.0.4.3.

* Wed Jan 25 2023 Pavel Valena <pvalena@redhat.com> - 1:7.0.4.2-1
- Update to activerecord 7.0.4.2.

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Sep 15 2022 Pavel Valena <pvalena@redhat.com> - 1:7.0.4-1
- Update to activerecord 7.0.4.

* Tue Aug 02 2022 Vít Ondruch <vondruch@redhat.com> - 1:7.0.2.3-3
- Fix Minitest 5.16+ compatibility.
  Resolves: rhbz#2113685

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:7.0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Mar 14 2022 Pavel Valena <pvalena@redhat.com> - 1:7.0.2.3-1
- Update to activerecord 7.0.2.3.

* Wed Feb 09 2022 Pavel Valena <pvalena@redhat.com> - 1:7.0.2-1
- Update to activerecord 7.0.2.

* Thu Feb 03 2022 Pavel Valena <pvalena@redhat.com> - 1:7.0.1-1
- Update to activerecord 7.0.1.

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Sep 17 2021 Pavel Valena <pvalena@redhat.com> - 1:6.1.4.1-1
- Update to activerecord 6.1.4.1.

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 30 2021 Pavel Valena <pvalena@redhat.com> - 1:6.1.4-1
- Update to activerecord 6.1.4.

* Tue May 18 2021 Pavel Valena <pvalena@redhat.com> - 1:6.1.3.2-1
- Update to activerecord 6.1.3.2.

* Fri Apr 09 2021 Pavel Valena <pvalena@redhat.com> - 1:6.1.3.1-1
- Update to activerecord 6.1.3.1.

* Thu Feb 18 2021 Pavel Valena <pvalena@redhat.com> - 1:6.1.3-1
- Update to activerecord 6.1.3.

* Mon Feb 15 2021 Pavel Valena <pvalena@redhat.com> - 1:6.1.2.1-1
- Update to activerecord 6.1.2.1.

* Wed Jan 27 2021 Pavel Valena <pvalena@redhat.com> - 1:6.1.1-1
- Update to activerecord 6.1.1.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:6.0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct  8 11:46:23 CEST 2020 Pavel Valena <pvalena@redhat.com> - 1:6.0.3.4-1
- Update to activerecord 6.0.3.4.
  Resolves: rhbz#1877501

* Tue Sep 22 00:45:21 CEST 2020 Pavel Valena <pvalena@redhat.com> - 1:6.0.3.3-1
- Update to activerecord 6.0.3.3.
  Resolves: rhbz#1877501

* Mon Aug 17 05:04:27 GMT 2020 Pavel Valena <pvalena@redhat.com> - 1:6.0.3.2-1
- Update to activerecord 6.0.3.2.
  Resolves: rhbz#1742794

* Mon Aug 03 07:01:37 GMT 2020 Pavel Valena <pvalena@redhat.com> - 6.0.3.1-1
- Update to ActiveRecord 6.0.3.1.
  Resolves: rhbz#1742794

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Apr 17 2020 Vít Ondruch <vondruch@redhat.com> - 1:5.2.3-4
- Fix Ruby 2.7 test errors.
  Resovles: rhbz#1799986

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 28 2019 Pavel Valena <pvalena@redhat.com> - 1:5.2.3-1
- Update to Active Record 5.2.3.

* Thu Mar 14 2019 Pavel Valena <pvalena@redhat.com> - 1:5.2.2.1-1
- Update to Active Record 5.2.2.1.

* Thu Feb 07 2019 Vít Ondruch <vondruch@redhat.com> - 1:5.2.2-4
- Drop unnecessary erubis dependency.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jan 11 2019 Pavel Valena <pvalena@redhat.com> - 1:5.2.2-2
- Fix Ruby 2.6 compatibility

* Wed Dec 05 2018 Pavel Valena <pvalena@redhat.com> - 1:5.2.2-1
- Update to Active Record 5.2.2.

* Wed Aug 08 2018 Pavel Valena <pvalena@redhat.com> - 1:5.2.1-1
- Update to Active Record 5.2.1.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 23 2018 Pavel Valena <pvalena@redhat.com> - 1:5.2.0-1
- Update to Active Record 5.2.0.

* Fri Feb 16 2018 Pavel Valena <pvalena@redhat.com> - 1:5.1.5-1
- Update to Active Record 5.1.5.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Pavel Valena <pvalena@redhat.com> - 1:5.1.4-1
- Update to Active Record 5.1.4.

* Tue Aug 08 2017 Pavel Valena <pvalena@redhat.com> - 1:5.1.3-1
- Update to Active Record 5.1.3.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 27 2017 Pavel Valena <pvalena@redhat.com> - 1:5.1.2-1
- Update to Active Record 5.1.2.

* Mon May 22 2017 Pavel Valena <pvalena@redhat.com> - 1:5.1.1-1
- Update to Active Record 5.1.1.

* Thu Mar 02 2017 Pavel Valena <pvalena@redhat.com> - 1:5.0.2-1
- Update to Active Record 5.0.2.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:5.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Vít Ondruch <vondruch@redhat.com> - 1:5.0.1-2
- Fix unstable ReflectionTest#test_read_attribute_names test.

* Mon Jan 02 2017 Pavel Valena <pvalena@redhat.com> - 1:5.0.1-1
- Update to Active Record 5.0.1.
- Fix warnings: Fixnum and Bignum are deprecated in Ruby trunk

* Mon Aug 15 2016 Pavel Valena <pvalena@redhat.com> - 1:5.0.0.1-1
- Update to Activerecord 5.0.0.1

* Thu Jul 07 2016 Vít Ondruch <vondruch@redhat.com> - 1:5.0.0-1
- Update to ActiveRecord 5.0.0.

* Tue Mar 08 2016 Pavel Valena <pvalena@redhat.com> - 1:4.2.6-1
- Update to activerecord 4.2.6

* Wed Mar 02 2016 Pavel Valena <pvalena@redhat.com> - 1:4.2.5.2-1
- Update to activerecord 4.2.5.2
- Add sqlite3 executable to BR

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:4.2.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Pavel Valena <pvalena@redhat.com> - 1:4.2.5.1-1
- Update to activerecord 4.2.5.1

* Wed Nov 18 2015 Pavel Valena <pvalena@redhat.com> - 1:4.2.5-1
- Update to activerecord 4.2.5

* Wed Aug 26 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.4-1
- Update to activerecord 4.2.4

* Tue Jun 30 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.3-1
- Update to activerecord 4.2.3

* Mon Jun 22 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.2-1
- Update to activerecord 4.2.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar 20 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.1-1
- Update to activerecord 4.2.1

* Mon Feb 09 2015 Josef Stribny <jstribny@redhat.com> - 1:4.2.0-1
- Update to activerecord 4.2.0

* Mon Aug 25 2014 Josef Stribny <jstribny@redhat.com> - 4.1.5-1
- Update to activerecord 4.1.5

* Fri Jul 04 2014 Josef Stribny <jstribny@redhat.com> - 4.1.4-1
- Update to activerecord 4.1.4

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:4.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Josef Stribny <jstribny@redhat.com> - 1:4.1.1-1
- Update to ActiveRecord 4.1.1

* Thu Apr 17 2014 Josef Stribny <jstribny@redhat.com> - 1:4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Fri Apr 11 2014 Josef Stribny <jstribny@redhat.com> - 1:4.1.0-1
- Update to ActiveRecord 4.1.0

* Wed Feb 26 2014 Josef Stribny <jstribny@redhat.com> - 1:4.0.3-1
- Update to ActiveRecord 4.0.3

* Wed Dec 11 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.2-2
- Enable tests
- Patch for new sqlite

* Thu Dec 05 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.2-1
- Update to ActiveRecord 4.0.2
- Disable tests

* Thu Nov 21 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.1-2
- Fix: this shouldn't be scl spec

* Mon Nov 11 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.1-1
- Update to ActiveRecord 4.0.1

* Fri Oct 04 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.0-2
- Convert to scl

* Thu Aug 01 2013 Josef Stribny <jstribny@redhat.com> - 1:4.0.0-1
- Update to ActiveRecord 4.0.0.

* Tue Mar 19 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.13-1
- Update to ActiveRecord 3.2.13.

* Mon Mar 04 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.12-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Tue Feb 12 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.12-1
- Update to ActiveRecord 3.2.12.

* Wed Jan 09 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.11-1
- Update to ActiveRecord 3.2.11.

* Thu Jan 03 2013 Vít Ondruch <vondruch@redhat.com> - 1:3.2.10-1
- Update to ActiveRecord 3.2.10.

* Mon Aug 13 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.2.8-1
- Update to ActiveRecord 3.2.8.

* Mon Jul 30 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.2.7-1
- Update to ActiveRecord 3.2.7.

* Tue Jul 24 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.2.6-2
- Fixed missing epoch in -doc subpackage.

* Thu Jul 19 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.2.6-1
- Update to ActiveRecord 3.2.6.

* Fri Jun 15 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.0.15-1
- Update to ActiveRecord 3.0.15.

* Fri Jun 01 2012 Vít Ondruch <vondruch@redhat.com> - 1:3.0.13-1
- Update to ActiveRecord 3.0.13.

* Tue Jan 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 1:3.0.11-1
- Rebuilt for Ruby 1.9.3.
- Update to ActionRecord 3.0.11

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Aug 22 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.10-1
- Update to ActiveRecord 3.0.10

* Mon Jul 04 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.9-1
- Update to ActiveRecord 3.0.9

* Fri Mar 25 2011 Vít Ondruch <vondruch@redhat.com> - 1:3.0.5-1
- Updated to ActiveRecord 3.0.5

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 10 2011 Mohammed Morsi <mmorsi@redhat.com> - 1:3.0.3-1
- Update to rails 3

* Wed Sep 08 2010 Mohammed Morsi <mmorsi@redhat.com> - 1:2.3.8-4
- Updated postgres fix to resolve security issue

* Mon Aug 16 2010 Mohammed Morsi <mmorsi@redhat.com> - 1:2.3.8-3
- Included postgres fix (patch also pushed upstream, see rails issue tracker)

* Thu Aug 12 2010 Mohammed Morsi <mmorsi@redhat.com> - 1:2.3.8-2
- Updated patch0 to correctly parse sqlite3 version

* Wed Aug 04 2010 Mohammed Morsi <mmorsi@redhat.com> - 1:2.3.8-1
- Update to 2.3.8

* Thu Jan 28 2010 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1:2.3.5-1
- Update to 2.3.5

* Wed Oct  7 2009 David Lutterkort <lutter@redhat.com> - 1:2.3.4-2
- Bump Epoch to ensure upgrade path from F-11

* Fri Sep 18 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 2.3.4-1
- Update to 2.3.4
- Enable check

* Sun Jul 26 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 2.3.3-1
- New upstream version

* Mon Mar 16 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 2.3.2-1
- New upstream version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Nov 24 2008 Jeroen van Meeuwen <kanarip@fedoraproject.org> - 2.2.2-1
- New upstream version
- Fixed rpmlint errors zero-length files and script-without-shebang

* Thu Nov 20 2008 David Lutterkort <lutter@redhat.com> - 2.1.1-2
- Do not mark lib/ as doc

* Tue Sep 16 2008 David Lutterkort <dlutter@redhat.com> - 2.1.1-1
- New version (fixes CVE-2008-4094)

* Thu Jul 31 2008 Michael Stahnke <stahnma@fedoraproject.org> - 2.1.0-1
- New Upstream

* Tue Apr  8 2008 David Lutterkort <dlutter@redhat.com> - 2.0.2-2
- Fix dependency

* Mon Apr 07 2008 David Lutterkort <dlutter@redhat.com> - 2.0.2-1
- New version

* Mon Dec 10 2007 David Lutterkort <dlutter@redhat.com> - 2.0.1-1
- New version

* Thu Nov 29 2007 David Lutterkort <dlutter@redhat.com> - 1.15.6-1
- New version

* Wed Nov 14 2007 David Lutterkort <dlutter@redhat.com> - 1.15.5-2
- Fix buildroot
- Properly mark docs in geminstdir

* Tue Oct 30 2007 David Lutterkort <dlutter@redhat.com> - 1.15.5-1
- Initial package
