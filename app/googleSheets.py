from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
##page name (the spreadsheet pages have the name of the current year)
SAMPLE_SPREADSHEET_ID = 'WRITE_HERE_THE_SPREADSHEET_ID'

def getSpreadSheet():

    creds = None
    if os.path.exists('secret/token.json'):
        creds = Credentials.from_authorized_user_file('secret/token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'secret/client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('secret/token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('sheets', 'v4', credentials=creds)
    return service.spreadsheets()

def getValuesSpreedSheet(nameSheet:str, rangeInitial:str, rangeFinal:str):
    sheets = getSpreadSheet()
    buildRangeName = nameSheet+'!'+rangeInitial+':'+rangeFinal

    result = sheets.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=buildRangeName).execute()
    return result.get('values', [])

## @param listValues: example [['April','$125.00'], ['May','$15.00']]
## To update an existing value, type the desired cell range. example: rangeInitial = 'A1';
def setValuesSpreedSheet(nameSheet:str, rangeInitial:str, listValues:list):
    sheets = getSpreadSheet()
    buildRangeName = nameSheet+'!'+rangeInitial

    sheets.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                        range=buildRangeName, 
                        valueInputOption='USER_ENTERED',
                        body={'values':listValues}).execute()

## @param year : '2023'
# return empty cell: example return 'A6'
def getFirstRowEmpty(year:str):
    values = getValuesSpreedSheet(year, 'A1', 'D')
    length = len(values)
    return (f'A{length+1}')

##receives a dictionary list and converts it to a two-dimensional list 
# (format that Google Sheets understands)
def convertDesignPattern(dataList):
    data = [[element[key] for key in element] for element in dataList]
    return data

##checks if the same name already exists in the spreadsheet. 
# returns a two-dimensional list with non-duplicate data
def checkDuplicity(oldData, newData):
    indices_to_remove = []
    for i, new_item in enumerate(newData):
        for j, old_item in enumerate(oldData):
            if new_item[0] == old_item[0]:
                indices_to_remove.append(i)
                break
    
    for index in sorted(indices_to_remove, reverse=True):
        del newData[index]
    
    return newData
