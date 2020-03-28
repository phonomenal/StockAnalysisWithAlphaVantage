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

myStockDict = {'1. open': 33.73, '2. high': 33.9, '3. low': 32.7, '4. close': 33.03, '5. volume': 78700076.0, 'symbol': 'AMD', 'username': 'jameha', 'date': '2019-10-29'}

myStockDictMultiple = [{'1_open': 46.32, '2_high': 47.975, '3_low': 45.9, '4_close': 46.58, '5_volume': 74273700.0, 'symbol': 'AMD', 'username': 'jameha', 'date': '2020-03-27'}, {'1_open': 45.78, '2_high': 47.5, '3_low': 45.4, '4_close': 47.5, '5_volume': 73276429.0, 'symbol': 'AMD', 'username': 'jameha', 'date': '2020-03-26'}, {'1_open': 46.79, '2_high': 47.875, '3_low': 44.425, '4_close': 44.63, '5_volume': 93760389.0, 'symbol': 'AMD', 'username': 'jameha', 'date': '2020-03-25'}]

# x = mycol.insert_many(myStockDictMultiple)

query_GetUserStockGtDate = { "username": "jameha", "symbol":"AMD", "date": { "$gt" : "2020-03-03"} }

#use aggreate method to sort queries
results_SortedByAsc = mycol.aggregate([{
    "$match": query_GetUserStockGtDate
},
{
    "$sort": {
        "2_high": pymongo.ASCENDING
    }
}])

#Convert Cursor Deque to List
results_List = list(results_SortedByAsc)

result_MaxHigh = results_List[-1]

results_MinHigh = results_List[0]

print("The max high price during this time frame was on: " + result_MaxHigh['date'])
print("At the price of: " + str(result_MaxHigh['2_high']))

print("The min high price during this time frame was on: " + results_MinHigh['date'])
print("At the price of: " + str(results_MinHigh['2_high']))



class AzureCosmosCRUD() :
    
    def __init__(self, dataObjectReturned):
        self.dataObjectReturned = dataObjectReturned

    def insertDataToMongo(self):
        
        x = mycol.insert_many(self.dataObjectReturned)