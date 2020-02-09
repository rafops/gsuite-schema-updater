# G Suite customSchemas mass updater

Install pre-requisites:

```bash
./install.sh
```

[Generate a credentials file](https://developers.google.com/admin-sdk/directory/v1/guides/delegation):

- Open [Service accounts](https://console.developers.google.com/iam-admin/serviceaccounts)
- Click CREATE
- Set project name as “schema-updater” and click CREATE
- Click select a project and select “schema-updater”
- Click CREATE SERVICE ACCOUNT
- Set service account name as “schema-updater” and click CREATE
- In the service account permissions click CONTINUE
- Click CREATE KEY
- Select JSON and click CREATE
- Download the `schema-updater-*.json` file and save it as `credentials.json` on this folder
- Click CLOSE on the private key saved to your computer then click DONE
- In the service account entry click Actions (three dots) and Edit
- In the service account details click SHOW DOMAIN-WIDE DELEGATION
- Check “Enable G Suite Domain-wide Delegation” and click CONFIGURE CONSENT SCREEN
- On the user type select “Internal” and click CREATE
- On the oauth consent screen set application name as “schema-updater” and click Save
- On the left menu click Credentials
- Click edit service account named “schema-updater” by clicking the pencil
- In the service account details click SHOW DOMAIN-WIDE DELEGATION
- Check “Enable G Suite Domain-wide Delegation” and click SAVE
- In the service accounts click Manage service accounts
- In the entry named schema-updater click View Client ID in Domain wide delegation
- Take note of the Client ID and click SAVE
- Go to G Suite domain's [Admin console](http://admin.google.com/)
- Click Security
- Click Advanced settings and Manage API client access
- On the Client Name set the value as the Client ID previously noted
- On the one or more API scopes, set the value as “https://www.googleapis.com/auth/admin.directory.user” and click Authorize
- Open [Service accounts](https://console.developers.google.com/iam-admin/serviceaccounts)
- Click select a project and select “schema-updater”
- On the search bar search for “Admin SDK” and click on Admin SDK result
- In the Admin SDK click ENABLE

Create and configure `config.json` from `config.json.example`

Run:

```bash
./run.sh
```