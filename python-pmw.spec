%define	oname	Pmw
%define	module	%(echo %oname | tr [:upper:] [:lower:])

Summary:	Python toolkit for building compound Tkinter widgets
Name:		python-%{module}
Version:	2.0.0
Release:	1
License:	MIT and GPLv2+
Group:		Development/Python
Url:		http://pmw.sourceforge.net/
Source0:	https://pypi.python.org/packages/source/P/%{oname}/%{oname}-%{version}.tar.gz
Buildarch:	noarch

BuildRequires:	pkgconfig(python3)
BuildRequires:	python3egg(setuptools)

Requires:	blt
Requires:	python
Requires:	tkinter

Provides:	%{oname} = %{version}-%{release}

%description
%{oname} is a toolkit for building high-level compound widgets in Python
using the Tkinter module. It contains a set of flexible and extensible
megawidgets, including notebooks, comboboxes, selection widgets, paned
widgets, scrolled widgets and dialog windows.

%files -f python3/FILELIST
%doc python2/Pmw/Pmw_2_0_0

#----------------------------------------------------------------------------

%package -n python2-%{module}
Summary:	Python2 toolkit for building compound Tkinter widgets
#Version:	1.3.3
Group:		Development/Python

BuildRequires:	pkgconfig(python)
BuildRequires:	pythonegg(setuptools)

Requires:	blt
Requires:	python2
Requires:	tkinter

%description -n python2-%{module}
%{oname} is a toolkit for building high-level compound widgets in Python
using the Tkinter module. It contains a set of flexible and extensible
megawidgets, including notebooks, comboboxes, selection widgets, paned
widgets, scrolled widgets and dialog windows.

%files -n python2-%{module} -f python2/FILELIST
%doc python2/Pmw/Pmw_1_3_3

#----------------------------------------------------------------------------

%prep
%setup -qc -n %{module}-%{version}

# set python2 and python3 branch
mv %{oname}-%{version} python3
cp -a python3 python2

%build
# build python2 module
pushd python2
%{__python2} setup.py build
popd

# build python3 module
pushd python3
%{__python3} setup.py build
popd

%install
# install python2 module
pushd python2
%{__python2} setup.py install --skip-build --root=%{buildroot} --record=FILELIST

# remove *.pyc files from FILELIST
sed -i -e'/\\*.pyc$/d' FILELIST
popd

# install python3 module
pushd python3
%{__python3} setup.py install --skip-build --root=%{buildroot} --record=FILELIST

# remove *.pyc files from FILELIST
sed -i -e '/\\*.pyc$/d' FILELIST
popd


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


