import PIL
from PIL import ImageEnhance, ImageGrab, ImageOps, Image, ImageDraw
import pytesseract
import pyautogui as p
import time
import cv2
import numpy as np
import itertools as it

def read_num():
    main_image = PIL.ImageGrab.grab(bbox = (594, 244, 595, 245)).convert("RGB")
    main_image.save("shot.png")
    print(main_image.getpixel((0,0)))

p.keyDown('command')
p.press('tab')
p.press('tab')
p.keyUp('command')
time.sleep(1)
read_num()
p.keyDown('command')
p.press('tab')
p.press('tab')
p.keyUp('command')
