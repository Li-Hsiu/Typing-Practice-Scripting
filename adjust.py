# run this file to try out different constants to fit different machines
import cv2 as cv
import numpy as np
import pygetwindow as gw
import pytesseract
from PIL import ImageGrab
from constant import windowName, x, y, h, w
import time

time.sleep(3)
windows = gw.getAllWindows()  # run this file to get the window name
for window in windows:
    print(window.title)

window = gw.getWindowsWithTitle(str(windowName))[0]
screenshot = ImageGrab.grab(bbox=(x, y, h, w))
text = pytesseract.image_to_string(screenshot, config='--psm 6')
text = text.replace(' ', '-').replace(':', '-')
word_list = text.split('-')
word_list = [word.strip() for word in word_list if word]
result = '-'.join(word_list)
print(result)
screenshot = np.array(screenshot)
cv.imshow("screenshot", screenshot)
cv.waitKey(0)