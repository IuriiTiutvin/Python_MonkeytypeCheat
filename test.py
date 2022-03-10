import PIL
from PIL import ImageEnhance, ImageGrab, ImageOps, Image, ImageDraw
import pytesseract
import pyautogui as p
import time
import cv2
import numpy as np

background = Image.new("RGB", (2560, 1600), (255, 255, 255))
background1 = Image.new("RGB", (2560, 1600), (0, 0, 0))
mask = PIL.Image.open("Wordscape/mask.png")
lower_val = np.array([0,0,0])
upper_val = np.array([1,1,1])
brown_lower = np.array([95,0,45])
brown_upper = np.array([97,1,47])
kernel = np.ones((5, 5), 'uint8')



def process_pict():
    global background
    global background1
    global mask
    global lower_val
    global upper_val
    global brown_lower
    global brown_upper
    global kernel

    main_image = PIL.ImageGrab.grab().convert("RGB")
    if sum(main_image.getpixel((1280,1280))) > 450:#white Image
        image = Image.composite(main_image, background, mask)
        image = np.array(image)
    else:#black Image
        image = Image.composite(main_image, background1, mask)
        image = np.array(PIL.ImageOps.invert(image))

    brown_mask = cv2.inRange(image, brown_lower, brown_upper)
    image[brown_mask>0]=(0, 0, 0)

    letter_mask = cv2.inRange(image, lower_val, upper_val)
    image = cv2.bitwise_not(letter_mask)
    cv2.imwrite('shot.png', cv2.erode(image, kernel, iterations=1))
    image = cv2.erode(image, kernel, iterations=15)

    _,binary = cv2.threshold(image,100,255,cv2.THRESH_BINARY)
    contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 3:
        contours = contours[:-1]
        return contours
    else:
        process_pict()



p.keyDown('command')
p.press('tab')
p.press('tab')
p.keyUp('command')
time.sleep(1)

process_pict()

p.keyDown('command')
p.press('tab')
p.press('tab')
p.keyUp('command')
