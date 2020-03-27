import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
import azure.cosmos.http_constants as http_constants
import pymongo
from Environment_Settings import settings
import os

uri = settings.DB_CONNECTION_STRING
client = pymongo.MongoClient(uri)

mydb = client["AlphaVantageDataBase"]
mycol = mydb["AlphaVantageLists"]

mydict = {"symbol": "Ivan", "name": "Le", "amount": 37.60 }

x = mycol.insert_one(mydict)

print("Item inserted to collection with id: " + x.inserted_id)