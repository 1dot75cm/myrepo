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
Obsoletes:	wiz-note <= 2.1.13git20140926

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
# change library path
%ifarch x86_64
sed -i 's@lib/wiznote/plugins@lib64/%{name}/plugins@' \
	src/main.cpp \
	src/plugins/coreplugin/CMakeLists.txt \
	src/plugins/helloworld/CMakeLists.txt \
	src/plugins/markdown/CMakeLists.txt \
	lib/aggregation/CMakeLists.txt \
	lib/extensionsystem/CMakeLists.txt
%else
sed -i 's@lib/wiznote/plugins@lib/%{name}/plugins@' \
	src/main.cpp \
	src/plugins/coreplugin/CMakeLists.txt \
	src/plugins/helloworld/CMakeLists.txt \
	src/plugins/markdown/CMakeLists.txt \
	lib/aggregation/CMakeLists.txt \
	lib/extensionsystem/CMakeLists.txt
%endif

# change share path
sed -i 's@share/wiznote@share/%{name}@' \
	src/utils/pathresolve.cpp \
	src/main.cpp \
	src/CMakeLists.txt

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
make %{?_smp_mflags}
popd

%install
rm -rf $RPM_BUILD_ROOT
pushd dist
make install DESTDIR=%{buildroot}
popd

# change exec filename
mv %{buildroot}%{_bindir}/WizNote %{buildroot}%{_bindir}/%{name}
mv %{buildroot}%{_datadir}/applications/wiznote.desktop \
   %{buildroot}%{_datadir}/applications/%{name}.desktop

# change desktop
sed -i -e 's@Name=WizNote@Name=WizNote Develop@' \
       -e '/Name\[zh\_*/s@为知笔记@为知笔记开发版@' \
       -e 's@Exec=WizNote@Exec=%{name}@' \
       -e 's@Icon=wiznote@Icon=%{name}@' \
   %{buildroot}%{_datadir}/applications/%{name}.desktop

# change icon filename
for i in `ls %{buildroot}%{_datadir}/icons/hicolor/`; do
   mv %{buildroot}%{_datadir}/icons/hicolor/${i}/apps/wiznote.png \
      %{buildroot}%{_datadir}/icons/hicolor/${i}/apps/%{name}.png
done

# export library path
install -d %{buildroot}/etc/ld.so.conf.d/
echo "%{_libdir}/%{name}/plugins/" > %{buildroot}/etc/ld.so.conf.d/%{name}.conf

rm -rf %{buildroot}%{_datadir}/licenses/
rm -rf %{buildroot}%{_datadir}/icons/hicolor/{512x512,8x8}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE README.md CHANGELOG.md
%{_sysconfdir}/ld.so.conf.d/%{name}.conf
%{_libdir}/%{name}/plugins/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}/*
#@exclude @{_datadir}/licenses/

%changelog
* Thu Oct 16 2014 mosquito <sensor.wen@gmail.com> - 2.1.14git20141015-1
- Development version 2.1.14git20141015
