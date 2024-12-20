%global srcversion 24-11

Name:           pgn-extract
Version:        %(echo %{srcversion} | tr - .)
Release:        %autorelease
Summary:        Portable Game Notation (PGN) Manipulator for Chess Games

# typedef.h is GPLv1+, the rest is GPLv3+
License:        GPL-3.0-or-later AND GPL-1.0-or-later
URL:            https://www.cs.kent.ac.uk/~djb/pgn-extract
Source:         %{url}/%{name}-%{srcversion}.tgz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  sed

%description
pgn-extract is a command-line program for searching, manipulating and
formatting chess games recorded in the Portable Game Notation (PGN) or
something close. It is capable of handling files containing millions of games.
It also recognizes Chess960 encodings.

%prep
%autosetup -n %{name}

# Fix default path for eco.pgn
sed -i 's:"eco.pgn":"%{_datadir}/%{name}/eco.pgn":' main.c

# Fix end of line encoding and permissions
sed -i 's/\r$//' style.css
chmod -x style.css

%build
%make_build OPTIMISE=

%install
install -Dpm0755 -t %{buildroot}%{_bindir} %{name}
install -Dpm0644 -t %{buildroot}%{_datadir}/%{name} eco.pgn
install -Dpm0644 %{name}.man %{buildroot}%{_mandir}/man1/%{name}.1

%check
pushd test
%make_build
./runtests
popd

%files
%license COPYING copyright
%doc index.html changes.html help.html style.css
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
