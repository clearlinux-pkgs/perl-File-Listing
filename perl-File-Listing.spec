#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-File-Listing
Version  : 6.04
Release  : 26
URL      : http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/File-Listing-6.04.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/G/GA/GAAS/File-Listing-6.04.tar.gz
Summary  : parse directory listing
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-File-Listing-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(HTTP::Date)

%description
NAME
File::Listing - parse directory listing
SYNOPSIS
use File::Listing qw(parse_dir);
$ENV{LANG} = "C";  # dates in non-English locales not supported
for (parse_dir(`ls -l`)) {
($name, $type, $size, $mtime, $mode) = @$_;
next if $type ne 'f'; # plain file
#...
}

%package dev
Summary: dev components for the perl-File-Listing package.
Group: Development
Provides: perl-File-Listing-devel = %{version}-%{release}
Requires: perl-File-Listing = %{version}-%{release}

%description dev
dev components for the perl-File-Listing package.


%package perl
Summary: perl components for the perl-File-Listing package.
Group: Default
Requires: perl-File-Listing = %{version}-%{release}

%description perl
perl components for the perl-File-Listing package.


%prep
%setup -q -n File-Listing-6.04
cd %{_builddir}/File-Listing-6.04

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

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.30.2/File/Listing.pm
