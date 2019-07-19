import json
import uuid
from common_functions import connection_string


def open_json(file):
    """
    Opens a json file
    :param file: json file
    :return: dictionary of json data
    """
    with open(file) as data:
        loaded_data = json.load(data)
    return loaded_data


def select_all_json():
    """
    Select all data from SQL Table
    :return:Print rows of data from SQL
    """
    conn = connection_string()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ANTzOCR.dbo.FoodStuff")
    description = cursor.description
    column_names = [col[0] for col in description]
    json_dictionary = [dict(zip(column_names, row)) for row in cursor]

    file_name = str(uuid.uuid4().hex)
    with open(file_name + ".json", "w") as file:
        json.dump(json_dictionary, file)


def select_by_id_json(food_id):
    """
        Select data by id from SQL Table
        :return:Create json file from row of data based on id
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
    json_dictionary = [dict(zip(column_names, row)) for row in cursor]

    file_name = str(uuid.uuid4().hex)
    with open(file_name + ".json", "w") as file:
        json.dump(json_dictionary, file)
