import pandas as pd
import numpy as np
from matplotlib.pylab import plt #load plot library


df = pd.read_csv("../data/well_monthly_2017.csv", header=0)

cumulative_months = []
months_label = []
for m in range(1, 13):
    if m < 10:
        pad = '0' + str(m)
    else:
        pad = str(m)
    year_month = "2017-" + pad
    month_data = df[df["month"]==year_month]
    month_data.drop(columns=["month", "well"], inplace=True)
    cumulative_month = sum(month_data.values.flatten())

    cumulative_months.append(cumulative_month)
    months_label.append("m-" + str(m))


month_count = 12
y_pos = np.arange(month_count)

plt.bar(y_pos, cumulative_months, align='center', alpha=0.5)
plt.xticks(y_pos, months_label)
plt.ylabel('Pumped water')
plt.title('Well water pumped in one year 2017')

plt.show()