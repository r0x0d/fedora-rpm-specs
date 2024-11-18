%global pkgname qrcode

Name:           python-%{pkgname}
Version:        8.0
Release:        %autorelease
Summary:        Python QR Code image generator

License:        BSD-3-Clause
URL:            https://github.com/lincolnloop/python-qrcode
Source0:        %{pypi_source qrcode}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
# Explicit requires (#2271500)
Requires:       python3-pypng


%description
This module uses the Python Imaging Library (PIL) to allow for the\
generation of QR Codes.


%package -n python3-%{pkgname}
Summary:        Python QR Code image generator
Obsoletes:      python3-qrcode-core < 7.4.2-2
Provides:       python3-qrcode-core = %{version}-%{release}

%description -n python3-%{pkgname}
This module uses the Python Imaging Library (PIL) to allow for the
generation of QR Codes. Python 3 version.


%pyproject_extras_subpkg -n python3-%{pkgname} pil


%generate_buildrequires
# RHEL does not include the extra test dependencies (coverage, pillow)
%pyproject_buildrequires %{?!rhel:-x test -x pil -x png}


%prep
%autosetup -n qrcode-%{version} -p1
# Remove shebang
sed -i '1d' qrcode/console_scripts.py


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files qrcode


%check
%pytest -v


%files -n python3-%{pkgname} -f %{pyproject_files}
%doc README.rst CHANGES.rst
%license LICENSE
%{_bindir}/qr


%changelog
%autochangelog
