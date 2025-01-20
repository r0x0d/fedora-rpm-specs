# Generated from rake-0.7.3.gem by gem2rpm -*- rpm-spec -*-
%global	majorver	13.2.1
#%%global	preminorver	.beta.5
%global	rpmminorver	.%(echo %preminorver | sed -e 's|^\\.\\.*||')
%global	fullver	%{majorver}%{?preminorver}

%global	gem_name	rake

%global	baserelease	202

Summary:	Rake is a Make-like program implemented in Ruby
Name:		rubygem-%{gem_name}

Version:	%{majorver}
Release:	%{?preminorver:0.}%{baserelease}%{?preminorver:%{rpmminorver}}%{?dist}
# SPDX confirmed
License:	MIT
URL:		https://github.com/ruby/rake
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem

# git clone --no-checkout https://github.com/ruby/rake
# cd rake && git archive -v -o rake-13.1.0-tests.txz v13.1.0 Rakefile test
Source1: %{gem_name}-%{version}-tests.txz

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	ruby
# %%check
BuildRequires:	rubygem(minitest) >= 5
BuildRequires:	rubygem(test-unit)
BuildArch:	noarch

%description
Rake is a Make-like program implemented in Ruby. Tasks and dependencies are
specified in standard Ruby syntax.

%package	doc
Summary:	Documentation for %{name}
# Directory ownership issue
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description    doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -a 1
mv ../%{gem_name}-%{version}.gemspec .

%build
gem build ./%{gem_name}-%{version}.gemspec
%gem_install

pushd ./%{gem_instdir}
rm -fr \
	Rakefile \
	test/ \
	%{nil}
popd
cp -a \
	Rakefile \
	test/ \
	./%{gem_instdir}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/exe -type f | xargs chmod a+x

# cleanup
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.gitignore .rubocop.yml .travis.yml \
	.github \
	appveyor.yml \
	Gemfile \
	Rakefile \
	rake.gemspec \
	test \
	bin
	%{nil}
popd

# Install man pages into appropriate place.
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{gem_instdir}/doc/rake.1 %{buildroot}%{_mandir}/man1

%check
pushd .%{gem_instdir}

# Get rid of Bundler.
sed -i '/bundler/ s/^/#/' Rakefile

export TESTOPTS=--verbose
export VERBOSE=y
export RUBYLIB=$(pwd)/lib
ruby ./exe/rake test
popd

%files
%dir %{gem_instdir}
%{_bindir}/rake
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/exe
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{_mandir}/man1/*

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/doc
%doc %{gem_instdir}/*.rdoc

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 13.2.1-202
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 13.2.1-201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat May 04 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 13.2.1-200
- 13.2.1

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 13.1.0-201
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Oct 28 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 13.1.0-200
- 13.1.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.6-202
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 23 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 13.0.6-201
- Clean up release number

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.6-200.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.6-200.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.6-200.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 29 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 13.0.6-200
- 13.0.6

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.3-200.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.3-200.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 24 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 13.0.3-200
- 13.0.3
- Skip TestRakeFunctional#test_signal_propagation_in_tests for now

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.1-203.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 18 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 13.0.1-203
- Again use rake for test, as this is rake package
- Remove files again instead of using %%exclude

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 13.0.1-202
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 22 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 13.0.1-200
- 13.0.1

* Tue Aug 06 2019 Pavel Valena <pvalena@redhat.com> - 12.3.3-202
- Update to Rake 12.3.3.

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 12.3.2-201.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 05 2019 Vít Ondruch <vondruch@redhat.com> - 12.3.2-201
- Coveralls is not needed.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 12.3.2-200.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 26 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 12.3.2-200
- 12.3.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 12.3.1-200.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Apr  6 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 12.3.1-200
- 12.3.1
- Bump release number

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 12.3.0-100.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan  1 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 12.3.0-100
- A Happy New Year and 12.3.0

* Fri Nov 10 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 12.2.1-100
- 12.2.1

* Wed Sep 13 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 12.1.0-100
- 12.1.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 12.0.0-100.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 17 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 12.0.0-100
- 12.0.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 11.3.0-100.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 15 2016 Vít Ondruch <vondruch@redhat.com> - 11.3.0-100
- Update to Rake 11.3.0.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 10.4.2-100.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Sep 24 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 10.4.2-100
- 10.4.2

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.0.4-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.0.4-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.0.4-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 28 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 10.0.4-1
- 10.0.4

* Fri Feb 22 2013 Vít Ondruch <vondruch@redhat.com> - 10.0.3-3
- Rebuid due to error in RubyGems stub shebang.

* Tue Feb 19 2013 Vít Ondruch <vondruch@redhat.com> - 10.0.3-2
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10.0.3-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan  2 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 10.0.3-1
- 10.0.3

* Tue Jan  1 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 10.0.2-1
- Update to 10.0.2

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2.2-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 09 2012 Vít Ondruch <vondruch@redhat.com> - 0.9.2.2-2
- Rebuilt for Ruby 1.9.3.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2.2-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.9.2.2-1
- 0.9.2.2

* Sat Jun 11 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.9.2-1
- 0.9.2

* Sun Jun  5 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.9.1-2
- Add BR: rubygem(minitest) for %%check

* Sat Jun  4 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.9.1-1
- 0.9.1

* Fri Mar 18 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.9.0-0.4.beta.5
- 0.9.0 beta.5

* Mon Mar  7 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.9.0-0.3.beta.4
- 0.9.0 beta.4

* Fri Mar  4 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.9.0-0.2.beta.1
- 0.9.0 beta.1

* Thu Feb 24 2011 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.9.0-0.1.beta.0
- 0.9.0 beta.0
- Split out document files

* Thu Feb 10 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.7-4
- Use BuildRequires, not BuildRequires(check)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jun 18 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.8.7-1
- 0.8.7
- Enable %%check

* Tue Mar 17 2009 Jeroen van Meeuwen <j.van.meeuwen@ogd.nl> - 0.8.4-1
- New upstream version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 27 2008 David Lutterkort <lutter@redhat.com> - 0.8.3-1
- Cleanup multiply listed files
- Set permissions in doc/, lib/ and test/ to 644

* Thu May 15 2008 Alan Pevec <apevec@redhat.com> 0.8.1-2
- fix shebang in scripts

* Thu May 15 2008 Alan Pevec <apevec@redhat.com> 0.8.1-1
- new upstream version

* Thu Aug 23 2007 David Lutterkort <dlutter@redhat.com> - 0.7.3-2
- Fix license tag
- Remove bogus shebangs in lib/ and test/

* Mon Jun 18 2007 David Lutterkort <dlutter@redhat.com> - 0.7.3-1
- Initial package
