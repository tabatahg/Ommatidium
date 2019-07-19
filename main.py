"""Getting CSV to dictionary for now"""

from SQL_commands_csv import *
from csv_to_object import open_csv


def run_open_csv():
    """
    Opens a CSV file
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
    print(data.keys(), data.values())
    print(data["Name"], data["Calories"], data["Carbohydrate"], data["Fat"], data["Protein"])
    x = """
                    INSERT INTO ANTzOCR.dbo.Foodstuff (Name, Calories, Carbohydrate, Fat, Protein)
                    VALUES
                    ({}, {}, {}, {}, {}) 
        """
    print(x.format(data["Name"], data["Calories"], data["Carbohydrate"], data["Fat"], data["Protein"]))
    insert_sql(data)


def run_select_by_id():
    select_by_id_sql(input("food id here:"))


if __name__ == "__main__":
    run_select_all_sql()

    # run_select_by_id()

# csv_to_sql()
# show = run_open_csv()
# print(show)

