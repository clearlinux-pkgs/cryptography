#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cryptography
Version  : 2.8
Release  : 122
URL      : https://github.com/pyca/cryptography/archive/2.8/cryptography-2.8.tar.gz
Source0  : https://github.com/pyca/cryptography/archive/2.8/cryptography-2.8.tar.gz
Summary  : cryptography is a package which provides cryptographic recipes and primitives to Python developers.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause Python-2.0
Requires: cryptography-license = %{version}-%{release}
Requires: cryptography-python = %{version}-%{release}
Requires: cryptography-python3 = %{version}-%{release}
Requires: cffi
Requires: six
BuildRequires : asn1crypto-python
BuildRequires : attrs-python
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-golang
BuildRequires : cffi
BuildRequires : cryptography_vectors
BuildRequires : hypothesis-python
BuildRequires : idna
BuildRequires : ipaddress
BuildRequires : iso8601
BuildRequires : openssl-dev
BuildRequires : packaging
BuildRequires : pretend
BuildRequires : pyparsing
BuildRequires : python3-dev
BuildRequires : pytz
BuildRequires : six
BuildRequires : util-linux

%description
Example test files for PEM Serialization Backend tests
Contains
1. ec_private_key.pem - Contains an Elliptic Curve key generated using OpenSSL, from the curve secp256r1.
2. ec_private_key_encrypted.pem - Contains the same Elliptic Curve key as ec_private_key.pem, except that
it is encrypted with AES-256 with the password "123456".
3. ec_public_key.pem - Contains the public key corresponding to ec_private_key.pem, generated using OpenSSL.
4. rsa_private_key.pem - Contains an RSA 2048 bit key generated using OpenSSL, protected by the secret
"123456" with DES3 encryption.
5. rsa_public_key.pem - Contains an RSA 2048 bit public generated using OpenSSL from rsa_private_key.pem.
6. dsaparam.pem - Contains 2048-bit DSA parameters generated using OpenSSL; contains no keys.
7. dsa_private_key.pem - Contains a DSA 2048 bit key generated using OpenSSL from the parameters in
dsaparam.pem, protected by the secret "123456" with DES3 encryption.
8. dsa_public_key.pem - Contains a DSA 2048 bit key generated using OpenSSL from dsa_private_key.pem.

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
Provides: pypi(cryptography)

%description python3
python3 components for the cryptography package.


%prep
%setup -q -n cryptography-2.8
cd %{_builddir}/cryptography-2.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582914347
# -Werror is for werrorists
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
cp %{_builddir}/cryptography-2.8/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/cryptography/de33ead2bee64352544ce0aa9e410c0c44fdf7d9
cp %{_builddir}/cryptography-2.8/LICENSE.BSD %{buildroot}/usr/share/package-licenses/cryptography/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8
cp %{_builddir}/cryptography-2.8/LICENSE.PSF %{buildroot}/usr/share/package-licenses/cryptography/acf6b1628b04fe43a99071223cdbd7b66691c264
cp %{_builddir}/cryptography-2.8/vectors/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/cryptography/de33ead2bee64352544ce0aa9e410c0c44fdf7d9
cp %{_builddir}/cryptography-2.8/vectors/LICENSE.BSD %{buildroot}/usr/share/package-licenses/cryptography/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cryptography/acf6b1628b04fe43a99071223cdbd7b66691c264
/usr/share/package-licenses/cryptography/de33ead2bee64352544ce0aa9e410c0c44fdf7d9
/usr/share/package-licenses/cryptography/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
