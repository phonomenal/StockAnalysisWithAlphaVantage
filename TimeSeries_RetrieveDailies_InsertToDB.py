from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
from Environment_Settings import settings
import json
import AzureCosmoDB_Insert

#Name of User, for tracking purposes
userName = 'jameha'

#stock symbol
stockSymbol = 'MSFT'

#Number of rows(time frame) you want returned from the query
rowsOfData = 10

ts = TimeSeries(key=settings.API_KEY, output_format='pandas')

#The response outputsize is meant to prevent too much data being returned if not neccessary
if rowsOfData > 100:
    data, meta_data = ts.get_daily(symbol=stockSymbol, outputsize='full')
elif rowsOfData < 100:
    data, meta_data = ts.get_daily(symbol=stockSymbol, outputsize='compact')

#This will return the stock data for the time frame, but DOES NOT include the date in each record
ts_DataReturn = data.head(rowsOfData)

#Retrieving the dates of the stock data results
dataDatesReturned = ts_DataReturn._stat_axis.date

#Convets Panda Data Frame to dictionary object for easier processing
ts_DictDataConverted = ts_DataReturn.to_dict(orient='records')

#In the below loop we stitch together the dictionary object with the acceptable field name, date, calculated values, user identifier, etc.
i = 0
for entry in ts_DictDataConverted:
    entry['1_open'] = entry.pop('1. open')
    entry['2_high'] = entry.pop('2. high')
    entry['3_low'] = entry.pop('3. low')
    entry['4_close'] = entry.pop('4. close')
    entry['5_volume'] = entry.pop('5. volume')
    entry['open_close_percent'] = entry['4_close']/entry['1_open'] - 1
    entry['symbol'] = stockSymbol
    entry['username'] = userName
    entry['date'] = str(dataDatesReturned[i])
    i += 1

#Print out the results from our query
for tsValue in ts_DataReturn:
    print(tsValue)

#Insert results to Cosmos DB, feel free to comment out the below two lines if you do not have your database configured
AzCosmos = AzureCosmoDB_Insert.AzureCosmosCRUD(ts_DictDataConverted)
AzCosmos.insertDataToMongo()
