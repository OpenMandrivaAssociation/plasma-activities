%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

# Renamed in 5.90.0
%define oldlibname %mklibname KF6Activities
%define olddevname %mklibname KF6Activities -d

%define libname %mklibname PlasmaActivities
%define devname %mklibname PlasmaActivities -d
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} | sed -e 's,/,-,g')

Name: plasma-activities
Version: 6.4.2
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/plasma/plasma-activities/-/archive/%{gitbranch}/plasma-activities-%{gitbranchd}.tar.bz2#/plasma-activities-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{version}/plasma-activities-%{version}.tar.xz
%endif
Summary: Core components for the KDE's Activities System
URL: https://invent.kde.org/frameworks/plasma-activities
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: python
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: boost-devel
BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
Requires: %{libname} = %{EVRD}

# Renamed 2025-04-27 after 6.0
%rename plasma6-plasma-activities

%description
Core components for the KDE's Activities System

%package -n %{libname}
Summary: Core components for the KDE's Activities System
Group: System/Libraries
Requires: %{name} = %{EVRD}
%rename %{oldlibname}

%description -n %{libname}
Core components for the KDE's Activities System

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
%rename %{olddevname}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Core components for the KDE's Activities System

%package doc
Summary: API documentation for %{name} in Qt Assistant format
Group: Development/C++

%description doc
API documentation for %{name} in Qt Assistant format

%files
%{_bindir}/plasma-activities-cli6
%{_datadir}/qlogging-categories6/plasma-activities.categories
%{_datadir}/qlogging-categories6/plasma-activities.renamecategories

%files -n %{devname}
%{_includedir}/PlasmaActivities
%{_libdir}/cmake/PlasmaActivities
%{_libdir}/pkgconfig/PlasmaActivities.pc

%files doc
%doc %{_qtdir}/doc/PlasmaActivities.*

%files -n %{libname}
%{_libdir}/libPlasmaActivities.so*
%{_qtdir}/qml/org/kde/activities
