from alpha_vantage.sectorperformance import SectorPerformances
import matplotlib.pyplot as plt
from Environment_Settings import settings

sp = SectorPerformances(key=settings.API_KEY, output_format='pandas')
data, meta_data = sp.get_sector()
data['Rank A: Real-Time Performance'].plot(kind='bar')
plt.title('Real Time Performance (%) per Sector')
plt.tight_layout()
plt.grid()
plt.show()