# Native package script for Gogs

This repository contains scripts for packaging `gogs` into various platform-specific native packages.
The following platforms are currently supported:

  * Fedora/CentOS/RedHat RPM: `rpm/`

The following are possible  platforms:

  * Windows MSI: `msi/`
  * Debian/Ubuntu DEB: `deb/`
  * OS X PKG: `osx/`
  * OpenSUSE RPM: `suse/`
  * Oracle Solaris: `suse/`

Steps for Centos 7: 
  *  make sure rpmbuild environment in your home directory is setup.
  *  Put gogs and packaging repos at same level.

```
       packaging
       ├── LICENSE
       ├── README.md
       └── rpm
           ├── gogs.service
           ├── gogs.spec
           └── Makefile

        gogs
        ├── cmd
        ├── conf
        ├── docker
        ├── Dockerfile
        ├── Dockerfile.rpi
        ├── glide.lock
        ├── glide.yaml
        ├── gogs              # generated gogs exe file.
        ├── gogs.go
        ├── LICENSE
        ├── Makefile
        ├── models
        ├── modules
        ├── packager
        ├── public
        ├── README.md
        ├── README_ZH.md
        ├── routers
        ├── scripts
        └── templates
```

  *  "cd gogs" to genereate gogs binary at gogs top directory.
     * go get -u -tags "sqlite tidb pam cert" github.com/gogits/gogs
     * go build  -x tags "sqlite tidb pam cert"  .
  *  "cd ../packaging" to creating rpm.
     *  "make -n" to see the dryrun 
     *  "make" or "make rpm" to create gogs rpm.

