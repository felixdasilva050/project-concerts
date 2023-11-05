import requests
import json

#If you prefer, change the firebase URL
URL_FIREBASE = 'https://concerts-estacio-default-rtdb.firebaseio.com/'

##begin CRUD 
def create(dados:dict):
    request = requests.post(f'{URL_FIREBASE}/events/.json', data= json.dumps(dados))
    if(request.status_code != 200):
        print(request.text)

def readAll():
    request = requests.get(f'{URL_FIREBASE}/events/.json')
    if(request.status_code != 200):
        print((f'code error: {request} text: {request.text}'))
    return request.json()

def updateById(dados:dict, id:str):
    request = requests.patch(f'{URL_FIREBASE}/events/{id}/.json', data= json.dumps(dados))
    if(request.status_code != 200):
        print((f'code error: {request} text: {request.text}'))

def deleteById(id:str):
    request = requests.patch(f'{URL_FIREBASE}/events/{id}/.json')
    if(request.status_code != 200):
        print((f'code error: {request} text: {request.text}'))

##end CRUD
