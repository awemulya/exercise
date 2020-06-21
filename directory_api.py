from googleapiclient import discovery
from google.oauth2 import service_account
SCOPES = ['https://www.googleapis.com/auth/admin.directory.user',
          'https://www.googleapis.com/auth/admin.directory.group',
          'https://www.googleapis.com/auth/admin.directory.group.member']
SERVICE_ACCOUNT_FILE = 'SA.json'


def get_users():
    user_email = 'ron@test.authomize.com'
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    delegated_credentials = credentials.with_subject(user_email)
    service = discovery.build('admin', 'directory_v1', credentials=delegated_credentials)

    service.users().makeAdmin(userKey=user_email, body={"status": True}).execute()
    results = service.users().list().execute()
    users = results.get('users', [])

    if not users:
        print('No users in the domain.')
    else:
        print('Users:')
        for user in users:
            print(u'{0} ({1})'.format(user['primaryEmail'],
                                      user['name']['fullName']))


def get_groups():
    user_email = 'ron@test.authomize.com'
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    delegated_credentials = credentials.with_subject(user_email)
    service = discovery.build('admin', 'directory_v1', credentials=delegated_credentials)

    service.users().makeAdmin(userKey=user_email, body={"status": True}).execute()
    results = service.groups().list().execute()
    groups = results.get('groups', [])

    if not groups:
        print('No groups in the domain.')
    else:
        print('groups:')
        for group in groups:
            print(group.__dict__)


def get_user_in_groups(group):
    user_email = 'ron@test.authomize.com'
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    delegated_credentials = credentials.with_subject(user_email)
    service = discovery.build('admin', 'directory_v1', credentials=delegated_credentials)

    service.users().makeAdmin(userKey=user_email, body={"status": True}).execute()
    results = service.members().list(groupKey=group).execute()
    members = results.get('members', [])

    if not members:
        print('No members in the group.')
    else:
        print('members:')
        for member in members:
            print(member.__dict__)

