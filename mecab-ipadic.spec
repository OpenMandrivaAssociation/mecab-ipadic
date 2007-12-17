%define version		2.7.0
%define src_version	2.7.0-20070801
%define release		%mkrel 20070801.1

Name:		mecab-ipadic
Summary:	IPA dictionary for MeCab
Version:	%{version}
Release:	%{release}
License:	BSD-like
Group:		System/Internationalization
URL:		http://mecab.sourceforge.jp/
Source0:	http://prdownloads.sourceforge.jp/mecab/18371/%{name}-%{src_version}.tar.bz2
Requires:		mecab >= 0.96
BuildRequires:		mecab-devel >= 0.96
BuildRequires:          mecab
%description
IPA dictionary for MeCab.


%prep
%setup -q -n %{name}-%{src_version}

%build
%configure2_5x --libexecdir=/usr/lib --with-charset=utf8

perl -i -p -e "s/libexec/%_lib/g" Makefile
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root)
/usr/lib/mecab/dic/*




