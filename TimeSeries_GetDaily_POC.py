from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
from Environment_Settings import settings
import json
import AzureCosmoDB_Insert

#Name of User, for tracking purposes
userName = 'jameha'

#stock symbol

stockSymbol = 'AMD'

#Number of rows you want returned from the query
rowsOfData = 25

ts = TimeSeries(key=settings.API_KEY, output_format='pandas')
if rowsOfData > 100:
    data, meta_data = ts.get_daily(symbol=stockSymbol, outputsize='full')
elif rowsOfData < 100:
    data, meta_data = ts.get_daily(symbol=stockSymbol, outputsize='compact')

dataWeeksReturned = data.head(rowsOfData)

if dataWeeksReturned.shape[0] == rowsOfData:

    #retrieving the dates filtered from the weeks returned
    dataDatesReturned = dataWeeksReturned._stat_axis.date

    #Convets Panda Data Frame to dictionary object
    dataObjectReturned = dataWeeksReturned.to_dict(orient='records')

    i = 0
    for entry in dataObjectReturned:
        entry['1_open'] = entry.pop('1. open')
        entry['2_high'] = entry.pop('2. high')
        entry['3_low'] = entry.pop('3. low')
        entry['4_close'] = entry.pop('4. close')
        entry['5_volume'] = entry.pop('5. volume')
        entry['symbol'] = stockSymbol
        entry['username'] = userName
        entry['date'] = str(dataDatesReturned[i])
        i += 1

    pprint(dataWeeksReturned)
    print(dataObjectReturned)

    #Insert results to Cosmos DB

    AzCosmos = AzureCosmoDB_Insert.AzureCosmosCRUD(dataObjectReturned)

    AzCosmos.insertDataToMongo()

else:
    print("Rows of data requested did not match what was returned, /n Ensure you are using either compact or full outputsizes /n Exiting")
    exit()
