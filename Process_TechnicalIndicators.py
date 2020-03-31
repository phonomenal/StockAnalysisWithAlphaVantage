from AV_TechIndicators import AlphaVantageAPI

symbol = 'MSFT'

av_API = AlphaVantageAPI(symbol)

#Run BBANDS method, returning array of data and metadata of the request
bbands_TimePeriod = 60
techIndicators_bbands = av_API.techIndicator_get_bbands(bbands_TimePeriod)

#Run RSI method, returning array of data and metadata of the request  
rsi_TimePeriod = 60
techIndicators_RSI = av_API.techIndicator_get_RSI(rsi_TimePeriod)

#Run MCAD method
techIndicators_MCAD = av_API.techIndicator_get_MACD()

#Run VWAP, time interval set in minutes
vwap_TimeInterval = '60min'
vwap_DataFormat = 'pandas'
techIndicators_VWAP = av_API.techIndicator_get_VWAP(vwap_TimeInterval, vwap_DataFormat)
if vwap_DataFormat == 'pandas':
    #Get lastest VWAP entries
    techIndicators_VWAP = techIndicators_VWAP[0]

#testing parsing to dict, orienting records
vwap_DictObject = techIndicators_VWAP.to_dict(orient='records')
vwap_DatesParsed = techIndicators_VWAP._stat_axis._data

print(techIndicators_VWAP) 

#Dict object appeneded with symbol and datetime
i = 0
for entry in vwap_DictObject:
    entry['symbol'] = symbol
    entry['date'] = str(vwap_DatesParsed[i])
    i += 1

#Run VWAP, time interval set in minutes
obv_TimePeriod = 'daily'
techIndicators_OBV = av_API.techIndicator_get_OBV(obv_TimePeriod)

#Print Results of each method for a date list
result_Date=['2020-03-27','2020-03-26','2020-03-25']


for date in result_Date:
    print("Technical Indicators for: " + symbol + " on date: " + date)
    print(techIndicators_bbands[0][date])
    print(techIndicators_RSI[0][date])
    print(techIndicators_MCAD[0][date])
    print(techIndicators_OBV[0][date])


print(techIndicators_VWAP[0]) 

