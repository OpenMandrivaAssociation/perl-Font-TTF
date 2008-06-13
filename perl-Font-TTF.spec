%define module	Font-TTF
%define name	perl-%{module}
%define version	0.45
%define release	%mkrel 1

Summary:	Perl module for TrueType Font hacking
Version:	%{version}
Name:		%{name}
Release:	%{release}
License:	Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/Font/%{module}-%{version}.tar.gz
BuildArch:	noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Perl module to manipulate TTF fonts, needed by perl-Text-PDF.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}/%{perl_vendorlib}/Font/TTF/Win32.pm

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.TXT
%{_mandir}/*/*
%{perl_vendorlib}/Font/
%{perl_vendorlib}/ttfmod.pl

