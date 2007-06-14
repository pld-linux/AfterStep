# TODO: what are man3 pages?
# if not API docs - shouldn't be in another section?
# if API docs - no devel files are installed (well, except perl, but AFAICS perl is not installed at all)
#
# Conditional build:
%bcond_with	mmx	# use MMX
#
%ifarch pentium3 pentium4 athlon %{x8664}
%define		with_mmx	1
%endif
Summary:	AfterStep Window Manager
Summary(ja.UTF-8):	AfterStep ウィンドウマネージャ (NeXT風)
Summary(pl.UTF-8):	AfterStep - zarządca okien
Name:		AfterStep
Version:	2.2.6
Release:	0.1
License:	GPL v2+
Vendor:		The AfterStep Team (see TEAM in docdir)
Group:		X11/Window Managers
Source0:	ftp://ftp.afterstep.org/stable/%{name}-%{version}.tar.bz2
# Source0-md5:	05dfcd730a49ac791a3361d71ae9d68f
#Source1:	%{name}.RunWM
Source3:	%{name}-xsession.desktop
Patch0:		%{name}-no_bash_fix.patch
Patch1:		%{name}-install_man.patch
Patch2:		%{name}-opt.patch
Patch3:		%{name}-link.patch
URL:		http://www.afterstep.org/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	giflib-devel
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	pkgconfig
BuildRequires:	sgml-tools
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
#Requires:	wmconfig >= 0.9.9-5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/wm-properties

%description
AfterStep is a continuation of the BowMan window manager which was
originally put together by Bo Yang. BowMan was based on the fvwm
window manager, written by Robert Nation. Fvwm was based on code from
twm. And so on... It was originally designed to emulate some of the
look and feel of the NEXTSTEP user interface, but has since taken
steps towards adding more useful, requested, and neat features
especially in 1.4 version! The changes which comprise AfterStep's
personality were originally part of BowMan development, but due to a
desire to move past simple emulation and into a niche as its own
valuable window manager, AfterStep designers decided to change the
project name and move on.

Important features of AfterStep include:
- 1. Wharf: a free-floating application loader which can "Swallow"
  running programs and also can contain "Folders" of more
  applications.
- 2. Gradient filled TitleBars with 5 button: help/zap, action/tasks,
  iconize/maximise, shade/stick & close/destroy buttons
- 3. Gradient filled root window PopUp menus which can be configured
  to accomodate different tastes and styles of management
- 4. NEXTSTEP style icons which give a consistent look to the entire
  desktop
- 5. Pixmapped Pager with desktop pixmmaping
- 6. Easy to use look files, to share you desktop appearance with your
  friends
- 7. Start menu entries in a hierarchy of directories
- 8. WinList: a tasklist which can be horizontal or vertical
- 9. Many modules & asapps to give a good look to your X window
  station

%description -l pl.UTF-8
AfterStep jest kontynuacją zarządcy okienek o nazwie BowMan, który
został opracowany przez Bo Yanga. BowMan bazował na innym zarządcy
okien o nazwie fvwm napisanym przez Roberta Nationa, a sam fvwm
bazował na kodzie źródłowym zarządcy okien twm. I tak dalej...
AfterStep początkowo miał imitować część zachowania interfejsu
użytkownika NEXTSTEP, ale potem rozwinął się w kierunku dodawania
bardziej przydatnych, pożądanych i przyjemnych możliwości, szczególnie
w wersji 1.4. Zmiany obejmujące osobowość AfterStepa były początkowo
częścią rozwoju BowMana, ale ze względu na chęć wykroczenia poza
prostą imitację do niszy samodzielnego wartościowego zarządcy okien,
projektanci AfterStepa zdecydowali się zmienić nazwę.

Najważniejsze cechy AfterStepa obejmują:
- 1. Dok - obiekt do ładowania aplikacji mogący "połykać" uruchomione
  programy i zawierać "foldery" większej liczby aplikacji
- 2. Wypełnione gradientem paski tytułowe z 5 przyciskami:
  pomoc/zabicie, akcja/zadania, ikona/maksymalizacja,
  cień/przyklejenie oraz zamknięcie/zniszczenie
- 3. Wypełnione gradientem wyskakujące menu w głównym oknie,
  konfigurowalne aby sprostać różnym smakom i stylom zarządzania
- 4. Ikony w stylu NEXTSTEPA dające spójny wygląd całego pulpitu
- 5. Pager z pixmapami pulpitu
- 6. Łatwe w użyciu pliki wyglądu, dzięki którym można dzielić wygląd
  pulpitu z kolegami
- 7. Wpisy menu Start o hierarchii katalogowej
- 8. WinList - pozioma lub pionowa lista zadań
- 9. Wiele modułów i aplikacji AfterStepa (asapps) dających dobry
  wygląd stacji X Window

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

cp -f autoconf/configure*.in .

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
cd libAfterBase
%{__autoconf}
%{__autoheader}
cd ../libAfterImage
%{__autoconf}
%{__autoheader}
cd ..
%configure \
	%{!?with_mmx:--disable-mmx-optimization} \
	--enable-i18n \
	--enable-sharedlibs \
	--with-gif \
	--with-helpcommand="xterm -e man" \
	--with-jpeg \
	--with-png \
	--with-xpm

%{__make}
sgml2html doc/afterstep.sgml

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_wmpropsdir},%{_datadir}/xsessions,/etc/sysconfig/wmstyle}

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT

install AfterStep.desktop $RPM_BUILD_ROOT%{_wmpropsdir}

#install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/afterstep.sh
install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/xsessions/AfterStep.desktop

rm -f $RPM_BUILD_ROOT%{_bindir}/{sessreg,xpmroot}
rm -rf $RPM_BUILD_ROOT%{_datadir}/afterstep/doc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/code doc/languages TODO *.html
%doc UPGRADE NEW README TEAM README.RedHat doc/languages/*
#%attr(755,root,root) /etc/sysconfig/wmstyle/*.sh
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libAfter*.so.*.*
%{_wmpropsdir}/AfterStep.desktop
%{_datadir}/afterstep
%{_datadir}/xsessions/AfterStep.desktop
%{_mandir}/man1/*
# ???
#%%{_mandir}/man3/*
