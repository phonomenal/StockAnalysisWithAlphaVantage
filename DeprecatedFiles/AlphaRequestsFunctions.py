import json
import requests
import re, datetime
from Environment_Settings import settings

class AlphaRequests() :
    
    def __init__(self, tickerSymbol):
        self.tickerSymbol = tickerSymbol

    def getTodayHighPrice(self):
        apiKey = settings.API_KEY
        response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + self.tickerSymbol + "&apikey=" + apiKey)

        json_data = json.loads(response.text)
        
        if len(json_data) != 1:  

            metadata = json_data["Meta Data"]

            lastRefreshDate = metadata["3. Last Refreshed"]

            match = re.search('\d{4}-\d{2}-\d{2}', lastRefreshDate)
            date = datetime.datetime.strptime(match.group(), '%Y-%m-%d').date()

            lastRefreshDateConvert = date.strftime('%Y-%m-%d')

            timeSeriesDay = json_data["Time Series (Daily)"]
            
            timeSeriesToday = timeSeriesDay[lastRefreshDateConvert]

            timeSeriesTodayHigh = timeSeriesToday["2. high"]
            
            stockResult = {"price": timeSeriesTodayHigh, "time": lastRefreshDate}

            return stockResult
        else:
            invalidAPI = "Stock ticker not valid"
            return invalidAPI

    def getQuoteLatest(self):
        apiKey = settings.API_KEY
        response = requests.get("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=" + self.tickerSymbol + "&apikey=" + apiKey)

        json_data = json.loads(response.text)

        globalQuote = json_data["Global Quote"]

        return globalQuote