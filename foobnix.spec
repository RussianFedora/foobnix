%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%define rel	6

Summary:	Simple and Powerful music player for Linux
Summary(ru):	Простой и мощный плеер музыки для ОС Linux
Name:		foobnix
Version:	0.2.5
Release:	1%{?dist}

URL:		http://www.foobnix.com/
License:	GPLv3
Source:		https://launchpad.net/~foobnix-player/+archive/foobnix/+files/%{name}_%{version}-6m.tar.gz
Group:		Applications/Multimedia
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	python-chardet
BuildRequires:	pygtk2-devel 
BuildRequires:	pygtk2-libglade
BuildRequires:	python-mutagen
BuildRequires:	python-simplejson
BuildRequires:	python-setuptools 
BuildRequires:	gstreamer-plugins-good
BuildRequires:	gstreamer-plugins-bad
BuildRequires:	gstreamer-plugins-bad-free
BuildRequires:	gstreamer-plugins-bad-free-extras
BuildRequires:	gstreamer-ffmpeg
BuildRequires:	gstreamer-plugins-ugly
BuildRequires:	gstreamer-python
BuildRequires:	gettext-devel
BuildRequires:	fuseiso
BuildRequires:	python-keybinder

Requires:	python-chardet
Requires:	python-mutagen
Requires:	gstreamer-plugins-good
Requires:	gstreamer-python
Requires:	gstreamer-ffmpeg
Requires:	gstreamer-plugins-ugly

BuildArch:	noarch


%description 
Simple and Powerful music player for Linux

All best features in one player. Foobnix small, fast, customize, powerful
music player with user-friendly interface.


%description -l ru
Простой и мощный плеер музыки для ОС Linux


%prep
%setup -q -n %{name}_%{version}-%{rel}
sed -i 's!\$!;!g' foobnix.desktop


%build
python setup.py build


%install
rm -rf %{buildroot}

python setup.py install --root=%{buildroot}

# fix E: wrong-file-end-of-line-encoding 
sed -i 's/\r//' %{buildroot}%{python_sitelib}/%{name}/thirdparty/google/browser.py

# these files should me executable
chmod 755 %{buildroot}%{python_sitelib}/%{name}/thirdparty/google/browser.py
chmod 755 %{buildroot}%{python_sitelib}/%{name}/preferences/preferences_window.py
chmod 755 %{buildroot}%{python_sitelib}/%{name}/thirdparty/google/search.py
chmod 755 %{buildroot}%{python_sitelib}/%{name}/thirdparty/google/__init__.py

%find_lang %{name}


%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr (-,root,root,0755)
%doc README COPYING CHANGELOG
%{_bindir}/%{name}
%{python_sitelib}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/%{name}*
%{_datadir}/pixmaps/theme/cat.jpg
%{_datadir}/pixmaps/theme/flower.jpg
%{_mandir}/man1/%{name}*


%changelog
* Thu Feb 24 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.2.5-1
- update to 0.2.5

* Tue Jan 25 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.2.3-1
- initla build
