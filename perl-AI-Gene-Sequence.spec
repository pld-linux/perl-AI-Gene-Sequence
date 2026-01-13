#
# Conditional build:
%bcond_without	tests	# don't perform "make test"

%define		pdir	AI
%define		pnam	Gene-Sequence
Summary:	A base class for storing and mutating genetic sequences
Summary(pl.UTF-8):	Klasa bazowa do przechowywania i mutowania sekwencji genetycznych
Name:		perl-AI-Gene-Sequence
Version:	0.22
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	82023860faf60163eaef71c8f9a3c592
URL:		http://search.cpan.org/dist/AI-Gene-Sequence/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a class which provides generic methods for the creation and
mutation of genetic sequences. Various mutations are provided as is a
way to ensure that genes created by mutations remain useful (for
instance, if a gene gives rise to code, it can be tested for correct
syntax).

%description -l pl.UTF-8
Ta klasa udostępnia ogólne metody do tworzenia i mutacji sekwencji
genetycznych. Zawiera różne mutacje, aby zapewnić, że geny stworzone
przez mutacje pozostaną użyteczne (na przykład, jeśli gen da przyrost
kodu, może być sprawdzona poprawność składni).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
mkdir lib
mv AI lib

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"AI::Gene::Sequence")' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/AI/Gene
%{_mandir}/man3/*
