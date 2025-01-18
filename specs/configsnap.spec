Name:           configsnap
Version:        0.20.1
Release:        12%{?dist}
Summary:        Record and compare system state
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/rackerlabs/%{name}
Source0:        https://github.com/rackerlabs/%{name}/archive/%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  help2man
%if 0%{?rhel} >= 8 || 0%{?fedora}
BuildRequires:  python3-devel
%else
BuildRequires:  python2-devel
%endif

%description
configsnap records important system state information and can optionally compare
with a previous state and identify changes

%prep
%setup -q

%build
%if 0%{?rhel} >= 8 || 0%{?fedora}
sed -i 's#/bin/python$#/bin/python3#g' ./%{name}
%endif
help2man --include=%{name}.help2man --no-info ./%{name} -o %{name}.man


%install
mkdir -p %{buildroot}%{_sbindir} \
  %{buildroot}%{_mandir}/man1 \
  %{buildroot}%{_sysconfdir}/%{name}
install -p -m 0755 %{name} %{buildroot}%{_sbindir}
install -p -m 0644 %{name}.man %{buildroot}%{_mandir}/man1/%{name}.1
install -p -m 0600 additional.conf %{buildroot}%{_sysconfdir}/%{name}/additional.conf

%files
%{!?_licensedir:%global license %doc}
%license LICENSE
%doc README.md
%doc NEWS
%doc MAINTAINERS.md
%config(noreplace) %{_sysconfdir}/%{name}/additional.conf
%{_mandir}/man1/%{name}.1*
%{_sbindir}/%{name}
%dir %{_sysconfdir}/%{name}

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 0.20.1-11
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon May 17 2021 Christos Triantafyllidis <christos.triantafyllidis@rackspace.co.uk> - 0.20.1-2
- Fedora review recommendations

* Wed May 12 2021 Christos Triantafyllidis <christos.triantafyllidis@rackspace.co.uk> - 0.20.1-1
- Update python binary for python3 based distros

* Fri May 07 2021 Nick Rhodes <nrhodes91@gmail.com> - 0.20.0-3
- Fix build issues in Koji

* Fri May 07 2021 Nick Rhodes <nrhodes91@gmail.com> - 0.20.0-1
- Port to python3 compatibility (PR 120)

* Sun Aug 16 2020 Nick Rhodes <nrhodes91@gmail.com> - 0.19.0-1
- Added lsblk and blkid (PR 115)
- Fix flake8 warnings (PR 118)
- Filtering out update line in pcs status (PR 112)

* Mon Feb 03 2020 Nick Rhodes <nrhodes91@gmail.com> - 0.18.0-1
- Improvements to get_diff (PR 110)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 03 2019 Nick Rhodes <nrhodes91@gmail.com> - 0.17.1-1
- Convert relative basedir to absolute path (PR 103)

* Sun Jun 16 2019 Nick Rhodes <nrhodes91@gmail.com> - 0.17.0-1
- Update diff function to use Popen.communicate() (PR 101)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 02 2018 Nick Rhodes <nrhodes91@gmail.com> - 0.16.2-1
- Only report skipping default additional.conf file when using custom file

* Sun Nov 04 2018 Nick Rhodes <nrhodes91@gmail.com> - 0.16.1-1
- Revert previous --config release with argparse rewrite
- Add --config option for specifying custom a configuration file using optparse
- Filter the "ip address show" output to remove lines containing valid_lft XXsec preferred_lft XXsec

* Wed Oct 17 2018 Nick Rhodes <nrhodes91@gmail.com> - 0.16-1
- Add --config option for specifying custom a configuration file

* Sat Sep 15 2018 Nick Rhodes <nrhodes91@gmail.com> - 0.15-1
- Added copy_dir function to recursively backup and diff directories
- Add ability to use copy_dir in additional.conf along with a file pattern match

* Tue Jul 31 2018 Paolo Gigante <paolo.gigante.sa@gmail.com> - 0.14-1
- Adjusted -w option to only overwrite specific tagged files
- Add option to compare existing files without gathering new data using the -C/--compare-only option
- Added the option to capture post data and compare to phases other than *.pre using the --pre option
- Added option to force a compare even id the phase does not contain "post" or "rollback" using the --force-compare option

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 17 2017 Piers Cornwell <piers.cornwell@rackspace.co.uk> 0.13-1
- New option -a to create a tar archive of the output
- New option -w to overwrite existing output
- PEP8 fixes
- Modify check for PHP presence

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jun 12 2017 Piers Cornwell <piers.cornwell@rackspace.co.uk> 0.12-2
- Record Pacemaker status
- Don't raise exception if command doesn't exist
- Add alternative path for lspci
- Allow MySQL show databases to fail
- Record PHP state
- Record iptables rules
- Documented tested platforms
- Optional custom collection

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 25 2017 Christos Triantafyllidis <christos.triantafyllidis@rackspace.co.uk> 0.11-2
- Updated spec according to Fedora Guidelines

* Wed Dec 21 2016 Piers Cornwell <piers.cornwell@rackspace.co.uk> 0.11-1
- Renamed from getData to configsnap
- Backup grubenv for grub2
- Support for Fedora
- Added man page
- Record dm-multipath information
- Continue if lvm isn't present
- Allow PowerPath to be present, but with no LUNs

* Wed Jul 27 2016 Piers Cornwell <piers.cornwell@rackspace.co.uk> 0.10-1
- Initial public release, version 0.10

* Mon May 9 2016 Piers Cornwell <piers.cornwell@rackspace.co.uk> 0.9-1
- Initial standalone tagged release, version 0.9
