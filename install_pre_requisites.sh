#!/bin/bash

if [ -z "$(which python3)" ] ; then

  if [ -z "$(which brew)" ] ; then
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
