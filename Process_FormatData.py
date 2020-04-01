from Environment_Settings import settings

class DataFormatter() :
    
    def __init__(self, symbol):
        self.symbol = symbol

    def format_DataFrameToDict(self, dataFrameObj):
        #Variable to DataFrame and MetaData
        data_DFObj = dataFrameObj[0]
        metaData_DFObj = dataFrameObj[1]

        #Dataframe parsing to dict, orienting records and grabbing date values
        response_DictObject = data_DFObj.to_dict(orient='records')
        response_DatesParsed = data_DFObj._stat_axis._data

        lenOfDict = len(response_DictObject)
        lenofDates = response_DatesParsed.size

        #check that the parse object len matches len of dates returned
        if lenOfDict == lenofDates:
            i = 0
            for entry in response_DictObject:
                entry['symbol'] = self.symbol
                entry['date'] = str(response_DatesParsed[i])
                i += 1
        return response_DictObject
        
