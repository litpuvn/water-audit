import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
import pandas as pd


df = pd.read_csv("../data/monthly_active.csv", sep=",", header=0)


months = df[["month"]].values.flatten()
n_groups = len(months)

active_counts = df[["active"]].values.flatten()
inactive_counts = df[["inactive"]].values.flatten()
fstatus_counts = df[["fstatus"]].values.flatten()

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.4

rects1 = ax.bar(index, active_counts, bar_width,
                alpha=opacity, color='b',
                label='Active')

rects2 = ax.bar(index + bar_width, inactive_counts, bar_width,
                alpha=opacity, color='r',
                label='Inactive')

rects3 = ax.bar(index + 2*bar_width, fstatus_counts, bar_width,
                alpha=opacity, color='g',
                label='Fstatus')

ax.set_xlabel('Month')
ax.set_ylabel('Count')
ax.set_title('Status count by month')
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(months)
ax.legend()

fig.tight_layout()
plt.show()