import csv


def open_csv(file):
    """
    Opens a csv file
    :param file: csv file
    :return: list of csv data
    """
    with open(file, "r") as data:
        data_in_python = csv.reader(data)
        data_list = []
        for each_line in data_in_python:
            data_list += each_line
    return data_list


