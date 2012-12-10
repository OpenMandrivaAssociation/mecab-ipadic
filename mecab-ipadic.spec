%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define src_version	2.7.0-20070801

Name:		mecab-ipadic
Summary:	IPA dictionary for MeCab
Version:	2.7.0
Release:	20070801.3
License:	BSD-like
Group:		System/Internationalization
URL:		http://mecab.sourceforge.jp/
Source0:	http://prdownloads.sourceforge.jp/mecab/18371/%{name}-%{src_version}.tar.bz2
Requires:	mecab
BuildRequires:	mecab-devel
BuildRequires:	mecab

%description
IPA dictionary for MeCab.

%prep
%setup -q -n %{name}-%{src_version}

%build
%configure2_5x --libexecdir=/usr/lib --with-charset=utf8

perl -i -p -e "s/libexec/%{_lib}/g" Makefile
%make

%install
%makeinstall_std

%files
%{_libdir}/mecab/dic/*

