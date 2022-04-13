import keyboard
import time
from selenium import webdriver
import re
import pyautogui as p


driver = webdriver.Chrome('/Users/yura/Desktop/Python/chromedriver')
driver.get("http://monkeytype.com")

def html():
    result = driver.page_source.partition("""class="word active""")[2].partition("""class="keymap hidden""")[0]
    result = re.sub("""class="word""", '> <', result)
    x = re.findall(r"\>([a-z ])\<", result)
    x.append(' ')
    return x

list = []

def type():
    global list
    #may edit this time.sleep() to your liking
    #0.03 has a max speed of 240(for reference)
    time.sleep(0.03)
    if len(list) == 0:
        list = html()
    webdriver.ActionChains(driver).send_keys(list[0]).perform()
    list = list[1:]

p.keyDown('command')
p.press('tab')
p.press('tab')
p.press('tab')
p.keyUp('command')

def main():
    while True:
        if keyboard.is_pressed('a'):
            type()
        if keyboard.is_pressed('b'):
            type()
        if keyboard.is_pressed('c'):
            type()
        if keyboard.is_pressed('d'):
            type()
        if keyboard.is_pressed('e'):
            type()
        if keyboard.is_pressed('f'):
            type()
        if keyboard.is_pressed('g'):
            type()
        if keyboard.is_pressed('h'):
            type()
        if keyboard.is_pressed('i'):
            type()
        if keyboard.is_pressed('j'):
            type()
        if keyboard.is_pressed('k'):
            type()
        if keyboard.is_pressed('l'):
            type()
        if keyboard.is_pressed('m'):
            type()
        if keyboard.is_pressed('n'):
            type()
        if keyboard.is_pressed('o'):
            type()
        if keyboard.is_pressed('p'):
            type()
        if keyboard.is_pressed('q'):
            type()
        if keyboard.is_pressed('r'):
            type()
        if keyboard.is_pressed('s'):
            type()
        if keyboard.is_pressed('t'):
            type()
        if keyboard.is_pressed('u'):
            type()
        if keyboard.is_pressed('v'):
            type()
        if keyboard.is_pressed('w'):
            type()
        if keyboard.is_pressed('x'):
            type()
        if keyboard.is_pressed('y'):
            type()
        if keyboard.is_pressed('z'):
            type()
main()
