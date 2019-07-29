from common_functions import connection_string


def test_insert_sql():
    """
    Test Insert
    :return:
    """
    conn = connection_string()
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
    """
    conn = connection_string()
    cursor = conn.cursor()
    food_name = data["Name"]
    food_name_string = repr(food_name)
    insert_command = """
                     INSERT INTO ANTzOCR.dbo.Foodstuff (Name, Calories, Carbohydrate, Fat, Protein)
                     VALUES
                     ({}, {}, {}, {}, {}) 
                     """
    cursor.execute(insert_command.format(food_name_string
                                         , data["Calories"]
                                         , data["Carbohydrate"]
                                         , data["Fat"]
                                         , data["Protein"]))
    print("Insert Complete")
    conn.commit()
