#!/bin/sh
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

install_pip() {
    if [[ `pip --version` == *"site-packages"* ]]; then
        echo '[ALREADY_INSTALLED]pip already installed' >&1
        return 0
    fi
    #install wget
    yum -y install wget

    #install python setuptools
    if [ "`rpm -qa | grep python-setuptools`" = "" ]; then
        yum -y install python-setuptools
        if [ `rpm -qa | grep python-setuptools` = "" ]; then
            echo '[FAILURE]setuptools is not installed' >&2
            exit 1
        else
            echo '[SUCCESS]setuptools installed successfully' >&1
        fi
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
    sudo pip install virtualenvwrapper
    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/Devel
    source /usr/bin/virtualenvwrapper.sh
    if [[ ! "`pip list | grep virtualenvwrapper`" == *"virtualenvwrapper"* ]]; then
        echo '[FAILURE]fail to install virtualenvwrapper' >&2
    else
        echo '[SUCCESS]virtualenvwrapper installed successfully' >&1
    fi
}
##################################start initializing

yum -y install vim

yum -y install wget

#install pip - start
install_pip

#install Git
install_git

#install virtialenvwraper
install_virtualenvwrapper

##################################end of initializing
