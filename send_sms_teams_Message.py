import requests,json,sys
from twilio.rest import Client
import time
import pymsteams


myTeamsMessage = pymsteams.connectorcard("https://<teamschannelwebhookurl>")

headers = {"Content-type": "application/json"}

status = sys.argv[1]
client = sys.argv[2]
location = sys.argv[3]
systemname = sys.argv[4]
fallbacktxt = "Server: "+ systemname + " is " + status + " for Client: " + client +" at Location: " + location
pretext = "<message/subject>"

myTeamsMessage.title(fallbacktxt)
myTeamsMessage.text("Status: " + status)
myTeamsMessage.send()



account_sid = <account_sid>
auth_token = <auth_token>
client = Client(account_sid, auth_token)
smstolist = ['<Number List>']
smsbody = '<sms Content>'
smsfrom = '<twilionumber>'
for smsnum in smstolist:
    message = client.messages.create(
                              body= pretext+" - "+fallbacktxt,
                              from_= smsfrom,
                              to= smsnum
                          )
    time.sleep(1)
    print(message.sid)
