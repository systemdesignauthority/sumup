from __future__ import print_function
import pickle
import os.path
import base64
import email
from bs4 import BeautifulSoup
import re

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Reference
# https://www.geeksforgeeks.org/how-to-read-emails-from-gmail-using-gmail-api-in-python/

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    """Get sales for a given campain.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)

        # request a list of all the messages
        results = service.users().messages().list(userId='me').execute() 
        messages = results.get('messages', [])
        for message in messages:
            
            # Get the message from its id
            txt = service.users().messages().get(userId='me', id=message['id']).execute()
         
            # Use try-except to avoid any Errors
            try:
                # Get value of 'payload' from dictionary 'txt'
                payload = txt['payload']
                headers = payload['headers']
  
                # Look for Subject and Sender Email in the headers
                for d in headers:
                    if d['name'] == 'Subject':
                        subject = d['value']
                    if d['name'] == 'From':
                        sender = d['value']
  
                # Only interested in messages that are new order and from sumupstore.com
                if (subject=="New order") and (sender=="\"SumUp.com\" <no-reply@sumupstore.com>"):

                    # The Body of the message is in Encrypted format. So, we have to decode it.
                    # Get the data and decode it with base 64 decoder.
                    parts = payload.get('parts')[0]
                    data = parts['body']['data']
                    data = data.replace("-","+").replace("_","/")
                    decoded_data = base64.b64decode(data)
  
                    # Now, the data obtained is in lxml. So, we will parse 
                    # it with BeautifulSoup library
                    #soup = BeautifulSoup(decoded_data , "html.parser")
                    #body = soup.body()

                    #decoded_data_clean = decoded_data.decode("utf-8").replace("\r","").replace("\n","").replace(" +","").replace(" +","")
                    decoded_data_clean = re.sub('  {2,}', '', decoded_data.decode("utf-8")).replace("\r","")
                    
                    
                    print(decoded_data_clean)
                    
                    no_pos = decoded_data_clean.find("New order")
                    pm_pos = decoded_data_clean.find("Payment method")
                    dm_pos = decoded_data_clean.find("Delivery method")
                    cd_pos = decoded_data_clean.find("Customer details")
                    pl_pos = decoded_data_clean.find("Pick-up location")
                    vo_pos = decoded_data_clean.find("View order")
                    os_pos = decoded_data_clean.find("Order Summary")
                    t_pos = decoded_data_clean.find("Total")

                    print(decoded_data_clean[no_pos:pm_pos])

                    print("/nline")
                    print(re.findall('#.*',decoded_data_clean[no_pos:pm_pos]))
                    print(re.findall('....\/..\/..',decoded_data_clean[no_pos:pm_pos]))
                    print(re.findall('..:..:..',decoded_data_clean[no_pos:pm_pos]))
                    print(re.findall('[a-zA-Z_]+',decoded_data_clean[no_pos+11:pm_pos]))
                    print("/nline")

                    print(decoded_data_clean[pm_pos:dm_pos])
                    print(decoded_data_clean[dm_pos:cd_pos])
                    print(decoded_data_clean[cd_pos:pl_pos])
                    print(decoded_data_clean[pl_pos:vo_pos])
                    #print(decoded_data_clean[vo_pos:os_pos])
                    print(decoded_data_clean[os_pos:t_pos])
                    print(decoded_data_clean[t_pos:])

                    # Printing the subject, sender's email and message
                    #print("Subject: ", subject)
                    #print("From: ", sender)
                    #print("Message: ", body)
                    #print("Message: ", decoded_data)
                    #print('\n')



            except:
                pass
         
         
            #service.users().messages().get(userId='me', id=message['id']).execute()
            #messagesPayload = messages.get('payload', [])
            #messagesPayload.append )



        #if not labels:
        #    print('No labels found.')
        #    return
        #print('Labels:')
        #for label in labels:
        #    print(label['name'])

        if not messages:
            print('No messages found.')
            return
        print('Messages:')
        for message in messages:
            print(message['id'])

     #   print('Messages Bodys:')
     #   for messageBody in messageBodys:
     #       print(messageBody)


    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()