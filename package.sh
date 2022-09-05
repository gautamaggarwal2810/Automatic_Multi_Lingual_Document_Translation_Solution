#!/bin/ksh
rm -rf target/
mkdir target
cd target
cp -r ../src/* .
zip -r translation-helix.zip .
