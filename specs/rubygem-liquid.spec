%global gem_name liquid

Name:           rubygem-%{gem_name}
Summary:        Secure, non-evaling end user template engine
Version:        4.0.3
Release:        %autorelease
License:        MIT

URL:            http://www.liquidmarkup.org
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem

# Disable running stack profiler in the test suite
Patch0:         00-test-unit-context-disable-stack-profiler.patch

# Remove shebang and executable bit from the test_helper.rb
Patch1:         01-test-helper-remove-shebang-and-executable-bit.patch

# Disable two tests that are broken with ruby 2.7
Patch2:         02-tests-integration-drop_test-disable-tests-broken-wit.patch

# Fix parse_tree_visitor_test.rb for Ruby 3. Upstream has this for liquid 5.0.0,
# patch can be removed when updated to 5.0.0 in Fedora.
# https://github.com/Shopify/liquid/commit/81149344a5ba53b30e8ab7d77d605dc484a0a3ff
Patch3:         03-fix-parse-tree-visitor-test-for-ruby-3.patch
# Patch for supporting ruby 3.2, ruby3.2 removes "tainted"ness completely
# Partially backported from https://github.com/Shopify/liquid/commit/065ccbc4aa5b4955dae9743509907bd9ad0db0b9
Patch4:         04-ruby32-remove-tainted.patch
# 2 patches related to glibc 2.38.9000-20 qsort behavior change
# Extracted from https://github.com/Shopify/liquid/pull/1476 :
# applying only the part needed for the above glibc qsort change
Patch5:         05-pr1476-nil_safe_compare-comparison-func.patch
# https://github.com/Shopify/liquid/pull/1760
Patch6:         06-pr1760-change-make-nil_safe_casecmp-judge-compatible-for-ni.patch

BuildArch:      noarch

BuildRequires:  ruby(release)
BuildRequires:  ruby >= 2.1.0
BuildRequires:  rubygems-devel >= 1.3.7

BuildRequires:  rubygem(bigdecimal)
BuildRequires:  rubygem(minitest)

Requires:       rubygem(bigdecimal)

%description
Liquid is a template engine which was written with very specific requirements:
* It has to have beautiful and simple markup. Template engines which don't
  produce good looking markup are no fun to use.
* It needs to be non evaling and secure. Liquid templates are made so that
  users can edit them. You don't want to run code on your server which your
  users wrote.
* It has to be stateless. Compile and render steps have to be separate so that
  the expensive parsing and compiling can be done once and later on you can
  just render it passing in a hash with local variables and objects.


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
Documentation for %{name}.


%prep
%autosetup -p1 -n %{gem_name}-%{version}


%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install


%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/


%check
pushd .%{gem_instdir}
ruby -I"lib:test" -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd


%files
%license %{gem_instdir}/LICENSE

%dir %{gem_instdir}
%{gem_libdir}
%{gem_spec}

%exclude %{gem_cache}


%files doc
%doc %{gem_instdir}/History.md
%doc %{gem_instdir}/README.md

%doc %{gem_docdir}

%{gem_instdir}/test


%changelog
%autochangelog