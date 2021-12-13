from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
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

    service = build('calendar', 'v3', credentials=creds)

    # AEST GMT Offset
    GMT_OFF = '+11:00'

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    startTime = datetime.datetime.fromisoformat('2021-12-13 18:00:00')
    endTime = datetime.datetime.fromisoformat('2021-12-13 19:00:00')
    
    print('Creating a new event')
    request_body = {
        'summary': 'First Google Calendar Event API Call',
        'start' : {'dateTime': '2021-12-14T18:00:00%s' % GMT_OFF},
        'end' : {'dateTime': '2021-12-14T19:00:00%s' % GMT_OFF},
        'attendees': [
            {'email': 'aiden.gu97@gmail.com'}
        ]
    }
    events_result = service.events().insert(calendarId='primary',
                                            sendUpdates='all', body=request_body).execute()

    if not events_result:
        print('Request failed')
    else:
        print(events_result)


if __name__ == '__main__':
    main()