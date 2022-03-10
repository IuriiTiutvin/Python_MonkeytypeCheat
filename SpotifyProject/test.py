import PIL
from PIL import ImageEnhance, ImageGrab, ImageOps, Image, ImageDraw
import pytesseract
import pyautogui as p
import time
import cv2
import numpy as np
import itertools as it

mask = PIL.Image.open("mask.png")
lower_val = np.array([0,0,0])
upper_val = np.array([1,1,1])
kernel = np.ones((5,5), np.uint8)

#must be manually set
num_of_songs = 13208
current_song_num = 0

def set_up():
    p.keyDown('command')
    p.press('tab')
    p.press('tab')
    p.keyUp('command')
    time.sleep(1)
    p.moveTo(700, 270)
    time.sleep(1)
    p.scroll(-10)

def read_num():
    global mask
    global lower_val
    global upper_val
    global kernel

    main_image = PIL.ImageGrab.grab(bbox = (560, 200, 630, 300)).convert("RGB")

    image = np.array(main_image)

    letter_mask = cv2.inRange(image, lower_val, upper_val)
    image = cv2.bitwise_not(letter_mask)
    cv2.imwrite('shot.png', image)
    #image = cv2.erode(image, kernel, iterations=15)

    _,binary = cv2.threshold(image,100,255,cv2.THRESH_BINARY)
    contours,hierarchy = cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

#while current_song_num != num_of_songs:
