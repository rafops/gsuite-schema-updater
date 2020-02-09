from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from pprint import pprint
import json

# from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/admin.directory.user']


def main():
    # Configuration
    adminUser = None
    customAttr = {}
    targetUsers = []
    with open('config.json') as f:
        config = json.load(f)
        if 'adminUser' in config:
            adminUser = config['adminUser']
        if 'customAttr' in config:
            customAttr = config['customAttr']
        if 'targetUsers' in config:
            targetUsers = config['targetUsers']

    creds = Credentials.from_service_account_file(
        'credentials.json',
        subject=adminUser,
        scopes=SCOPES)

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
            userEmail = user['primaryEmail']

            # Skip if not a target
            if userEmail not in targetUsers:
                print(u'skipping {0} ({1})'.format(user['primaryEmail'], user['name']['fullName']))
                continue

            print(u'updating {0} ({1})'.format(user['primaryEmail'], user['name']['fullName']))

            customSchemas = {}
            if 'customSchemas' in user:
                customSchemas = user['customSchemas']
                print('before:')
                pprint(user['customSchemas'])

            category = {}
            if customAttr['category'] in customSchemas:
                category = customSchemas[customAttr['category']]
            category[customAttr['name']] = [{'type': 'work', 'value': customAttr['value']}]
            customSchemas[customAttr['category']] = category
            user['customSchemas'] = customSchemas
            print('after:')
            pprint(user['customSchemas'])

            service.users().patch(userKey=userEmail, body=user).execute()


if __name__ == '__main__':
    main()