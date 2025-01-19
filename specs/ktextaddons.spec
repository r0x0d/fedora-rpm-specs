# EPEL10 does not have kf5
%if 0%{?rhel} && 0%{?rhel} >= 10
%bcond_with kf5
%else
%bcond_without kf5
%endif

Name:          ktextaddons
Version:       1.5.4
Release:       3%{?dist}
Summary:       Various text handling addons

License:       CC0-1.0 AND LGPL-2.0-or-later AND GPL-2.0-or-later AND BSD-3-Clause

URL:           https://invent.kde.org/libraries/%{name}

Source0:       http://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules


BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Keychain)
BuildRequires: cmake(Qt6TextToSpeech)
BuildRequires: cmake(Qt6UiPlugin)

BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6SyntaxHighlighting)

%if %{with kf5}
BuildRequires: kf5-rpm-macros

BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Keychain)
BuildRequires: cmake(Qt5TextToSpeech)
BuildRequires: cmake(Qt5UiPlugin)

BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5Sonnet)
BuildRequires: cmake(KF5SyntaxHighlighting)
%endif


%description
%{summary}.


%if %{with kf5}
%package        qt5
Obsoletes:      ktextaddons < 1.5.2
Provides:       ktextaddons = %{version}-%{release}
Summary:        Qt5 libraries for %{name}
Requires:       %{name}-common = %{version}-%{release}
%description    qt5
%{summary}.

%package        qt5-devel
Summary:        Development files for %{name}
Obsoletes:      ktextaddons-devel < 1.5.2
Provides:       ktextaddons-devel = %{version}-%{release}
%description    qt5-devel
%{summary}.
%endif

%package        qt6
Summary:        Qt6 libraries for %{name}
Requires:       %{name}-common = %{version}-%{release}
%description    qt6
%{summary}.

%package        qt6-devel
Summary:        Development files for %{name}
%description    qt6-devel
%{summary}.

%package        qt6-doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    qt6-doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%package        common
Summary:        Translations and documents for %{name}
Obsoletes:      ktextaddons-docs < 1.5.3-1
BuildArch:      noarch
%description    common
%{summary}.

%prep
%autosetup -p1


%build
mkdir %{name}_qt6
pushd %{name}_qt6
%cmake_kf6 -S .. -DQT_MAJOR_VERSION=6
%cmake_build
popd

%if %{with kf5}
mkdir %{name}_qt5
pushd %{name}_qt5
%cmake_kf5 -DQT_MAJOR_VERSION=5 -S ..
%cmake_build
popd
%endif



%install
pushd %{name}_qt6
%cmake_install
popd
%if %{with kf5}
pushd %{name}_qt5
%cmake_install
popd
%endif

%find_lang %{name} --all-name


%if %{with kf5}
%files qt5
%license LICENSES/
%{_kf5_libdir}/libKF5TextAddonsWidgets.so.1
%{_kf5_libdir}/libKF5TextAddonsWidgets.so.%{version}
%{_kf5_libdir}/libKF5TextAutoCorrectionCore.so.1
%{_kf5_libdir}/libKF5TextAutoCorrectionCore.so.%{version}
%{_kf5_libdir}/libKF5TextAutoCorrectionWidgets.so.1
%{_kf5_libdir}/libKF5TextAutoCorrectionWidgets.so.%{version}
%{_kf5_libdir}/libKF5TextCustomEditor.so.1
%{_kf5_libdir}/libKF5TextCustomEditor.so.%{version}
%{_kf5_libdir}/libKF5TextEmoticonsCore.so.1
%{_kf5_libdir}/libKF5TextEmoticonsCore.so.%{version}
%{_kf5_libdir}/libKF5TextEmoticonsWidgets.so.1
%{_kf5_libdir}/libKF5TextEmoticonsWidgets.so.%{version}
%{_kf5_libdir}/libKF5TextEditTextToSpeech.so.1
%{_kf5_libdir}/libKF5TextEditTextToSpeech.so.%{version}
%{_kf5_libdir}/libKF5TextGrammarCheck.so.1
%{_kf5_libdir}/libKF5TextGrammarCheck.so.%{version}
%{_kf5_libdir}/libKF5TextTranslator.so.1
%{_kf5_libdir}/libKF5TextTranslator.so.%{version}
%{_kf5_libdir}/libKF5TextUtils.so.1
%{_kf5_libdir}/libKF5TextUtils.so.%{version}
%{_kf5_plugindir}/translator/translator_bing.so
%{_kf5_plugindir}/translator/translator_deepl.so
%{_kf5_plugindir}/translator/translator_google.so
%{_kf5_plugindir}/translator/translator_libretranslate.so
%{_kf5_plugindir}/translator/translator_lingva.so
%{_kf5_plugindir}/translator/translator_yandex.so
%{_kf5_datadir}/qlogging-categories5/ktextaddons.categories
%{_kf5_datadir}/qlogging-categories5/ktextaddons.renamecategories

