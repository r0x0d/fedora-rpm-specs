# Running the tests requires ipython which requires python-stack-data which
# introduces a circular dependency back on python-executing
%bcond tests 1
# When tests are enabled, should we also run “very slow” tests?
%bcond slow_tests 1

Name:           python-executing
Version:        2.2.0
Release:        1%{?dist}
Summary:        Python library for inspecting the current frame run footprint

License:        MIT
URL:            https://github.com/alexmojaki/executing
%dnl Source:         %{pypi_source executing}
Source:         %{pypi_source executing}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Get information about what a Python frame is currently doing, particularly the
AST node being executed}

%description %_description

%package -n python3-executing
Summary:        %{summary}

%description -n python3-executing %_description


%prep
%autosetup -p1 -n executing-%{version}
# Remove coverage and coverage-enable-subprocess
# from testing deps.
sed -Ei "/coverage-?/d" setup.cfg


%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION="%(echo '%{version}' | cut -d '^' -f 1)"
%pyproject_buildrequires %{?with_tests:-t}


%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%(echo '%{version}' | cut -d '^' -f 1)"
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files executing


%check
%pyproject_check_import
%if %{with tests}
%if %{with slow_tests}
export EXECUTING_SLOW_TESTS=1
%endif
%tox -- -- -rs
%endif


%files -n python3-executing -f %{pyproject_files}
%doc README.md
%license LICENSE.txt


%changelog
* Wed Jan 22 2025 Lumír Balhar <lbalhar@redhat.com>
- Update to 2.2.0 (rhbz#2339704)

* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0^20240916git3f11fdc-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Sep 21 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 2.1.0^20240916git3f11fdc-1
- Package a post-release snapshot to fix regressions
- Add a build conditional to optionally enable very slow tests; enable them

* Mon Sep 02 2024 Lumír Balhar <lbalhar@redhat.com> - 2.1.0-1
- Update to 2.1.0 (rhbz#2309044)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 2.0.1-6
- Rebuilt for Python 3.13

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 2.0.1-5
- Bootstrap for Python 3.13

* Wed Jun 05 2024 Lumír Balhar <lbalhar@redhat.com> - 2.0.1-4
- Fix compatibility with Python 3.13 (rhbz#2283503)

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 30 2023 Lumír Balhar <lbalhar@redhat.com> - 2.0.1-1
- Update to 2.0.1 (rhbz#2246826)

* Fri Oct 20 2023 Karolina Surma <ksurma@redhat.com> - 2.0.0-2
- Conditionalize tests to prevent circular dependency when bootstrapping new Python

* Mon Oct 02 2023 Lumír Balhar <lbalhar@redhat.com> - 2.0.0-1
- Update to 2.0.0 (rhbz#2241493)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 02 2023 Python Maint <python-maint@redhat.com> - 1.2.0-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Nov 01 2022 Lumír Balhar <lbalhar@redhat.com> - 1.2.0-1
- Update to 1.2.0
Resolves: rhbz#2138547

* Sun Oct 09 2022 Lumír Balhar <lbalhar@redhat.com> - 1.1.1-1
- Update to 1.1.1
Resolves: rhbz#2133192

* Mon Sep 26 2022 Lumír Balhar <lbalhar@redhat.com> - 1.1.0-1
- Update to 1.1.0
Resolves: rhbz#2110285

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.2-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Roman Inflianskas <rominf@aiven.io> - 0.8.2-1
- Initial package
