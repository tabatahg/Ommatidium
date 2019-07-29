try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def image_to_text(image):
    image_string = pytesseract.image_to_string((Image.open(image)))
    calories = image_string.find("Calories", 0, 12)
    print(calories)
