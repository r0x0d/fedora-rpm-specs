Name:           python-zmq
Version:        25.1.2
Release:        %autorelease
Summary:        Python bindings for zeromq

# As noted in https://github.com/zeromq/pyzmq/blob/v26.2.0/RELICENSE/README.md:
#   pyzmq starting with 26.0.0 is fully licensed under the 3-clause Modified
#   BSD License. A small part of the core (Cython backend only) was previously
#   licensed under LGPLv3 for historical reasons. Permission has been granted
#   by the contributors of the vast majority of those components to relicense
#   under MPLv2 or BSD. This backend has been completely replaced in pyzmq 26,
#   and the new implementation is fully licensed under BSD-3-Clause, so pyzmq
#   is now under a single license.
# Since this package is currently at 25.1.2, the entire source is BSD-3-Clause
# (LICENSE.BSD), except:
#   - Some core files (the low-level Cython bindings) are LGPL-3.0-or-later
#     (LICENSE.LESSER); based on comments in file headers, this is just
#     zmq/backend/cython/_device.pyx.
#   - zmq/ssh/forward.py, which is derived from a Paramiko demo, is
#     LGPL-2.1-or-later
#   - zmq/eventloop/zmqstream.py is Apache-2.0
# Additionally, the following do not affect the license of the binary RPMs:
#   - tools/run_with_env.cmd is CC0-1.0; for distribution in the source RPM, it
#     is covered by “Existing uses of CC0-1.0 on code files in Fedora packages
#     prior to 2022-08-01, and subsequent upstream versions of those files in
#     those packages, continue to be allowed. We encourage Fedora package
#     maintainers to ask upstreams to relicense such files.”
#     https://gitlab.com/fedora/legal/fedora-license-data/-/issues/91#note_1151947383
#   - examples/device/device.py and examples/win32-interrupt/display.py are
#     LicenseRef-Fedora-Public-Domain; approved in “Review of
#     python-zmq examples dedicated to the public domain,”
#     https://gitlab.com/fedora/legal/fedora-license-data/-/issues/616; see
#     https://gitlab.com/fedora/legal/fedora-license-data/-/merge_requests/716
License:        %{shrink:
                BSD-3-Clause AND
                LGPL-3.0-or-later AND
                LGPL-2.1-or-later AND
                Apache-2.0
                }
URL:            https://zeromq.org/languages/python/
%global forgeurl https://github.com/zeromq/pyzmq
Source0:        %{forgeurl}/archive/v%{version}/pyzmq-%{version}.tar.gz
# BUG: A file is licensed Apache-2.0, but the license text is not distributed
# https://github.com/zeromq/pyzmq/issues/2048
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt#/LICENSE.Apache-2.0

# Python 3.13 compatibility
Patch:          %{forgeurl}/pull/1961.patch

BuildRequires:  gcc
BuildRequires:  pkgconfig(libzmq)
BuildRequires:  python3-devel

%global common_description %{expand:
This package contains Python bindings for ZeroMQ. ØMQ is a lightweight and fast
messaging implementation.}

%description %{common_description}


%package -n python3-pyzmq
Summary:        %{summary}

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_provides_for_importable_modules
%py_provides    python3-zmq

# Beginning with Fedora 42, the binary packages are renamed from
# python3-zmq/python3-zmq-tests to python3-pyzmq/python3-pyzmq-tests to match
# the canonical package name. Ideally, the source package would also be called
# python-pyzmq, but it’s not worth going through the package renaming process
# for this. The Obsoletes/Conflicts provide a clean upgrade path, and can be
# removed after Fedora 44 end-of-life.
Obsoletes:      python3-zmq < 25.1.1-29
Conflicts:      python3-zmq < 25.1.1-29

%description -n python3-pyzmq %{common_description}


%package -n python3-pyzmq-tests
Summary:        Test suite for Python bindings for zeromq
# This subpackage does not contain any of the files that are under other
# licenses; see the comment above the main License tag.
License:        BSD-3-Clause

Requires:       python3-pyzmq%{?_isa} = %{version}-%{release}

# See notes about binary package renaming in the python3-pyzmq subpackage.
%py_provides    python3-zmq-tests
Obsoletes:      python3-zmq-tests < 25.1.1-29
Conflicts:      python3-zmq-tests < 25.1.1-29

# Based on test-requirements.txt; see test-requirements-filtered.txt, as
# generated in %%prep. The BR’s duplicate the generated ones, which is
# unfortunate, but necessary to make sure that we don’t have unsatisfied
# runtime/install-time dependencies. It would be better if we didn’t have to
# ship the tests at all – maybe we don’t?
BuildRequires:  %{py3_dist cython}
Requires:       %{py3_dist cython}
BuildRequires:  %{py3_dist pymongo}
Requires:       %{py3_dist pymongo}
BuildRequires:  %{py3_dist pytest}
Requires:       %{py3_dist pytest}
BuildRequires:  %{py3_dist pytest-asyncio}
Requires:       %{py3_dist pytest-asyncio}
BuildRequires:  %{py3_dist setuptools}
Requires:       %{py3_dist setuptools}
BuildRequires:  %{py3_dist tornado}
Requires:       %{py3_dist tornado}

# Add some manual test dependencies that aren’t in test-requirements.txt, but
# which enable additional tests.
#
# Tests in zmq/tests/mypy.py require mypy, but see:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
#
# Some tests in zmq/tests/test_context.py and zmq/tests/test_socket.py require
# pyczmq, which is not packaged and has not been updated in a decade.
#
# Enable more tests in zmq/tests/test_message.py:
BuildRequires:  %{py3_dist numpy}
Recommends:     %{py3_dist numpy}

%description -n python3-pyzmq-tests %{common_description}

This package contains the test suite for the Python bindings.


%prep
%autosetup -p1 -n pyzmq-%{version}

# Remove any Cython-generated .c files in order to regenerate them:
find zmq -name '*.c' -print -delete

# Remove shebangs from non-script sources. The find-then-modify pattern
# preserves mtimes on sources that did not need to be modified.
find 'src' -type f -name '*.py' \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r sed -r -i '1{/^#!/d}'

# BUG: A file is licensed Apache-2.0, but the license text is not distributed
# https://github.com/zeromq/pyzmq/issues/2048
cp -p '%{SOURCE1}' .

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -r \
    -e 's/^(black|codecov|coverage|flake8|mypy|pytest-cov)\b/# &/' \
    test-requirements.txt | tee test-requirements-filtered.txt


%generate_buildrequires
%pyproject_buildrequires test-requirements-filtered.txt


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l zmq


%check
# to avoid partially initialized zmq module from cwd
mkdir -p _empty
cd _empty
ln -s %{buildroot}%{python3_sitearch}/zmq/ ../pytest.ini ./

# test_draft seems to get incorrectly run:
# https://github.com/zeromq/pyzmq/issues/1853
k="${k-}${k+ and }not test_draft"

%ifarch ppc64le
# These crash on Python 3.12; TODO: investigate
k="${k-}${k+ and }not test_green_device"
k="${k-}${k+ and }not (Green and (test_raw or test_timeout or test_poll))"
%endif

%pytest --maxfail 2 -k "${k-}" -v -rs zmq/tests


%files -n python3-pyzmq -f %{pyproject_files}
%doc README.md
%exclude %{python3_sitearch}/zmq/tests/


%files -n python3-pyzmq-tests
%{python3_sitearch}/zmq/tests/


%changelog
%autochangelog