%files qt5-devel
%{_kf5_includedir}/TextAddonsWidgets/
%{_kf5_includedir}/TextAutoCorrectionCore/
%{_kf5_includedir}/TextAutoCorrectionWidgets/
%{_kf5_includedir}/TextCustomEditor/
%{_kf5_includedir}/TextEditTextToSpeech/
%{_kf5_includedir}/TextEmoticonsCore/
%{_kf5_includedir}/TextEmoticonsWidgets/
%{_kf5_includedir}/TextGrammarCheck/
%{_kf5_includedir}/TextTranslator/
%{_kf5_includedir}/TextUtils/
%{_kf5_libdir}/libKF5TextAddonsWidgets.so
%{_kf5_libdir}/libKF5TextAutoCorrectionCore.so
%{_kf5_libdir}/libKF5TextAutoCorrectionWidgets.so
%{_kf5_libdir}/libKF5TextCustomEditor.so
%{_kf5_libdir}/libKF5TextEditTextToSpeech.so
%{_kf5_libdir}/libKF5TextEmoticonsCore.so
%{_kf5_libdir}/libKF5TextEmoticonsWidgets.so
%{_kf5_libdir}/libKF5TextGrammarCheck.so
%{_kf5_libdir}/libKF5TextTranslator.so
%{_kf5_libdir}/libKF5TextUtils.so
%{_kf5_libdir}/cmake/KF5TextAddonsWidgets/
%{_kf5_libdir}/cmake/KF5TextAutoCorrectionCore/
%{_kf5_libdir}/cmake/KF5TextAutoCorrectionWidgets/
%{_kf5_libdir}/cmake/KF5TextCustomEditor/
%{_kf5_libdir}/cmake/KF5TextEmoticonsCore/
%{_kf5_libdir}/cmake/KF5TextEmoticonsWidgets/
%{_kf5_libdir}/cmake/KF5TextEditTextToSpeech/
%{_kf5_libdir}/cmake/KF5TextGrammarCheck/
%{_kf5_libdir}/cmake/KF5TextTranslator/
%{_kf5_libdir}/cmake/KF5TextUtils/
%{_kf5_qtplugindir}/designer/textcustomeditor.so
%{_kf5_qtplugindir}/designer/texttranslatorwidgets5.so
%endif

%files qt6
%license LICENSES/
%{_kf6_libdir}/libKF6TextAddonsWidgets.so.1
%{_kf6_libdir}/libKF6TextAddonsWidgets.so.%{version}
%{_kf6_libdir}/libKF6TextAutoCorrectionCore.so.1
%{_kf6_libdir}/libKF6TextAutoCorrectionCore.so.%{version}
%{_kf6_libdir}/libKF6TextAutoCorrectionWidgets.so.1
%{_kf6_libdir}/libKF6TextAutoCorrectionWidgets.so.%{version}
%{_kf6_libdir}/libKF6TextCustomEditor.so.1
%{_kf6_libdir}/libKF6TextCustomEditor.so.%{version}
%{_kf6_libdir}/libKF6TextEmoticonsCore.so.1
%{_kf6_libdir}/libKF6TextEmoticonsCore.so.%{version}
%{_kf6_libdir}/libKF6TextEmoticonsWidgets.so.1
%{_kf6_libdir}/libKF6TextEmoticonsWidgets.so.%{version}
%{_kf6_libdir}/libKF6TextEditTextToSpeech.so.1
%{_kf6_libdir}/libKF6TextEditTextToSpeech.so.%{version}
%{_kf6_libdir}/libKF6TextGrammarCheck.so.1
%{_kf6_libdir}/libKF6TextGrammarCheck.so.%{version}
%{_kf6_libdir}/libKF6TextTranslator.so.1
%{_kf6_libdir}/libKF6TextTranslator.so.%{version}
%{_kf6_libdir}/libKF6TextUtils.so.1
%{_kf6_libdir}/libKF6TextUtils.so.%{version}
%{_kf6_plugindir}/translator/translator_bing.so
%{_kf6_plugindir}/translator/translator_deepl.so
%{_kf6_plugindir}/translator/translator_google.so
%{_kf6_plugindir}/translator/translator_libretranslate.so
%{_kf6_plugindir}/translator/translator_lingva.so
%{_kf6_plugindir}/translator/translator_yandex.so
%{_kf6_datadir}/qlogging-categories6/ktextaddons.categories
%{_kf6_datadir}/qlogging-categories6/ktextaddons.renamecategories


