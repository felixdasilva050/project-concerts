import firebase as db
import googleSheets as gSheets
import bot
import re
from flask import jsonify

##receives a two-dimensional list and converts it to a dictionary list and return this list
def buildDataEvents(dataList:list):
    data = [
        {'name':item[0], 
         'date':item[1], 
         'location': item[2]
        } for item in dataList
    ]
    return data

def getAllData():
    return db.readAll()

def getById(id:str):
    dados = db.readAll()
    for code in dados:
        if code == id:
            return dados.get(code)

##checks the database for duplicates and 
# returns a dictionary list with non-duplicate data
# @params(newData) spreadsheet dictionary list
# @params(databaseData) dataBase dictionary list
def verifySimilar(newData, databaseData):
    new_names = [d['name'] for d in newData]
    
    database_names = [databaseData[key]['name'] for key in databaseData]

    indices_to_remove = []

    for i, name in enumerate(new_names):
        if name in database_names:
            indices_to_remove.append(i)

    for index in sorted(indices_to_remove, reverse=True):
        del newData[index]

    return newData

##read the spreadsheet to populate the database with new data (if any)
def updateDatabase():
    dataList = buildDataEvents(gSheets.getValuesSpreedSheet('2023','A2','D'))
    dataDb = getAllData()
    if(dataList != [] and dataDb != None):
        verifySimilar(dataList, dataDb)
        
    if(dataList != []):
        for elemento in dataList:
            db.create(elemento)
    return dataList

#starts the bot filling the entire spreadsheet
def executeBot():
    events_pernambuco = gSheets.convertDesignPattern(bot.get_pernambuco_events())
    oldList = gSheets.getValuesSpreedSheet('2023', 'A2','D')
    newList = gSheets.checkDuplicity(oldList,events_pernambuco)
    rowEmpty = gSheets.getFirstRowEmpty('2023')
    gSheets.setValuesSpreedSheet('2023',rowEmpty,newList)

def getAllByLocation(location:str):
    dados = db.readAll()
    padrao = re.compile(re.escape(location), re.IGNORECASE)
    response = []
    for code in dados:
        if(re.search(padrao, dados.get(code).get('location'))):
            response.append(dados.get(code))

    return response

def getAllByDate(date_str: str):
    dados = db.readAll()
    response = []
    dateConverted = date_str.replace('-','/')
    for code in dados:
        data = dados.get(code).get('date')
        
        pattern = re.compile(fr'\b{re.escape(date_str)}\b|\b\d{{2}}/{re.escape(date_str)}\b')

        if re.search(pattern, data):
            response.append(dados.get(code))

    return response