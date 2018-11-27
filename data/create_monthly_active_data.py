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
    consumption = 0
    meters = dict()
    accounts = dict()

    with open(filePath) as reader:
        for index, l in enumerate(reader):
            data = l.split()
            if len(data) < 12:
                # print("bad line index:", index, ";content:", l)
                bad_line_count = bad_line_count + 1
                continue
            status = data[0].upper()
            account = data[1]
            if account not in accounts:
                accounts[account] = 0
            else:
                print("accoount overlapped", account)
            accounts[account] = accounts[account] + 1

            feature_count = len(data)
            meter_index = feature_count - 6
            meter = data[meter_index]
            if meter not in meters:
                meters[meter] = 0
            # else:
            #     print("meter number overlapped:", meter)


            meters[meter] = meters[meter] + 1

            consumption_index = feature_count-4
            current_consumption = float(data[consumption_index])

            if current_consumption > 300:
                current_consumption = 0

            if status == 'I':
                inactive = inactive + 1
            elif status == 'A':
                active = active + 1
            elif status == 'F':
                fstatus = fstatus + 1
            else:
                others = others + 1

            total = total + 1
            consumption = consumption + current_consumption
        # print(filePath, ";Bad line count:", bad_line_count)
    return len(accounts), len(meters), active, inactive, fstatus, others, total, consumption

# for m, filePath in data_month.items():
#     account_count, meter_count, active, inactive, fstatus, others, total, consumption = extract_active_count(filePath='../confi_data/' + filePath)
#     verified = False
#     if total != (active + inactive + fstatus + others):
#         print("not verified:", m, "; file:", filePath)
#     # break


with open("monthly_active.csv", "w", newline='') as csvfile:
    my_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    my_writer.writerow(["month", "account", "meter", "active", "inactive", "fstatus", "other", "total_reading", "consumption"])

    for m, filePath in data_month.items():
        account_count, meter_count, active, inactive, fstatus, others, total, consumption = extract_active_count(filePath='../confi_data/' + filePath)
        verified = False
        my_writer.writerow([m, account_count, meter_count, active, inactive, fstatus, others, total, consumption])
        if total != (active + inactive + fstatus + others):
            print("not verified:", m, "; file:", filePath)


