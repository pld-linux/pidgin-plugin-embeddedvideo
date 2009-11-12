%define pidgin_ver %(pkg-config --modversion pidgin 2>/dev/null || echo ERROR)
Summary:	Show youtube and vimeo videos in pidgin
Summary(hu.UTF-8):	Youtube és vimeo videók megjelenítése a pidgin-ben
Name:		pidgin-plugin-embeddedvideo
Version:	1.0
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://pidgin-embeddedvideo.googlecode.com/files/pidgin-embeddedvideo-%{version}.tar.gz
# Source0-md5:	1bd5dc2a0a060f1f70fb6ff242b5cab8
URL:		http://code.google.com/p/pidgin-embeddedvideo/
BuildRequires:	gtk-webkit-devel >= 1.1.12
BuildRequires:	pidgin-devel >= 2.2
BuildRequires:	pkgconfig
Requires:	pidgin >= %{pidgin_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Show youtube and vimeo videos in pidgin.

%description -l hu.UTF-8
Youtube és vimeo videók megjelenítése a pidgin-ben.

%prep
%setup -q -n pidgin-embeddedvideo

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README NEWS ChangeLog
%attr(755,root,root) %{_libdir}/pidgin/*.so
%{_libdir}/pidgin/embeddedvideo
