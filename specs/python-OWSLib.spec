# Sphinx-generated HTML documentation is not suitable for packaging; see
# https://bugzilla.redhat.com/show_bug.cgi?id=2006555 for discussion.
#
# We can generate PDF documentation as a substitute.
# EPEL10 does not (yet) have pandoc.
%bcond doc_pdf %{undefined el10}

Name:           python-OWSLib
Version:        0.32.0
Release:        %autorelease
Summary:        OGC Web Service utility library

License:        BSD-3-Clause
URL:            https://geopython.github.io/OWSLib
# A filtered source archive, obtained by (see Source1):
#
#   ./get_source %%{version}
#
# is required because tests/resources/ contains XML data files that appear to
# have been pulled from various GIS databases, and the license terms for these
# files are unclear.
#
# The unfiltered base source URL would be:
#
# https://github.com/geopython/OWSLib/archive/%%{version}/OWSLib-%%{version}.tar.gz
#
# We *could* use the PyPI sdist, which does not contain tests/resources/, but
# it also does not contain any tests at all. We can still run some tests
# without the XML files, and we would like to do so.
Source0:        OWSLib-%{version}-filtered.tar.zst
Source1:        get_source

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with doc_pdf}
BuildRequires:  make
BuildRequires:  python3-sphinx-latex
BuildRequires:  latexmk
BuildRequires:  pandoc
%endif

%global common_description %{expand:
OWSLib is a Python package for client programming with Open Geospatial
Consortium (OGC) web service (hence OWS) interface standards, and their related
content models.

Full documentation is available at http://geopython.github.io/OWSLib

OWSLib provides a common API for accessing service metadata and wrappers for
numerous OGC Web Service interfaces.}

%description %{common_description}


%package -n python3-OWSLib
Summary:        %{summary}

%py_provides python3-owslib

%description -n python3-OWSLib %{common_description}


%package doc
Summary:        Documentation and examples for OWSLib

%description doc
%{summary}.


%prep
%autosetup -n OWSLib-%{version}

# Don’t analyze/report test coverage
sed -r -i 's/[-]-cov[^[:blank:]]*[[:blank:]][^[[:blank:]]+//g' tox.ini
# Don’t generate linting/coverage dependencies.
#
# We don’t have python3dist(pandoc) packaged, and besides, we don’t actually
# need python3dist(pandoc)—only the pandoc command-line tool, which we have
# manually BR’d.
#
# Don’t generate twine dependency, which is just for the upstream maintainer
# uploading to PyPI.
sed -r -e '/^(flake8|pytest-cov|twine|coverage|coveralls)\b/d' \
    requirements-dev.txt | tee requirements-dev-filtered.txt

# We don’t need shebangs in the examples. The pattern of selecting files
# before modifying them with sed keeps us from unnecessarily discarding the
# original mtimes on unmodified files.
find 'examples' -type f -name '*.py' \
    -exec gawk '/^#!/ { print FILENAME }; { nextfile }' '{}' '+' |
  xargs -r sed -r -i '1{/^#!/d}'
