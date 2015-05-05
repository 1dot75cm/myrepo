%global debug_package %{nil}

# cmake version
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
   %define _cmake cmake
%else if 0%{?rhel} = 6
   %define _cmake cmake28
%endif

Name:		wiznote-beta
Version:	2.1.14git20141015
Release:	1%{?dist}
Summary:	WizNote QT Client
Group:		Applications/Editors
License:	GPLv3
URL:		https://github.com/WizTeam/WizQTClient
Source:		%{name}-%{version}.tar.xz
Patch0:		fix_build_error.patch
BuildRequires:	gcc-c++
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-qttools-devel
BuildRequires:	qt5-qtwebkit-devel
BuildRequires:	boost-devel
BuildRequires:	zlib-devel
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
BuildRequires:	cmake >= 2.8.4
%else if 0%{?rhel} = 6
BuildRequires:	cmake28 >= 2.8.4
%endif

# qt4 build requires
#BuildRequires:	qt-devel
#BuildRequires:	qtwebkit-devel

%description
WizNote is an opensource cross-platform cloud based note-taking client.
This is a development version.

%prep
%setup -q
%patch0 -p1

%build
mkdir dist
pushd dist
%{_cmake} .. \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DBUILD_STATIC_LIBRARIES=ON \
	-DCLUCENE_BUILD_SHARED_LIBRARIES=ON \
	-DCRYPTOPP_BUILD_SHARED_LIBS=ON \
	-DCRYPTOPP_BUILD_STATIC_LIBS=ON \
	-DWIZNOTE_USE_QT5=ON \
	-DCMAKE_BUILD_TYPE=Release
#-DCMAKE_INSTALL_RPATH="$ORIGIN;$ORIGIN/..;$ORIGIN/../lib64/%{name}/plugins"
#-DWIZNOTE_PLUGIN_DIR=%{_libdir}/%{name}/plugins
make %{?_smp_mflags}
popd

%install
rm -rf $RPM_BUILD_ROOT
pushd dist
make install DESTDIR=%{buildroot}
popd

install -d %{buildroot}%{_libdir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}

# lib/wiznote -> lib64/wiznote-beta
mv %{buildroot}/usr/lib/wiznote/* %{buildroot}%{_libdir}/%{name}
%ifarch x86_64
rm -rf %{buildroot}/usr/lib/
%else
rm -rf %{buildroot}/usr/lib/wiznote/
%endif
mv %{buildroot}%{_bindir}/WizNote %{buildroot}%{_bindir}/%{name}
mv %{buildroot}%{_datadir}/applications/wiznote.desktop \
   %{buildroot}%{_datadir}/applications/%{name}.desktop

# share/wiznote -> share/wiznote-beta
mv %{buildroot}%{_datadir}/wiznote/* %{buildroot}%{_datadir}/%{name}
rm -rf %{buildroot}%{_datadir}/wiznote

# change desktop
sed -i  -e 's@Exec=WizNote@Exec=%{name}@' \
	-e 's@Icon=wiznote@Icon=%{name}@' \
   %{buildroot}%{_datadir}/applications/%{name}.desktop

# change icon file name
for i in `ls %{buildroot}%{_datadir}/icons/hicolor/`; do
   mv %{buildroot}%{_datadir}/icons/hicolor/${i}/apps/wiznote.png \
      %{buildroot}%{_datadir}/icons/hicolor/${i}/apps/%{name}.png
done
rm -rf %{buildroot}%{_datadir}/licenses/
rm -rf %{buildroot}%{_datadir}/icons/hicolor/{512x512,8x8}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE README.md CHANGELOG.md
%{_libdir}/%{name}/plugins/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}/*
#@exclude @{_datadir}/licenses/

%changelog
* Thu Oct 16 2014 mosquito <sensor.wen@gmail.com> - 2.1.14git20141015-1
- Development version 2.1.14git20141015
