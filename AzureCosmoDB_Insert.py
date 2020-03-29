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
        
        mycol.insert_many(self.dataObjectReturned)

    #not sure how to update many properly when there are dupe entries in the database
    def updateDataToMongo(self):
        
        latestDate = self.dataObjectReturned[0]
        latestDate['date']

        mycol.update_many(filter=({'date': {'$lt': latestDate}}), update={'$set':self.dataObjectReturned}, upsert=True)    
    
