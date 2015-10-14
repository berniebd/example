import shutil
from PIL import Image
from pytesseract import pytesseract
import requests

__author__ = 'bida'

resp = requests.get("http://10.3.254.23:8080/dangwebx/randCodeImage?a=1444784364985", stream=True)
with open("tmp.png", "wb") as f:
    f.write(resp.raw.read())
    shutil.copyfileobj(resp.raw, f)

image = Image.open("tmp.png")
print pytesseract.image_to_string(image)
