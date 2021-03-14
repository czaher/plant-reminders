import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

def sendMessage(smsMessage):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=smsMessage,
            from_=os.environ['TWILIO_NUMBER'],
            to = os.environ['CONTACT_NUMBER'],
        )

messageToSend = 'water your 🪴s'
sendMessage(messageToSend)


