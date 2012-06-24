Summary:	LDP System Administrator's Guide
Summary(fr):	Guide de l'administrateur syst�me du LDP
Summary(de):	LDP-System-Administrator-Handbuch 
Summary(pl):	Podr�cznik Administratora Systemu LDP
Summary(tr):	DP Sistem Y�neticisi K�lavuzu
Name:		sag
Version:	0.5
Release:	4
Group:		Documentation
Group(pl):	Dokumentacja
Source:		http://sunsite.unc.edu/LDP/sag-0.5.html.tar.gz
Copyright:	distributable
BuildArch:	noarch
Buildroot:	/tmp/%{name}-%{version}-root

%description
This is a generic guide to the System Administration of Linux systems.
Check http://sunsite.unc.edu/LDP for more information about the
Linux Documentation Project, and possible updates to this version.

%description -l fr
Guide g�n�rique pour l'administration syst�me sous Linux. Consultez
http://sunsite.unc.edu/LDP pour plus d'informations sur le Projet de
Documentation Linux, et les �ventuelles mises � jour de cette version.

%description -l de
Eine allgemeine F�hrung durch die Systemadministration von Linux-
Systemen. F�r weitere Infos zum Linux Dokumentationsprojekt und f�r 
m�gliche Updates zu dieser Version besuchen Sie http://sunsite.unc.edu/LDP.

%description -l pl
To jest og�lny przewodnik Administratora Systemu Linux. Wi�cej informacji
na temat Projektu Dokumentacji Linuxa (LDP) oraz uaktualnienia tego dokumentu
mo�esz znale�� pod adresem http://sunsite.unc.edu/LDP.

%description -l tr
Bu paket, Linux'da sistem y�neticili�ini anlatan rehberi i�erir. LDP (Linux
Documentation Project) hakk�nda daha fazla bilgi ve olas� s�r�m de�i�iklikleri
i�in http://sunsite.unc.edu/LDP sayfas�na bak�n�z.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/doc/LDP/sag

cp -ar * $RPM_BUILD_ROOT/usr/doc/LDP/sag

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)

/usr/doc/LDP/sag

%changelog
* Mon Feb  8 1999 Micha� Kuratczyk <kurkens@polbox.com>
  [0.5-4]
- sloted BuildRoot into PLD standard
- simplification in %files

* Sat Feb  6 1999 Micha� Kuratczyk <kurkens@polbox.com>
  [0.5-3]
- added pl translations
- replaced "mkdir -p" with "install -d"
- rewrote %files section
- changed BuildRoot
- simplification in %install
- moved %changelog to the end of spec
- cosmetic changes

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 24 1997 Otto Hammersmith <otto@redhat.com>
- created the package
