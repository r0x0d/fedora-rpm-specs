# Generated by go2rpm 1.3
%bcond_without check

# https://github.com/denisbrodbeck/machineid
%global goipath         github.com/denisbrodbeck/machineid
Version:                1.0.1

%gometa

%global common_description %{expand:
Get the unique machine id of any host (without admin privileges).}

%global golicenses      LICENSE.md
%global godocs          README.md logo.png

Name:           %{goname}
Release:        %autorelease
Summary:        Get the unique machine id of any host (without admin privileges)

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}

%package -n     machineid
Summary:        %{summary}
%description -n machineid
%{common_description}

%gopkg

%prep
%goprep

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
%gocheck
%endif

%files -n machineid
%license LICENSE.md
%doc README.md logo.png
%{_bindir}/*

%gopkgfiles

%changelog
%autochangelog