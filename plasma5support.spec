#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: da8b975
#
Name     : plasma5support
Version  : 6.0.2
Release  : 1
URL      : https://download.kde.org/stable/plasma/6.0.2/plasma5support-6.0.2.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.0.2/plasma5support-6.0.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 LGPL-2.0
Requires: plasma5support-data = %{version}-%{release}
Requires: plasma5support-lib = %{version}-%{release}
Requires: plasma5support-license = %{version}-%{release}
Requires: plasma5support-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Plasma5Support Framework
Migration aids for KF5 -> KF6 migration
contains:
# Dataengines
Dataengine support is not in the kf6 version of plasma anymore. Dataengines should be migrated to QML imports, but in the meantime remaining engines can use the dataengine implementation here

%package data
Summary: data components for the plasma5support package.
Group: Data

%description data
data components for the plasma5support package.


%package dev
Summary: dev components for the plasma5support package.
Group: Development
Requires: plasma5support-lib = %{version}-%{release}
Requires: plasma5support-data = %{version}-%{release}
Provides: plasma5support-devel = %{version}-%{release}
Requires: plasma5support = %{version}-%{release}

%description dev
dev components for the plasma5support package.


%package lib
Summary: lib components for the plasma5support package.
Group: Libraries
Requires: plasma5support-data = %{version}-%{release}
Requires: plasma5support-license = %{version}-%{release}

%description lib
lib components for the plasma5support package.


%package license
Summary: license components for the plasma5support package.
Group: Default

%description license
license components for the plasma5support package.


%package locales
Summary: locales components for the plasma5support package.
Group: Default

%description locales
locales components for the plasma5support package.


%prep
%setup -q -n plasma5support-6.0.2
cd %{_builddir}/plasma5support-6.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1710360150
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1710360150
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/plasma5support
cp %{_builddir}/plasma5support-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/plasma5support/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/plasma5support-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/plasma5support/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/plasma5support-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/plasma5support/20079e8f79713dce80ab09774505773c926afa2a || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang libplasma5support

%files
%defattr(-,root,root,-)
/usr/lib64/qt6/qml/org/kde/plasma/plasma5support/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/plasma/plasma5support/plasma5supportplugin.qmltypes
/usr/lib64/qt6/qml/org/kde/plasma/plasma5support/qmldir

%files data
%defattr(-,root,root,-)
/usr/share/plasma5support/services/dataengineservice.operations
/usr/share/plasma5support/services/plasmoidservice.operations
/usr/share/plasma5support/services/storage.operations
/usr/share/qlogging-categories6/plasma5support.categories
/usr/share/qlogging-categories6/plasma5support.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/Plasma5Support/Plasma5Support/DataContainer
/usr/include/Plasma5Support/Plasma5Support/DataEngine
/usr/include/Plasma5Support/Plasma5Support/DataEngineConsumer
/usr/include/Plasma5Support/Plasma5Support/Plasma5Support
/usr/include/Plasma5Support/Plasma5Support/PluginLoader
/usr/include/Plasma5Support/Plasma5Support/Service
/usr/include/Plasma5Support/Plasma5Support/ServiceJob
/usr/include/Plasma5Support/plasma5support/datacontainer.h
/usr/include/Plasma5Support/plasma5support/dataengine.h
/usr/include/Plasma5Support/plasma5support/dataengineconsumer.h
/usr/include/Plasma5Support/plasma5support/plasma5support.h
/usr/include/Plasma5Support/plasma5support/plasma5support_export.h
/usr/include/Plasma5Support/plasma5support/pluginloader.h
/usr/include/Plasma5Support/plasma5support/service.h
/usr/include/Plasma5Support/plasma5support/servicejob.h
/usr/include/Plasma5Support/plasma5support/version.h
/usr/include/Plasma5Support/plasma5support_version.h
/usr/lib64/cmake/Plasma5Support/Plasma5SupportConfig.cmake
/usr/lib64/cmake/Plasma5Support/Plasma5SupportConfigVersion.cmake
/usr/lib64/cmake/Plasma5Support/Plasma5SupportMacros.cmake
/usr/lib64/cmake/Plasma5Support/Plasma5SupportTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Plasma5Support/Plasma5SupportTargets.cmake
/usr/lib64/libPlasma5Support.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libPlasma5Support.so.6
/usr/lib64/libPlasma5Support.so.6.0.2
/usr/lib64/qt6/qml/org/kde/plasma/plasma5support/libplasma5supportplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/plasma5support/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/plasma5support/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/plasma5support/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f libplasma5support.lang
%defattr(-,root,root,-)

