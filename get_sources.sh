#!/bin/bash

ORIGNAME=foobnix
GIT_REVISION=5295204

wget https://github.com/$ORIGNAME/$ORIGNAME/tarball/$GIT_REVISION
mv $GIT_REVISION $ORIGNAME-$ORIGNAME-$GIT_REVISION.tar.gz
