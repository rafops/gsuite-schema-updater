#!/bin/bash

if ! [ -f "config.json" ] ; then
  echo "Configuration file config.json not found, please check README.md"
  exit 1
fi

if ! [ -f "credentials.json" ] ; then
  echo "Credentials file credentials.json not found, please check README.md"
  exit 1
fi

if [ -n "$(uname -a | grep "^Linux ubuntu")" ] ; then
  docker run -it --rm -v "$(pwd)/:/root/workdir/" gsuite-schema-updater /root/workdir/run.sh
elif [ -n "$(command -v python3)" ] ; then
  python3 update_target.py
else
  echo "Python3 not installed, please check README.md"
  exit 1
fi
