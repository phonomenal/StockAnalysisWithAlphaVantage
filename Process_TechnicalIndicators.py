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

result_Date=['2020-03-27','2020-03-26','2020-03-25']

for date in result_Date:
    print("Technical Indicators for: " + symbol + " on date: " + date)
    print(techIndicators_bbands[0][date])
    print(techIndicators_RSI[0][date])
    print(techIndicators_MCAD[0][date])
