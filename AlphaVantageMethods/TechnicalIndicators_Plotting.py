from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt
from Environment_Settings import settings

ti = TechIndicators(key= settings.API_KEY, output_format='pandas')
data, meta_data = ti.get_bbands(symbol='MSFT', interval='60min', time_period=60)
data.plot()
plt.title('BBbands indicator for  MSFT stock (60 min)')
plt.show()