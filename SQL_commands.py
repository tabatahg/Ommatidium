"""Import SQL commands from here"""

import pyodbc
import uuid
import csv


def select_all_sql():
    """
    Select all data from SQL Table
    :return:Print rows of data from SQL
    """
    conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          r"Server=localhost;"
                          r"Database=ANTzOCR;"
                          r"Trusted_Connection=yes;")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ANTzOCR.dbo.FoodStuff")

    file_name = str(uuid.uuid4().hex)
    with open(file_name + ".csv", "w") as file:
        for row in cursor.fetchall():
            print(row)
            data_handler = csv.writer(file, delimiter=",")
            data_handler.writerow(row)


def select_by_id_sql(food_id):
    """
    Select data by id from SQL Table
    :return:Print row of data from SQL based on id
    """
    conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          r"Server=localhost;"
                          r"Database=ANTzOCR;"
                          r"Trusted_Connection=yes;")
    cursor = conn.cursor()

    select_with_id = """
                     Select Name, Calories, Carbohydrate, Fat, Protein
                     FROM
                     ANTzOCR.dbo.Foodstuff
                     Where FoodId = {}
                     """
    cursor.execute(select_with_id.format(food_id))

    for row in cursor.fetchall():
        print(row)


def test_insert_sql():
    """
    Test Insert
    :return:
    """
    conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          r"Server=localhost;"
                          r"Database=ANTzOCR;"
                          r"Trusted_Connection=yes;")
    cursor = conn.cursor()

    cursor.execute("""
                    INSERT INTO ANTzOCR.dbo.Foodstuff (Name, Calories, Carbohydrate, Fat, Protein)
                    VALUES
                    ('biscuits', 200, 40, 2, 3) 
                   """)
    conn.commit()
    print("input complete")


def insert_sql(data):
    """
    Test Insert
    :return:
    """
    conn = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                          r"Server=localhost;"
                          r"Database=ANTzOCR;"
                          r"Trusted_Connection=yes;")
    cursor = conn.cursor()
    food_name = data["Name"]
    food_name_string = repr(food_name)
    insert_command = """
                     INSERT INTO ANTzOCR.dbo.Foodstuff (Name, Calories, Carbohydrate, Fat, Protein)
                     VALUES
                     ({}, {}, {}, {}, {}) 
                     """
    cursor.execute(insert_command.format(food_name_string, data["Calories"], data["Carbohydrate"], data["Fat"], data["Protein"]))
    print("Insert Complete")
    conn.commit()

