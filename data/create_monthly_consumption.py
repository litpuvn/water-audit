import pandas as pd
import csv

df = pd.read_csv("utilities.csv", sep=",", header=0)

months_consumption = dict()

with open("water_monthly_consumption.csv", "w", newline='') as csvfile:
    my_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    my_writer.writerow(["month", "water_consumption"])

    for _, row in df.iterrows():
        month = row["datetime"]
        consumption = row["water"]

        if month not in months_consumption:
            months_consumption[month] = 0

        months_consumption[month] = months_consumption[month] + consumption

    sorted_months = sorted(months_consumption)
    for m in sorted_months:
        my_writer.writerow([m, months_consumption[m] // 1000 ])