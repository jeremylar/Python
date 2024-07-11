from google.oauth2 import service_account
import googleapiclient.discovery
from googleapiclient.errors import HttpError



SCOPES = ['https://www.googleapis.com/auth/gmail.settings.basic']
SERVICE_ACCOUNT_FILE = '<service account name - in same directory as py file>'

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
credentials.client_email = "<service account email address>"
credentials.token_uri = "https://oauth2.googleapis.com/token"


userKey = '<user email address to find delegates>'       
delegated_credentials = credentials.with_subject(userKey)
service = googleapiclient.discovery.build('gmail', 'v1', credentials=delegated_credentials)

try:
    results = service.users().settings().delegates().list(userId = userKey).execute()
    print(results)
except HttpError as error:
   # TODO(developer) - Handle errors from gmail API.
   print(f'An error occurred: {error}')
