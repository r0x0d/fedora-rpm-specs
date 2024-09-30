%global common_description %{expand:
Falcon is a minimalist ASGI/WSGI framework for building mission-critical REST
APIs and microservices, with a focus on reliability, correctness, and
performance at scale.  When it comes to building HTTP APIs, other frameworks
weigh you down with tons of dependencies and unnecessary abstractions. Falcon
cuts to the chase with a clean design that embraces HTTP and the REST
architectural style.}

Name:           python-falcon
Epoch:          1
Version:        3.1.3
Release:        %autorelease
Summary:        Fast ASGI+WSGI framework for building data plane APIs at scale
License:        Apache-2.0
URL:            https://falconframework.org
Source:         %{pypi_source falcon}

# downstream-only patch to remove bundled library
Patch:          0001-Use-system-mimeparse.patch
# downstream-only patch to fix %%pyproject_buildrequires
Patch:          0002-Use-actual-path-to-version-attribute-in-setup.cfg.patch
# downstream-only patch to remove coverage build requirement
Patch:          0003-Remove-coverage-test-requirement.patch
# https://github.com/falconry/falcon/pull/2217
Patch:          0004-feat-parse_header-provide-our-own-implementation-of-parse_header-2217.patch

BuildRequires:  gcc


%description %{common_description}


%package -n python3-falcon
Summary:        %{summary}
BuildRequires:  python3-devel


%description -n python3-falcon %{common_description}


%prep
%autosetup -p 1 -n falcon-%{version}
rm -rf falcon/vendor


%generate_buildrequires
%pyproject_buildrequires -e mintest


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files falcon


%check
%tox -e mintest


%files -n python3-falcon -f %{pyproject_files}
%doc README.rst
%{_bindir}/falcon-bench
%{_bindir}/falcon-inspect-app
%{_bindir}/falcon-print-routes


%changelog
%autochangelog
