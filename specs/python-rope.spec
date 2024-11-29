# Use forge macros to pull from GitHub
%global forgeurl https://github.com/python-rope/rope

Name:           python-rope
Version:        1.13.0
Release:        %autorelease
Summary:        Python Code Refactoring Library
%global tag %{version}
%forgemeta
License:        LGPL-3.0-or-later
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch

BuildRequires:  python3-devel


%global _description %{expand:
Rope is the world’s most advanced open source Python refactoring
library (yes, I totally stole that tagline from Postgres).

Most Python syntax up to Python 3.10 is supported. Please file bugs and
contribute patches if you encounter gaps.}

%description %_description


%package -n python3-rope
Summary:        %summary

%description -n python3-rope %_description


%package -n python-rope-doc
Summary:        %summary documentation
Requires:       python3-rope = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python-rope-doc %{expand:
Documentation for %{summary}.}


%prep
%forgeautosetup -p1

# Remove linter from dev requirements
sed -i '/pytest-cov/d' pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -x dev


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l rope


%check
%if v"0%{?python3_version}" >= v"3.13"
# Test failures with Python 3.13.3rc3
# https://github.com/python-rope/rope/issues/801
k="${k-}${k+ and }not (AutoImportTest and test_skipping_directories_not_accessible_because_of_permission_error)"
k="${k-}${k+ and }not (DocstringNoneAssignmentHintingTest and test_hint_parametrized_iterable)"
k="${k-}${k+ and }not (DocstringNoneAssignmentHintingTest and test_hint_parametrized_iterator)"
k="${k-}${k+ and }not (DocstringNotImplementedAssignmentHintingTest and test_hint_parametrized_iterable)"
k="${k-}${k+ and }not (DocstringNotImplementedAssignmentHintingTest and test_hint_parametrized_iterator)"
k="${k-}${k+ and }not (PEP0484CommentNoneAssignmentHintingTest and test_hint_parametrized_iterable)"
k="${k-}${k+ and }not (PEP0484CommentNoneAssignmentHintingTest and test_hint_parametrized_iterator)"
k="${k-}${k+ and }not (PEP0484CommentNotImplementedAssignmentHintingTest and test_hint_parametrized_iterable)"
k="${k-}${k+ and }not (PEP0484CommentNotImplementedAssignmentHintingTest and test_hint_parametrized_iterator)"
%endif
%pytest -v ${k+-k }"${k-}"


%files -n python3-rope -f %{pyproject_files}
%doc docs/README.md *.md


%files -n python-rope-doc
%doc docs/*.rst README.rst


%changelog
%autochangelog
