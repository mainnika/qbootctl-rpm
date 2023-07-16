%global _vpath_srcdir sdk/%{name}/projects/meson

Name:           qbootctl
Version:        0.1.2
Release:        1%{?dist}
Summary:        Qualcomm bootctl HAL for Linux

License:        GPL-3.0-or-later
URL:            https://gitlab.com/sdm845-mainline
Source:         https://gitlab.com/sdm845-mainline/qbootctl/-/archive/main/qbootctl-main.zip

BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  zlib-devel
BuildRequires:  linux-headers
BuildRequires:  gcc
BuildRequires:  gcc-c++
Requires:       zlib

%prep
%autosetup -c

%build
%meson
%meson_build

%install
%meson_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_bindir}/qbootctl
