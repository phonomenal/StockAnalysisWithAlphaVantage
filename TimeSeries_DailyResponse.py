from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
from Environment_Settings import settings
import json

ts = TimeSeries(key=settings.API_KEY, output_format='pandas')
data, meta_data = ts.get_weekly(symbol='AMD')
weeksOfData = 25

dataWeeksReturned = data.head(weeksOfData)

#retrieving the dates filtered from the weeks returned
dataDatesReturned = dataWeeksReturned._stat_axis.date

#Convets Panda Data Frame to dictionary object
dObject = dataWeeksReturned.to_dict(orient='records')

dateValue = str(dataDatesReturned[0])

i = 0
for entry in dObject:
    entry['date'] = dataDatesReturned[i]
    i += 1

pprint(dataWeeksReturned)

print(dObject)
