#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-Listing
Version  : 6.14
Release  : 38
URL      : https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/File-Listing-6.14.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/File-Listing-6.14.tar.gz
Summary  : 'Parse directory listing'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-File-Listing-license = %{version}-%{release}
Requires: perl-File-Listing-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(HTTP::Date)

%description
NAME
File::Listing - Parse directory listing
VERSION
version 6.14
SYNOPSIS
use File::Listing qw(parse_dir);
$ENV{LANG} = "C";  # dates in non-English locales not supported
foreach my $file (parse_dir(`ls -l`)) {
my ($name, $type, $size, $mtime, $mode) = @$file;
next if $type ne 'f'; # plain file
#...
}

# directory listing can also be read from a file
open my $listing, "zcat ls-lR.gz|";
$dir = parse_dir($listing, '+0000');

%package dev
Summary: dev components for the perl-File-Listing package.
Group: Development
Provides: perl-File-Listing-devel = %{version}-%{release}
Requires: perl-File-Listing = %{version}-%{release}

%description dev
dev components for the perl-File-Listing package.


%package license
Summary: license components for the perl-File-Listing package.
Group: Default

%description license
license components for the perl-File-Listing package.


%package perl
Summary: perl components for the perl-File-Listing package.
Group: Default
Requires: perl-File-Listing = %{version}-%{release}

%description perl
perl components for the perl-File-Listing package.


%prep
%setup -q -n File-Listing-6.14
cd %{_builddir}/File-Listing-6.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-File-Listing
cp %{_builddir}/File-Listing-6.14/LICENSE %{buildroot}/usr/share/package-licenses/perl-File-Listing/03789e14d5943d4febabe7618ebbd4771f51b056
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/File::Listing.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-File-Listing/03789e14d5943d4febabe7618ebbd4771f51b056

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
