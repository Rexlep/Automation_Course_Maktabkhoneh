from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Tesseract\tesseract.exe"

image = Image.open("R.jpg")

text = pytesseract.image_to_string(image)
print(text)