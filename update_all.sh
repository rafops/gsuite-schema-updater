#!/bin/bash

if [ -f "credentials.json" ] ; then
  python3 update_all.py
else
  cat <<EOS

1. Open the following web page and click “Enable the Directory API”:

   https://developers.google.com/admin-sdk/directory/v1/quickstart/python

2. Login as G Suite administrator

3. Click DOWNLOAD CLIENT CONFIGURATION

4. Copy credentials.json to this folder

5. Create and configure `config.json' from `config.json.example`

6. Run ./update_all.sh

EOS
fi
