#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x235AE5F129F9ED98 (paul.l.kehrer@gmail.com)
#
Name     : cryptography
Version  : 2.1.4
Release  : 82
URL      : http://pypi.debian.net/cryptography/cryptography-2.1.4.tar.gz
Source0  : http://pypi.debian.net/cryptography/cryptography-2.1.4.tar.gz
Source99 : http://pypi.debian.net/cryptography/cryptography-2.1.4.tar.gz.asc
Summary  : cryptography is a package which provides cryptographic recipes and primitives to Python developers.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: cryptography-python3
Requires: cryptography-python
Requires: asn1crypto
Requires: cffi
Requires: idna
Requires: ipaddress
Requires: six
Requires: sphinx_rtd_theme
BuildRequires : asn1crypto
BuildRequires : asn1crypto-legacypython
BuildRequires : asn1crypto-python
BuildRequires : attrs-legacypython
BuildRequires : attrs-python
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
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pretend
BuildRequires : pycparser-legacypython
BuildRequires : pyparsing
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : pytz
BuildRequires : setuptools
BuildRequires : six
Patch1: 0002-Don-t-try-and-install-the-vectors-dependency.patch

%description
=================

%package legacypython
Summary: legacypython components for the cryptography package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the cryptography package.


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
%setup -q -n cryptography-2.1.4
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519401802
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1519401802
rm -rf %{buildroot}
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

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
