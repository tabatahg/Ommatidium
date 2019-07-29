try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from common_functions import create_json_file, create_csv_file

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def image_to_text(image):
    """
    Convert image to text file
    :param image: File path for Image
    :return: list of data
    """
    image_string = pytesseract.image_to_string((Image.open(image)))

    name_value = ""
    if len(name_value) == 0:
        name_value = input("Input name here: ")

    calories_index = image_string.find("Calories")
    calories = image_string[calories_index:calories_index+12].split(" ")
    calorie_key, calorie_value = " ".join(calories).split(" ")
    print(calorie_key, calorie_value)

    fat_index = image_string.find("Fat")
    fat = image_string[fat_index:fat_index+6].split(" ")
    fat_data = " ".join(fat)
    fat_key, fat_value = fat_data[:fat_data.find("g")].split(" ")
    print(fat_key, fat_value)

    carbohydrate_index = image_string.find("Carbohydrate")
    carbohydrate = image_string[carbohydrate_index:carbohydrate_index+16].split(" ")
    carbohydrate_data = " ".join(carbohydrate)
    carbohydrate_key, carbohydrate_value = carbohydrate_data[:carbohydrate_data.find("g")].split(" ")
    print(carbohydrate_key, carbohydrate_value)

    protein_index = image_string.find("Protein")
    protein = image_string[protein_index:protein_index+10].split(" ")
    protein_data = " ".join(protein)
    protein_key, protein_value = protein_data[:protein_data.find("g")].split(" ")
    print(protein_key, protein_value)

    data_key = ["Name", calorie_key, fat_key, carbohydrate_key, protein_key]
    data_value = [name_value, calorie_value, fat_value, carbohydrate_value, protein_value]
    print("--------->", data_key, data_value)

    data_dictionary = dict(zip(data_key, data_value))
    print(data_dictionary)
    create_file(input(file_query), data_dictionary)
    return data_dictionary


def create_file(number, data_dictionary):
    if number == "1":
        create_json_file(data_dictionary)
    elif number == "2":
        create_csv_file(data_dictionary)
    else:
        pass


file_query = """
             1 = JSON. 
             
             2 = CSV. 
             
             3 = No 
             
             Do you want to create a file? """
