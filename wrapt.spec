#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : wrapt
Version  : 1.11.2
Release  : 52
URL      : https://files.pythonhosted.org/packages/23/84/323c2415280bc4fc880ac5050dddfb3c8062c2552b34c2e512eb4aa68f79/wrapt-1.11.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/23/84/323c2415280bc4fc880ac5050dddfb3c8062c2552b34c2e512eb4aa68f79/wrapt-1.11.2.tar.gz
Summary  : Module for decorators, wrappers and monkey patching.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: wrapt-license = %{version}-%{release}
Requires: wrapt-python = %{version}-%{release}
Requires: wrapt-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : python3-dev

%description
=====
        
        |Travis| |AppVeyor| |Coveralls| |PyPI|
        
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

%package license
Summary: license components for the wrapt package.
Group: Default

%description license
license components for the wrapt package.


%package python
Summary: python components for the wrapt package.
Group: Default
Requires: wrapt-python3 = %{version}-%{release}

%description python
python components for the wrapt package.


%package python3
Summary: python3 components for the wrapt package.
Group: Default
Requires: python3-core
Provides: pypi(wrapt)

%description python3
python3 components for the wrapt package.


%prep
%setup -q -n wrapt-1.11.2
cd %{_builddir}/wrapt-1.11.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602134079
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/wrapt
cp %{_builddir}/wrapt-1.11.2/LICENSE %{buildroot}/usr/share/package-licenses/wrapt/a33869ea84bae0e6f673c38a1fb27c9b90610249
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/wrapt/a33869ea84bae0e6f673c38a1fb27c9b90610249

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
