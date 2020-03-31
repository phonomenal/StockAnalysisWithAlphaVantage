from AV_TechIndicators import AlphaVantageAPI
from Process_FormatData import DataFormatter

symbol = 'MSFT'

av_API = AlphaVantageAPI(symbol)
df_Obj = DataFormatter(symbol)


#Run MCAD method
techIndicators_MCAD = av_API.techIndicator_get_MACD()

#Run RSI method, returning array of data and metadata of the request  
rsi_TimePeriod = 60
rsi_DataFormat = 'pandas'
techIndicators_RSI = av_API.techIndicator_get_RSI(rsi_TimePeriod, rsi_DataFormat)
if type(techIndicators_RSI) == tuple:
    rsi_DictObjForInsert = df_Obj.format_DataFrameToDict(techIndicators_RSI)

#Run VWAP, time interval set in minutes
vwap_TimeInterval = '60min'
vwap_DataFormat = 'pandas'
techIndicators_VWAP = av_API.techIndicator_get_VWAP(vwap_TimeInterval, vwap_DataFormat)
if vwap_DataFormat == 'pandas':
    #Get lastest VWAP entries
    techIndicators_VWAP = techIndicators_VWAP
#Process returned dataframe to a dict object for insert method to db
if type(techIndicators_VWAP) == tuple:
    vwap_DictObjForInsert = df_Obj.format_DataFrameToDict(techIndicators_VWAP)

#Run BBANDS method, returning array of data and metadata of the request
bbands_TimePeriod = 60
bbands_DataFormat = 'pandas'
techIndicators_bbands = av_API.techIndicator_get_bbands(bbands_TimePeriod, bbands_DataFormat)
if type(techIndicators_VWAP) == tuple:
    bbands_DictObjForInsert = df_Obj.format_DataFrameToDict(techIndicators_bbands)




#Run OBV, time interval set in minutes
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

