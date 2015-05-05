%global debug_package %{nil}

# cmake version
%if 0%{?fedora} >= 19 || 0%{?rhel} >= 7
   %define _cmake cmake
%else if 0%{?rhel} = 6
   %define _cmake cmake28
%endif

Name:		wiz-note
Version:	2.1.13git20140923
Release:	1%{?dist}
Summary:	WizNote QT Client
Group:		Applications/Editors
License:	GPLv3
URL:		https://github.com/WizTeam/WizQTClient
Source:		%{name}-%{version}.tar.xz
BuildRequires:	gcc-c++
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-qttools-devel
BuildRequires:	qt5-qtwebkit-devel
BuildRequires:	boost-devel
BuildRequires:	zlib-devel
%if 0%{?fedora} >= 19
BuildRequires:	cmake >= 2.8.4
%else if 0%{?rhel} = 6
BuildRequires:	cmake28 >= 2.8.4
%endif

%description
WizNote is an opensource cross-platform cloud based note-taking client.

%prep
%setup -q

%build
mkdir dist
pushd dist
%{_cmake} .. \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DWIZNOTE_USE_QT5=ON \
	-DCMAKE_BUILD_TYPE=Release
make %{?_smp_mflags}
popd

%install
rm -rf $RPM_BUILD_ROOT
pushd dist
make install DESTDIR=%{buildroot}
popd

rm -rf %{buildroot}%{_datadir}/licenses/
rm -rf %{buildroot}%{_datadir}/icons/hicolor/{512x512,8x8}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE README.md CHANGELOG.md
/usr/lib/wiznote/plugins/*
%{_bindir}/WizNote
%{_datadir}/applications/wiznote.desktop
%{_datadir}/icons/hicolor/*/apps/wiznote.png
%{_datadir}/wiznote/*
#%exclude %{_datadir}/licenses/

%changelog
* Tue Sep 23 2014 mosquito <sensor.wen@gmail.com>
- update version 2.1.13git20140923
- Changelog see: https://github.com/WizTeam/WizQTClient/commits/v2.1.13
* Thu Sep 11 2014 mosquito <sensor.wen@gmail.com>
- update version 2.1.13
* Wed Sep 10 2014 i@marguerite.su
- update version 2.1.12
* Sat Mar 22 2014 i@marguerite.su
- initial version 2.1.2
