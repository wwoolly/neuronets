import csv
from datastruct import Weather
from datastruct import \
    (SUN, OVERCAST, RAIN,
     COLD, SWEET, HOT,
     HIGH, NORMAL, LOW)

from datastruct import \
    (OUTLOOK, TEMPERATURE, HUMIDITY, WIND, PLAY)


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
    return outlook, temperature, humidity, wind, play


def is_line_correct(line):
    outlook = (line[0] >= 0 & line[0] <= 2)
    temperature = (line[1] >= 0 & line[1] <= 2)
    humidity = (line[2] >= 0 & line[2] <= 2)
    wind = (line[3] >= 0 & line[3] <= 2)

    return outlook & temperature & humidity & wind


def add_item(table, item):
    table[OUTLOOK].append(item[0])
    table[TEMPERATURE].append(item[1])
    table[HUMIDITY].append(item[2])
    table[WIND].append(item[3])
    table[PLAY].append(item[4])


def csv_reader(file_obj):
    reader = csv.reader(file_obj, delimiter=',')

    out = {
        OUTLOOK: [],
        TEMPERATURE: [],
        HUMIDITY: [],
        WIND: [],
        PLAY: []
    }
    for row in reader:
        item = parse_csv_line(row)
        if is_line_correct(item): add_item(out, item)

    return out
