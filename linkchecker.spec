Name:           linkchecker

Version:        10.4.0
Release:        %autorelease
Summary:        Check HTML documents for broken links
License:        GPL-2.0-or-later
URL:            https://linkcheck.github.io/linkchecker/
Source:         %pypi_source LinkChecker

BuildArch:      noarch

BuildRequires:  gettext

BuildRequires:  python3-devel

# For compiling the translations
BuildRequires:  python3dist(polib)

# For the tests (subset of [tool.hatch.envs.test])
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(pyopenssl)
BuildRequires:  python3dist(parameterized)
# Not packaged yet
# BuildRequires:  python3dist(miniboa)

%description
LinkChecker is a website validator. LinkChecker checks links in web documents or full websites.

Features:
- Recursive and multithreaded checking and site crawling
- Output in colored or normal text, HTML, SQL, CSV, XML or a sitemap graph in 
different formats
- HTTP/1.1, HTTPS, FTP, mailto: and local file links support
- Restriction of link checking with regular expression filters for URLs
- Proxy support
- Username/password authorization for HTTP and FTP
- Honors robots.txt exclusion protocol
- Cookie support
- HTML5 support
- A command line and web interface
- Various check plugins available

%prep
%autosetup -p1 -n LinkChecker-%{version}
# Adjust tests for recently (Python 3.13, 3.12.4+) added text/markdown mimetype
# https://github.com/linkchecker/linkchecker/issues/823
sed -i 's@application/octet-stream@text/markdown@' tests/checker/data/file.markdown.result


%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files linkcheck

%check
%pytest -n auto

%files -f %{pyproject_files}
%doc README.rst doc/changelog.txt doc/upgrading.txt
%{_bindir}/linkchecker
%{_mandir}/man1/linkchecker*.1*
%{_mandir}/man5/linkcheckerrc.5*
%lang(de) %{_mandir}/de/man1/linkchecker*.1*
%lang(de) %{_mandir}/de/man5/linkcheckerrc.5*
%dir %{_datadir}/linkchecker/
%doc %{_datadir}/linkchecker/examples/

%changelog
%autochangelog
