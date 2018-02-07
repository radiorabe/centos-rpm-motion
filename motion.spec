Name:		motion
Version:	4.1.1
Release:	1%{?dist}
Summary:	Motion, a software motion detector. 

Group:		Appications
License:	GPLv2
URL:		https://motion-project.github.io
Source0:	https://github.com/Motion-Project/motion/archive/release-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	ffmpeg-devel
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libzip-devel

%description
Motion is a program that monitors the video signal from one or more cameras
and is able to detect if a significant part of the picture has changed. Or
in other words, it can detect motion.


%prep
%setup -q -n motion-release-%{version}


%build
autoreconf -fiv
%configure
make %{?_smp_mflags}


%install
%make_install


%files
%doc README.md CHANGELOG COPYING CREDITS 
%doc %{_docdir}/%{name}
%{_mandir}/man1/motion.1.gz
%config(noreplace) %{_sysconfdir}/%{name}/motion-dist.conf
%config(noreplace) %{_sysconfdir}/%{name}/camera*dist.conf
%{_bindir}/motion
%{_datarootdir}/%{name}/
