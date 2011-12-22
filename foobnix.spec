%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%global gitcommit df1d44b
%global date 20111222
%global realver 2.5.32
#https://github.com/foobnix/foobnix/blob/master/src/foobnix/version.py


Summary:    Simple and powerful music player for Linux
Summary(ru):Простой и мощный плеер музыки для ОС Linux
Name:       foobnix
Version:    %{realver}
Release:    1.%{date}git%{gitcommit}%{dist}.R

URL:    http://www.foobnix.com/?lang=en
License:    GPLv3
Source0:    https://github.com/foobnix/foobnix/tarball/%{gitcommit}
Source100:  README.RFRemix
Group:      Applications/Multimedia

BuildRequires:  desktop-file-utils
BuildRequires:  gettext

Requires:   dbus-python
Requires:   gstreamer-python
Requires:   pygtk2
Requires:   pylast
Requires:   python-chardet
Requires:   python-lyricwiki
Requires:   python-mutagen
Requires:   python-simplejson
Requires:   python-xgoogle

BuildArch:  noarch


%description
Simple and powerful music player for Linux with all necessary features. Foobnix
is a small, fast, customizable, powerful music player with user-friendly
interface.


%description -l ru
Простой и мощный плеер музыки для ОС Linux.


%prep
%setup -q -n %{name}-%{name}-%{gitcommit}
#rm -rf src/foobnix/thirdparty
rm -rf dist
#mv src/po/by.po src/po/be.po
sed -i -e "/^#\!\/usr\/bin\/env/d" src/foobnix/preferences/preferences_window.py


%build
cp %{SOURCE100} .
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
%doc src/README src/COPYING src/CHANGELOG README.RFRemix
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
* Thu Dec 22 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 2.5.32-1.20111222gitdf1d44b.R
- Update to the latest git snapshot

* Wed Nov 02 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 2.5.25-1.20001102git38b5ed8.R
- Update to the latest git snapshot
- Drop patches
- Update versioning

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
