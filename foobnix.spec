%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%global gitcommit 49ac470


Summary:	Simple and powerful music player for Linux
Summary(ru):	Простой и мощный плеер музыки для ОС Linux
Name:		foobnix
Version:	2.5.25
Release:	1.git%{gitcommit}%{?dist}.R

URL:		http://www.foobnix.com/?lang=en
License:	GPLv3
# wget https://github.com/foobnix/foobnix/tarball/eeb56ad
#Source0:	%{name}-%{name}-%{gitcommit}.tar.gz
Source0:	https://github.com/foobnix/foobnix/tarball/%{gitcommit}
Patch1:		foobnix-0001-Drop-bundled-python-libraries.patch
Patch2:		foobnix-0002-Don-t-install-doc-files-Fedora-specific.patch
Patch3:		foobnix-0003-Partially-revert-4cade9edcc48d134648e4751c5cafe13e2f.patch
Patch4:		foobnix-0004-Don-t-use-get_release_year-from-forked-pylast.patch
Group:		Applications/Multimedia
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	desktop-file-utils
BuildRequires:	gettext

Requires:	dbus-python
Requires:	gstreamer-python
Requires:	pygtk2
Requires:	pylast
Requires:	python-chardet
Requires:	python-lyricwiki
Requires:	python-mutagen
Requires:	python-simplejson
Requires:	python-xgoogle

BuildArch:	noarch


%description
Simple and powerful music player for Linux with all necessary features. Foobnix
is a small, fast, customizable, powerful music player with user-friendly
interface.


%description -l ru
Простой и мощный плеер музыки для ОС Linux.


%prep
%setup -q -n %{name}-%{name}-%{gitcommit}
%patch1 -p1 -b .bundled_libs
%patch2 -p1 -b .no_docs
%patch3 -p1 -b .revert_po_removal
%patch4 -p1 -b .no_private_funcs
rm -rf src/foobnix/thirdparty
rm -rf dist
#mv src/po/by.po src/po/be.po
sed -i -e "/^#\!\/usr\/bin\/env/d" src/foobnix/preferences/preferences_window.py


%build
cd src
python setup.py build


%install
rm -rf %{buildroot}
cd src
python setup.py install --root %{buildroot}

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

cd -
%find_lang %{name}


%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr (-,root,root,0755)
%doc src/README src/COPYING src/CHANGELOG
%{_bindir}/%{name}
%{python_sitelib}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/%{name}*
%{_datadir}/pixmaps/vk.png
%{_datadir}/pixmaps/theme/cat.jpg
%{_datadir}/pixmaps/theme/flower.jpg
%{_mandir}/man1/%{name}*


%changelog
* Mon Sep 19 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 2.5.25-1.git49ac470
- Update to the latest git snapshot

* Mon Sep 12 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.5.23-1.git5295204
- Ver. 2.5.24

* Sun Sep 11 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.5.23-1.gite391906
- Update to the latest git snapshot

* Sun Aug 14 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.5.23-1.giteeb56ad
- Update to the latest git snapshot

* Sat Jul 09 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.5.17-2.git4c93748
- Don't use functions specific to the forked copy of pylast

* Sat Jul 09 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.5.17-1.git4c93748
- Update to the latest git snapshot

* Wed Jun 29 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.5.16-1.git31ad572
- Update to the latest git snapshot

* Fri Jun 03 2011 Peter Lemenkov <lemenkov@gmail.com> - 2.5.15-1.git12b0915
- Update to the latest git tag

* Thu Feb 24 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.2.5-1
- update to 0.2.5

* Tue Jan 25 2011 Arkady L. Shane <ashejn@yandex-team.ru> - 0.2.3-1
- initla build
