Summary:	Pacman game for KDE
Summary(pl.UTF-8):	Gra pacman dla KDE
Name:		kpacman
Version:	0.3.2
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/kpacman/%{name}-%{version}.tar.gz
# Source0-md5:	4405bd9f7a78d005f8540c8d610eb188
Source1:	%{name}.desktop
Patch0:		%{name}-keys.patch
URL:		http://kpacman.sourceforge.net/
BuildRequires:	kdegames-devel
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kpacman is an implementation of the pacman game for KDE. Multiple game
modes/schemes are available, including Ms. Pacman. Sound is not yet
supported.

#% description -l pl.UTF-8

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
kde_htmldir="%{_kdedocdir}"; export kde_htmldir

%configure \
	--%{!?debug:dis}%{?debug:en}able-debug

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/kde/kpacman.desktop

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/apps/%{name}
%{_desktopdir}/kde/kpacman.desktop
%{_datadir}/config/kpacmanrc
%{_iconsdir}/*/*/*/*.png
