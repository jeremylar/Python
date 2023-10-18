"""This Script outputs in CLI the signature for the email address in MAIN
#Make sure current oath libraries are installed - Windows*: pip3 install --upgrade google-api-python-client oauth2client
Service_Account_File has this structure:
{
    "type": "service_account",
    "project_id": "project-name",
    "private_key_id": "Key name from console.cloud.google.com from the service account/permissions page",
    "private_key": "copy paste the actual key here",
    "client_email": "email from console.cloud.google.com service accounts/details page",
    "client_id": "Unique ID from console.cloud.google.com service accounts/details page",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/[client email for service]"
}
"""

from __future__ import print_function

from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def update_signature(userkey):
    SERVICE_ACCOUNT_FILE = 'msp-signature-reset-eab0440c7d28.json'
    
    api_name='gmail'
    api_version='v1'
    SCOPES1 = ["https://www.googleapis.com/auth/gmail.settings.basic"]
    
    
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE,scopes=SCOPES1) 
    delegated_credentials = credentials.with_subject(userKey)
    
    # Build the service object.

    try:
        # create gmail api client
        service = build(api_name, api_version, credentials=delegated_credentials)
        
        primary_alias = None

        aliases = service.users().settings().sendAs().list(userId=userkey).execute()
        for alias in aliases.get('sendAs'):
            if alias.get('isPrimary'):
                primary_alias = alias
                break
        
        print(primary_alias['signature'])


    except HttpError as error:
        print(F'An error occurred: {error}')
        result = None


if __name__ == '__main__':
    userKey="email@domain.com"
    update_signature(userKey)