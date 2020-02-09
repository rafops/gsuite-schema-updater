#!/bin/bash

# Ubuntu
if [ -n "$(uname -a | grep "^Linux ubuntu")" ] ; then
  if [ -z "$(command -v docker)" ] ; then
    echo -n "Install Docker? [Yn]: "
    read answer
    if [ "${answer}" == "Y" ] ; then
      sudo apt install docker-ce docker-ce-cli containerd.io -y
    fi
  fi
fi

# Docker available except when using docker-machine
if [ -n "$(command -v docker)" ] && [ -z "$(command -v docker-machine)" ] ; then
  ./build.sh
  exit 0
fi

# MacOS/Homebrew/Python3
if [ -z "$(command -v python3)" ] ; then
  if [ -z "$(command -v brew)" ] ; then
    echo -n "Install Homebrew? [Yn]: "
    read answer
    if [ "${answer}" == "Y" ] ; then
      /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    fi
  fi

  echo -n "Install Python 3? [Yn]: "
  read answer
  if [ "${answer}" == "Y" ] ; then
    brew install python3
  fi
fi

python3 -m pip install --upgrade pip google-api-python-client google-auth-httplib2 google-auth-oauthlib
