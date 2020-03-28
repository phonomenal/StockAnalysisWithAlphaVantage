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

class AzureCosmosCRUD() :
    
    def __init__(self, dataObjectReturned):
        self.dataObjectReturned = dataObjectReturned

    def insertDataToMongo(self):
        
        x = mycol.insert_many(self.dataObjectReturned)