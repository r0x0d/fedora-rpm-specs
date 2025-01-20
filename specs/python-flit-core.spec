# When bootstrapping new Python we need to build flit in bootstrap mode.
# The Python RPM dependency generators and pip are not yet available.
%bcond bootstrap 0

# Tests are enabled by default, unless we bootstrap.
# Disable them to avoid a circular build dependency on testpath.
%bcond tests %{without bootstrap}

Name:           python-flit-core
Version:        3.10.1
Release:        2%{?dist}
Summary:        PEP 517 build backend for packages using Flit

# flit-core is BSD-3-Clause
# flit_core/versionno.py contains a regex that is from packaging, BSD-2-Clause
License:        BSD-3-Clause AND BSD-2-Clause

URL:            https://flit.pypa.io/
Source:         %{pypi_source flit_core}

BuildArch:      noarch
BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3-pytest
# Test deps that require flit-core to build:
BuildRequires:  python3-testpath
%endif

%global _description %{expand:
This provides a PEP 517 build backend for packages using Flit.
The only public interface is the API specified by PEP 517,
at flit_core.buildapi.}

%description %_description


%package -n python3-flit-core
Summary:        %{summary}
Conflicts:      python3-flit < 2.1.0-2

# RPM generators are not yet available when we bootstrap
%if %{with bootstrap}
Provides:       python%{python3_pkgversion}dist(flit-core) = %{version}
Provides:       python%{python3_version}dist(flit-core) = %{version}
Requires:       python(abi) = %{python3_version}
%endif

%description -n python3-flit-core %_description


%prep
%autosetup -p1 -n flit_core-%{version}

# Remove vendored tomli that flit_core includes to solve the circular dependency on older Pythons
# (flit_core requires tomli, but flit_core is needed to build tomli).
# We don't use this, as tomllib is a part of standard library since Python 3.11.
rm -rf flit_core/vendor


%if %{without bootstrap}
%generate_buildrequires
%pyproject_buildrequires
%endif


%build
%if %{with bootstrap}
%{python3} -m flit_core.wheel
%else
%pyproject_wheel
%endif

%install
%if %{with bootstrap}
%{python3} bootstrap_install.py --install-root %{buildroot} dist/flit_core-%{version}-py3-none-any.whl
# for consistency with %%pyproject_install:
rm %{buildroot}%{python3_sitelib}/flit_core-*.dist-info/RECORD
%else
%pyproject_install
%endif

%check
%py3_check_import flit_core flit_core.buildapi
%if %{with tests}
%pytest
%endif


%files -n python3-flit-core
%license LICENSE
%doc README.rst
%{python3_sitelib}/flit_core-*.dist-info/
%{python3_sitelib}/flit_core/


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Nov 22 2024 Michel Lind <salimma@fedoraproject.org> - 3.10.1-1
- Update to 3.10.1
- Resolves: rhbz#2322947

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 3.9.0-8
- Rebuilt for Python 3.13

* Thu Jun 06 2024 Python Maint <python-maint@redhat.com> - 3.9.0-7
- Bootstrap for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.9.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 3.9.0-3
- Rebuilt for Python 3.12

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.9.0-2
- Bootstrap for Python 3.12

* Fri May 26 2023 Miro Hrončok <mhroncok@redhat.com> - 3.9.0-1
- Update to 3.9.0

* Fri May 19 2023 Miro Hrončok <mhroncok@redhat.com> - 3.8.0-3
- Fork python-flit-core from the python-flit package
- Adjust the License tag to include flit_core/versionno.py's regex (BSD-2-Clause)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Nov 10 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 3.8.0-1
- Update to 3.8.0
- Fixes: rhbz#2140390

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sun Jun 26 2022 Maxwell G <gotmax@e.email> - 3.7.1-4
- Removed unnecessarily vendored tomli.

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.7.1-3
- Rebuilt for Python 3.11

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.7.1-2
- Bootstrap for Python 3.11

* Wed Mar 16 2022 Charalampos Stratakis <cstratak@redhat.com> - 3.7.1-1
- Update to 3.7.1
- Fixes: rhbz#2057214

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Nov 29 2021 Tomáš Hrnčiar <thrnciar@redhat.com> - 3.5.1-1
- Update to 3.5.1

* Tue Oct 26 2021 Tomáš Hrnčiar <thrnciar@redhat.com> - 3.4.0-1
- Update to 3.4.0

* Wed Aug 04 2021 Tomas Hrnciar <thrnciar@redhat.com> - 3.3.0-1
- Update to 3.3.0
- Fixes: rhbz#1988744

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.2.0-4
- Rebuilt for Python 3.10

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.2.0-3
- Bootstrap for Python 3.10

* Sat May 29 2021 Miro Hrončok <mhroncok@redhat.com> - 3.2.0-2
- Adapt to pyproject-rpm-macros 0-40+

* Tue Mar 30 2021 Karolina Surma <ksurma@redhat.com> - 3.2.0-1
- Update to 3.2.0
Resolves: rhbz#1940399
- Remove tests from the flip_core package

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 19 2020 Miro Hrončok <mhroncok@redhat.com> - 3.0.0-2
- Replace deprecated pytoml with toml

* Mon Sep 21 2020 Tomas Hrnciar <thrnciar@redhat.com> - 3.0.0-1
- Update to 3.0.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-3
- Rebuilt for Python 3.9

* Sun May 24 2020 Miro Hrončok <mhroncok@redhat.com> - 2.3.0-2
- Bootstrap for Python 3.9

* Mon May 11 2020 Tomas Hrnciar <thrnciar@redhat.com> - 2.3.0-1
- Update to 2.3.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 20 2020 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.2.0-1
- Update to 2.2.0

* Sat Dec 14 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1.0-2
- Properly package flit-core and restore /usr/bin/flit (#1783610)

* Tue Dec 03 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 10 2019 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.3-1
- Update to 1.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Sep 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1-1
- Update to 1.1

* Sat Aug 18 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0-4
- Drop pypandoc as requires

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0-2
- Rebuilt for Python 3.7

* Sun Apr 08 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0-1
- Update to 1.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 09 2018 Miro Hrončok <mhroncok@redhat.com> - 0.13-2
- Recommend Pygments

* Sat Dec 23 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> -  0.13-1
- Update to 0.13

* Thu Nov 16 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12.2-1
- Update to 0.12.2

* Wed Nov 08 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12.1-1
- Update to 0.12.1

* Mon Nov 06 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12-2
- Add pytoml as dependency

* Sun Nov 05 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.12-1
- Update to 0.12
- Add pytoml as buildrequires

* Mon Aug 14 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.11.4-1
- Update to 0.11.4
- Drop file-encoding patch (fixed upstream)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 13 2017 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.11.1-1
- Update to 0.11.1

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Michal Cyprian <mcyprian@redhat.com> - 0.9-5
- Use python install wheel macro

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9-4
- Rebuild for Python 3.6

* Thu Sep 29 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 0.9-3
- Updated spec file with license comments and provides

* Sat Sep 24 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 0.9-2
- spec file cleanup

* Sat Jul 2 2016 Elliott Sales de Andrade <quantum.analyst@gmail.com> 0.9-1
- Initial RPM release
