%define upstream_name	 Font-TTF
%define upstream_version 0.48

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl module for TrueType Font hacking
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Font/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
Perl module to manipulate TTF fonts, needed by perl-Text-PDF.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
