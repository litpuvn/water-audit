import pandas as pd
import numpy as np
import csv



def create_data(filename, year, writer):

    months = range(12)

    with open(filename) as reader:
        reader.readline()
        for line in reader:
            line = line.strip("\n")
            if len(line) < 1:
                continue
            parts = line.split(",")

            for index, m in enumerate(months):
                starting_index = index * 4

                if starting_index >= len(parts):
                    continue

                day = parts[starting_index]
                if day == '' or len(day) < 1:
                    continue
                try:

                    gpm = parts[starting_index + 1]
                    flow = parts[starting_index + 2]

                    if len(gpm) > 0 and float(gpm) < 0.1:
                        continue
                    if len(flow) > 0 and float(flow) < 0.1:
                        continue

                    date_val = str(year) + "-" + str(m+1) + "-" + day

                    writer.writerow([date_val, gpm, flow.strip("\n")])
                except:
                    print("year:", year, "broken line:", line)

fname1 = "../confi_data/sewage_water/Sewer logs for TTU-2017.csv"
fname2 = "../confi_data/sewage_water/Sewer logs for TTU-2018.csv"

with open("sewage.csv", "w", newline='') as csvfile:
    my_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    my_writer.writerow(["datetime", "gpm", "flow"])

    create_data(fname1, "2017", my_writer)
    create_data(fname2, "2018", my_writer)

