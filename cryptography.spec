#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x235AE5F129F9ED98 (paul.l.kehrer@gmail.com)
#
Name     : cryptography
Version  : 3.1
Release  : 127
URL      : https://files.pythonhosted.org/packages/12/be/c9cc7d7ab71dbcc9e4e517ead0cdd48e8c9a48d7b8bdddb738e90d08279a/cryptography-3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/12/be/c9cc7d7ab71dbcc9e4e517ead0cdd48e8c9a48d7b8bdddb738e90d08279a/cryptography-3.1.tar.gz
Source1  : https://files.pythonhosted.org/packages/12/be/c9cc7d7ab71dbcc9e4e517ead0cdd48e8c9a48d7b8bdddb738e90d08279a/cryptography-3.1.tar.gz.asc
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
BuildRequires : iso8601
BuildRequires : openssl-dev
BuildRequires : packaging
BuildRequires : pretend
BuildRequires : pyparsing
BuildRequires : pytz
BuildRequires : six

%description
=================

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
Requires: pypi(cffi)
Requires: pypi(six)

%description python3
python3 components for the cryptography package.


%prep
%setup -q -n cryptography-3.1
cd %{_builddir}/cryptography-3.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1598649878
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cryptography
cp %{_builddir}/cryptography-3.1/LICENSE.APACHE %{buildroot}/usr/share/package-licenses/cryptography/de33ead2bee64352544ce0aa9e410c0c44fdf7d9
cp %{_builddir}/cryptography-3.1/LICENSE.BSD %{buildroot}/usr/share/package-licenses/cryptography/ea5b412c09f3b29ba1d81a61b878c5c16ffe69d8
cp %{_builddir}/cryptography-3.1/LICENSE.PSF %{buildroot}/usr/share/package-licenses/cryptography/acf6b1628b04fe43a99071223cdbd7b66691c264
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
