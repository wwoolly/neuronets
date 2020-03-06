import reader


def scan_file(path):
    statistics = None
    with open(path, "r") as f_obj:
        statistics = reader.csv_reader(f_obj)


scan_file("input.csv")
