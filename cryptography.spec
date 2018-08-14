#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cryptography
Version  : 2.3.1
Release  : 98
URL      : https://github.com/pyca/cryptography/archive/2.3.1.tar.gz
Source0  : https://github.com/pyca/cryptography/archive/2.3.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause Python-2.0
Requires: cryptography-python3
Requires: cryptography-license
Requires: cryptography-python
Requires: asn1crypto
Requires: cffi
Requires: idna
Requires: six
BuildRequires : asn1crypto
BuildRequires : asn1crypto-legacypython
BuildRequires : asn1crypto-python
BuildRequires : attrs-legacypython
BuildRequires : attrs-python
BuildRequires : buildreq-distutils23
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-golang
BuildRequires : cffi
BuildRequires : cffi-legacypython
BuildRequires : cryptography_vectors
BuildRequires : enum34
BuildRequires : hypothesis-legacypython
BuildRequires : hypothesis-python
BuildRequires : idna
BuildRequires : ipaddress
BuildRequires : iso8601
BuildRequires : openssl-dev
BuildRequires : packaging
BuildRequires : pretend
BuildRequires : pycparser-legacypython
BuildRequires : pyparsing
BuildRequires : python-dev
BuildRequires : pytz
BuildRequires : setuptools-legacypython
BuildRequires : six
Patch1: 0002-Don-t-try-and-install-the-vectors-dependency.patch

%description
pyca/cryptography
=================
.. image:: https://img.shields.io/pypi/v/cryptography.svg
:target: https://pypi.org/project/cryptography/
:alt: Latest Version

%package legacypython
Summary: legacypython components for the cryptography package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the cryptography package.


%package license
Summary: license components for the cryptography package.
Group: Default

%description license
license components for the cryptography package.


%package python
Summary: python components for the cryptography package.
Group: Default
Requires: cryptography-python3

%description python
python components for the cryptography package.


%package python3
Summary: python3 components for the cryptography package.
Group: Default
Requires: python3-core

%description python3
python3 components for the cryptography package.


%prep
%setup -q -n cryptography-2.3.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534275584
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1534275584
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/cryptography
cp LICENSE.APACHE %{buildroot}/usr/share/doc/cryptography/LICENSE.APACHE
cp LICENSE.BSD %{buildroot}/usr/share/doc/cryptography/LICENSE.BSD
cp LICENSE.PSF %{buildroot}/usr/share/doc/cryptography/LICENSE.PSF
cp vectors/LICENSE.APACHE %{buildroot}/usr/share/doc/cryptography/vectors_LICENSE.APACHE
cp vectors/LICENSE.BSD %{buildroot}/usr/share/doc/cryptography/vectors_LICENSE.BSD
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/cryptography/LICENSE.APACHE
/usr/share/doc/cryptography/LICENSE.BSD
/usr/share/doc/cryptography/LICENSE.PSF
/usr/share/doc/cryptography/vectors_LICENSE.APACHE
/usr/share/doc/cryptography/vectors_LICENSE.BSD

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
