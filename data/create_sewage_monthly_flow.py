import pandas as pd
import csv

df = pd.read_csv("sewage.csv", header=0)

cumulative_data = dict()

for _, row in df.iterrows():
    datetime = row["datetime"]
    parts = datetime.split("-")
    if len(parts) < 3:
        raise Exception("bad data on: " + datetime)

    year = parts[0]
    month = parts[1]
    day = parts[2]

    year_month = year + '-' + month
    if year_month not in cumulative_data:
        cumulative_data[year_month] = 0

    cumulative_data[year_month] = cumulative_data[year_month] + row["flow"]


with open("sewage_monthly_flow.csv", "w", newline='') as csvfile:
    my_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    my_writer.writerow(["month", "flow"])

    for month, flow in cumulative_data.items():
        my_writer.writerow([month, flow])


