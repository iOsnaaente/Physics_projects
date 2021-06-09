from PIL import Image 


import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'D:\\Tesseract-OCR\\tesseract.exe'

with Image.open( "D:\Desktop\\2.png") as img : 
    out = pytesseract.image_to_string( img )

print(out)

input() 