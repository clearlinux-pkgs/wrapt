#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : wrapt
Version  : 1.10.10
Release  : 22
URL      : http://pypi.debian.net/wrapt/wrapt-1.10.10.tar.gz
Source0  : http://pypi.debian.net/wrapt/wrapt-1.10.10.tar.gz
Summary  : Module for decorators, wrappers and monkey patching.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: wrapt-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
wrapt
=====
|Travis| |Coveralls| |PyPI|
The aim of the **wrapt** module is to provide a transparent object proxy
for Python, which can be used as the basis for the construction of function
wrappers and decorator functions.

%package python
Summary: python components for the wrapt package.
Group: Default

%description python
python components for the wrapt package.


%prep
%setup -q -n wrapt-1.10.10

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489678847
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1489678847
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python2*/*
/usr/lib/python3*/*
