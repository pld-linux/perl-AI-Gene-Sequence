%include	/usr/lib/rpm/macros.perl
%define	pdir	AI
%define	pnam	Gene-Sequence
Summary:	A base class for storing and mutating genetic sequences
Summary(pl):	Klasa bazowa do przechowywania i mutowania sekwencji genetycznych
Name:		perl-%{pdir}-%{pnam}
Version:	0.21
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a class which provides generic methods for the creation and
mutation of genetic sequences.  Various mutations are provided as
is a way to ensure that genes created by mutations remain useful
(for instance, if a gene gives rise to code, it can be tested for
correct syntax).

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/AI/Gene
%{_mandir}/man3/*
