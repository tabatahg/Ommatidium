import pyodbc
import uuid
import json
import pandas as pd


def connection_string():
    conn_string = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                                 r"Server=localhost;"
                                 r"Database=ANTzOCR;"
                                 r"Trusted_Connection=yes;")
    return conn_string


subdir_json = "json_files/"
subdir_csv = "csv_files/"


def create_json_file(json_dictionary):
    file_name = str(uuid.uuid4().hex)
    with open(subdir_json + file_name + ".json", "w") as file:
        json.dump(json_dictionary, file)


def create_csv_file(data_dictionary):
    file_name = str(uuid.uuid4().hex)
    pd.DataFrame([data_dictionary]).to_csv(subdir_csv + file_name + ".csv", index=False)
