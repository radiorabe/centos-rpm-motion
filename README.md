# centos-rpm-motion
CentOS 7 RPM Specfile for [motion](https://motion-project.github.io) which is part of [RaBe's video package collection](https://build.opensuse.org/project/show/home:radiorabe:video).

## Usage
There are pre-built binary packages for CentOS 7 available on [Radio RaBe's OBS video package repository](https://build.opensuse.org/project/show/home:radiorabe:video), which can be installed as follows:

```bash
yum install -y \
  epel-release \
  http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm

curl -o /etc/yum.repos.d/home:radiorabe:video.repo \
     http://download.opensuse.org/repositories/home:/radiorabe:/video/CentOS_7/home:radiorabe:video.repo

yum install motion
```
