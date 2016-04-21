RPM=rpm
ALL=$(RPM)
WDIR=$(HOME)
VER=0.9
REV=20
RPMVERSION=$(VER)-$(REV)
GOGSVERSION=gogs-$(VER).$(REV)
GOGSDIR=../../gogs
##############################################################################
# standard targets (all, clean, installrpm,removerpm)

all: $(ALL)

clean:
	find . -type f -name "*~" -exec rm  -f  {} \;
	(rm -rf $(WDIR)/rpmbuild/RPMS/x86_64/gogs-$(RPMVERSION).x86_64.rpm \
           $(WDIR)/rpmbuild/SRPMS/gogs-$(RPMVERSION).src.rpm \
          $(GOGSDIR)/$(GOGSVERSION).tar.gz  $(GOGSVERSION).tar.gz  $(GOGSVERSION))
 

# rpm making automation for CentOS/RHEL.
ARCH ?= $(shell arch)
ifeq ($(ARCH),x86_64)
RPM_ARCH := x86_64
else
    ifeq ($(ARCH),i686)
RPM_ARCH := i386
    else
$(error Unknown arch "$(ARCH)".)
    endif
endif

# RPM_ARCH := noarch
tball: 
	# @create gogs tar ball.
	(cd $(GOGSDIR);rm -f $(GOGSVERSION))
	(cd $(GOGSDIR);ln -s . $(GOGSVERSION))
	(cd $(GOGSDIR);tar zhcf $(GOGSVERSION).tar.gz --exclude $(GOGSVERSION)/$(GOGSVERSION).tar.gz --exclude $(GOGSVERSION)/$(GOGSVERSION) --exclude RCS --exclude CVS --exclude build-* --exclude *~ --exclude .git* $(GOGSVERSION)/)
	(cd $(GOGSDIR);rm -f $(GOGSVERSION))
	# build the rpm using rpmbuild from ./rmbuild as topdir
	rm -rf ${WDIR}/rpmbuild && mkdir -p ${WDIR}/rpmbuild/SOURCES
	cp  $(GOGSDIR)/$(GOGSVERSION).tar.gz ${WDIR}/rpmbuild/SOURCES/$(GOGSVERSION).tar.gz
build: tball
	rpmbuild -bb --define "_topdir ${WDIR}/rpmbuild"   ./gogs.spec
rpm:  tball
	rpmbuild -ba --define "_topdir ${WDIR}/rpmbuild"   ./gogs.spec
gitcommit:
	git commit -a -m "lazy commit via make gitpush"

gitpush: gitcommit
	git push origin develop

installrpm: 
	sudo $(RPM) -Uvh $(HOME)/rpmbuild/RPMS/x86_64/gogs-$(RPMVERSION).x86_64.rpm
removerpm:
	sudo $(RPM) -e gogs

-include Makefile.my # Put your extra targets for your environment in this makefile.
