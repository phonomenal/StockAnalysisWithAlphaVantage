from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
from Environment_Settings import settings
import json

#Name of User, for tracking purposes
userName = 'jameha'

#stock symbol

stockSymbol = 'AMD'

#Number of rows you want returned from the query
rowsOfData = 104

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
    dObject = dataWeeksReturned.to_dict(orient='records')

    i = 0
    for entry in dObject:
        while i < rowsOfData:
            entry['symbol'] = stockSymbol
            entry['username'] = userName
            entry['date'] = dataDatesReturned[i]
            i += 1

    pprint(dataWeeksReturned)

    print(dObject)
else:
    print("Rows of data requested did not match what was returned, /n Ensure you are using either compact or full outputsizes /n Exiting")
    exit()
