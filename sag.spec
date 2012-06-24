Summary:	LDP System Administrator's Guide
Summary(de):	LDP-System-Administrator-Handbuch
Summary(fr):	Guide de l'administrateur syst�me du LDP
Summary(pl):	Podr�cznik Administratora Systemu LDP
Summary(tr):	DP Sistem Y�neticisi K�lavuzu
Name:		sag
Version:	0.9
Release:	2
License:	GFDL
Group:		Documentation
Source0:	http://www.tldp.org/LDP/sag/%{name}.html.tar.gz
# Source0-md5:	50bd18473819ccac5264955683cea1ab
URL:		http://www.tldp.org/LDP/sag/
Requires:	LDP-base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a generic guide to the System Administration of Linux systems.
Check http://www.tldp.org/ for more information about the Linux
Documentation Project, and possible updates to this version.

%description -l fr
Guide g�n�rique pour l'administration syst�me sous Linux. Consultez
http://www.tldp.org/ pour plus d'informations sur le Projet de
Documentation Linux, et les �ventuelles mises � jour de cette version.

%description -l de
Eine allgemeine F�hrung durch die Systemadministration von Linux-
Systemen. F�r weitere Infos zum Linux Dokumentationsprojekt und f�r
m�gliche Updates zu dieser Version besuchen Sie
<http://www.tldp.org/>.

%description -l pl
To jest og�lny przewodnik Administratora Systemu Linux. Wi�cej
informacji na temat Projektu Dokumentacji Linuksa (LDP) oraz
uaktualnienia tego dokumentu mo�esz znale�� pod adresem
<http://www.tldp.org/>.

%description -l tr
Bu paket, Linux'da sistem y�neticili�ini anlatan rehberi i�erir. LDP
(Linux Documentation Project) hakk�nda daha fazla bilgi ve olas� s�r�m
de�i�iklikleri i�in http://www.tldp.org/ sayfas�na bak�n�z.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LDP/sag
cp -a * $RPM_BUILD_ROOT%{_docdir}/LDP/sag

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LDP/sag
