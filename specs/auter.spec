Name:           auter
Version:        1.0.0
Release:        15%{?dist}
Summary:        Prepare and apply updates
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/rackerlabs/%{name}
Source0:        https://github.com/rackerlabs/%{name}/archive/%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  help2man
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
BuildRequires:  systemd
%endif
Requires:       crontabs
%if 0%{?fedora} >= 18
Requires:       dnf
%else
Requires:       yum
%endif

%description
auter (optionally) pre-downloads updates and then runs automatically on a
set schedule, optionally rebooting to finish applying the updates.

%prep
%setup -q

%build
help2man --section=1 ./auter -N -o auter.man -n "Automatic Update Transaction Execution by Rackspace" --include=auter.help2man-sections

%install
%if 0%{?fedora} >= 15 || 0%{?rhel} >= 7
mkdir -p %{buildroot}%{_tmpfilesdir}
echo "d %{_rundir}/%{name} 0755 root root -" > %{buildroot}%{_tmpfilesdir}/%{name}.conf
mkdir -p %{buildroot}%{_rundir}/%{name}
touch %{buildroot}%{_rundir}/%{name}/%{name}.pid
%else
mkdir -p %{buildroot}%{_localstatedir}/run/%{name}
touch %{buildroot}%{_localstatedir}/run/%{name}/%{name}.pid
%endif

install -d -p -m 0755 \
  %{buildroot}%{_sharedstatedir}/%{name} \
  %{buildroot}%{_var}/cache/%{name} \
  %{buildroot}%{_sysconfdir}/%{name}/pre-reboot.d \
  %{buildroot}%{_sysconfdir}/%{name}/post-reboot.d \
  %{buildroot}%{_sysconfdir}/%{name}/pre-apply.d \
  %{buildroot}%{_sysconfdir}/%{name}/post-apply.d \
  %{buildroot}%{_sysconfdir}/%{name}/pre-prep.d \
  %{buildroot}%{_sysconfdir}/%{name}/post-prep.d

install -D -p -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -D -p -m 0644 %{name}.cron %{buildroot}%{_sysconfdir}/cron.d/%{name}
install -D -p -m 0755 %{name}.yumdnfModule %{buildroot}%{_usr}/lib/%{name}/auter.module
install -D -p -m 0644 %{name}.man %{buildroot}%{_mandir}/man1/%{name}.1
install -D -p -m 0644 %{name}.conf.man %{buildroot}%{_mandir}/man5/%{name}.conf.5
install -D -p -m 0644 %{name}.conf %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf

%post
# If this is the first time install, create the lockfile
if [ $1 -eq 1 ]; then
  /usr/bin/auter --enable
fi
exit 0

%preun
# If this is a complete removal, then remove lockfile
if [ $1 -eq 0 ]; then
 /usr/bin/auter --disable
fi
exit 0

%files
%{!?_licensedir:%global license %doc}
%license LICENSE
%doc README.md
%doc NEWS
%doc MAINTAINERS.md
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.conf.5*
%{_sharedstatedir}/%{name}
%dir %{_sysconfdir}/%{name}
%dir %{_var}/cache/auter
%dir %{_sysconfdir}/%{name}/pre-reboot.d
%dir %{_sysconfdir}/%{name}/post-reboot.d
%dir %{_sysconfdir}/%{name}/pre-apply.d
%dir %{_sysconfdir}/%{name}/post-apply.d
%dir %{_sysconfdir}/%{name}/pre-prep.d
%dir %{_sysconfdir}/%{name}/post-prep.d
%dir %{_usr}/lib/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/cron.d/%{name}
%{_bindir}/%{name}
%{_usr}/lib/%{name}/auter.module
%if 0%{?el6}
%dir %{_localstatedir}/run/%{name}/
%ghost %{_localstatedir}/run/%{name}/%{name}.pid
%else
%dir %{_rundir}/%{name}/
%ghost %{_rundir}/%{name}/%{name}.pid
%{_tmpfilesdir}/%{name}.conf
%endif

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 24 2024 Miroslav Suchý <msuchy@redhat.com> - 1.0.0-14
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 29 2019 Nick Rhodes <nrhodes91@gmail.com> 1.0.0-1
- #220 Introduce package dependant reboots using AUTOREBOOT option
- #215 Remove rpm and deb package build tests from travis
- #223 Parallelize the travis jobs
- #224/#225 Clean up ShellCheck warnings

* Tue Mar 05 2019 Nick Rhodes <nrhodes91@gmail.com> 0.12.3-1
- #214 Log a machine readable status to the last-{prep,apply} output files

