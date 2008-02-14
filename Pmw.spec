%define	oname	Pmw
%define	name	python-pmw
%define	version	1.3.2
%define	release	%mkrel 1


Summary:	Python toolkit for building compound Tkinter widgets
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	MIT
Group:		Development/Python
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url:		http://www.dscpl.com.au/pmw
Source0:	%{oname}.%{version}.tar.lzma
Requires:	blt tkinter python
Obsoletes:	%{oname}
Provides:	%{oname} = %{version}-%{release}
Buildarch:	noarch
BuildRequires:	python-devel

%description
Pmw is a toolkit for building high-level compound widgets in Python 
using the Tkinter module. It consists of a set of base classes and a 
library of flexible and extensible megawidgets built on this foundation. 
These megawidgets include notebooks, comboboxes, selection widgets, paned 
widgets, scrolled widgets and dialog windows. 

%prep
%setup -q -n %{oname}.%{version}
mv src/%{oname}/%{oname}_1_3/doc src/%{oname}/README .

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{python_sitelib}
cp -r src/%{oname} %{buildroot}%{python_sitelib}

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root,0755)
%doc README doc/*
%{python_sitelib}/%{oname}
