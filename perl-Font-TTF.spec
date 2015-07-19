%define upstream_name	 Font-TTF
%define upstream_version 1.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Perl module for TrueType Font hacking
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Font/Font-TTF-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(IO::String)
BuildArch:	noarch

%description
Perl module to manipulate TTF fonts, needed by perl-Text-PDF.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std
rm -f %{buildroot}%{perl_vendorlib}/Font/TTF/Win32.pm

%files
%doc README.TXT
%{_mandir}/*/*
%{perl_vendorlib}/Font/
%{perl_vendorlib}/ttfmod.pl


%changelog
* Fri Dec 17 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.480.0-1mdv2011.0
+ Revision: 622685
- update to new version 0.48

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.450.0-1mdv2011.0
+ Revision: 407750
- rebuild using %%perl_convert_version

* Fri Jun 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.45-1mdv2009.0
+ Revision: 218702
- update to new version 0.45

* Tue Jun 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.44-1mdv2009.0
+ Revision: 217451
- update to new version 0.44

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 23 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.43-1mdv2008.1
+ Revision: 111418
- update to new version 0.43

* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.42-1mdv2008.1
+ Revision: 109522
- new version

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 0.41-1mdv2008.0
+ Revision: 20095
- 0.41


* Sat Sep 02 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-09-02 14:43:14 (59602)
- 0.40

* Sat Sep 02 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 2006-09-02 14:39:28 (59601)
Import perl-Font-TTF

* Fri Mar 10 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.38.1-1mdk
- 0.38.1

* Mon Jan 30 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.37-1mdk
- 0.37

* Tue Jun 21 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.35-1mdk
- 0.35
- Cleanup spec

* Thu Dec 25 2003 Michael Scherer <misc@mandrake.org> 0.34-2mdk
- remove useless win32 files

* Thu Dec 25 2003 Michael Scherer <misc@mandrake.org> 0.34-1mdk 
- introdution in contrib.