%files qt6-devel
%{_kf6_includedir}/TextAddonsWidgets/
%{_kf6_includedir}/TextAutoCorrectionCore/
%{_kf6_includedir}/TextAutoCorrectionWidgets/
%{_kf6_includedir}/TextCustomEditor/
%{_kf6_includedir}/TextEditTextToSpeech/
%{_kf6_includedir}/TextEmoticonsCore/
%{_kf6_includedir}/TextEmoticonsWidgets/
%{_kf6_includedir}/TextGrammarCheck/
%{_kf6_includedir}/TextTranslator/
%{_kf6_includedir}/TextUtils/
%{_kf6_libdir}/libKF6TextAddonsWidgets.so
%{_kf6_libdir}/libKF6TextAutoCorrectionCore.so
%{_kf6_libdir}/libKF6TextAutoCorrectionWidgets.so
%{_kf6_libdir}/libKF6TextCustomEditor.so
%{_kf6_libdir}/libKF6TextEditTextToSpeech.so
%{_kf6_libdir}/libKF6TextEmoticonsCore.so
%{_kf6_libdir}/libKF6TextEmoticonsWidgets.so
%{_kf6_libdir}/libKF6TextGrammarCheck.so
%{_kf6_libdir}/libKF6TextTranslator.so
%{_kf6_libdir}/libKF6TextUtils.so
%{_kf6_libdir}/cmake/KF6TextAddonsWidgets/
%{_kf6_libdir}/cmake/KF6TextAutoCorrectionCore/
%{_kf6_libdir}/cmake/KF6TextAutoCorrectionWidgets/
%{_kf6_libdir}/cmake/KF6TextCustomEditor/
%{_kf6_libdir}/cmake/KF6TextEmoticonsCore/
%{_kf6_libdir}/cmake/KF6TextEmoticonsWidgets/
%{_kf6_libdir}/cmake/KF6TextEditTextToSpeech/
%{_kf6_libdir}/cmake/KF6TextGrammarCheck/
%{_kf6_libdir}/cmake/KF6TextTranslator/
%{_kf6_libdir}/cmake/KF6TextUtils/
%{_kf6_qtplugindir}/designer/textcustomeditor.so
%{_kf6_qtplugindir}/designer/texttranslatorwidgets6.so
%{_qt6_docdir}/*.tags

%files qt6-doc
%{_qt6_docdir}/*.qch

%files common -f %{name}.lang
%doc README.md

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Mar 28 2024 Marie Loise Nolden <loise@kde.org> - 1.5.4-1
- update to 1.5.4

* Sun Mar 10 2024 Marie Loise Nolden <loise@kde.org> - 1.5.3-5
- add missing BuildArch: noarch to -qt6-doc package

* Sun Mar 3 2024 Marie Loise Nolden <loise@kde.org> - 1.5.3-4
- move qt designer plugin to -devel (qt5 and qt6)

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 11 2024 Alessandro Astone <ales.astone@gmail.com> - 1.5.3-1
- 1.5.3
- Rename "docs" subpackage to "common", as it doesn't make sense to have string translations in "docs"
- Add qt6-doc subpackage for KF6 API

* Tue Dec 5 2023 Steve Cossette <farchord@gmail.com> - 1.5.2-1
- 1.5.2

* Sun Sep 24 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1.5.1-1
- Update to 1.5.1

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon May 08 2023 Kevin Kofler <Kevin@tigcc.ticalc.org> - 1.1.1-2
- Add missing BuildRequires: cmake(Qt5TextToSpeech)

* Fri Mar 24 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1.1.1-1
- Update to version 1.1.1

* Tue Mar 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1.1.0-5
- Use proper license field

* Tue Mar 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1.1.0-4
- Add license and doc files

* Tue Mar 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1.1.0-3
- Add BuildRequires: cmake

* Tue Mar 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1.1.0-2
- Move header files to the devel subpackage

* Tue Mar 21 2023 Marc Deop i Argemí <marcdeop@fedoraproject.org> - 1.1.0-1
- Initial release
