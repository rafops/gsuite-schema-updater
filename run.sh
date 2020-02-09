#!/bin/bash

if ! [ -f "config.json" ] ; then
  echo "config.json not found. Please check README.md"
  exit 1
fi

if ! [ -f "credentials.json" ] ; then
  echo "credentials.json not found. Please check README.md"
  exit 1
fi

if [ -n "$(uname -a | grep "^Linux ubuntu")" ] ; then
  docker run -it --rm -v "$(pwd)/:/root/workdir/" gsuite-schema-updater /root/workdir/run.sh
elif [ -n "$(which python3)" ] ; then
  python3 update_target.py
else
  echo "python3 not found. Please check README.md"
  exit 1
fi
