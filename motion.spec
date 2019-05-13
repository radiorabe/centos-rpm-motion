Name:		motion
Version:	4.2.2
Release:	0.2%{?dist}
Summary:	Motion, a software motion detector. 

Group:		Appications
License:	GPLv2
URL:		https://motion-project.github.io
Source0:	https://github.com/Motion-Project/motion/archive/release-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	motion.service

BuildRequires:	ffmpeg-devel
BuildRequires:	gettext
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libmicrohttpd-devel
BuildRequires:	libzip-devel

%description
Motion is a program that monitors the video signal from one or more cameras
and is able to detect if a significant part of the picture has changed. Or
in other words, it can detect motion.

%pre
getent group motion >/dev/null || groupadd -r motion
getent passwd motion >/dev/null || \
    useradd -r -g motion -d /var/lib/motion -m \
    -c "motion system user account" motion
exit 0

%prep
%setup -q -n motion-release-%{version}

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install
/bin/install -d %{buildroot}%{_exec_prefix}/lib/systemd/system/
/bin/install -c %{SOURCE1} -m 644 %{buildroot}%{_exec_prefix}/lib/systemd/system/
%find_lang %{name}

%files -f %{name}.lang
%doc README.md CHANGELOG COPYING CREDITS 
%doc %{_docdir}/%{name}
%{_mandir}/man1/motion.1.gz
%config(noreplace) %{_sysconfdir}/%{name}/motion-dist.conf
%config(noreplace) %{_sysconfdir}/%{name}/camera*dist.conf
%{_bindir}/motion
%{_datarootdir}/%{name}/
%{_exec_prefix}/lib/systemd/system/motion.service
