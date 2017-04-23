#
# Conditional build:
%bcond_with	mmx		# use MMX
%bcond_with	gnome2		# build with support for GNOME2 wm-properties
#
%ifarch pentium3 pentium4 athlon %{x8664}
%define		with_mmx	1
%endif
# versions from libAfter{Base,Image}/configure.in respectively
%define	afterbase_ver	1.14
%define	afterimage_ver	1.20
Summary:	AfterStep Window Manager
Summary(ja.UTF-8):	AfterStep ウィンドウマネージャ (NeXT風)
Summary(pl.UTF-8):	AfterStep - zarządca okien
Name:		AfterStep
Version:	2.2.11
Release:	1
License:	GPL v2+
Group:		X11/Window Managers
Source0:	ftp://ftp.afterstep.org/stable/%{name}-%{version}.tar.bz2
# Source0-md5:	dbedd3dd4cd6bad56edcab4ee6fb4de8
#Source1:	%{name}.RunWM
Source3:	%{name}-xsession.desktop
Patch0:		%{name}-no_bash_fix.patch
Patch1:		%{name}-ldconfig.patch
Patch2:		%{name}-opt.patch
Patch3:		%{name}-link.patch
Patch4:		%{name}-libpng-1.5.patch
Patch5:		%{name}-inline.patch
URL:		http://www.afterstep.org/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	fltk-devel
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	giflib-devel
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librsvg-devel
BuildRequires:	libtiff-devel
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	sgml-tools
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXinerama-devel
Requires:	libAfterBase = %{afterbase_ver}-%{release}
Requires:	libAfterImage = %{afterimage_ver}-%{release}
#Requires:	wmconfig >= 0.9.9-5
Conflicts:	filesystem < 3.0-20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/gnome/wm-properties

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

%package devel
Summary:	Development files for AfterStep libraries
Summary(pl.UTF-8):	Pliki programistyczne bibliotek AfterStepa
Group:		Development/Libraries
Requires:	libAfterBase-devel = %{afterbase_ver}-%{release}
Requires:	libAfterImage-devel = %{afterimage_ver}-%{release}
# doesn't require main

%description devel
Header files together with miscellaneous AfterStep static libraries:
libASGTK, libAfterConf, libAfterStep.

%description devel -l pl.UTF-8
Pliki nagłówkowe oraz różne statyczne biblioteki AfterStepa:
libASGTK, libAfterConf, libAfterStep.

%package -n libAfterBase
Summary:	AfterStep base functions library
Summary(pl.UTF-8):	Biblioteka podstawowych funkcji AfterStepa
Version:	%{afterbase_ver}
Group:		Libraries
Conflicts:	AfterStep < 2.2.11-0.3

%description -n libAfterBase
AfterStep base functions library.

%description -n libAfterBase -l pl.UTF-8
Biblioteka podstawowych funkcji AfterStepa.

%package -n libAfterBase-devel
Summary:	Header files for AfterBase library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AfterBase
Version:	%{afterbase_ver}
Group:		Development/Libraries
Requires:	libAfterBase = %{afterbase_ver}-%{release}
Requires:	xorg-lib-libX11-devel

%description -n libAfterBase-devel
Header files for AfterBase library.

%description -n libAfterBase-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AfterBase.

%package -n libAfterBase-static
Summary:	Static AfterBase library
Summary(pl.UTF-8):	Statyczna biblioteka AfterBase
Version:	%{afterbase_ver}
Group:		Development/Libraries
Requires:	libAfterBase-devel = %{afterbase_ver}-%{release}

%description -n libAfterBase-static
Static AfterBase library.

%description -n libAfterBase-static -l pl.UTF-8
Statyczna biblioteka AfterBase.

%package -n libAfterImage
Summary:	AfterStep image functions library
Summary(pl.UTF-8):	Biblioteka graficznych funkcji AfterStepa
Version:	%{afterimage_ver}
Group:		Libraries
Requires:	libAfterBase = %{afterbase_ver}-%{release}

