Summary:	LDP System Administrator's Guide
Summary(fr):	Guide de l'administrateur système du LDP
Summary(de):	LDP-System-Administrator-Handbuch
Summary(pl):	Podrêcznik Administratora Systemu LDP
Summary(tr):	DP Sistem Yöneticisi Kýlavuzu
Name:		sag
Version:	0.7
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://sunsite.unc.edu/LDP/%{name}.html.tar.gz
#Source0:	http://www.linuxdoc.org/LDP/%{name}-%{version}.html.tar.gz
URL:		http://www.linuxdoc.org/LDP/sag/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a generic guide to the System Administration of Linux systems.
Check http://www.linuxdoc.org/ for more information about the Linux
Documentation Project, and possible updates to this version.

%description -l fr
Guide générique pour l'administration système sous Linux. Consultez
http://www.linuxdoc.org/ pour plus d'informations sur le Projet de
Documentation Linux, et les éventuelles mises à jour de cette version.

%description -l de
Eine allgemeine Führung durch die Systemadministration von Linux-
Systemen. Für weitere Infos zum Linux Dokumentationsprojekt und für
mögliche Updates zu dieser Version besuchen Sie
http://www.linuxdoc.org/ .

%description -l pl
To jest ogólny przewodnik Administratora Systemu Linux. Wiêcej
informacji na temat Projektu Dokumentacji Linuxa (LDP) oraz
uaktualnienia tego dokumentu mo¿esz znale¼æ pod adresem
http://www.linuxdoc.org/ .

%description -l tr
Bu paket, Linux'da sistem yöneticiliðini anlatan rehberi içerir. LDP
(Linux Documentation Project) hakkýnda daha fazla bilgi ve olasý sürüm
deðiþiklikleri için http://www.linuxdoc.org/ sayfasýna bakýnýz.

%prep
#%setup -q -n %{name}-%{version}.html
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LDP/sag

cp -ar * $RPM_BUILD_ROOT%{_docdir}/LDP/sag

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LDP/sag
