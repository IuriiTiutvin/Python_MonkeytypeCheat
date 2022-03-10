import PIL
from PIL import ImageEnhance, ImageGrab, ImageOps, Image, ImageDraw
import pytesseract
import pyautogui as p
import time
import cv2
import numpy as np

coordinates = {'d': [(684.5, 737.0), (535.5, 665.0)], 'n': [(593.5, 737.0)], 'e': [(743.0, 665.0)], 'h': [(557.0, 575.0)], 'u': [(722.0, 574.0)], 'o': [(639.5, 535.0)]}
words = "DEN,DONE,DUD,DUDE,DUH,DUN,DUNE,DUO,END,HOE,HONE,HONED,HOUND,HOUNDED,HUE,NOD,NODE,NUDE,ODD,UNDO".lower().split(',')

def start():
    def start_lvl():
        time.sleep(1)
        p.click(500, 30)
        time.sleep(1)
        p.click(810, 170)
        time.sleep(1)
        p.click(760, 360)

    side = PIL.ImageGrab.grab(bbox = (880, 1500, 881, 1501)).convert("RGB").getpixel((0,0))
    mid = PIL.ImageGrab.grab(bbox = (1280, 1500, 1281, 1501)).convert("RGB").getpixel((0,0))
    if side == (255, 255, 255):
        p.press('esc')
        time.sleep(1)
        start_lvl()
    elif mid == (255, 255, 255):
        start_lvl()
        return
    else:
        while True:
            p.press('esc')
            time.sleep(1)
            mid = PIL.ImageGrab.grab(bbox = (1280, 1500, 1281, 1501)).convert("RGB").getpixel((0,0))
            if mid == (255, 255, 255):
                start_lvl()
                break

#seems perfect
def word_prntr():
    global coordinates
    global words
    print(words)
    for i in words:
        print(i)
        #time.sleep(0.1)
        p.moveTo(coordinates.get(i[0])[0][0], coordinates.get(i[0])[0][1])
        coordinates[i[0]] = coordinates[i[0]][1:] + [coordinates[i[0]][0]]
        p.mouseDown()
        for j in i[1:]:
            #time.sleep(0.04)
            p.moveTo(coordinates.get(j)[0][0], coordinates.get(j)[0][1])
            coordinates[j] = coordinates[j][1:] + [coordinates[j][0]]
        p.mouseUp()
    p.press('esc')
    time.sleep(3)


p.keyDown('command')
p.press('tab')
p.press('tab')
p.keyUp('command')
time.sleep(1)

while True:
    start()
    time.sleep(1)
    word_prntr()


p.keyDown('command')
p.press('tab')
p.press('tab')
p.keyUp('command')
