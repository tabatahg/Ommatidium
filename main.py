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
    Imports CSV and inserts to SQL
    """
    data = run_open_json()
    insert_sql(data)


def run_select_by_id_csv():
    select_by_id_sql(input("food id here:"))


def run_select_by_id_json():
    select_by_id_json(input("Input food id here:"))


def run_image_to_text():
    image_to_text(input("Insert image address: "))


def run_commands(command):
    commands.get(command)()


commands = {
    "select_Id_JSON": run_select_by_id_json,
    "select_all_JSON": select_all_json,
    "json_to_sql": json_to_sql,
    "csv_to_sql": csv_to_sql,
    "run_open_json": run_open_json,
    "run_select_all_sql": run_select_all_sql,
    "image_to_text": run_image_to_text,
}

if __name__ == "__main__":
    run_commands(input("Insert command: "))
# show = run_open_csv()
# print(show)
