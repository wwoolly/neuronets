import csv
from datastruct import Weather
from datastruct import \
    (SUN, OVERCAST, RAIN,
     COLD, SWEET, HOT,
     HIGH, NORMAL, LOW)


# returns list with one line from csv file
def parse_csv_line(row):
    outlook = -1
    if row[0] == 'Sun': outlook = SUN
    elif row[0] == 'Overcast': outlook = OVERCAST
    elif row[0] == 'Rain': outlook = RAIN

    temperature = -1
    if row[1] == 'Cold': temperature = COLD
    elif row[1] == 'Sweet': temperature = SWEET
    elif row[1] == 'Hot': temperature = HOT

    humidity = -1
    if row[2] == 'High': humidity = HIGH
    elif row[2] == 'Normal': humidity = NORMAL

    wind = -1
    if row[3] == 'High': wind = HIGH
    elif row[3] == 'Low': wind = LOW

    play = False
    if row[4] == 'Yes': play = True
    elif row[4] == 'No': play = False
    # print(outlook, temperature, humidity, wind, play)
    return Weather(outlook, temperature, humidity, wind, play)


def csv_reader(file_obj):
    reader = csv.reader(file_obj, delimiter=',')

    out = list()
    for row in reader:
        item = parse_csv_line(row)
        if item.is_correct(): out.append(item)

    return out
