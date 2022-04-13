import PIL
from PIL import ImageEnhance, ImageGrab, ImageOps, Image, ImageDraw
import pytesseract
import pyautogui as p
import time
import cv2
import numpy as np

file = open("data/all_levels.txt", 'r')
answers = file.readlines()
answers = [None] + [i.lower()[:-1].split(',') for i in answers]
file.close()

background = Image.new("RGB", (2560, 1600), (255, 255, 255))
background1 = Image.new("RGB", (2560, 1600), (0, 0, 0))
mask = PIL.Image.open("mask.png")
lower_val = np.array([0,0,0])
upper_val = np.array([1,1,1])
brown_lower = np.array([95,0,45])
brown_upper = np.array([97,1,47])
kernel = np.ones((5,5), np.uint8)
previous_string = ''

    
def start():
    left = PIL.ImageGrab.grab(bbox = (880, 1500, 881, 1501)).convert("RGB").getpixel((0,0))
    right = PIL.ImageGrab.grab(bbox = (1640, 1520, 1641, 1521)).convert("RGB").getpixel((0,0))
    #print(side, mid)
    if left == (255, 255, 255):
        return
    if right == (255, 255, 255):
        p.click(640, 450)
        time.sleep(0.5)
        p.click(640, 640)
        return
    else:
        time.sleep(12)
        while True:
            p.press('esc')
            p.click(640, 640)
            time.sleep(3)
            right = PIL.ImageGrab.grab(bbox = (1640, 1520, 1641, 1521)).convert("RGB").getpixel((0,0))
            #print(mid)
            if right == (255, 255, 255):
                p.click(640, 450)
                time.sleep(0.5)
                p.click(640, 640)
                return


#seems perfect
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


#seems perfect
def get_coordinates(cnts):
    global lvl
    global previous_string
    global redo
    print(len(cnts))
    image = cv2.imread('shot.png')
    coords = []
    string = ''

    for c in cnts:
        M = cv2.moments(c)
        x = int(M["m10"] / M["m00"])
        y = int(M["m01"] / M["m00"])
        next = pytesseract.image_to_string(image[y-90:y+90, x-90:x+90], lang='eng', config='--psm 10')
        next = next.strip().lower()
        print(next)

        if next == '' or next == '|':
            string += 'i'
        elif len(next) > 1:
            string += list(next)[0]
        else:
            string += next
        coords.append((x/2, y/2))

    if string == previous_string:
        lvl = lvl - 1
        redo = True
    previous_string = string
    print(string)

    coordinates = {}
    for i in range(0, len(string)):
        coordinates[list(string)[i]] = []
    for i in range(0, len(string)):
        coordinates[list(string)[i]].append(coords[i])
    print(coordinates)
    return coordinates


#seems perfect
def word_prntr(coordinates, words):
    print(words)
    for i in words:
        print(i)
        time.sleep(0.1)
        p.moveTo(coordinates.get(i[0])[0][0], coordinates.get(i[0])[0][1])
        coordinates[i[0]] = coordinates[i[0]][1:] + [coordinates[i[0]][0]]
        p.mouseDown()
        for j in i[1:]:
            time.sleep(0.04)
            p.moveTo(coordinates.get(j)[0][0], coordinates.get(j)[0][1])
            coordinates[j] = coordinates[j][1:] + [coordinates[j][0]]
        p.mouseUp()
    p.press('esc')
    p.press('esc')
    time.sleep(3)


#seems perfect
def log(completion_time, level, redo):
    global lvl
    level = [len(i) for i in level]
    level.sort(reverse = True)
    log = open('data/log.txt', 'a')
    if not redo:
        log.write(f'level ${lvl}$ completed at {str(time.time())} sec, p/sec ratio: @{((len(level) - 2)*(level[0] - 2)+2)/completion_time}@\n')
    else:
        log.write(f'level ${lvl}$ **IS A REDO** at {str(time.time())} sec, p/sec ratio: @{((len(level) - 2)*(level[0] - 2)+2)/completion_time}@\n')
    log.close()
    level_file = open("data/level.txt", 'w')
    level_file.write(str(lvl+1))
    level_file.close()


p.keyDown('command')
p.press('tab')
p.press('tab')
p.keyUp('command')
time.sleep(1)

while True:
    redo = False
    level_file = open("data/level.txt", 'r')
    lvl = int(level_file.read())
    level_file.close()
    #print(level)
    start()
    time.sleep(1)
    t1 = time.time()
    coords_to_use = get_coordinates(process_pict())
    word_prntr(coords_to_use, answers[lvl])
    t2 = time.time()
    log(t2-t1, answers[lvl], redo)

p.keyDown('command')
p.press('tab')
p.press('tab')
p.keyUp('command')
