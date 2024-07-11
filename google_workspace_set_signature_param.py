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
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/[client email for]"
}
"""
#edit the html below and save as an html file in same location as py file - save 
"""<div><table border="0" cellpadding="0" cellspacing="0"><tr><td><span style="color:rgb(102,102,102);font-family:garamond,times new roman,serif">Name</span><br></td></tr><tr><td><span style="color:rgb(102,102,102);font-family:garamond,times new roman,serif"><b>Persons Title </b></span></td></tr><tr><td><span style="color:rgb(102,102,102);font-family:garamond,times new roman,serif">Company Name</span><br></td></tr><tr><td><span style="color:rgb(102,102,102);font-family:garamond,times new roman,serif">Company Name</span><br></td></tr><tr><td><span style="color:rgb(102,102,102);font-family:garamond,times new roman,serif">Address Street</span><br></td></tr><tr><td><span style="color:rgb(102,102,102);font-family:garamond,times new roman,serif">Address City</span><br></td></tr><tr><td><span style="color:rgb(102,102,102);font-family:garamond,times new roman,serif">Tel: #</span><br></td></tr><tr><td><span style="color:rgb(102,102,102);font-family:garamond,times new roman,serif">Fax: #</span><br></td></tr><tr><td><span style="color:rgb(17,85,204)"><a href="http://urlcompanywebsite" target="_blank">Company Website</a></span></td></tr><tr><td><span style="color:rgb(102,102,102);font-family:garamond,times new roman,serif">CompanyTagLine!</span><br></td></tr><tr><td><span><a href="http://urlcompanywebsite" target="_blank"><img src="https://urlcompanylogo" width="81" height="96"></a></span><br></td></tr><tr><td><span><a href="https://www.instagram.com/companyname" target="_blank"><img src="instagram url" alt="https://www.instagram.com/explore/locations/url" width="40" height="40"></a></span><span><a href="https://www.linkedin.com/company/url" target="_blank"><img src="https://linkedin image" alt="https://www.linkedin.com/company/url" width="40" height="40"></a></span></td></tr></table></div>"""

from __future__ import print_function
import sys,re
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def update_signature():
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if( len(sys.argv)>0 and re.fullmatch(regex,sys.argv[1])):
        
        SERVICE_ACCOUNT_FILE = '<name of json account file in same directory as py>'

        api_name='gmail'
        api_version='v1'
        SCOPES1 = ["https://www.googleapis.com/auth/gmail.settings.basic"]

        userKey = sys.argv[1]
        credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE,scopes=SCOPES1) 
        delegated_credentials = credentials.with_subject(userKey)

        # Build the service object.

        try:
            # create gmail api client
            service = build(api_name, api_version, credentials=delegated_credentials)

            primary_alias = None

            aliases = service.users().settings().sendAs().list(userId=userKey).execute()
            for alias in aliases.get('sendAs'):
                if alias.get('isPrimary'):
                    primary_alias = alias
                    break
                
            print(primary_alias['signature'])
            f =open("outputsignature.html","w")
            f.write(primary_alias['signature'])
            f.close()


        except HttpError as error:
            print(F'An error occurred: {error}')
            result = None
    else:
        print("Enter Email")

if __name__ == '__main__':
    update_signature()
