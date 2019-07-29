"""Import SQL commands from here"""

import uuid
import csv
from common_functions import connection_string, create_csv_file


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


def select_all_sql():
    """
    Select all data from SQL Table
    :return:Print rows of data from SQL into CSV file
    """
    conn = connection_string()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ANTzOCR.dbo.FoodStuff")

    file_name = str(uuid.uuid4().hex)
    with open(file_name + ".csv", "w") as file:
        for row in cursor.fetchall():
            print(row)
            data_handler = csv.writer(file, delimiter=",")
            data_handler.writerow(row)


def select_by_id_sql_csv(food_id):
    """
    Select data by id from SQL Table
    :return:Print row of data from SQL based on id
    """
    conn = connection_string()
    cursor = conn.cursor()

    select_with_id = """
                     Select Name, Calories, Carbohydrate, Fat, Protein
                     FROM
                     ANTzOCR.dbo.Foodstuff
                     Where FoodId = {}
                     """
    cursor.execute(select_with_id.format(food_id))

    description = cursor.description
    column_names = [col[0] for col in description]
    csv_dictionary = [dict(zip(column_names, row)) for row in cursor]
    create_csv_file(csv_dictionary[0])

