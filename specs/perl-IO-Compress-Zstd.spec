Name:           perl-IO-Compress-Zstd
Version:        2.213
Release:        1%{?dist}
Summary:        Write zstd files/buffers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/IO-Compress-Zstd/
Source0:        https://cpan.metacpan.org/authors/id/P/PM/PMQS/IO-Compress-Zstd-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(Compress::Stream::Zstd)
BuildRequires:  perl(Compress::Stream::Zstd::Compressor)
BuildRequires:  perl(Compress::Stream::Zstd::Decompressor)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Compress::Base::Common)
BuildRequires:  perl(IO::Compress::Base) >= %{version}
BuildRequires:  perl(IO::Compress::Zip)
BuildRequires:  perl(IO::Compress::Zip::Constants)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Uncompress::AnyUncompress)
BuildRequires:  perl(IO::Uncompress::Base) >= %{version}
BuildRequires:  perl(IO::Uncompress::Unzip)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::CPAN::Meta::JSON)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod) >= 1.00


%description
This module provides a Perl interface that allows writing zstd compressed
data to files or buffer.


%prep
%setup -q -n IO-Compress-Zstd-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}


%install
%{make_install}
%{_fixperms} %{buildroot}/*


%check
make test COMPRESS_ZLIB_RUN_ALL=1


%files
%doc Changes README
%{perl_vendorlib}/IO/
%{_mandir}/man3/IO::Compress::Zstd.3pm*
%{_mandir}/man3/IO::Uncompress::UnZstd.3pm*


%changelog
* Mon Sep 09 2024 Xavier Bachelot <xavier@bachelot.org> 2.213-1
- Update to 2.213 (RHBZ#2309074)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.212-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Apr 29 2024 Xavier Bachelot <xavier@bachelot.org> 2.212-1
- Update to 2.212 (RHBZ#2277507)

* Mon Apr 08 2024 Xavier Bachelot <xavier@bachelot.org> 2.211-1
- Update to 2.211 (RHBZ#2273779)

* Mon Feb 26 2024 Xavier Bachelot <xavier@bachelot.org> 2.207-1
- Update to 2.207 (RHBZ#2265223)
- Enable 106prime-zstd.t test

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.206-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.206-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 27 2023 Xavier Bachelot <xavier@bachelot.org> 2.206-1
- Update to 2.206 (RHBZ#2225677)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.205-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jul 17 2023 Xavier Bachelot <xavier@bachelot.org> 2.205-1
- Update to 2.205 (RHBZ#2223223)

* Mon Jun 05 2023 Xavier Bachelot <xavier@bachelot.org> 2.204-1
- Update to 2.204 (RHBZ#2168409)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.201-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.201-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.201-1
- 2.201 bump

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.103-2
- Perl 5.36 rebuild

* Mon May 09 2022 Jitka Plesnikova <jplesnik@redhat.com> - 2.103-1
- 2.103 bump

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.101-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Nov 16 2021 Xavier Bachelot <xavier@bachelot.org> 2.101-2
- Review fixes

* Thu Oct 07 2021 Xavier Bachelot <xavier@bachelot.org> 2.101-1
- Specfile autogenerated by cpanspec 1.78.