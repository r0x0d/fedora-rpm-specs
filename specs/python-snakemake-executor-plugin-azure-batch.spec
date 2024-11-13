Name:           python-snakemake-executor-plugin-azure-batch
Version:        0.3.0
Release:        %autorelease
Summary:        A Snakemake executor plugin for submitting jobs to Microsoft Azure Batch

# SPDX
License:        MIT
URL:            https://github.com/snakemake/snakemake-executor-plugin-azure-batch
# We use the GitHub archive instead of the PyPI sdist to get CHANGELOG.md and
# the tests.
Source:         %{url}/archive/v%{version}/snakemake-executor-plugin-azure-batch-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
# See: [tool.poetry.dev-dependencies] in pyproject.toml
BuildRequires:  snakemake >= 8

%global common_description %{expand:
%{summary}.}

%description %{common_description}


%package -n python3-snakemake-executor-plugin-azure-batch
Summary:        %{summary}

%description -n python3-snakemake-executor-plugin-azure-batch %{common_description}


%prep
%autosetup -n snakemake-executor-plugin-azure-batch-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files snakemake_executor_plugin_azure_batch


%check
%pyproject_check_import
# All tests require network access and Azure credentials.


%files -n python3-snakemake-executor-plugin-azure-batch -f %{pyproject_files}
%license LICENSE
%doc CHANGELOG.md
%doc README.md


%changelog
%autochangelog
