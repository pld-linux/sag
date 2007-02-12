Summary:	LDP System Administrator's Guide
Summary(de.UTF-8):   LDP-System-Administrator-Handbuch
Summary(fr.UTF-8):   Guide de l'administrateur système du LDP
Summary(pl.UTF-8):   Podręcznik Administratora Systemu LDP
Summary(tr.UTF-8):   DP Sistem Yöneticisi Kılavuzu
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

%description -l fr.UTF-8
Guide générique pour l'administration système sous Linux. Consultez
http://www.tldp.org/ pour plus d'informations sur le Projet de
Documentation Linux, et les éventuelles mises à jour de cette version.

%description -l de.UTF-8
Eine allgemeine Führung durch die Systemadministration von Linux-
Systemen. Für weitere Infos zum Linux Dokumentationsprojekt und für
mögliche Updates zu dieser Version besuchen Sie
<http://www.tldp.org/>.

%description -l pl.UTF-8
To jest ogólny przewodnik Administratora Systemu Linux. Więcej
informacji na temat Projektu Dokumentacji Linuksa (LDP) oraz
uaktualnienia tego dokumentu możesz znaleźć pod adresem
<http://www.tldp.org/>.

%description -l tr.UTF-8
Bu paket, Linux'da sistem yöneticiliğini anlatan rehberi içerir. LDP
(Linux Documentation Project) hakkında daha fazla bilgi ve olası sürüm
değişiklikleri için http://www.tldp.org/ sayfasına bakınız.

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
