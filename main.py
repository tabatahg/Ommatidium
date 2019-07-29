"""Getting CSV to dictionary for now"""

from SQL_commands_csv import *
from SQL_commands_json import *
from SQL_commands_common import *
from OCR_component import image_to_text


def run_open_json():
    """
    Opens a json file
    :return: a dictionary of json file
    """
    json_dict = open_json(input("Import Json file:"))
    return json_dict


def run_open_csv():
    """
    Opens a CSV file

    data index[0-4] are keys. data index[5:] are values
    :return: data in dictionary
    """
    data = open_csv(input("Import CSV file:"))
    data_keys = data[:5]
    data_values = data[5:]
    dictionary = dict(zip(data_keys, data_values))
    return dictionary


def run_select_all_sql():
    """
    Select all from SQL
    :return: CSV file
    """
    select_all_sql()


def run_test_insert_sql():
    """
    Test code for insert with hard code values
    """
    test_insert_sql()


def csv_to_sql():
    """
    Imports CSV and inserts to SQL
    """
    data = run_open_csv()
    insert_sql(data)


def json_to_sql():
    """
    Imports json and inserts to SQL
    """
    data = run_open_json()
    insert_sql(data)


def run_select_by_id_csv():
    select_by_id_sql(input("food id here:"))


def run_select_by_id_json():
    select_by_id_json(input("Input food id here:"))


def run_image_to_text():
    image_to_text(input("Insert image address: "))


def run_image_to_sql():
    image_to_text(input("Insert image address: "))
    json_to_sql()


def run_commands(command):
    """
    Run a command as per the number
    :param command:
    "select_Id_JSON"= 1,
    "select_all_JSON": 2,
    "json_to_sql": 3,
    "csv_to_sql": 4,
    "run_open_json": 5,
    "run_select_all_sql": 6,
    "image_to_text": 7,
    "image_to_sql": 8
    :return: the command number
    """
    commands.get(command)()


commands = {
    "1": run_select_by_id_json,
    "2": select_all_json,
    "3": json_to_sql,
    "4": csv_to_sql,
    "5": run_open_json,
    "6": run_select_all_sql,
    "7": run_image_to_text,
    "8": run_image_to_sql,
}

if __name__ == "__main__":
    run_commands(input("Insert command: "))

# show = run_open_csv()
# print(show)
