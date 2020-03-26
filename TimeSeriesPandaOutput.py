from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
ts = TimeSeries(key='4PN8G24M5N3NI7GQ', output_format='pandas')
data, meta_data = ts.get_intraday(symbol='GOOG',interval='1min', outputsize='full')
pprint(data.head(2))