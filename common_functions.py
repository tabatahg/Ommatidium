import pyodbc


def connection_string():
    conn_string = pyodbc.connect("Driver={ODBC Driver 17 for SQL Server};"
                                 r"Server=localhost;"
                                 r"Database=ANTzOCR;"
                                 r"Trusted_Connection=yes;")
    return conn_string
