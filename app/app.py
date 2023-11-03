from flask import Flask, jsonify
import managerDB as manager
import time

APP = Flask(__name__)

@APP.route('/eventos', methods=['GET'])
def getAllEvent():
    response = jsonify(manager.getAllData())
    response.headers['Content-Type']='application/json; charset=utf-8'
    return response

@APP.route('/eventos/<string:id>', methods=['GET'])
def getById(id:str):
    response = jsonify(manager.getById(id))
    response.headers['Content-Type']='application/json; charset=utf-8'
    return response

@APP.route('/eventos/date/<string:date>', methods=['GET'])
def getByDate(date:str):
    response = jsonify(manager.getAllByDate(date))
    response.headers['Content-Type']='application/json; charset=utf-8'
    return response

@APP.route('/eventos/location/<string:location>', methods=['GET'])
def getByLocation(location:str):
    response = jsonify(manager.getAllByLocation(location))
    response.headers['Content-Type']='application/json; charset=utf-8'
    return response

@APP.route('/reloadDataBase/<string:password>', methods=['GET'])
def reloadDataBase(password):
    if(password != 'recarreg@tudoAi321'):
        response = jsonify({'message':'access denied'})
        return response
    else: 
        manager.executeBot()
        time.sleep(10)
        manager.updateDatabase()
        response = jsonify({'message':'access granted'})
        return response
        


APP.run(port=5000, host='localhost')