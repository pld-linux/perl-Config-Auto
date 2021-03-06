#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Config
%define		pnam	Auto
Summary:	Config::Auto - magical config file parser
Summary(pl.UTF-8):	Config::Auto - magiczny parser plików konfiguracyjnych
Name:		perl-Config-Auto
Version:	0.42
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Config/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	baa0907e5c79c0bf8c91cfe8b56577de
URL:		http://search.cpan.org/dist/Config-Auto/
%if %{with tests}
BuildRequires:	perl-Config-IniFiles
BuildRequires:	perl-IO-String
BuildRequires:	perl-YAML
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Magical config file parser.

%description -l pl.UTF-8
Magiczny parser plików konfiguracyjnych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL -x \
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
%doc Changes README
%{perl_vendorlib}/Config/Auto.pm
%{_mandir}/man3/*
