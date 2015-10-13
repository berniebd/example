from PIL import Image
from pytesseract import pytesseract

__author__ = 'bida'

image = Image.open("d:\\randCodeImage.jpg")
print pytesseract.image_to_string(image)
