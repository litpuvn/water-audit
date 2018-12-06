import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
import pandas as pd
import matplotlib as mpl


df = pd.read_csv("../data/sewage_monthly_flow.csv", sep=",", header=0)

value_2017 = []
value_2018 = []

for _, row in df.iterrows():
    datetime = row['month']
    if datetime.startswith('2017'):
        value_2017.append(row["flow"])
    else:
        value_2018.append(row["flow"])

fig, ax = plt.subplots()

index = np.arange(12)
bar_width = 0.35
opacity = 0.4
for i in range(len(value_2018), len(index)):
    value_2018.append(0)

rects1 = ax.bar(index, value_2017, bar_width,
                alpha=opacity, color='b',
                label='Consumption 2017')
rects2 = ax.bar(index+bar_width, value_2018, width=bar_width, color='g', align='center', label='Consumption 2018')

ax.set_xlabel('Month - 2018')
ax.set_ylabel('Reading')
ax.set_title('Sewage Water Flow by month')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(index)

ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))
ax.legend((rects1[0], rects2[0]), ('2017', '2018'))


fig.tight_layout()
plt.show()