%description -n libAfterImage
AfterStep image functions library.

%description -n libAfterImage -l pl.UTF-8
Biblioteka graficznych funkcji AfterStepa.

%package -n libAfterImage-devel
Summary:	Header files for AfterImage library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AfterImage
Version:	%{afterimage_ver}
Group:		Development/Libraries
Requires:	libAfterBase-devel = %{afterbase_ver}-%{release}
Requires:	libAfterImage = %{afterimage_ver}-%{release}
Requires:	freetype-devel >= 2.0
Requires:	gdk-pixbuf2-devel >= 2.0
Requires:	giflib-devel
Requires:	libjpeg-devel
Requires:	libpng-devel
Requires:	librsvg-devel
Requires:	libtiff-devel
Requires:	xorg-lib-libXext-devel

%description -n libAfterImage-devel
Header files for AfterImage library.

%description -n libAfterImage-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AfterImage.

%package -n libAfterImage-static
Summary:	Static AfterImage library
Summary(pl.UTF-8):	Statyczna biblioteka AfterImage
Version:	%{afterimage_ver}
Group:		Development/Libraries
Requires:	libAfterImage-devel = %{afterimage_ver}-%{release}

%description -n libAfterImage-static
Static AfterImage library.

%description -n libAfterImage-static -l pl.UTF-8
Statyczna biblioteka AfterImage.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

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

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%{?with_gnome2:install AfterStep.desktop $RPM_BUILD_ROOT%{_wmpropsdir}}

#install %{SOURCE1} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/afterstep.sh
install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/xsessions/AfterStep.desktop

# demo programs source and comments don't belong to man3 (and mans in general)
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man3/{asflip,asgrad,asmerge,asscale,astext,astile,asview,common}.*

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/afterstep/doc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n libAfterBase -p /sbin/ldconfig
%postun	-n libAfterBase -p /sbin/ldconfig

