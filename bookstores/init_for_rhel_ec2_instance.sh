#!/bin/sh
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

yum -y install vim
yum -y install wget
yum -y install python-setuptools

if [ `rpm -qa | grep setuptools` = "" ]; then
    echo '[FAILURE]setuptools is not installed' >&2
    exit 1
else
    echo '[SUCCESS]setuptools installed successfully' >&1
fi

wget https://bootstrap.pypa.io/get-pip.py

python get-pip.py

rm get-pip.py

if [[ ! `pip --version` == *"site-packages"* ]]; then
    echo '[FAILURE]fail to install pip' >&2
    exit 1
else
    echo '[SUCCESS]pip installed successfully' >&1
fi

pip --version

