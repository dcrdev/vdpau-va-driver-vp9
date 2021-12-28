#!/bin/bash
DIST="fc35"
ARCH="x86_64"
MOCK_CONFIG="fedora-34-x86_64"
SOURCE=`spectool -g -f -C ./ ./vdpau-va-driver-vp9.spec | grep Downloaded | sed 's/Downloaded: //g'`

md5sum "$SOURCE" > sources

mock -r "/etc/mock/$MOCK_CONFIG.cfg" --clean
mock -r "/etc/mock/$MOCK_CONFIG.cfg" --init

mock -r "/etc/mock/$MOCK_CONFIG.cfg" --spec=./vdpau-va-driver-vp9.spec --sources=. --resultdir=./build/$DIST/SRPMS --buildsrpm && \
mock -r "/etc/mock/$MOCK_CONFIG.cfg" rebuild ./build/$DIST/SRPMS/*.src.rpm --resultdir=./build/$DIST/$ARCH
