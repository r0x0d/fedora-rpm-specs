# Generated from mustermann-1.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name mustermann

# Circular dependency with rubygem-sinatra
%{?_with_bootstrap: %global bootstrap 1}

Name: rubygem-%{gem_name}
Version: 1.1.1
Release: 12%{?dist}
Summary: Your personal string matching expert
License: MIT
URL: https://github.com/sinatra/mustermann
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Support and mustermann-contrib routines required by test suite.
# git clone https://github.com/sinatra/mustermann.git && cd mustermann
# git checkout v1.1.1 && tar czvf mustermann-1.1.1-support.tgz support/
Source1: %{gem_name}-%{version}-support.tgz
# tar czvf mustermann-1.1.1-mustermann-contrib.tgz mustermann-contrib/
Source2: %{gem_name}-%{version}-mustermann-contrib.tgz
# https://github.com/sinatra/mustermann/commit/8be5bd4ac3642d9c9582d0a7258f3197fa54bb96
# Ruby3.2 removes Object#:~
Patch0:  %{gem_name}-2.0.2-ruby32-regex_match-for-object.patch
# Similarly, from https://github.com/sinatra/mustermann/pull/113
Patch1:  %{gem_name}-1.1.1-ruby32-regex_match-for-object-2.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.2.0
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(rspec-its)
%if ! 0%{?bootstrap}
BuildRequires: rubygem(sinatra)
%endif
BuildRequires: rubygem(rack-test)
BuildArch: noarch

%description
A library implementing patterns that behave like regular expressions.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1 -b 2
%patch -P0 -p2
%patch -P1 -p2
# Drop ruby2_keywords dependency that is required by Ruby < 2.7.
%gemspec_remove_dep -g ruby2_keywords

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

%if ! 0%{?bootstrap}
# Run the test suite
%check
# We don't ship tool.
sed -i "/^require 'tool\/warning_filter'/ s/^/#/" \
  %{_builddir}/support/lib/support/env.rb
# We don't test coverage.
sed -i "/^require 'support\/coverage'/ s/^/#/" \
  %{_builddir}/support/lib/support.rb

pushd .%{gem_instdir}
# Mustermann extension is only available on Sinatra 1.x.
mv spec/extension_spec.rb{,.disabled}
sed -i "/^require 'mustermann\/extension'/ s/^/#/" \
  spec/mustermann_spec.rb
sed -i '/^  describe :extend_object do$/,/^  end$/ s/^/#/' \
  spec/mustermann_spec.rb

rspec -I%{_builddir}/{support,mustermann-contrib}/lib spec
popd
%endif

%files
%dir %{gem_instdir}
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_instdir}/mustermann.gemspec
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.md
%{gem_instdir}/bench
%{gem_instdir}/spec

%changelog
* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 17 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.1-8
- Backport upstream fix for ruby32 Object#:~ removal

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Pavel Valena <pvalena@redhat.com> - 1.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_3.1

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 18 2020 Jun Aruga <jaruga@redhat.com> - 1.1.1-1
- Update to Mustermann 1.1.1.

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Jun Aruga <jaruga@redhat.com> - 1.0.2-4
- Skip test cases for Ruby 2.6 incompatibility.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 27 2018 Jun Aruga <jaruga@redhat.com> - 1.0.2-1
- Update to Mustermann 1.0.2.

* Thu Feb 15 2018 Jun Aruga <jaruga@redhat.com> - 1.0.1-1
- Update to Mustermann 1.0.1.

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 09 2017 Jun Aruga <jaruga@redhat.com> - 1.0.0-1
- Initial package