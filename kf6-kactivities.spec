%define libname %mklibname KF6Activities
%define devname %mklibname KF6Activities -d
%define git 20230726

Name: kf6-kactivities
Version: 5.240.0
Release: %{?git:0.%{git}.}1
Source0: https://invent.kde.org/frameworks/kactivities/-/archive/master/kactivities-master.tar.bz2#/kactivities-%{git}.tar.bz2
Summary: Core components for the KDE's Activities System
URL: https://invent.kde.org/frameworks/kactivities
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
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
BuildRequires: boost-devel
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6WindowSystem)
Requires: %{libname} = %{EVRD}

%description
Core components for the KDE's Activities System

%package -n %{libname}
Summary: Core components for the KDE's Activities System
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
Core components for the KDE's Activities System

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Core components for the KDE's Activities System

%prep
%autosetup -p1 -n kactivities-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_datadir}/qlogging-categories6/kactivities.*
%{_bindir}/kactivities-cli6

%files -n %{devname}
%{_includedir}/KF6/KActivities
%{_libdir}/cmake/KF6Activities
%{_qtdir}/mkspecs/modules/qt_KActivities.pri
%{_qtdir}/doc/KF6Activities.*
%{_libdir}/pkgconfig/KF6Activities.pc

%files -n %{libname}
%{_libdir}/libKF6Activities.so*
%{_qtdir}/qml/org/kde/activities
