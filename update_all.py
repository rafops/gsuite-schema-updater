from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from pprint import pprint
import json

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/admin.directory.user']


def main():
    # Configuration
    customAttr = {}
    with open('config.json') as f:
      customAttr = json.load(f)

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=34373)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('admin', 'directory_v1', credentials=creds)

    # Call the Admin SDK Directory API
    print('Getting users in the domain...')
    results = service.users().list(customer='my_customer', projection='full').execute()
    users = results.get('users', [])

    if not users:
        print('No users in the domain.')
    else:
        for user in users:
            print('=============================================')
            print(u'{0} ({1})'.format(user['primaryEmail'],
                user['name']['fullName']))
            userKey = user['primaryEmail']
            customSchemas = {}
            if 'customSchemas' in user:
                customSchemas = user['customSchemas']
                print('customSchema before:')
                pprint(user['customSchemas'])

            category = {}
            if customAttr['category'] in customSchemas:
                category = customSchemas[customAttr['category']]
            category[customAttr['name']] = [{'type': 'work', 'value': customAttr['value']}]
            customSchemas[customAttr['category']] = category
            user['customSchemas'] = customSchemas
            print('customSchema after:')
            pprint(user['customSchemas'])

            service.users().patch(userKey=userKey, body=user).execute()


if __name__ == '__main__':
    main()