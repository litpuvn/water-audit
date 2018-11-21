import csv



with open("well_monthly.csv", "w", newline='') as csvfile:
    my_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    my_writer.writerow(["month", "well", "pump"])

    with open('well_daily.csv') as filePointer:
        filePointer.readline()

        wells = dict()

        for line in filePointer:
            data = line.split(",")
            month = data[0]
            month = month[0:7]
            well = data[1]
            pump = float(data[2])

            if well not in wells:
                wells[well] = dict()

            month_well = wells[well]
            if month not in month_well:
                month_well[month] = 0

            month_well[month] = month_well[month] + pump

        for w, w_months in wells.items():
            for m, p in w_months.items():
                my_writer.writerow([m, w, p])

