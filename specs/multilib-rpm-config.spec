# https://fedoraproject.org/wiki/Packaging:Guidelines#Packaging_of_Additional_RPM_Macros
%global macrosdir       %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

%global rrcdir          %_libexecdir

Summary: Multilib packaging helpers
Name: multilib-rpm-config
Version: 1
Release: 28%{?dist}
License: GPL-2.0-or-later

# TODO: resolve directly in rpm/redhat-rpm-config (instead of this hack).
# Note that to avoid FTBFS against plain RHEL6, we can't put this hack before
# License tag.
%{!?_licensedir:%global license %%doc}

URL: https://fedoraproject.org/wiki/PackagingDrafts/MultilibTricks

BuildRequires: gcc

Source0: multilib-fix
Source1: macros.ml
Source2: README
Source3: COPYING
Source4: multilib-library
Source5: multilib-info

BuildArch: noarch

# Most probably we want to move everything here?
Requires: redhat-rpm-config

%description
Set of tools (shell scripts, RPM macro files) to help with multilib packaging
issues.


%prep
%setup -c -T
install -m 644 %{SOURCE2} %{SOURCE3} .


%build
%global ml_fix %rrcdir/multilib-fix
%global ml_info %rrcdir/multilib-info

lib_sed_pattern='/@LIB@/ {
    r %{SOURCE4}
    d
}'

sed -e 's|@ML_FIX@|%ml_fix|g' \
    -e 's|@ML_INFO@|%ml_info|g' \
    %{SOURCE1} > macros.multilib
sed -e "$lib_sed_pattern" \
    %{SOURCE0} > multilib-fix
sed -e "$lib_sed_pattern" \
    %{SOURCE5} > multilib-info


%install
mkdir -p %{buildroot}%{rrcdir}
mkdir -p %{buildroot}%{macrosdir}
install -m 644 -p macros.multilib %{buildroot}/%{macrosdir}
install -m 755 -p multilib-fix %{buildroot}/%{ml_fix}
install -m 755 -p multilib-info %{buildroot}/%{ml_info}


%check
mkdir tests ; cd tests
ml_fix="sh `pwd`/../multilib-fix --buildroot `pwd`"
capable="sh `pwd`/../multilib-info --multilib-capable"

mkdir template
cat > template/main.c <<EOF
#include "header.h"
int main () { call (); return 0; }
EOF
cat > template/header.h <<EOF
#include <stdio.h>
void call (void) { printf ("works!\n"); }
EOF

cp -r template basic
gcc ./basic/main.c
./a.out

pwd
if `$capable`; then
    cp -r template really-works
    $ml_fix --file /really-works/header.h
    gcc really-works/main.c
    ./a.out
    test -f really-works/header-*.h
fi

cp -r template other_arch
$ml_fix --file /other_arch/header.h --arch ppc64
test -f other_arch/header-*.h

cp -r template other_arch_fix
$ml_fix --file /other_arch_fix/header.h --arch ppc64p7
test -f other_arch_fix/header-ppc64.h

cp -r template aarch64-no-change
$ml_fix --file /aarch64-no-change/header.h --arch aarch64
test ! -f aarch64-no-change/header-*.h

test `$capable --arch x86_64` = true
test `$capable --arch aarch64` = false
test `$capable --arch ppc64p7` = true


%files
%license COPYING
%doc README
%{rrcdir}/*
%{macrosdir}/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 05 2024 Honza Horak <hhorak@redhat.com> - 1-24
- SPDX migration

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Feb 07 2023 Michal Schorm <mschorm@redhat.com> - 1-22
- Rebuilt to apply fix regarding switch from 'uname -i' to 'uname -m' in the last commits

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 14 2018 Honza Horak <hhorak@redhat.com> - 1-11
- Add shebang to multilib-info

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Apr 07 2017 Pavel Raiskup <praiskup@redhat.com> - 1-8
- fix FTBFS on plain RHEL6

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jul 01 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 1-6
- Fix testsuite on non-multilib arches (#1352164)

* Wed Jun 22 2016 Pavel Raiskup <praiskup@redhat.com> - 1-5
- document why there is no need for '#else' in the replacement header
- add basic testsuite

* Mon Jun 13 2016 Pavel Raiskup <praiskup@redhat.com> - 1-4
- use '-' as a field separator by default

* Thu Jun 09 2016 Pavel Raiskup <praiskup@redhat.com> - 1-3
- package separately from redhat-rpm-config

* Fri Nov 27 2015 Pavel Raiskup <praiskup@redhat.com> - 1-2
- fix licensing in Sources
- allow undefined %%namespace

* Wed Nov 18 2015 Pavel Raiskup <praiskup@redhat.com> - 1-1
- initial packaging
