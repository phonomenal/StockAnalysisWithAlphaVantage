from AV_TechIndicators import AlphaVantageAPI
from AzureCosmoDB_Insert import AzureCosmosCRUD
from Process_FormatData import DataFormatter

symbol = 'MSFT'

av_API = AlphaVantageAPI(symbol)
df_Obj = DataFormatter(symbol)

#Run RSI method, returning array of data and metadata of the request  
rsi_TimePeriod = 60
rsi_DataFormat = 'pandas'
techIndicators_RSI = av_API.techIndicator_get_RSI(rsi_TimePeriod, rsi_DataFormat)
if type(techIndicators_RSI) == tuple:
    rsi_DictObj = df_Obj.format_DataFrameToDict(techIndicators_RSI)
    #Specify the last X indexes of values to be included for insertion
    rsi_DictObjForInsert = rsi_DictObj[-366:]
    az_DB = AzureCosmosCRUD(rsi_DictObjForInsert)
    az_DB.insertDataToMongo()

#Run OBV, time interval set in minutes
obv_TimePeriod = 'daily'
obv_DataFormat = 'pandas'
techIndicators_OBV = av_API.techIndicator_get_OBV(obv_TimePeriod, obv_DataFormat)
if type(techIndicators_OBV) == tuple:
    obv_DictObjForInsert = df_Obj.format_DataFrameToDict(techIndicators_OBV)
    az_DB = AzureCosmosCRUD(obv_DictObjForInsert)
    az_DB.insertDataToMongo()

#Run MCAD method
mcad_DataFormat = 'pandas'
mcad_Interval = 'daily'
mcad_Series = 'close'
techIndicators_MCAD = av_API.techIndicator_get_MACD(mcad_DataFormat, mcad_Interval, mcad_Series)
if type(techIndicators_MCAD) == tuple:
    mcad_DictObjForInsert = df_Obj.format_DataFrameToDict(techIndicators_MCAD)

#Run VWAP, time interval set in minutes
vwap_TimeInterval = '60min'
vwap_DataFormat = 'pandas'
techIndicators_VWAP = av_API.techIndicator_get_VWAP(vwap_TimeInterval, vwap_DataFormat)
#Process returned dataframe to a dict object for insert method to db
if type(techIndicators_VWAP) == tuple:
    vwap_DictObjForInsert = df_Obj.format_DataFrameToDict(techIndicators_VWAP)

#Run BBANDS method, returning array of data and metadata of the request
bbands_TimePeriod = 60
bbands_DataFormat = 'pandas'
techIndicators_bbands = av_API.techIndicator_get_bbands(bbands_TimePeriod, bbands_DataFormat)
if type(techIndicators_VWAP) == tuple:
    bbands_DictObjForInsert = df_Obj.format_DataFrameToDict(techIndicators_bbands)

#Process and Send formatted dict obj data to DB

