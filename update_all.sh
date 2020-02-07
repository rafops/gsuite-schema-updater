#!/bin/bash

if [ -f "credentials.json" ] ; then
  python3 update_all.py
else
  cat <<EOS

Open the following web page and click “Enable the Directory API”:

https://developers.google.com/admin-sdk/directory/v1/quickstart/python

Login as G Suite administrator

DOWNLOAD CLIENT CONFIGURATION

Copy credentials.json to this folder

EOS
fi
