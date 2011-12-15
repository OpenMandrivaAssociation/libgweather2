%define name libgweather2
%define oname libgweather
%define version 2.30.3
%define release %mkrel 6
%define major 1
%define libname %mklibname gweather %major
%define develname %mklibname -d gweather %major
%define olddevelname %mklibname -d gnome-applets

Summary: GNOME Weather applet library
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{oname}/%{oname}-%{version}.tar.bz2
License: GPLv2+
Group: System/Libraries
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libsoup-devel
BuildRequires: gtk+2-devel
BuildRequires: libGConf2-devel
BuildRequires: intltool
BuildRequires: libxml2-utils
#gw libtool dep:
BuildRequires: dbus-glib-devel
Conflicts: gnome-applets < 2.21.3

%description
This is a library to provide Weather data to the GNOME panel applet.

%package -n %libname
Group: System/Libraries
Summary: GNOME Weather applet library
Requires: %name >= %version

%description -n %libname
This is a library to provide Weather data to the GNOME panel applet.

%package -n %develname
Group: Development/C
Summary: GNOME Weather applet library
Requires: %libname = %version
Provides: %name-devel = %version-%release
Obsoletes: %olddevelname < 2.21.3

%description -n %develname
This is a library to provide Weather data to the GNOME panel applet.

%prep
%setup -q -n %oname-%version

%build
%configure2_5x
%make 

%install
rm -rf %{buildroot} %oname.lang
%makeinstall_std
%find_lang %oname
for xmlfile in  %buildroot%_datadir/%oname/Locations.*.xml; do
echo "%lang($(basename $xmlfile|sed -e s/Locations.// -e s/.xml//)) $(echo $xmlfile | sed s!%buildroot!!)" >> %oname.lang
done

%clean
rm -rf %{buildroot}

%post
%post_install_gconf_schemas gweather
%preun
%preun_uninstall_gconf_schemas gweather


%files -f %oname.lang
%defattr(-,root,root)
%doc AUTHORS NEWS
%_sysconfdir/gconf/schemas/gweather.schemas
%dir %_datadir/%oname
%_datadir/%oname/locations.dtd
%_datadir/%oname/Locations.xml
%_datadir/icons/gnome/*/status/weather*

%files -n %libname
%defattr(-, root, root)
%_libdir/libgweather.so.%{major}*

%files -n %develname
%defattr(-, root, root)
%doc ChangeLog
%attr(644,root,root) %_libdir/lib*a
%_libdir/lib*.so
%_libdir/pkgconfig/*.pc
%_includedir/*
%_datadir/gtk-doc/html/%oname
