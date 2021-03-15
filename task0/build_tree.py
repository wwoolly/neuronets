import reader


def scan_file(path):
    with open(path, "r") as f_obj:
        statistics = reader.csv_reader(f_obj)
    return statistics


def freq(table, col, v):
    return table[col].count(v)


statistics = scan_file("input.csv")
# #0 in the list - number of 'yes', #1 - number of 'no'
probability = list(range(2))
element_number = len(statistics)
