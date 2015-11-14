#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cryptography
Version  : 1.1
Release  : 29
URL      : https://pypi.python.org/packages/source/c/cryptography/cryptography-1.1.tar.gz
Source0  : https://pypi.python.org/packages/source/c/cryptography/cryptography-1.1.tar.gz
Summary  : cryptography is a package which provides cryptographic recipes and primitives to Python developers.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: cryptography-python
BuildRequires : cffi
BuildRequires : cryptography_vectors
BuildRequires : cryptography_vectors-python
BuildRequires : enum34
BuildRequires : hypothesis-python
BuildRequires : idna-python
BuildRequires : ipaddress-python
BuildRequires : iso8601-python
BuildRequires : openssl-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pretend-python
BuildRequires : py-python
BuildRequires : pyasn1
BuildRequires : pyasn1-modules
BuildRequires : pycparser
BuildRequires : pycparser-python
BuildRequires : pytest
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six

%description
Cryptography
============
.. image:: https://img.shields.io/pypi/v/cryptography.svg
:target: https://pypi.python.org/pypi/cryptography/
:alt: Latest Version

%package python
Summary: python components for the cryptography package.
Group: Default
Requires: idna-python
Requires: ipaddress-python

%description python
python components for the cryptography package.


%prep
%setup -q -n cryptography-1.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
