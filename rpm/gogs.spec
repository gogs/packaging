%define gogsuser git
%define gogsgroup git
%define homedir   /usr/local
Name: gogs
Version: 0.9
Release: 20

Summary: A painless self-hosted Git service
License: MIT
Packager: T.J. Yang <tjyang2001@gmail.com>
Group: Applications/System
Url: https://github.com/gogits/gogs
Source0: gogs-%{version}
BuildArch: x86_64
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: golang
# TBC.
#%if 0%{?el6}
#Requires:  sqlite,mysql-server
#%else
#Requires:  sqlite,mariadb-server,mariadb
#%endif



%description
Gogs is a painless self-hosted Git Service written in Go. It aims to make the easiest, fastest and most painless way to set up a self-hosted Git service. With Go, this can be done in independent binary distribution across ALL platforms that Go supports, including Linux, Mac OS X, and Windows.
Packaging  Note: This version of gogs binary has all "sqlite tidb pam cert" components.

%prep

%setup -q -n %{name}-0.9.20

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
mkdir -p %{buildroot}%{homedir}/gogs
mkdir -p %{buildroot}/var/log/gogs
touch  %{buildroot}/var/log/gogs/gogs.log

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/gogs/log
rsync -azp  .  --exclude=gogs/rpmbuild  --exclude=#.* %{buildroot}%{homedir}/gogs

# Prepare systemd gogs.service file
mkdir -p %{buildroot}/etc/systemd/system
sudo rsync -azpv  %{buildroot}%{homedir}/gogs/contrib/gogs.service  %{buildroot}/etc/systemd/system/gogs.service

%preun
# Graceful shutdown gogs if running
# TBC.
# https://www.redhat.com/archives/rpm-list/2008-September/msg00007.html
%files
%ghost %{_localstatedir}/log/gogs/%{name}.log
%attr(-,%{gogsuser},%{gogsgroup}) %{_localstatedir}/log/gogs/%{name}.log

%ghost /etc/systemd/system/gogs.service
%attr(-,root,root) /etc/systemd/system/gogs.service

%dir %{homedir}/%{name}
%attr(-,%{gogsuser},%{gogsgroup}) %{homedir}/%{name}

%post
# remove all the binary and configs
# hack before fix
rsync -azp  %{homedir}/gogs/contrib/gogs.service  /etc/systemd/system/gogs.service
chown root:root /etc/systemd/system/gogs.service

%changelog
* Sun Apr 17 2016 T.J. Yang <tjyang2001@gmail.com> 1.0
- Initial rpm.spec file for gogs.
- TODOs:
- 1. Adding more logic in pre/post stages.
-    1.1 Detect packageio.in's gogs rpm package to avoid conflict.
- 2. Adding Centos 6 support.
- 3. Adding "go build -x"  process into %build.





