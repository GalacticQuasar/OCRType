import keyboard
import random
import time
from pytesseract import pytesseract
from PIL import ImageGrab
import os


def escape_program(key_event: keyboard.KeyboardEvent):
    print("ESCAPE KEY PRESSED -> EXITING APPLICATION")
    os._exit(1)


keyboard.hook_key("esc", escape_program)
print("The escape key is ESC.")
print("Take a screenshot of the text to type (WIN + SHIFT + S).")
input("Click ENTER when you have taken the screenshot (and saved it to clipboard).")

img = ImageGrab.grabclipboard()

# Optical Character Recognition (Image -> text)
path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.tesseract_cmd = path
text: str = pytesseract.image_to_string(img).strip().replace('\n', ' ')

# More Text Processing
if not text[0].isalpha():
    text = text[1:]

print("----------")
print(text)
print("----------")

print("Press CTRL when you are ready to type!")
keyboard.wait('ctrl')

time.sleep(0.5)

variance = 1
for c in text:
    keyboard.write(c)
    time.sleep(random.uniform(0.001, 0.1))
    variance -= 0.025 if variance > 0.025 else 0
    if random.random() < 0.5:
        variance += 0.1

print("DONE")
