#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : wrapt
Version  : 1.10.11
Release  : 29
URL      : http://pypi.debian.net/wrapt/wrapt-1.10.11.tar.gz
Source0  : http://pypi.debian.net/wrapt/wrapt-1.10.11.tar.gz
Summary  : Module for decorators, wrappers and monkey patching.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: wrapt-python3
Requires: wrapt-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=====
        
        |Travis| |Coveralls| |PyPI|
        
        The aim of the **wrapt** module is to provide a transparent object proxy
        for Python, which can be used as the basis for the construction of function
        wrappers and decorator functions.
        
        The **wrapt** module focuses very much on correctness. It therefore goes
        way beyond existing mechanisms such as ``functools.wraps()`` to ensure that
        decorators preserve introspectability, signatures, type checking abilities
        etc. The decorators that can be constructed using this module will work in
        far more scenarios than typical decorators and provide more predictable and
        consistent behaviour.
        
        To ensure that the overhead is as minimal as possible, a C extension module
        is used for performance critical components. An automatic fallback to a
        pure Python implementation is also provided where a target system does not
        have a compiler to allow the C extension to be compiled.
        
        Documentation
        -------------

%package python
Summary: python components for the wrapt package.
Group: Default
Requires: wrapt-python3

%description python
python components for the wrapt package.


%package python3
Summary: python3 components for the wrapt package.
Group: Default
Requires: python3-core

%description python3
python3 components for the wrapt package.


%prep
%setup -q -n wrapt-1.10.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523310710
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
