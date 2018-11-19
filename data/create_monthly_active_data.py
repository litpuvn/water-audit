import csv
import pandas as pd

data_month = {
    '01': 'jan_23.txt',
    '02': 'feb_20.txt',
    '03': 'march_23.txt',
    '04': 'april_23.txt',
    '05': 'may_22.txt',
    '06': 'jun_21.txt',
    '07': 'july_24.txt',
    '08': 'aug_20.txt',
    '09': 'sept_24.txt',
    '10': 'oct_23.txt',
    '11': 'nov_17.txt',
    '12': 'dec_17.txt',
}

def extract_active_count(filePath):
    active = 0
    inactive = 0
    fstatus = 0
    others = 0
    total = 0
    bad_line_count = 0
    with open(filePath) as reader:
        for index, l in enumerate(reader):
            data = l.split()
            if len(data) < 12:
                # print("bad line index:", index, ";content:", l)
                bad_line_count = bad_line_count + 1
                continue
            status = data[0].upper()

            if status == 'I':
                inactive = inactive + 1
            elif status == 'A':
                active = active + 1
            elif status == 'F':
                fstatus = fstatus + 1
            else:
                others = others + 1

            total = total + 1
        print(filePath, ";Bad line count:", bad_line_count)
    return active, inactive, fstatus, others, total

with open("monthly_active.csv", "w", newline='') as csvfile:
    my_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    my_writer.writerow(["month", "active", "inactive", "fstatus", "other", "total"])

    for m, filePath in data_month.items():
        active, inactive, fstatus, others, total = extract_active_count(filePath='../confi_data/' + filePath)
        verified = False
        my_writer.writerow([m, active, inactive, fstatus, others, total])
        if total != (active + inactive + fstatus + others):
            print("not verified:", m, "; file:", filePath)


