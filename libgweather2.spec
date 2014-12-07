%define url_ver %(echo %{version}|cut -d. -f1,2)

%define oname	libgweather
%define major	1
%define libname	%mklibname gweather %{major}
%define devname	%mklibname -d gweather %{major}

Summary:	GNOME Weather applet library
Name:		libgweather2
Version:	2.30.3
Release:	16
License:	GPLv2+
Group:		System/Libraries
Url:		http://www.gnome.org
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/libgweather/%{url_ver}/%{oname}-%{version}.tar.bz2
BuildRequires:	intltool
BuildRequires:	libxml2-utils
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libsoup-2.4)
Conflicts:	%{oname}

%description
This is a library to provide Weather data to the GNOME panel applet.

%package -n %{libname}
Group:		System/Libraries
Summary:	GNOME Weather applet library
Suggests:	%{name} = %{version}-%{release}

%description -n %{libname}
This is a library to provide Weather data to the GNOME panel applet.

%package -n %{devname}
Group:		Development/C
Summary:	GNOME Weather applet library
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%setup -qn %{oname}-%{version}

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%find_lang %{oname}
for xmlfile in %{buildroot}%{_datadir}/%{oname}/Locations.*.xml; do
echo "%lang($(basename $xmlfile|sed -e s/Locations.// -e s/.xml//)) $(echo $xmlfile | sed s!%{buildroot}!!)" >> %{oname}.lang
done

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

%files -n %{devname}
%doc ChangeLog
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
%{_datadir}/gtk-doc/html/%{oname}

