%global debug_package %{nil}

Name:           foobnix
Version:        3.1.00
Release:        1%{?dist}
Summary:        Simple and Powerful music player for Linux

License:        GPLv3
URL:            http://foobnix.com
Source0:        https://github.com/foobnix/foobnix/archive/3.1.tar.gz

BuildRequires:  desktop-file-utils, gettext
Requires:       python-chardet, python-simplejson, python-setuptools, python-mutagen
Requires:       pygobject3, webkitgtk3, keybinder3
Requires:       libsoup, libnotify

BuildArch:      noarch

%description
Simple and powerful music player for Linux with all necessary features. Foobnix
is a small, fast, customizable, powerful music player with user-friendly
interface.

%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__python} setup.py install --root %{buildroot}

%find_lang %{name}

%files -f %{name}.lang
%doc README CHANGELOG
%license COPYING
%{_bindir}/%{name}
%{python_sitelib}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}*
%{_mandir}/man1/%{name}*

%changelog
* Tue Jul 14 2015 Maxim Orlov <murmansksity@gmail.com> - 3.1.00-1
- Update to 3.1.00

* Tue Feb 18 2014 Vasiliy N. Glazov <vascom2@gmail.com> - 2.6.10-1.20140218git236be1f.R
- Update to 2.6.10

* Thu Jan 03 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 2.6.09-1.20121206git35fcb24.R
- Update to 2.6.09

* Thu Dec 22 2011 Vasiliy N. Glazov <vascom2@gmail.com> - 2.5.35-1.20120315gitc555fab.R
- Update to the latest git snapshot

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
