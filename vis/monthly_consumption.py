import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
import pandas as pd
import matplotlib as mpl


df = pd.read_csv("../data/monthly_active.csv", sep=",", header=0)


months = df[["month"]].values.flatten()
n_groups = len(months)

consumption = df[["consumption"]].values.flatten()


fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.4

rects1 = ax.bar(index, consumption, bar_width,
                alpha=opacity, color='b',
                label='Consumption')

ax.set_xlabel('Month - 2018')
ax.set_ylabel('Reading')
ax.set_title('Water consumption by month')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(months)

ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('{x:,.0f}'))


fig.tight_layout()
plt.show()