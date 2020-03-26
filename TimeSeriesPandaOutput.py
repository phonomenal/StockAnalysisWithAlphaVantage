from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
<<<<<<< HEAD
from Environment_Settings import settings
ts = TimeSeries(key=settings.API_KEY, output_format='pandas')
data, meta_data = ts.get_intraday(symbol='GOOG',interval='1min', outputsize='full')
pprint(data.head(2))