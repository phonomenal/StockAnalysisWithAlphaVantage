from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
from Environment_Settings import settings
import json
import AzureCosmoDB_Insert

#Name of User, for tracking purposes
userName = 'jameha'

#stock symbol

stockSymbol = 'M'

dictObjTest = [{'5_volume': 62874843.0, 'date': '2020-03-30','symbol':'MSFT', 'username': '330Test'}]

#proper dict format [{'5_volume': 62874843.0, 'date': '2020-03-30','symbol':'MSFT', 'username': '330Test'}]
#{'2020-03-30 15:40': {'VWAP': '158.1427'}, '2020-03-30 15:30': {'VWAP': '158.1427'}, '2020-03-30 14:30': {'VWAP': '158.0904'}, '2020-03-30 13:30': {'VWAP': '157.8660'}, '2020-03-30 12:30': {'VWAP': '157.5682'}, '2020-03-30 11:30': {'VWAP': '157.1056'}}

#Insert results to Cosmos DB, feel free to comment out the below two lines if you do not have your database configured
AzCosmos = AzureCosmoDB_Insert.AzureCosmosCRUD(dictObjTest)
AzCosmos.insertDataToMongo()

print('Insert passed without failure in code')