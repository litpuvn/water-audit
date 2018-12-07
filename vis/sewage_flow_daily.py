import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../data/sewage.csv", sep=",", header=0)

values = {}
for _, row in df.iterrows():
    datetime = row['datetime']
    parts = datetime.split("-")

    year = parts[0]
    month = parts[1]
    if len(month) < 2:
        month = '0' + month
    day = parts[2]
    if len(day) < 2:
        day = '0' + day

    my_datetime = year + '-' + month + '-' + day
    gpm = row["gpm"]
    values[my_datetime] = gpm

sorted_keys = sorted(values)

my_vals = []
for k in sorted_keys:
    my_vals.append(values[k])

plt.plot(my_vals)
plt.ylabel('Sewage Flow Rate')
plt.show()