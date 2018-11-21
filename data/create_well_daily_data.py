import csv

data_month = {
    '01': 'well_jan_2018.csv',
    '02': 'well_feb_2018.csv',
    '03': 'well_march_2018.csv',
    '04': 'well_april_2018.csv',
    '05': 'well_may_2018.csv',
    '06': 'well_june_2018.csv',
    '07': 'well_july_2018.csv',
    '08': 'well_august_2018.csv',
    '09': 'well_sept_2018.csv',
    '10': 'well_oct_2018.csv'
}


def extract_and_write(month, filename, writer):
    with open(filename) as file_pointer:
        file_pointer.readline()
        for line in file_pointer:
            line = line.lower()

            if line.startswith("total"):
                print("last line", line)
                break

            data = line.split(",")
            day = data[0]
            date_time = '2018-' + month + '-' + day

            well_total = 0
            for i in range(1,18):
                try:

                    well_i = float(data[i])
                    well_total = well_total + well_i
                    writer.writerow([date_time, i, well_i])
                except:
                    print("Soemthing went wrong: date", date_time, "; data:", data)
                    break
            if well_total <= 0.1:
                print("not valid calendar day:", date_time)
                continue
            day_total = float(data[len(data) - 1])
            if well_total != day_total:
                print("invalid calculation for day:", date_time, ";total=", day_total, "; calculated:", well_total)


with open("well_daily.csv", "w", newline='') as csvfile:
    my_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    my_writer.writerow(["date", "well", "pump"])

    for m, filePath in data_month.items():
        extract_and_write(month=m, filename='../confi_data/well_water/' + filePath, writer=my_writer)
        # break