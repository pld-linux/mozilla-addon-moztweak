Summary:	Mozilla tweaks
Summary(pl):	Modu� do zmiany wielu parametr�w mozilli
Name:		mozilla-addon-moztweak
%define		_realname	moztweak
Version:	1.0
Release:	2
License:	MPL
Group:		X11/Applications/Networking
Source0:	%{_realname}.jar
Source1:	%{_realname}-installed-chrome.txt
BuildArch:	noarch
Requires:	mozilla >= 1.0-7
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define         _chromedir      %{_libdir}/mozilla/chrome

%description
Mozilla tweaks - a module that supports customization of many Mozilla
parameters that are accessible only through manual editing of
user.prefs and other configuration files. MozTweak allows to change
those parameters from a nice menu.

%description -l pl
Modu� umo�liwiaj�cy zmian� wielu parametr�w mozilli, kt�re normalnie
mo�na ustawia� tylko poprzez r�czn� edycj� plik�w user.prefs i innych
plik�w konfiguracyjnych. MozTweak pozwala zmienia� te parametry za
pomoc� �adnego menu.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE0} $RPM_BUILD_ROOT%{_chromedir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%post
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
