%include	/usr/lib/rpm/macros.perl
%define	pdir	AI
%define	pnam	Gene-Sequence
Summary:	A base class for storing and mutating genetic sequences
Summary(pl):	Klasa bazowa do przechowywania i mutowania sekwencji genetycznych
Name:		perl-%{pdir}-%{pnam}
Version:	0.21
Release:	4
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a class which provides generic methods for the creation and
mutation of genetic sequences.  Various mutations are provided as
is a way to ensure that genes created by mutations remain useful
(for instance, if a gene gives rise to code, it can be tested for
correct syntax).

%description -l pl
Ta klasa udostêpnia ogólne metody do tworzenia i mutacji sekwencji
genetycznych. Zawiera ró¿ne mutacje, aby zapewniæ, ¿e geny stworzone
przez mutacje pozostan± u¿yteczne (na przyk³ad, je¶li gen da przyrost
kodu, mo¿e byæ sprawdzona poprawno¶æ sk³adni).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
mkdir lib
mv AI lib

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"AI::Gene::Sequence")' \
	INSTALLDIRS=vendor
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/AI/Gene
%{_mandir}/man3/*