# Some of them, but not all of them, were executable.
chmod -v a-x examples/*.py

# Because at least one notebook requires Internet access, we must continue past
# notebook errors when building documentation.
echo 'nbsphinx_allow_errors = True' >> docs/source/conf.py


%generate_buildrequires
%{pyproject_buildrequires \
    %{?with_doc_pdf:docs/requirements.txt} \
    requirements-dev-filtered.txt}


%build
%pyproject_wheel

%if %{with doc_pdf}
PYTHONPATH="${PWD}" %make_build -C docs latex \
    SPHINXOPTS='-j%{?_smp_build_ncpus}'
%make_build -C docs/build/latex LATEXMKOPTS='-quiet'
%endif


%install
%pyproject_install
%pyproject_save_files -l owslib


%check
# Otherwise, pytest finds the package twice in the Python path and complains.
rm -rf owslib

# This requires network access (during test collection!)
ignore="${ignore-} --ignore=tests/test_ogcapi_connectedsystems_osh.py"

# These require test data files from tests/resources/, which we have removed:
ignore="${ignore-} --ignore-glob=tests/doctests/*.txt"
k="${k-}${k+ and }not test_gm03"
ignore="${ignore-} --ignore=tests/test_iso_parsing.py"
ignore="${ignore-} --ignore=tests/test_ows_interfaces.py"
ignore="${ignore-} --ignore=tests/test_owscontext_atomxml.py"
k="${k-}${k+ and }not test_decode_single_json"
k="${k-}${k+ and }not test_load_parse"
k="${k-}${k+ and }not test_decode_full_json"
k="${k-}${k+ and }not test_load_bulk"
ignore="${ignore-} --ignore=tests/test_remote_metadata.py"
k="${k-}${k+ and }not TestOffline"
ignore="${ignore-} --ignore=tests/test_wfs_generic.py"
ignore="${ignore-} --ignore=tests/test_wms_datageo_130.py"
ignore="${ignore-} --ignore=tests/test_wms_jpl_capabilities.py"
k="${k-}${k+ and }not test_wps_getOperationByName"
k="${k-}${k+ and }not test_wps_checkStatus"
k="${k-}${k+ and }not test_wps_process_representation"
k="${k-}${k+ and }not test_wps_process_properties"
k="${k-}${k+ and }not test_wps_literal_data_input_parsing_references"
k="${k-}${k+ and }not test_wps_response_with_lineage"
ignore="${ignore-} --ignore=tests/test_wps_describeprocess_bbox.py"
ignore="${ignore-} --ignore=tests/test_wps_describeprocess_ceda.py"
ignore="${ignore-} --ignore=tests/test_wps_describeprocess_emu_all.py"
ignore="${ignore-} --ignore=tests/test_wps_describeprocess_usgs.py"
ignore="${ignore-} --ignore=tests/test_wps_execute.py"
ignore="${ignore-} --ignore=tests/test_wps_execute_invalid_request.py"
ignore="${ignore-} --ignore=tests/test_wps_getcapabilities_52n.py"
ignore="${ignore-} --ignore=tests/test_wps_getcapabilities_ceda.py"
ignore="${ignore-} --ignore=tests/test_wps_getcapabilities_usgs.py"
ignore="${ignore-} --ignore-glob=tests/test_wps_request*.py"
ignore="${ignore-} --ignore-glob=tests/test_wps_response*.py"
k="${k-}${k+ and }not test_metadata"
k="${k-}${k+ and }not test_responsibility"
k="${k-}${k+ and }not test_distributor"
k="${k-}${k+ and }not test_online_distribution"
k="${k-}${k+ and }not test_identification"
k="${k-}${k+ and }not test_identification_contact"
k="${k-}${k+ and }not test_identification_date"
k="${k-}${k+ and }not test_identification_extent"
k="${k-}${k+ and }not test_identification_keywords"
k="${k-}${k+ and }not test_get_all_contacts"
k="${k-}${k+ and }not test_aus"
k="${k-}${k+ and }not test_service"
k="${k-}${k+ and }not test_md_featurecataloguedesc"
k="${k-}${k+ and }not test_md_imagedescription"
k="${k-}${k+ and }not test_dq_dataquality"
k="${k-}${k+ and }not test_md_reference_system"
k="${k-}${k+ and }not test_service2"
k="${k-}${k+ and }not test_md_distribution"

%pytest -m 'not online' -k "${k-}" ${ignore-} -v -rs


%files -n python3-OWSLib -f %{pyproject_files}


%files doc
%license LICENSE
%doc AUTHORS.rst
%doc README.md
%doc examples/
%if %{with doc_pdf}
%doc docs/build/latex/OWSLib.pdf
%endif


%changelog
%autochangelog
