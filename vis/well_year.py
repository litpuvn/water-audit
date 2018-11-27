import pandas as pd
import numpy as np
from matplotlib.pylab import plt #load plot library


df = pd.read_csv("../data/well_monthly.csv", header=0)

cum_pump = []
wells_label = []
for well_i in range(1, 18):
    data_i = df[df["well"] == well_i]
    data_i.drop(columns=["month", "well"], inplace=True)

    data = data_i.values.flatten()
    effective = data[0:len(data)-1]
    my_cumulative_pump = sum(effective)
    cum_pump.append(my_cumulative_pump)
    print("well:", well_i, "; pump:", my_cumulative_pump)

    wells_label.append('W-' + str(well_i))

well_count = 17
y_pos = np.arange(well_count)

plt.bar(y_pos, cum_pump, align='center', alpha=0.5)
plt.xticks(y_pos, wells_label)
plt.ylabel('Pumped water')
plt.title('Well water pumped in one year 2017')

print("Total water usage:", sum(cum_pump))
plt.show()