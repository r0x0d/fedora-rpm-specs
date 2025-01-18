Name:           bodhi-client
Version:        8.3.0
Release:        2%{?dist}
Summary:        Bodhi client

License:        GPL-2.0-or-later
URL:            https://github.com/fedora-infra/bodhi
Source0:        %{pypi_source bodhi_client}
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-sphinx

Requires: koji

Obsoletes: python3-bodhi-client <= 5.7.5
# Replace the bodhi metapackage
Obsoletes: bodhi <= 5.7.5

%py_provides python3-bodhi-client

%description
Command-line client for Bodhi, Fedora's update gating system.

%prep
%autosetup -n bodhi_client-%{version}

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
%make_build -C docs man

%install
%pyproject_install
# Poetry doesn't support PEP 639 yet, so we still need to manually mark the
# license file.
# https://github.com/python-poetry/poetry/issues/9670
%pyproject_save_files -L bodhi

install -d %{buildroot}%{_mandir}/man1
install -pm0644 docs/_build/bodhi.1 %{buildroot}%{_mandir}/man1/
install -d %{buildroot}%{_sysconfdir}/bash_completion.d
install -pm0644 bodhi-client.bash %{buildroot}%{_sysconfdir}/bash_completion.d/bodhi-client.bash

%check
%pyproject_check_import
%{pytest} -v

%files -f %{pyproject_files}
%license %{python3_sitelib}/bodhi_client-%{version}.dist-info/COPYING
%{_bindir}/bodhi
%{_mandir}/man1/bodhi.1*
%config(noreplace) %{_sysconfdir}/bash_completion.d/bodhi-client.bash

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 8.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Nov 25 2024 Mattia Verga <mattia.verga@proton.me> - 8.3.0-1
- Update to 8.3.0

* Mon Nov 11 2024 Carl George <carlwgeorge@fedoraproject.org> - 8.2.0-2
- Correctly mark COPYING file as a license
- Remove unnecessary pytest-cov build requirement

* Mon Oct 28 2024 Mattia Verga <mattia.verga@proton.me> - 8.2.0-1
- Update to 8.2.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 8.1.0-2
- Rebuilt for Python 3.13

* Tue Apr 09 2024 Mattia Verga <mattia.verga@proton.me> - 8.1.0-1
- Update to 8.1.0

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 8.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Dec 09 2023 Mattia Verga <mattia.verga@proton.me> - 8.0.0-1
- Update to 8.0.0

* Tue Oct 03 2023 Mattia Verga <mattia.verga@proton.me> - 7.2.2-1
- Update to 7.2.2

* Sun Jul 30 2023 Mattia Verga <mattia.verga@proton.me> - 7.2.1-1
- Update to 7.2.1

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 03 2023 Python Maint <python-maint@redhat.com> - 7.2.0-2
- Rebuilt for Python 3.12

* Sun Apr 30 2023 Mattia Verga <mattia.verga@proton.me> - 7.2.0-1
- Update to 7.2.0

* Sat Mar 18 2023 Mattia Verga <mattia.verga@proton.me> - 7.1.1-1
- Update to 7.1.1

* Sat Mar 11 2023 Mattia Verga <mattia.verga@proton.me> - 7.1.0-1
- Update to 7.1.0

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 7.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jan 14 2023 Mattia Verga <mattia.verga@proton.me> - 7.0.1-1
- Update to 7.0.1
- Use SPDX identifier in license tag

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jul 15 2022 Aurelien Bompard <abompard@fedoraproject.org> - 6.0.1-3
- Require koji because we call its CLI (thanks adamw)

* Mon Jun 27 2022 Aurelien Bompard <abompard@fedoraproject.org> - 6.0.1-2
- Replace the bodhi metapackage

* Thu Jun 23 2022 Aurelien Bompard <abompard@fedoraproject.org> - 6.0.1-1
- Update to 6.0.1

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 6.0.0-3
- Rebuilt for Python 3.11

* Fri Jun 10 2022 Aurelien Bompard <abompard@fedoraproject.org> - 6.0.0-2
- rebuilt

* Fri Apr 08 2022 Aurelien Bompard <abompard@fedoraproject.org> - 6.0.0-1
- Update to 6.0.0.

* Wed Feb 23 2022 Ryan Lerch <rlerch@redhat.com> - 5.7.5-0
- Prepare the Bodhi client to be compatible with an OIDC-enabled server. PR#4391.

* Mon Jan 24 2022 Lenka Segura <lsegura@redhat.com> - 5.7.4-2
- rebuilt

* Sat Apr 24 2021 Kevin Fenzi <kevin@scrye.com> - 5.7.0-1
- Update to 5.7.0. Fixes rhbz#1949260

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 5.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Dec 29 2020 Mattia Verga <mattia.verga@protonmail.com> - 5.6.1-3
- Re-enable docs build
- Re-enable tests
- Increase required test coverage to 98.

* Mon Nov 30 2020 Clément Verna <cverna@fedoraproject.org> - 5.6.1-1
- Update to 5.6.1
  https://github.com/fedora-infra/bodhi/releases/tag/5.6.1
- Remove Graphql from the server.

* Sun Sep 27 2020 Kevin Fenzi <kevin@scrye.com> - 5.5.0-1
- Update to 5.5.0. Fixes bug #1815307

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 5.2.2-2
- Rebuilt for Python 3.9

* Wed Mar 25 2020 Clément Verna <cverna@fedoraproject.org> - 5.2.2-1
- Update to 5.2.2
  https://github.com/fedora-infra/bodhi/releases/tag/5.2.2

* Mon Mar 23 2020 Clément Verna <cverna@fedoraproject.org> - 5.2.1-1
- Update to 5.2.1
  https://github.com/fedora-infra/bodhi/releases/tag/5.2.1

* Thu Mar 19 2020 Clément Verna <cverna@fedoraproject.org> - 5.2.0-1
- Update to 5.2.0
  https://github.com/fedora-infra/bodhi/releases/tag/5.2.0

* Thu Jan 30 2020 Nils Philippsen <nils@redhat.com> - 5.1.1-1
- Update to 5.1.1.
  https://github.com/fedora-infra/bodhi/releases/tag/5.1.1

* Tue Jan 28 2020 Nils Philippsen <nils@redhat.com> - 5.1.0-3
- remove obsolete patch which caused the build to fail
- relax test coverage requirements

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild
