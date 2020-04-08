import sys 
from flask import *
import json
sys.path.append('./')
from DB_ADMIN import db
from bson.json_util import dumps
import requests

databaseObj1 = db.database()
databaseClient1 = databaseObj1.getClient2()
clientdetail_db = databaseClient1.empdb
clintdb_collection =clientdetail_db.empdetail






def view():
    try:
        return {"data": str([DATA for DATA in clintdb_collection.find({},{"_id":0})])}  
    except:
        return {"status":"Connection issue"}




def add_employee(data):
    try:
        employee = json.loads(data)
        name = employee["name"]
        mail = employee["mail"]
        address = employee["address"]
        mydict = {"name": name, "mail": mail, "address": address }
        clintdb_collection.insert_one(mydict)
        return {'status': "sucess"}
    except:
        return {"status":"failure"}



def update_employee(primary_key,data):
    try:
        employee = json.loads(data)
        name = employee["name"]
        address = employee["address"]
        olddata=  {'mail': primary_key}
        newdata = { "$set": { "name": name,"mail": primary_key, "address": address} }
        clintdb_collection.update_one(olddata, newdata)
        return jsonify({"emplyoee" : "emplyoee updated"})
    except:
        return {"status":"Employee data can not be updated"}

def delete_employee(primary_key):
    try:
        clintdb_collection.delete_one({"mail": primary_key})
        return jsonify({"emplyoee": "employee deleted"})
    except:
        return {"status":"Employee not deleted"}

