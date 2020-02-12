from __future__ import print_function
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import json


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/admin.directory.user']


def main():
    # Configuration
    adminUser = None
    schemas = {}
    targetUsers = []
    with open('config.json') as f:
        config = json.load(f)
        if 'adminUser' in config:
            adminUser = config['adminUser']
        if 'schemas' in config:
            schemas = config['schemas']
        if 'targetUsers' in config:
            targetUsers = config['targetUsers']

    # Credentials
    credentials = Credentials.from_service_account_file(
        'credentials.json',
        subject=adminUser,
        scopes=SCOPES)

    # Service
    service = build('admin', 'directory_v1', credentials=credentials)

    # Users
    print(u'* Listing users in the domain...')
    results = service.users().list(customer='my_customer', projection='full', maxResults=500, showDeleted=0).execute()
    users = results.get('users', [])

    if not users:
        print(u'* No users in the domain.')

    for user in users:
        userEmail = user['primaryEmail']
        print(u'* User is {0} ({1})'.format(user['primaryEmail'], user['name']['fullName']))

        # Skip if user is not a target
        if userEmail not in targetUsers:
            print(u'\t× User is not a target, skipping.')
            continue

        # Update if user is a target
        print(u'\t~ Updating user...')

        customSchemas = {}
        if 'customSchemas' in user:
            customSchemas = user['customSchemas']
            print(u'\t- {0}'.format(user['customSchemas']))

        for category in schemas:
            customSchemas[category] = schemas[category]

        user['customSchemas'] = customSchemas
        service.users().patch(userKey=userEmail, body=user).execute()

        print(u'\t+ {0}'.format(user['customSchemas']))


if __name__ == '__main__':
    main()
