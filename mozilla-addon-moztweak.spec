#
# TODO: check some "Preferences" problems related to this addon
#
Summary:	Mozilla tweaks
Summary(pl):	Modu³ do zmiany wielu parametrów mozilli
Name:		mozilla-addon-moztweak
%define		_realname	moztweak
Version:	1.2.2
Release:	5
License:	MPL
Group:		X11/Applications/Networking
Source0:	%{_realname}.jar
# Source0-md5:	ddb8a929515b4f8feefeb3eb4a787bc3
Source1:	%{_realname}-installed-chrome.txt
Requires(post,postun):	mozilla >= 5:1.7.3-3
Requires(post,postun):	textutils
Requires:	mozilla >= 2:1.0-7
# Seems to fix the "Preferences" problems. Does moztweak use some Java
# classes from tabextensions ?
Requires:	mozilla-addon-tabextensions
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
Mozilla tweaks - a module that supports customization of many Mozilla
parameters that are accessible only through manual editing of
user.prefs and other configuration files. MozTweak allows to change
those parameters from a nice menu.

%description -l pl
Modu³ umo¿liwiaj±cy zmianê wielu parametrów mozilli, które normalnie
mo¿na ustawiaæ tylko poprzez rêczn± edycjê plików user.prefs i innych
plików konfiguracyjnych. MozTweak pozwala zmieniaæ te parametry za
pomoc± ³adnego menu.

%prep

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE0} $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/mozilla-chrome+xpcom-generate

%postun
%{_sbindir}/mozilla-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
