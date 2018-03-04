#!/bin/bash

SCRIPT_DIR=`dirname $0`
BASE_DIR=`realpath ${SCRIPT_DIR}/..`

. ${SCRIPT_DIR}/python-google-speak-debian-setup.sh

ROOT_DIR=${BASE_DIR}/debian/${DEBIAN_PACKAGE}

TMP_DIR=${ROOT_DIR}/${REL_TMP_DIR}

mkdir -p ${TMP_DIR}

pushd . > /dev/null

# Baue PIP package python-google-speak
cd ${BASE_DIR}
python3 ./setup.py sdist
cp dist/${PY_PACKAGE} ${TMP_DIR}

cp -r ${BASE_DIR}/debian/DEBIAN ${ROOT_DIR}
cp bin/python-google-speak-debian-setup.sh ${TMP_DIR}/python-google-speak-debian-setup.sh

rm -f debian/${DEBIAN_PACKAGE}.deb
dpkg-deb --build debian/${DEBIAN_PACKAGE}