%post	-n libAfterImage -p /sbin/ldconfig
%postun	-n libAfterImage -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/code doc/languages TODO *.html
%doc UPGRADE NEW README TEAM README.RedHat doc/languages/*
%attr(755,root,root) %{_bindir}/ASFileBrowser
%attr(755,root,root) %{_bindir}/ASRun
%attr(755,root,root) %{_bindir}/ASWallpaper
%attr(755,root,root) %{_bindir}/Animate
%attr(755,root,root) %{_bindir}/Arrange
%attr(755,root,root) %{_bindir}/Banner
%attr(755,root,root) %{_bindir}/GWCommand
%attr(755,root,root) %{_bindir}/Ident
%attr(755,root,root) %{_bindir}/MonitorWharf
%attr(755,root,root) %{_bindir}/Pager
%attr(755,root,root) %{_bindir}/PrintDesktopEntries
%attr(755,root,root) %{_bindir}/Wharf
%attr(755,root,root) %{_bindir}/WinCommand
%attr(755,root,root) %{_bindir}/WinList
%attr(755,root,root) %{_bindir}/WinTabs
%attr(755,root,root) %{_bindir}/Xpm2Jpg
%attr(755,root,root) %{_bindir}/afterstep
%attr(755,root,root) %{_bindir}/afterstepdoc
%attr(755,root,root) %{_bindir}/ascolor
%attr(755,root,root) %{_bindir}/ascommand.pl
%attr(755,root,root) %{_bindir}/importasmenu
%attr(755,root,root) %{_bindir}/installastheme.pl
%attr(755,root,root) %{_bindir}/makeastheme.pl
%attr(755,root,root) %{_bindir}/postcard.sh
%{?with_gnome2:%{_wmpropsdir}/AfterStep.desktop}
#%attr(755,root,root) /etc/sysconfig/wmstyle/*.sh
%{_datadir}/afterstep
%{_datadir}/xsessions/AfterStep.desktop
%{_mandir}/man1/ASDatabase.1x*
%{_mandir}/man1/ASDatabaseEntry.1x*
%{_mandir}/man1/AfterStep.1x*
%{_mandir}/man1/Align.1x*
%{_mandir}/man1/Animate.1x*
%{_mandir}/man1/AnimateTypes.1x*
%{_mandir}/man1/Arrange.1x*
%{_mandir}/man1/AutoExec.1x*
%{_mandir}/man1/BalloonContents.1x*
%{_mandir}/man1/Base.1x*
%{_mandir}/man1/Bevel.1x*
%{_mandir}/man1/ColorScheme.1x*
%{_mandir}/man1/Feel.1x*
%{_mandir}/man1/FeelWindowBox.1x*
%{_mandir}/man1/Functions.1x*
%{_mandir}/man1/Gravity.1x*
%{_mandir}/man1/Look.1x*
%{_mandir}/man1/MyBackground.1x*
%{_mandir}/man1/MyFrame.1x*
%{_mandir}/man1/MyStyle.1x*
%{_mandir}/man1/Pager.1x*
%{_mandir}/man1/PagerDecorations.1x*
%{_mandir}/man1/Placement.1x*
%{_mandir}/man1/Sound.1x*
%{_mandir}/man1/SoundEvents.1x*
%{_mandir}/man1/SupportedHints.1x*
%{_mandir}/man1/TbarLayout.1x*
%{_mandir}/man1/Wharf.1x*
%{_mandir}/man1/WharfFolders.1x*
%{_mandir}/man1/WharfSounds.1x*
%{_mandir}/man1/WinCommand.1x*
%{_mandir}/man1/WinList.1x*
%{_mandir}/man1/WinTabs.1x*
%{_mandir}/man1/afterstep_faq.1x*
%{_mandir}/man1/asimagexml.1x*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/afterstep-config
%attr(755,root,root) %{_bindir}/asgtk-config
%{_libdir}/libASGTK.a
%{_libdir}/libAfterConf.a
%{_libdir}/libAfterStep.a
%{_includedir}/libASGTK
%{_includedir}/libAfterConf
%{_includedir}/libAfterStep

%files -n libAfterBase
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libAfterBase.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libAfterBase.so.0

%files -n libAfterBase-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libAfterBase.so
%{_includedir}/libAfterBase

%files -n libAfterBase-static
%defattr(644,root,root,755)
%{_libdir}/libAfterBase.a

%files -n libAfterImage
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ascheckttf
%attr(755,root,root) %{_bindir}/ascompose
%attr(755,root,root) %{_bindir}/asflip
%attr(755,root,root) %{_bindir}/asgrad
%attr(755,root,root) %{_bindir}/asi18n
%attr(755,root,root) %{_bindir}/asmerge
%attr(755,root,root) %{_bindir}/asscale
%attr(755,root,root) %{_bindir}/astext
%attr(755,root,root) %{_bindir}/astile
%attr(755,root,root) %{_bindir}/asvector
%attr(755,root,root) %{_bindir}/asview
%attr(755,root,root) %{_libdir}/libAfterImage.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libAfterImage.so.0

%files -n libAfterImage-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/afterimage-config
%attr(755,root,root) %{_bindir}/afterimage-libs
%attr(755,root,root) %{_libdir}/libAfterImage.so
%{_includedir}/libAfterImage
%{_mandir}/man3/afterimage.3x*
%{_mandir}/man3/ascmap.3x*
%{_mandir}/man3/ascompose.3x*
%{_mandir}/man3/asfont.3x*
%{_mandir}/man3/asimage.3x*
%{_mandir}/man3/asimagexml.3x*
%{_mandir}/man3/asvisual.3x*
%{_mandir}/man3/blender.3x*
%{_mandir}/man3/char2uni.3x*
%{_mandir}/man3/export.3x*
%{_mandir}/man3/imencdec.3x*
%{_mandir}/man3/import.3x*
%{_mandir}/man3/transform.3x*
%{_mandir}/man3/ximage.3x*

%files -n libAfterImage-static
%defattr(644,root,root,755)
%{_libdir}/libAfterImage.a
