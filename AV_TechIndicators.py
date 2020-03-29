from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt
from Environment_Settings import settings

class AlphaVantageAPI() :
    
    def __init__(self, symbol):
        self.symbol = symbol

    def techIndicator_get_bbands(self, timePeriod):
        #outputting data in JSON format in the below line
        ti = TechIndicators(key= settings.API_KEY, output_format='json')
        data, meta_data = ti.get_bbands(symbol=self.symbol, interval='daily', time_period=timePeriod)
        return data, meta_data
    
    def techIndicator_get_RSI(self, timePeriod):
        ti = TechIndicators(key= settings.API_KEY, output_format='json')
        data, meta_data = ti.get_rsi(symbol=self.symbol, interval='daily', time_period=timePeriod)
        return data, meta_data