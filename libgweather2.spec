%define oname libgweather
%define major 1
%define libname %mklibname gweather %{major}
%define develname %mklibname -d gweather %{major}
%define olddevelname %mklibname -d gnome-applets

Summary:	GNOME Weather applet library
Name:		libgweather2
Version:	2.30.3
Release:	8
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.gnome.org
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{oname}/%{oname}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	intltool
BuildRequires:	libxml2-utils
#gw libtool dep:
BuildRequires:	pkgconfig(dbus-glib-1)
Conflicts:	gnome-applets < 2.21.3
Conflicts:	%{oname}

%description
This is a library to provide Weather data to the GNOME panel applet.

%package -n %{libname}
Group:		System/Libraries
Summary:	GNOME Weather applet library

%description -n %{libname}
This is a library to provide Weather data to the GNOME panel applet.

%package -n %{develname}
Group:		Development/C
Summary:	GNOME Weather applet library
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{olddevelname} < 2.21.3

%description -n %{develname}
This is a library to provide Weather data to the GNOME panel applet.

%prep
%setup -q -n %{oname}-%{version}

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%find_lang %{oname}
for xmlfile in %{buildroot}%{_datadir}/%{oname}/Locations.*.xml; do
echo "%lang($(basename $xmlfile|sed -e s/Locations.// -e s/.xml//)) $(echo $xmlfile | sed s!%{buildroot}!!)" >> %{oname}.lang
done

%post
%post_install_gconf_schemas gweather
%preun
%preun_uninstall_gconf_schemas gweather


%files -f %{oname}.lang
%doc AUTHORS NEWS
%{_sysconfdir}/gconf/schemas/gweather.schemas
%dir %{_datadir}/%{oname}
%{_datadir}/%{oname}/locations.dtd
%{_datadir}/%{oname}/Locations.xml
%{_datadir}/icons/gnome/*/status/weather*

%files -n %{libname}
%{_libdir}/libgweather.so.%{major}*

%files -n %{develname}
%doc ChangeLog
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_datadir}/gtk-doc/html/%{oname}


%changelog
* Fri Dec 16 2011 Götz Waschk <waschk@mandriva.org> 2.30.3-7mdv2012.0
+ Revision: 743116
- fix deps and conflicts

* Thu Dec 15 2011 Götz Waschk <waschk@mandriva.org> 2.30.3-6
+ Revision: 741451
- readd old version of libgweather
- rebuild for new libpng
- update to new version 2.30.3
- rebuild for new libproxy
- update to new version 2.30.2
- update to new version 2.30.0
- update to new version 2.29.92
- update to new version 2.29.91
- update to new version 2.29.90
- update to new version 2.29.5
- new version
- add icons
- update to new version 2.28.0
- update to new version 2.27.92
- update to new version 2.27.91
- update build deps
- update to new version 2.26.2.1
- update to new version 2.26.1
- update to new version 2.26.0
- update to new version 2.25.92
- update to new version 2.25.91
- update to new version 2.25.5
- update to new version 2.25.4
- update to new version 2.25.3
- rebuild to get rid of libtasn1 dep
- new version
- update file list
- fix build deps
- update to new version 2.24.2
- new version
- update to new version 2.24.1
- new version
- new version
- new version
- new version
- new version
- rediff the patch
- update build deps
- new version
- new version
- update license
- update buildrequires
- new version
- fix build
- disable parallel make
- fix buildrequires
- new version
- add localized xml files
- new version
- new major
- new version
- new version
- new version
- import libgweather

  + mandrake <mandrake@mandriva.com>
    - %repsys markrelease
      version: 2.30.3
      release: 5
      revision: 705834
      Copying 2.30.3-5 to releases/ directory.

  + Funda Wang <fwang@mandriva.org>
    - rebuild to add gconf2 as req
    - rebuild for updated libsoup libtool archive

  + Oden Eriksson <oeriksson@mandriva.com>
    - mass rebuild
    - rebuilt against new libxcb

  + Frederic Crozat <fcrozat@mandriva.com>
    - really remove patch0
    - Remove patch0, already fixed upstream differently
    - Patch0: fix libgweather when using non-UTF8 locale

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

