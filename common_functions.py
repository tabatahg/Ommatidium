import pyodbc
import uuid
import json


def connection_string():
    conn_string = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                                 r"Server=localhost;"
                                 r"Database=ANTzOCR;"
                                 r"Trusted_Connection=yes;")
    return conn_string


subdir = "json_files/"


def create_json_file(json_dictionary):
    file_name = str(uuid.uuid4().hex)
    with open(subdir + file_name + ".json", "w") as file:
        json.dump(json_dictionary, file)