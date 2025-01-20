%global gem_name pry

%global slop_version 3.4.0

Name: rubygem-%{gem_name}
Version: 0.15.0
Release: 2%{?dist}
Summary: An IRB alternative and runtime developer console
License: MIT
URL: http://pry.github.io
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/pry/pry.git && cd pry
# git archive -v -o pry-0.15.0-spec.tar.gz v0.15.0 spec/
Source1: %{gem_name}-%{version}-spec.tar.gz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(coderay) => 1.1.0
BuildRequires: rubygem(method_source) => 0.8.1
BuildRequires: rubygem(rspec)
# editor specs fail if no editor is available (soft requirement)
BuildRequires: vi
BuildRequires: rubygem(irb)
# https://github.com/pry/pry/pull/1498
Provides: bundled(rubygem-slop) = %{slop_version}
BuildArch: noarch

%description
Pry is a runtime developer console and IRB alternative with powerful
introspection capabilities. Pry aims to be more than an IRB replacement. It is
an attempt to bring REPL driven programming to the Ruby language.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
[ `ruby -Ilib -rpry/slop -e "puts Pry::Slop::VERSION"` == '%{slop_version}' ]

ln -s %{_builddir}/spec spec

# Rakefile is used by editor test.
touch Rakefile

# Original test suite is run from non-versioned directory:
# https://github.com/pry/pry/blob/9d9ae4a0b0bd487bb41170c834b3fa417e161f23/spec/cli_spec.rb#L219
sed -i '/pry\/foo/ s/pry/pry-%{version}/' spec/cli_spec.rb

rspec -rspec_helper spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/pry
%license %{gem_instdir}/LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.15.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Nov 28 2024 Vít Ondruch <vondruch@redhat.com> - 0.15.0-1
- Update to Pry 0.15.0.
  Resolves: rhbz#2159362

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Oct 22 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.14.1-5
- Backport upstream fix to make testsuite work with ruby3.3 wrt
  ruby3.3 Reline implementation of readline

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.14.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Dec  7 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.14.1-2
- Explicitly add BR: rubygem(irb) for %%check

* Thu Oct 06 2022 Vít Ondruch <vondruch@redhat.com> - 0.14.1-1
- Update to Pry 0.14.1.
  Resolves: rhbz#1926203

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Apr 07 2021 Vít Ondruch <vondruch@redhat.com> - 0.13.1-5
- Add `BR: rubygem(irb)`, which was previosly pulled in indirectly.

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 11 2021 Vít Ondruch <vondruch@redhat.com> - 0.13.1-3
- Fix FTBFS due to Ruby 3.0 incompatibility.

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.13.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Apr 20 2020 Vít Ondruch <vondruch@redhat.com> - 0.13.1-1
- Update to Pry 0.13.1.
  Resolves: rhbz#1493806
  Resovles: rhbz#1800023

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 24 2017 Vít Ondruch <vondruch@redhat.com> - 0.10.4-2
- Fix Ruby 2.4 compatibility.

* Fri Oct 14 2016 Vít Ondruch <vondruch@redhat.com> - 0.10.4-1
- Update to Pry 0.10.4.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 09 2014 Ken Dreyer <ktdreyer@ktdreyer.com> - 0.10.1-1
- Update to latest upstream release (RHBZ #1108177)
- Remove gem2rpm auto-generated comment
- Update URL to latest upstream location
- Add generate-test-tarball.sh script since upstream no longer ships the tests
- Adjustments for https://fedoraproject.org/wiki/Changes/Ruby_2.1
- Use gem unpack / setup / build per Ruby packaging guidelines
- Use %%license tag

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Mar 03 2014 Vít Ondruch <vondruch@redhat.com> - 0.9.12.6-1
- Update to Pry 0.9.12.6.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.12-1
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0
- Updated to Pry 0.9.12.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Jul 31 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.9.10-1
- Initial package
