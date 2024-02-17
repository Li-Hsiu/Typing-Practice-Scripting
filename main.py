import pygetwindow as gw
import pytesseract
from PIL import ImageGrab
from constant import windowName, x, y, h, w
from directkeys import PressCharacter
import time
import keyboard

def start():
    while True:
        window = gw.getWindowsWithTitle(str(windowName))[0]
        screenshot = ImageGrab.grab(bbox=(x, y, h, w))
        text = pytesseract.image_to_string(screenshot, config='--psm 6')
        text = text.replace(' ', '-').replace(':', '-')
        word_list = text.split('-')
        word_list = [word.strip() for word in word_list if word]
        result = '-'.join(word_list)
        print(result)
        prev = "-"
        for char in result:
            if prev == '-':
                PressCharacter(char.upper())
            else:
                PressCharacter(char.lower())
            time.sleep(0.01)
            prev = char
        time.sleep(0.1)

while True:
    if keyboard.read_key() == "ctrl":
        start()
        