#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cryptography
Version  : 2.7
Release  : 115
URL      : https://github.com/pyca/cryptography/archive/2.7/cryptography-2.7.tar.gz
Source0  : https://github.com/pyca/cryptography/archive/2.7/cryptography-2.7.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause Python-2.0
Requires: cryptography-license = %{version}-%{release}
Requires: cryptography-python = %{version}-%{release}
Requires: cryptography-python3 = %{version}-%{release}
Requires: asn1crypto
Requires: cffi
Requires: six
BuildRequires : asn1crypto
BuildRequires : asn1crypto-python
BuildRequires : attrs-python
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-golang
BuildRequires : cffi
BuildRequires : cryptography_vectors
BuildRequires : enum34
BuildRequires : hypothesis-python
BuildRequires : idna
BuildRequires : ipaddress
BuildRequires : iso8601
BuildRequires : openssl-dev
BuildRequires : packaging
BuildRequires : pretend
BuildRequires : pyparsing
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : pytz
BuildRequires : six

%description
pyca/cryptography
=================
.. image:: https://img.shields.io/pypi/v/cryptography.svg
:target: https://pypi.org/project/cryptography/
:alt: Latest Version

%package license
Summary: license components for the cryptography package.
Group: Default

%description license
license components for the cryptography package.


%package python
Summary: python components for the cryptography package.
Group: Default
Requires: cryptography-python3 = %{version}-%{release}

%description python
python components for the cryptography package.


%package python3
Summary: python3 components for the cryptography package.
Group: Default
Requires: python3-core

%description python3
python3 components for the cryptography package.


%prep
%setup -q -n cryptography-2.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1563471165
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cryptography
cp LICENSE.APACHE %{buildroot}/usr/share/package-licenses/cryptography/LICENSE.APACHE
cp LICENSE.BSD %{buildroot}/usr/share/package-licenses/cryptography/LICENSE.BSD
cp LICENSE.PSF %{buildroot}/usr/share/package-licenses/cryptography/LICENSE.PSF
cp vectors/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/cryptography/vectors_LICENSE.APACHE
cp vectors/LICENSE.BSD %{buildroot}/usr/share/package-licenses/cryptography/vectors_LICENSE.BSD
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cryptography/LICENSE.APACHE
/usr/share/package-licenses/cryptography/LICENSE.BSD
/usr/share/package-licenses/cryptography/LICENSE.PSF
/usr/share/package-licenses/cryptography/vectors_LICENSE.APACHE
/usr/share/package-licenses/cryptography/vectors_LICENSE.BSD

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
