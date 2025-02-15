# Generated by go2rpm 1.8.2
%bcond_without check

# https://github.com/atotto/clipboard
%global goipath         github.com/atotto/clipboard
Version:                0.1.4

%gometa

%global common_description %{expand:
Provide copying and pasting to the Clipboard for Go.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Clipboard for golang

License:        BSD-3-Clause
URL:            %{gourl}
Source:         %{gosource}

BuildRequires:  xorg-x11-server-Xvfb
BuildRequires:  xclip

%description %{common_description}

%gopkg

%prep
%goprep

%generate_buildrequires
%go_generate_buildrequires

%build
for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/

%if %{with check}
%check
export DISPLAY=:99
xdpyinfo -display $DISPLAY > /dev/null || Xvfb $DISPLAY -screen 0 1024x768x16 &
%gocheck
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/gocopy
%{_bindir}/gopaste

%gopkgfiles

%changelog
%autochangelog
