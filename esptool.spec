Name:           esptool
Version:        4.7.0
Release:        %autorelease
Summary:        A utility to communicate with the ROM bootloader in Espressif ESP8266 & ESP32

License:        GPL-2.0-or-later
URL:            https://github.com/espressif/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

Provides:       %{name}.py = %{version}-%{release}


%description
%{name}.py A command line utility to communicate with the ROM bootloader in
Espressif ESP8266 & ESP32 WiFi microcontroller. Allows flashing firmware,
reading back firmware, querying chip parameters, etc.
Developed by the community, not by Espressif Systems.


%prep
%autosetup -p1


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files esptool espefuse espsecure
for NAME in %{name} espefuse espsecure esp_rfc2217_server ; do
  ln -s ./$NAME.py %{buildroot}%{_bindir}/$NAME
done


%check
# There is esptool[hsm] which pulls additional requirement on python-pkcs11
# It is not yet packaged in Fedora though
%pyproject_check_import -e 'espsecure.esp_hsm_sign*'


%files -f %{pyproject_files}
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}.py
%{_bindir}/espefuse
%{_bindir}/espefuse.py
%{_bindir}/espsecure
%{_bindir}/espsecure.py
%{_bindir}/esp_rfc2217_server
%{_bindir}/esp_rfc2217_server.py


%changelog
%autochangelog
