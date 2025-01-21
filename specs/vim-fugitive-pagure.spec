Name: vim-fugitive-pagure
Version: 1.5
Release: 5%{?dist}
Summary: Pagure support for vim-fugitive plugin
License: GPL-2.0-or-later
BuildArch: noarch

URL: https://github.com/FrostyX/vim-fugitive-pagure

# Sources can be obtained by
# git clone https://github.com/FrostyX/vim-fugitive-pagure.git
# cd vim-fugitive-pagure
# tito build --tgz
Source0: %{name}-%{version}.tar.gz

Requires: vim-common
Requires: vim-fugitive

BuildRequires: vim-filesystem
BuildRequires: python3-devel
BuildRequires: python3-pytest


%description
Pagure support for :Gbrowse feature provided by vim-fugitive plugin


%prep
%setup -q


%install
mkdir -p %{buildroot}%{vimfiles_root}/plugin
install -D -p -m 0644 plugin/* %{buildroot}%{vimfiles_root}/plugin/


%check
python3 -B -m pytest . -v -s


%files
%license LICENSE
%doc README.md
%{vimfiles_root}/plugin/fugitive-pagure.vim
%{vimfiles_root}/plugin/fugitive_pagure.py
%{vimfiles_root}/plugin/__init__.py


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Jakub Kadlcik <frostyx@email.cz> 1.5-1
- Update License to an SPDX expression (frostyx@email.cz)

* Tue Jul 28 2020 Jakub Kadlcik <frostyx@email.cz> 1.4-1
- Recognize pkgs.fedoraproject.org as a pagure URL (frostyx@email.cz)

* Thu Jul 09 2020 Jakub Kadlcik <frostyx@email.cz> 1.3-1
- Implement support for browsing commits (frostyx@email.cz)

* Wed Mar 25 2020 Jakub Kadlcik <frostyx@email.cz> 1.2-1
- Oops, fix the copy-pasted Source0 (frostyx@email.cz)

* Tue Mar 24 2020 Jakub Kadlcik <frostyx@email.cz> 1.1-1
- new package built with tito

* Sat Sep 21 2019 Jakub Kadlčík <jkadlcik@redhat.com> - 1.0-1
- Initial version

