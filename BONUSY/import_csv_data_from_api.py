from google.oauth2 import service_account
from googleapiclient.discovery import build
import time
from datetime import datetime

SERVICE_ACCOUNT_FILE = '/home/blox_land/Desktop/SCV2PL/sars-cov-2-poland.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        
spreadsheet_id1 = '1ksRYtgapnIE7pOs5OBjk4zFUOndT3p_IUjXWV9rM5BI'
sheet_id1 = 0
date = datetime.today().strftime('%Y-%m-%d') #'YYYY-MM-DD'


service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()


result = sheet.values().get(spreadsheetId=spreadsheet_id1,
                            range="BONUS!A1").execute()
values = result.get('values', [])

RUN1 = [['=IMPORTDATA(I1;";")',"","","","","","","","https://api.dane.gov.pl/resources/41967,liczba-osob-ktore-przystapiyzday-egzamin-maturalny/file","data"],
["","","","","","","","","",str(date)]]

request1 = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id1,
                                                  range="BONUS!A1",
                                                  valueInputOption="USER_ENTERED", body={"values": RUN1}).execute()
time.sleep(10)
print(request1)


RUN2 = {'requests': [
    {'copyPaste': {
        'source': {
            'sheetId': sheet_id1,
            'startRowIndex': 0,
            'endRowIndex': 885,
            'startColumnIndex': 0,
            'endColumnIndex': 8,
        },
        "destination": {
            'sheetId': sheet_id1,
            'startRowIndex': 0,
            'endRowIndex': 885,
            'startColumnIndex': 0,
            'endColumnIndex': 8,
        },
        "pasteType": "Paste_Values",

    }},

]}

request2 = service.spreadsheets().batchUpdate(
        spreadsheetId=spreadsheet_id1, body=RUN2).execute()

print(request2)
