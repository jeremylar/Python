from google.oauth2 import service_account
import googleapiclient.discovery
from googleapiclient.errors import HttpError



SCOPES = ['https://www.googleapis.com/auth/gmail.settings.sharing']
SERVICE_ACCOUNT_FILE = '<name of json file in same directory as py>'

credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
credentials.client_email = "<email address of service account>"
credentials.token_uri = "https://oauth2.googleapis.com/token"


userKey = '<user email address to set delegates for>'        
delegate = {"delegateEmail":"<email address we are adding as a delegate>"}
delegated_credentials = credentials.with_subject(userKey)
service = googleapiclient.discovery.build('gmail', 'v1', credentials=delegated_credentials)

try:
    results = service.users().settings().delegates().create(userId = userKey, body=delegate).execute()
    print(results)
except HttpError as error:
   # TODO(developer) - Handle errors from gmail API.
   print(f'An error occurred: {error}')
