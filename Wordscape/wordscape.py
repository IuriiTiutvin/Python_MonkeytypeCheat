import PIL
from PIL import ImageEnhance, ImageGrab, ImageOps, Image, ImageDraw
import pytesseract
import pyautogui as p
import time
import cv2
import numpy as np
import itertools as it

background = Image.new("RGB", (2560, 1600), (255, 255, 255))
background1 = Image.new("RGB", (2560, 1600), (0, 0, 0))
mask = PIL.Image.open("mask.png")
lower_val = np.array([0,0,0])
upper_val = np.array([1,1,1])
brown_lower = np.array([95,0,45])
brown_upper = np.array([97,1,47])
kernel = np.ones((5,5), np.uint8)

def dictionary():
    dictionary = {}
    dict_file = open("data/new_dict.txt", 'r')
    word_list = dict_file.readlines()
    dict_file.close()

    word_list = [i[:-1] for i in word_list if len(i[:-1]) > 2]
    for i in word_list:
        if i[0] in dictionary:
            if i[1] in dictionary.get(i[0]):
                if i[2] in dictionary.get(i[0]).get(i[1]):
                    dictionary.get(i[0]).get(i[1]).get(i[2]).append(i)
                else:
                    dictionary.get(i[0]).get(i[1])[i[2]] = [i]
            else:
                dictionary.get(i[0])[i[1]] = {}
                dictionary.get(i[0]).get(i[1])[i[2]] = [i]
        else:
            dictionary[i[0]] = {}
            dictionary.get(i[0])[i[1]] = {}
            dictionary.get(i[0]).get(i[1])[i[2]] = [i]
    return dictionary

dict = dictionary()


def start():
    side = PIL.ImageGrab.grab(bbox = (880, 1500, 881, 1501)).convert("RGB").getpixel((0,0))
    mid = PIL.ImageGrab.grab(bbox = (1280, 1500, 1281, 1501)).convert("RGB").getpixel((0,0))
    #print(side, mid)
    if side == (255, 255, 255):
        return
    elif mid == (255, 255, 255):
        p.click(640, 450)
        time.sleep(0.5)
        p.click(640, 640)
        return
    else:
        while True:
            p.press('esc')
            time.sleep(1)
            mid = PIL.ImageGrab.grab(bbox = (1280, 1500, 1281, 1501)).convert("RGB").getpixel((0,0))
            #print(mid)
            if mid == (255, 255, 255):
                p.click(640, 450)
                time.sleep(0.5)
                p.click(640, 640)
                break


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


def word_prntr(cnts):
    global dict
    print(len(cnts))
    image = cv2.imread('shot.png')

    letter_imgs = []
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

    coordinates = {}
    for i in range(0, len(string)):
        coordinates[list(string)[i]] = []
    for i in range(0, len(string)):
        coordinates[list(string)[i]].append(coords[i])
    print(coordinates)

    possible_words = []
    words = []
    for i in range(0, len(string)-2):
        possible_words += list(it.permutations(string, i+3))

    possible_words = [''.join(list(d)) for d in possible_words]
    for word in possible_words:
        if word[0] in dict:
            if word[1] in dict.get(word[0]):
                if word[2] in dict.get(word[0]).get(word[1]):
                    if word in dict.get(word[0]).get(word[1]).get(word[2]):
                        words.append(word)

    words = list(set(words))

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
    process_pict()
    word_prntr(process_pict())

p.keyDown('command')
p.press('tab')
p.press('tab')
p.keyUp('command')
