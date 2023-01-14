from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime
import time

SERVICE_ACCOUNT_FILE = 'json_file_from_google_credentials.json'

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        
service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()        


data_from_api = 'https://api.dane.gov.pl/resources/44100,liczba-osob-ktore-przystapiyzday-egzamin-maturalny/file'        
spreadsheet_id1 = '1ksRYtgapnIE7pOs5OBjk4zFUOndT3p_IUjXWV9rM5BI'
sheet_id1 = 1256508534

date = datetime.today().strftime('%Y-%m-%d') #'YYYY-MM-DD'


RUN1 = [['=IMPORTDATA("'+str(data_from_api)+'";";")',"","","","","","","","data"],
        ["","","","","","","","",str(date)]]
request1 = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id1,
                                                  range="BONUS_SOURCE!A1",
                                                  valueInputOption="USER_ENTERED",
                                                  body={"values": RUN1}).execute()
time.sleep(3)
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
request2 = service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id1,
                                              body=RUN2).execute()
print(request2)


print("(All Operations - Successfully!)")
