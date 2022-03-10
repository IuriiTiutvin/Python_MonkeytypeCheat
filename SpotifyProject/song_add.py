import PIL
from PIL import ImageEnhance, ImageGrab
import pytesseract
import pyautogui as p
import time
import re

groups = open("Database/groups_toadd.txt","r")
group_list = groups.readlines()
log = open("Database/log.txt","a")

p.keyDown('command')
p.press('tab')
p.press('tab')
p.keyUp('command')

def add_songs(artist):
    p.click(500, 220)
    time.sleep(2)
    for i in range(0, 5):
        time.sleep(0.1)
        p.press('tab')
    time.sleep(1)

    discography_check = PIL.ImageGrab.grab(bbox=(1850, 860, 1970, 900))
    discography_check = ImageEnhance.Sharpness(discography_check).enhance(100)
    discography_check = ImageEnhance.Contrast(discography_check).enhance(100)
    discography_check = pytesseract.image_to_string(discography_check).partition("\n")
    if discography_check[0] != 'SEE ALL':
        log.write(f"FAILURE: <*-<{artist}>-*> #?#<3 albums#?# \n")
        return

    for i in range(0, 2):
        p.press('tab')
    p.press('enter')
    time.sleep(5)
    '''
    img = PIL.ImageGrab.grab(bbox = (530, 782, 531, 783))
    img = img.convert("RGB")
    check = img.getpixel((0,0))
    print(check)
    if check != (23, 23, 23):
        return
    '''

    x = 2
    while True:
        time.sleep(1)
        p.click(520, 37)
        for i in range(0, x):
            p.press('tab')
            time.sleep(0.2)
        time.sleep(1)
        p.press('enter')
        time.sleep(1)

        img = PIL.ImageGrab.grab(bbox = (530, 782, 531, 783))
        img = img.convert("RGB")
        check = img.getpixel((0,0))
        print(check)
        if check == (23, 23, 23) or check == (24, 24, 24):
            break

        time.sleep(1)
        p.click(872, 524)
        time.sleep(1.1)
        p.keyDown('command')
        time.sleep(0.1)
        p.press('a')
        time.sleep(0.1)
        p.keyUp('command')
        time.sleep(1.1)
        p.rightClick(580, 530)
        time.sleep(1.1)
        p.click(660, 590)
        time.sleep(1.1)
        p.click(280, 30)
        time.sleep(1)
        x += 2


def artist_log(artist, found):
    if re.match("^[A-Za-z *()-:]*$", found):
        if artist.lower() == found.lower():
            log.write(f"SUCCESS: <*-<{artist}>-*> was found, coping songs\n")
            screenshot = PIL.ImageGrab.grab(bbox=(550, 270, 780, 490))
            screenshot.save(f"Database/artists_added/{found}.png")
            add_songs(artist)
        else:
            log.write(f"FAILURE: <*-<{artist}>-*> was not found, instead found #?#{found}#?#\n")
    else:
        log.write(f"FAILURE: <*-<{artist}>-*> was not found, contains unexpected charecters: :?:{found}:?:\n")


def next_artist(artist):
    p.click(100, 45)
    time.sleep(1)
    p.click(117, 84)
    time.sleep(1)
    p.click(430, 30)
    time.sleep(1)

    p.write(artist, interval=0.25)
    time.sleep(1)


    name = PIL.ImageGrab.grab(bbox=(550, 510, 2000, 590))
    verification = PIL.ImageGrab.grab(bbox=(590, 602, 690, 632))
    #name.save("shot.png")
    name = ImageEnhance.Sharpness(name).enhance(100)
    name = ImageEnhance.Contrast(name).enhance(100)
    verification = ImageEnhance.Contrast(verification).enhance(100)
    name = pytesseract.image_to_string(name).partition("\n")
    verification = pytesseract.image_to_string(verification).partition("\n")
    #print(name, verification)

    if verification[0] == 'ARTIST':
        artist_log(artist, name[0])
    else:
        log.write(f"FAILURE: <*-<{artist}>-*> was not found, 1st option was :?:NOT an ARTIST:?:\n")

#next_artist("Ateez")

for i in group_list:
    next_artist(i.partition("\n")[0])

groups.close()
log.close()


#read/write commands
'''
f= open("guru99.txt","+")
f.write("This is line %d\r\n" % (i+1))
f.close()
f.read()
f.readlines()
'''
