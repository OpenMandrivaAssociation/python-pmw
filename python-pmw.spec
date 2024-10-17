#NOTE: python3 version of this module is at 2.0.0.
#      python2 version of this module is at 1.3.3.
#      If you need python2 version please refer to
#      python2-pmw.spec

%define	oname	Pmw
%define	module	%(echo %oname | tr [:upper:] [:lower:])

Summary:	Python toolkit for building compound Tkinter widgets
Name:		python-%{module}
Version:	2.0.0
Release:	1
License:	MIT and GPLv2+
Group:		Development/Python
Url:		https://pmw.sourceforge.net/
Source0:	https://pypi.python.org/packages/source/P/%{oname}/%{oname}-%{version}.tar.gz
Buildarch:	noarch

BuildRequires:	pkgconfig(python3)
BuildRequires:	python3egg(setuptools)

Requires:	blt
Requires:	python
Requires:	tkinter

Provides:	%{oname} = %{version}-%{release}

Obsoletes:	%{name} < 2.0.0
Obsoletes:	%{oname} < 2.0.0

%description
%{oname} is a toolkit for building high-level compound widgets in Python
using the Tkinter module. It contains a set of flexible and extensible
megawidgets, including notebooks, comboboxes, selection widgets, paned
widgets, scrolled widgets and dialog windows.

%files -f python3/FILELIST
%doc Pmw/Pmw_2_0_0

#----------------------------------------------------------------------------

%prep
%setup -qc -n %{module}-%{version}
%autopatch -p1

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build --root=%{buildroot} --record=FILELIST

# remove *.pyc files from FILELIST
sed -i -e '/\\*.pyc$/d' FILELIST

%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.3.2-6mdv2010.0
+ Revision: 442392
- rebuild

* Sat Dec 27 2008 Adam Williamson <awilliamson@mandriva.org> 1.3.2-5mdv2009.1
+ Revision: 319601
- rebuild with python 2.6

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.3.2-4mdv2009.0
+ Revision: 259743
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.3.2-3mdv2009.0
+ Revision: 247590
- rebuild
- fix no-buildroot-tag

* Thu Nov 15 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.3.2-1mdv2008.1
+ Revision: 108959
- import python-pmw


