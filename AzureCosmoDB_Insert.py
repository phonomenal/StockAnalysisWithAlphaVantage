import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.errors as errors
import azure.cosmos.http_constants as http_constants
import pymongo
from Environment_Settings import settings
import os
import datetime

uri = settings.DB_CONNECTION_STRING
client = pymongo.MongoClient(uri)

mydb = client["AlphaVantageDataBase"]
mycol = mydb["AlphaVantageLists"]

mydict = {"symbol": "Ivan", "name": "Le", "amount": 37.60 }

myStockDict = {'1. open': 33.73, '2. high': 33.9, '3. low': 32.7, '4. close': 33.03, '5. volume': 78700076.0, 'symbol': 'AMD', 'username': 'jameha', 'date': new
Date(2019, 10, 29)}

x = mycol.insert_one(myStockDict)

print("Item inserted to collection with id: " + x.inserted_id)