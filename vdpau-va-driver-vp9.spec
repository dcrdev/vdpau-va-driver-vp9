%global commit 509d3b21a1084b4f492b50cced8835f4cd591c4a
%global short_commit %(c=%{commit}; echo ${c:0:7})
%global commit_date 20211012

Name:           vdpau-va-driver-vp9
Version:        0.7.4
Release:        0.2.%{commit_date}git%{short_commit}%{?dist}
Summary:        HW video decode support for VDPAU platforms with Chromium and VP9 Support
License:        GPLv2+
URL:            https://github.com/xuanruiqi/%{name}
Source0:        https://github.com/xuanruiqi/%{name}/archive/%{short_commit}/%{name}-%{commit}.tar.gz

Conflicts:      libva-vdpau-driver

BuildRequires:  libtool
BuildRequires:  libva-devel
BuildRequires:  libvdpau-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  gcc, gcc-c++
BuildRequires:  autoconf, automake

Requires:       mesa-dri-filesystem

%description
VDPAU Backend for Video Acceleration (VA) API with Chromium and VP9 Support.

%prep
%setup -qn %{name}-%{commit}

%build
./autogen.sh --prefix=/usr

make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -delete

%files
%doc AUTHORS COPYING NEWS README.md
%{_libdir}/dri/*.so

%changelog
* Tue Dec 28 2021 Dominic Robinson <dominic@dcrdev.com> 0.7.4-0.2.20211012git509d3b2
- new package built with tito

* Tue Dec 28 2021 Dominic Robinson <dominic@dcrdev.com> - 0.7.4-101
- Re-worked for later versions with VP9 support
* Sat Oct 13 2018 Akarshan Biswas <akarshan.biswas@hotmail.com> - 0.7.4-101
- Initial build
- Add compiler dependencies
