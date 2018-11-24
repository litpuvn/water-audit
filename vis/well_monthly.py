import pandas as pd
import numpy as np
from matplotlib.pylab import plt #load plot library


df = pd.read_csv("../data/well_monthly.csv", header=0)

months = range(1, 10)
for well_i in range(1, 18):
    data_i = df[df["well"] == well_i]
    data_i.drop(columns=["month", "well"], inplace=True)

    data = data_i.values.flatten()
    plt.plot(months, data[0:len(data)-1], label="Well " + str(well_i))
    print("well ", well_i)
plt.legend(loc='top left')
plt.xlabel("Month")
plt.ylabel("Pumped Amount")

plt.show()