%define module	Font-TTF
%define name	perl-%{module}
%define version	0.40
%define tarversion  %version
%define release	%mkrel 1

Summary:	Font::TTF Perl module
Version:	%{version}
Name:		%{name}
Release:	%{release}
License:	Artistic
Group:		Development/Perl
Source0:	http://www.cpan.org/CPAN/authors/id/M/MH/MHOSKEN/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}/
BuildRoot:	%{_tmppath}/%name-%tarversion-buildroot
BuildArch:	noarch

%description
Perl module to manipulate TTF fonts, needed by perl-Text-PDF.

%prep
%setup -q -n %{module}-%{tarversion}
perl -pi -e 's/\cM//' README.TXT

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -f $RPM_BUILD_ROOT/%{perl_vendorlib}/Font/TTF/Win32.pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.TXT
%{_mandir}/*/*
%{perl_vendorlib}/Font/
%{perl_vendorlib}/ttfmod.pl