* Tue Feb 12 2019 Nick Rhodes <nrhodes91@gmail.com> 0.12.2-1
- #207 check for process matching PID file content

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 11 2018 Nick Rhodes <nrhodes91@gmail.com> 0.12.1-1
- Add max-delay option to override MAXDLAY via command line
- Redirect stderr to stdout and capture in APPLYOUTPUT variable

* Thu Jul 12 2018 Paolo Gigante <paolo.gigante.sa@gmail.com> 0.12-1
- Added --skip-all-scripts to skip the executions of all custom scripts
- Added --skip-scripts-by-phase to skip the executions of custom scripts for the specified phase
- Added --skip-scripts-by-phase to skip the executions of custom scripts by name
- Added man page for auter.conf
- Updated auter.aptModule to reflect changes in auter.yumdnfModule
- added no-wall option
- Fix for --status when run as non-root user
- Logs auter output in /var/lib/auter/ when no updates are available
- Minor improvements to rotation of output files in /var/lib/auter/

* Fri Mar 16 2018 Nick Rhodes <nrhodes91@gmail.com> 0.11-5
- Hotfix for the AUTOREBOOT issue

* Fri Mar 16 2018 Paolo Gigante <paolo.gigante@rackspace.co.uk> 0.11-4
- Updated documentation and references to include apt for Ubuntu/debian
- Removed debugging message that was printed during apt update
- Added "Valid Options" in auter.conf
- Added the pre/post prep directories in auter.conf
- Added retention and rotation for last-prep-output and last-apply-output files in /var/lib/auter
- Corrected file permissions for the auter-postreboot cron file
- Added --stdout option to force output to stdout even if there is no active tty
- Added a package manager lock file check before prep and apply functions call the package manager
- Improved checks to confirm prepared patches are still required
- Adjusted some string arguments to arrays for better handling

* Mon Oct 30 2017 Paolo Gigante <paolo.gigante@rackspace.co.uk> 0.10-1
- Added pre and post prep script hooks
- Added a pidfile and process check to --status
- Added a auter success log with a last run timestamp
- Clear pidfile if the process is no longer running when disabling auter
- Added auter.aptModule for ubuntu/debian support

* Thu Mar 09 2017 Piers Cornwell <piers.cornwell@rackspace.co.uk> 0.9-1
- Capture package manager output
- Document the auter --reboot cron job
- Remove last-update file
- Add description text to the lock file
- Add error checking during prep
- Split out package manager specific code

* Mon Nov 14 2016 Piers Cornwell <piers.cornwell@rackspace.co.uk> 0.8-1
- Release version 0.8
- Added ONLYINSTALLFROMPREP option

* Thu Aug 04 2016 Piers Cornwell <piers.cornwell@rackspace.co.uk> 0.7-1
- Release version 0.7
- Updated the .spec file according to Fedora's guidelines
- Moved scriptdir from /var/lib/auter to /etc/auter
- Categorise log messages as INFO, WARNING or ERROR
- Remove pre-built man page

* Wed Jul 06 2016 Cameron Beere <cameron.beere@rackspace.co.uk> 0.6-1
- Release version 0.6
- Add maintainers file

* Thu Apr 28 2016 Cameron Beere <cameron.beere@rackspace.co.uk> 0.5-1
- Release version 0.5
- Added transaction ID logging
- Disable random sleepis when running from a tty
- Rename variables to be package manager agnostic
- Add cron examples for @reboot jobs
- Update default auter config file location
- Remove example script files
- Disable cronjobs & enable lockfile on installation
- Switch to using pre/post script directories instead of files
- Add better handling for option parsing
- Added CONFIGSET variable used to distinguish between distinct configs
- Various bugfixes

* Wed Mar 23 2016 Piers Cornwell <piers.cornwell@rackspace.co.uk> 0.4-1
- Release version 0.4
- Support DNF
- Add HACKING.md
- Exit if custom config file doesn't exist
- Change post reboot script to use cron instead of rc.local
- Report if there are no updates at prep time
- Record prep and apply output
- Updated man page

* Mon Mar 14 2016 Paolo Gigante <paolo.gigante@rackspace.co.uk> 0.3-1
- Release version 0.3
- Better defined exit codes
- Added bounds check for MAXDELAY
- Updated documentation with more details about configuration options
- Fixed logging error if downloadonly is not available

* Thu Mar 10 2016 Piers Cornwell <piers.cornwell@rackspace.co.uk> 0.2-1
- Release version 0.2
- Locking
- Trap Ctrl+C during dangerous section
- Add --status flag
- Move reboot script to /etc/rc.d/rc.local
- Add random delay
- Change from sysv service to --enable/--disable
- Added warnings when pre/post hooks exist but are not executable
- Removed yum transaction support
- Added pid locking to prevent multiple instances of auter running at the same time

* Wed Mar 02 2016 Mike Frost <mike.frost@rackspace.co.uk> 0.1-1
- Release version 0.1
