import pandas as pd
import numpy as np
from matplotlib.pylab import plt #load plot library


df = pd.read_csv("../data/well_monthly_2017.csv", header=0)

months = range(1, 13)
for well_i in range(1, 18):
    data_i = df[df["well"] == well_i]
    data_i.drop(columns=["month", "well"], inplace=True)

    data = data_i.values.flatten()
    plt.plot(months, data, label="Well " + str(well_i))
    print("well ", well_i)
plt.legend(loc='top left')
plt.xlabel("Month")
plt.ylabel("Pumped Amount 2017")

plt.show()