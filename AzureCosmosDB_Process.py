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
mycol = mydb["RSI"]

#query we pass to mongodb
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
print("With a volume of: " + str(result_MaxHigh['5_volume']))

print("The min high price during this time frame was on: " + results_MinHigh['date'])
print("At the price of: " + str(results_MinHigh['2_high']))
print("With a volume of: " + str(results_MinHigh['5_volume']))
