%bcond_without check

Name: python-dill
Version: 0.3.9
Release: 3%{?dist}
Summary: Serialize all of Python

License: BSD-3-Clause

URL: https://github.com/uqfoundation/dill
Source: %{pypi_source dill}

BuildArch: noarch

BuildRequires: python3-devel
# the test script calls 'python', this is easier than patching it
BuildRequires: python-unversioned-command

%global _description %{expand:
Dill extends Python's pickle module for serializing and de-serializing Python
objects to the majority of the built-in Python types. Serialization is the
process of converting an object to a byte stream, and the inverse of which is
converting a byte stream back to a Python object hierarchy.

Dill provides the user the same interface as the pickle module, and also
includes some additional features. In addition to pickling Python objects, dill
provides the ability to save the state of an interpreter session in a single
command. Hence, it would be feasible to save an interpreter session, close the
interpreter, ship the pickled file to another computer, open a new interpreter,
unpickle the session and thus continue from the 'saved' state of the original
interpreter session.

Dill can be used to store Python objects to a file, but the primary usage is to
send Python objects across the network as a byte stream. dill is quite
flexible, and allows arbitrary user defined classes and functions to be
serialized. Thus dill is not intended to be secure against erroneously or
maliciously constructed data. It is left to the user to decide whether the data
they unpickle is from a trustworthy source.

dill is part of pathos, a Python framework for heterogeneous computing.}

%description %{_description}


%package -n python3-dill
Summary:  %{summary}

%description -n python3-dill %{_description}


# The graph extra needs objgraph>=1.7.2; python-objgraph is not packaged
# The profile extra needs gprof2dot>=2022.7.29; python-gprof2dot is not packaged
%pyproject_extras_subpkg -n python3-dill readline


%prep
%autosetup -n dill-%{version}


%generate_buildrequires
%pyproject_buildrequires -x readline


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l dill

# We do not want to package these command-line tools, and we lack the necessary
# dependencies for the corresponding extras anyway.
rm %{buildroot}%{_bindir}/get_objgraph %{buildroot}%{_bindir}/get_gprof

# Remove shebangs from (installed) non-script sources. The find-then-modify
# pattern preserves mtimes on sources that did not need to be modified.
find '%{buildroot}%{python3_sitelib}/dill' -type f -name '*.py' ! -perm /0111 \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r sed -r -i '1{/^#!/d}'


# Skip offending tests to allow other packages to rebuiltd with py313
# https://bugzilla.redhat.com/show_bug.cgi?id=2264225
%check
%if %{with check}
%{py3_test_envvars} %{python3} dill/tests/__main__.py
%endif
%pyproject_check_import -t



%files -n python3-dill -f %{pyproject_files}
%doc README.md
%{_bindir}/undill


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Oct 10 2024 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.9-2
- Update to 0.3.9

* Tue Sep 17 2024 Miro Hrončok <mhroncok@redhat.com> - 0.3.9~~20240914.8b86f509-1
- Update to a git snapshot for Python 3.13 compatibility
- Fixes: rhbz#2264225

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 16 2024 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.8-3
- Skip offending test to allow other packages to rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.3.8-2
- Rebuilt for Python 3.13

* Mon Jan 29 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 0.3.8-1
- Update to 0.3.8 (close RHBZ#2260677)
- Update License to SPDX
- Update description from upstream
- Port to pyproject-rpm-macros
- Add a metapackage for the readline extra
- Run the tests
- Do package the undill command-line tool

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jul 23 2023 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.7-1
- New upstream source (0.3.7)

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.3.6-3
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jan 13 2023 Gwyn Ciesla <gwync@protonmail.com> - 0.3.6-1
- 0.3.6

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 08 2022 Adam Williamson <awilliam@redhat.com> - 0.3.5.1-3
- Backport several patches to fix Python 3.11 issues
- Backport PR #524 to fix test suite invocation
- Re-enable test suite, the way upstream runs it in tox

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.3.5.1-2
- Rebuilt for Python 3.11

* Wed Jun 01 2022 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.5.1-1
- New upstream source (0.3.5.1)

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.4-2
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.4-1
- New upstream source (0.3.4)

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 0.3.3-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Nov 25 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.3-1
- New upstream source (0.3.3)
- Upstream compressed with zip

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 30 2020 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.2-1
- New upstream source (0.3.2)

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.3.1.1-4
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.1.1-2
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Oct 02 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.1.1-1
- New upstream source (0.3.1.1)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.3.0-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 11 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 0.3.0-1
- New upstream source (0.3.0)

* Wed Feb 13 2019 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.9-1
- New upstream source (0.2.9)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug 21 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.8.2-2
- Drop python2 subpackage

* Tue Aug 21 2018 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.8.2-1
- New upstream source (0.2.8.2)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.2.7.1-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.7.1-2
- New upstream source (0.2.7.1)
- And the sources

* Tue Aug 08 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.2.6-3
- Fix %%python_provide invocation

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 16 2017 Sergio Pascual <sergiopr@fedoraproject.org> - 0.2.6-1
- New upstream source (0.2.6)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.2.5-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.5-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 13 2016 Sergio Pascual <sergio.pasra@gmail.com> - 0.2.5-1
- New upstream source (0.2.5)
- Updated upstream url
- Pypi url updated

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Nov 20 2015 Sergio Pascual <sergio.pasra@gmail.com> - 0.2.4-1
- New upstream source (0.2.4)

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Sep 12 2014 Sergio Pascual <sergio.pasra@gmail.com> - 0.2.1-2
- Add license macro
- Run tests
- Add numpy build req for tests

* Thu Sep 11 2014 Sergio Pascual <sergio.pasra@gmail.com> - 0.2.1-1
- New upstream (0.2.1)

* Fri Dec 13 2013 Sergio Pascual <sergio.pasra@gmail.com> - 0.2-0.1b1
- Initial specfile

