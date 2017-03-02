#!/bin/sh
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

install_pip() {
    #prerequisite: yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
    if [[ `pip --version` == *"site-packages"* ]]; then
        echo '[ALREADY_INSTALLED]pip already installed' >&1
        return 0
    fi

    yum -y install python2-pip

    if [[ ! `pip --version` == *"site-packages"* ]]; then
        echo '[FAILURE]fail to install pip' >&2
        exit 1
    else
        pip install --upgrade pip
        echo '[SUCCESS]pip installed successfully' >&1
    fi
    
}

install_git() {
    if [[ `git --version` == *"git version"* ]]; then
        echo '[ALREADY_INSTALLED]Git already installed' >&1
        return 0
    fi
    yum -y install curl-devel expat-devel gettext-devel openssl-devel zlib-devel
    yum -y install gcc perl-ExtUtils-MakeMaker

    cd /usr/src
    wget https://www.kernel.org/pub/software/scm/git/git-2.12.0.tar.gz
    tar xzf git-2.12.0.tar.gz

    cd git-2.12.0
    make prefix=/usr/local/git all
    make prefix=/usr/local/git install

    export PATH=$PATH:/usr/local/git/bin
    source /etc/bashrc

    git --version

    if [[ ! `git --version` == *"git version"* ]]; then
        echo '[FAILURE]fail to install Git' >&2
        exit 1
    else
        echo '[SUCCESS]Git installed successfully' >&1
    fi
}

install_virtualenvwrapper() {
    #prerequisite: pip

    if [[ "`pip list | grep virtualenvwrapper`" == *"virtualenvwrapper"* ]]; then
        echo '[ALREADY_INSTALLED]virtualenvwrapper already installed' >&1
        return 0
    fi
    pip install virtualenvwrapper
    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/Devel
    source /usr/bin/virtualenvwrapper.sh
    if [[ ! "`pip list | grep virtualenvwrapper`" == *"virtualenvwrapper"* ]]; then
        echo '[FAILURE]fail to install virtualenvwrapper' >&2
    else
        echo '[SUCCESS]virtualenvwrapper installed successfully' >&1
    fi
}

install_mysql() {

    yum -y install https://dev.mysql.com/get/mysql57-community-release-el7-9.noarch.rpm

    yum -y install mysql-community-server

    systemctl start mysqld.service

    grep 'A temporary password is generated for root@localhost' /var/log/mysqld.log |tail -1 > ~/mysql_password

    echo '[SUCCESS]mysql installed successfully' >&1
}

##################################start initializing

yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

yum -y install deltarpm

yum makecache

yum -y install vim

yum -y install wget

#install pip
install_pip

#install Git
install_git

#install virtialenvwraper
install_virtualenvwrapper

pip install django

install_mysql

yum -y update

##################################end of initializing


#ls -l /etc/yum.repos.d/redhat-rhui.repo
