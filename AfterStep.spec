Summary:	AfterStep Window Manager
Name:		AfterStep
Version:	1.7.111
Release:	1
Copyright:	GPL
Group:		X11/Window Managers
Group(pl):	X11/Zarz�dcy okien
Vendor:		The AfterStep Team (see TEAM in docdir)
Source:		ftp://ftp.afterstep.org/devel/snapshots/%{name}-%{version}.tar.bz2
Patch:		AfterStep-Wharf_maxsize.patch
URL:		http://www.afterstep.org/
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix	/usr/X11R6
%define		_mandir	/usr/X11R6/man

%description
AfterStep is a continuation of the BowMan window manager which was
originally put together by Bo Yang. BowMan was based on the fvwm window
manager, written by Robert Nation. Fvwm was based on code from twm. And so
on... It was originally designed to emulate some of the look and feel of the
NEXTSTEP user interface, but has since taken steps towards adding more
useful, requested, and neat features especially in 1.4 version ! The changes
which comprise AfterStep's personality were originally part of bowman
development, but due to a desire to move past simple emulation and into a
niche as its own valuable window manager, AfterStep designers decided to
change the project name and move on.

Important features of AfterStep include:

1. Wharf: a free-floating application loader which can "Swallow" running
   programs and also can contain "Folders" of more applications.
2. Gradient filled TitleBars with 5 button : help/zap, action/tasks,
   iconize/maximise, shade/stick & close/destroy buttons
3. Gradient filled root window PopUp menus which can be configured to
   accomodate different tastes and styles of management
4. NEXTSTEP style icons which give a consistent look to the entire desktop
5. Pixmapped Pager with desktop pixmmaping
6. Easy to use look files, to share you desktop appearance with your friends
7. Start menu entries in a hierarchy of directories
8. WinList : a tasklist which can be horizontal or vertical
9. Many modules & asapps to give a good look to your X window station

%prep
%setup -q
%patch -p1

%build
LDFLAGS="-s"; export LDFLAGS
%configure \
	--with-imageloader="xv -root -quit" \
	--with-helpcommand="xterm -e man" \
	--disable-availability \
	--enable-makemenusonboot \
	--enable-different-looknfeels \
	--with-xpm 

make
sgml2html doc/afterstep.sgml

%install
rm -rf $RPM_BUILD_ROOT

make install install.man DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT/%{_bindir}/{sessreg,xpmroot}
rm -rf $RPM_BUILD_ROOT/%{_datadir}/afterstep/doc

gzip -9nf UPGRADE NEW README TEAM README.RedHat doc/languages/* \
	$RPM_BUILD_ROOT/%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/code doc/languages TODO *.html
%doc {UPGRADE,NEW,README,TEAM,README.RedHat}.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/afterstep
%{_mandir}/man1/*

%changelog
