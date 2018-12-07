import csv
fname1 = "../confi_data/meter/ub36cons.dat"

def print_with_index(arr):
    for idx, val in enumerate(arr):
        print(idx, "::", val)


with open(fname1) as fpointer:
    water_reading_index = 28
    el_reading_index = 148
    gas_reading_index = 268
    sewage_reading_index = 379

    water_reading_2015 = range(29, 32)  # 3 months
    water_reading_2016 = range(32, 44)  # 12 months
    water_reading_2017 = range(44, 56)  # 12 months
    water_reading_2018 = range(56, 65)  # 9 months

    line = fpointer.readline()
    headers = line.split("~")
    # for idx, p in enumerate(parts):
    #     print(idx, "::", p)
    #
    # print(parts[water_reading_index + 1], parts[el_reading_index+1], parts[gas_reading_index+1], parts[sewage_reading_index+1])
    years = [range(10, 13), range(1, 13), range(1, 13), range(1, 10)]

    account_count = 0
    with open("utilities.csv", "w", newline='') as csvfile:
        my_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # my_writer.writerow(["account", "datetime", "water", "water_charge"])
        my_writer.writerow(["account", "datetime", "water", "electricity", "gas", "sewage"])
        for index, line in enumerate(fpointer):
            if len(line) < 2:
                continue
            account_count = account_count + 1
            parts = line.split("~")

            account = parts[0]

            # if account != '001-0001007-001':
            #     continue



            water_reading_index = 28
            water_charge_index = 100
            water_last_billing_date = 15
            water_last_billed_read_date = 24
            water_last_billed_reading = 25
            water_digits = 27
            water_meter_number = 28

            for i in range(29):
                print(headers[i], ":", parts[i])

            for i in range(36):
                print(parts[water_reading_index+1+i], parts[water_charge_index+1+i])

            el_reading_index = 148
            gas_reading_index = 268
            sewage_reading_index = 379

            for idx, months in enumerate(years):
                y = idx + 2015
                for m in months:
                    my_month = str(m)
                    if m < 10:
                        my_month = '0' + my_month
                    month = str(y) + '-' + my_month

                    try:
                        # water
                        water_reading_index = water_reading_index + 1
                        water_reading_val = parts[water_reading_index]
                        water_charge_index = water_charge_index + 1
                        water_charge_val = parts[water_charge_index]


                        # electricity
                        el_reading_index = el_reading_index + 1
                        el_reading_val = parts[el_reading_index]
                        # gas
                        gas_reading_index = gas_reading_index + 1
                        gas_reading_val = parts[gas_reading_index]
                        # sewage value
                        sewage_reading_index = sewage_reading_index + 1
                        sewage_reading_val = parts[sewage_reading_index]

                        # my_writer.writerow([account, month, water_reading_val.strip(), water_charge_val.strip()])

                        my_writer.writerow([account, month, water_reading_val.strip(), el_reading_val.strip(),
                                            gas_reading_val.strip(), sewage_reading_val.strip()])
                    except:
                        print("line len:",len(line), "parts len:", len(parts), "accessing water index:", water_reading_index)
                        print("bad line:", line)

    print("total account:", account_count)

