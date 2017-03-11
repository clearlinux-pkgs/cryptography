#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x235AE5F129F9ED98 (paul.l.kehrer@gmail.com)
#
Name     : cryptography
Version  : 1.8.1
Release  : 55
URL      : http://pypi.debian.net/cryptography/cryptography-1.8.1.tar.gz
Source0  : http://pypi.debian.net/cryptography/cryptography-1.8.1.tar.gz
Source99 : http://pypi.debian.net/cryptography/cryptography-1.8.1.tar.gz.asc
Summary  : cryptography is a package which provides cryptographic recipes and primitives to Python developers.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: cryptography-python
Requires: Sphinx
Requires: cffi
Requires: doc8
Requires: enum34
Requires: flake8
Requires: hypothesis
Requires: idna
Requires: ipaddress
Requires: iso8601
Requires: packaging
Requires: pretend
Requires: pyasn1
Requires: pytest
Requires: pytz
Requires: setuptools
Requires: six
BuildRequires : asn1crypto-python
BuildRequires : cffi
BuildRequires : cffi-python
BuildRequires : cryptography_vectors-python
BuildRequires : enum34-python
BuildRequires : idna-python
BuildRequires : ipaddress-python
BuildRequires : iso8601-python
BuildRequires : openssl-dev
BuildRequires : packaging-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pretend-python
BuildRequires : pyparsing-python
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : setuptools
Patch1: 0001-Remove-doctests.patch

%description
Cryptography
============
.. image:: https://img.shields.io/pypi/v/cryptography.svg
:target: https://pypi.python.org/pypi/cryptography/
:alt: Latest Version

%package python
Summary: python components for the cryptography package.
Group: Default

%description python
python components for the cryptography package.


%prep
%setup -q -n cryptography-1.8.1
%patch1 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489274281
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
export SOURCE_DATE_EPOCH=1489274281
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
