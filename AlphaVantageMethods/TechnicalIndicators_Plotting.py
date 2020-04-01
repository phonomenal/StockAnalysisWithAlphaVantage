from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt
# Import Environment settings outside out directory
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, 'pathToCode\\AlphaVantageDemo\\Environment_Settings')
import settings

import pathlib
pathlib.Path().absolute()

ti = TechIndicators(key= settings.API_KEY, output_format='pandas')
data, meta_data = ti.get_bbands(symbol='MSFT', interval='60min', time_period=60)
data.plot()
plt.title('BBbands indicator for  MSFT stock (60 min)')
plt.show()